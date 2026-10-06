#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro stažení/synchronizaci poslední publikované verze z testovacího serveru (FTP).
Umožňuje druhému správci webu stáhnout změny, které publikoval první správce.
Synchronizuje:
  - rozcestník index.html
  - složku verzeA/
  - složku verzeB/
"""

import os
import sys
import argparse
import time
from datetime import datetime
from ftplib import FTP, FTP_TLS
from dotenv import load_dotenv

# Zajištění UTF-8 výstupu na Windows konzoli
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Načtení proměnných z .env
load_dotenv()

FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")
FTP_PORT = int(os.getenv("FTP_PORT", "21"))
FTP_TLS_ENABLED = os.getenv("FTP_TLS", "false").lower() in ("true", "1", "yes")

# Výchozí kořenový adresář na serveru j4me.net pro Jedenáctku
BASE_REMOTE_DIR = "/web/11"
LOCAL_ROOT = os.path.dirname(os.path.abspath(__file__))

def parse_arguments():
    parser = argparse.ArgumentParser(description="Synchronizace (stažení) poslední verze z testovacího FTP serveru.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Přepsat všechny lokální soubory bez ohledu na datum a velikost."
    )
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Stáhnout pouze HTML soubory (blesková synchronizace textů a kódu)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Pouze zkontrolovat rozdíly oproti serveru, nic nestahovat."
    )
    return parser.parse_args()

def check_env():
    missing = []
    if not FTP_HOST: missing.append("FTP_HOST")
    if not FTP_USER: missing.append("FTP_USER")
    if not FTP_PASS: missing.append("FTP_PASS")
    if missing:
        print(f"❌ Chyba: V souboru .env chybí nastavení: {', '.join(missing)}")
        print("💡 Zkontrolujte soubor .env (vzor je v .env.example).")
        sys.exit(1)

def connect_ftp():
    check_env()
    print(f"🔌 Připojuji se k FTP serveru {FTP_HOST}:{FTP_PORT}...")
    try:
        if FTP_TLS_ENABLED:
            ftp = FTP_TLS()
            ftp.connect(FTP_HOST, FTP_PORT, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.prot_p()
        else:
            ftp = FTP()
            ftp.connect(FTP_HOST, FTP_PORT, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)

        ftp.set_pasv(True)
        ftp.encoding = "utf-8"
        print("✅ Úspěšně přihlášeno k FTP.")
        return ftp
    except Exception as e:
        print(f"❌ Chyba připojení: {e}")
        sys.exit(1)

def sync_remote_dir(ftp, remote_dir, local_dir, force=False, html_only=False, dry_run=False):
    """Rekurzivně stáhne vzdálenou složku do lokální složky, stahuje pouze novější/chybějící soubory."""
    stats = {
        "updated": 0,
        "up_to_date": 0,
        "bytes_downloaded": 0,
        "errors": 0
    }

    try:
        ftp.cwd(remote_dir)
    except Exception as e:
        print(f"  ⚠️ Složka {remote_dir} na serveru nebyla nalezena: {e}")
        return stats

    entries = []
    try:
        ftp.retrlines("MLSD", entries.append)
        is_mlsd = True
    except Exception:
        try:
            entries = ftp.nlst()
            is_mlsd = False
        except Exception:
            return stats

    items = []
    if is_mlsd:
        for entry in entries:
            parts = entry.split(";", 1)
            if len(parts) == 2:
                facts = entry.split(";")
                name = facts[-1].strip()
                fact_dict = {}
                for f in facts[:-1]:
                    if "=" in f:
                        k, v = f.split("=", 1)
                        fact_dict[k.lower()] = v
                item_type = fact_dict.get("type", "file")
                size = int(fact_dict.get("size", 0)) if "size" in fact_dict else None
                modify = fact_dict.get("modify")
                mtime = None
                if modify:
                    try:
                        mtime = datetime.strptime(modify[:14], "%Y%m%d%H%M%S").timestamp()
                    except Exception:
                        pass
                items.append((name, item_type, size, mtime))
    else:
        for name in entries:
            if name in (".", ".."): continue
            is_dir = False
            try:
                ftp.cwd(f"{remote_dir}/{name}")
                is_dir = True
                ftp.cwd(remote_dir)
            except Exception:
                is_dir = False
            items.append((name, "dir" if is_dir else "file", None, None))

    for name, item_type, rem_size, rem_mtime in items:
        if name in (".", ".."): continue

        if item_type in ("dir", "pdir", "cdir"):
            sub_remote = f"{remote_dir}/{name}"
            sub_local = os.path.join(local_dir, name)
            sub_stats = sync_remote_dir(ftp, sub_remote, sub_local, force, html_only, dry_run)
            stats["updated"] += sub_stats["updated"]
            stats["up_to_date"] += sub_stats["up_to_date"]
            stats["bytes_downloaded"] += sub_stats["bytes_downloaded"]
            stats["errors"] += sub_stats["errors"]
            # Vrátit se zpět do původní složky
            ftp.cwd(remote_dir)
        else:
            if html_only and not name.lower().endswith(('.html', '.htm')):
                continue

            local_file = os.path.join(local_dir, name)
            needs_down = False
            reason = ""

            if not os.path.exists(local_file):
                needs_down = True
                reason = "nový soubor"
            elif force:
                needs_down = True
                reason = "vynuceno (--force)"
            else:
                loc_stat = os.stat(local_file)
                loc_size = loc_stat.st_size
                loc_mtime = loc_stat.st_mtime

                if rem_size is not None and rem_size != loc_size:
                    needs_down = True
                    reason = f"velikost server: {rem_size} B vs lokální: {loc_size} B"
                elif rem_mtime is not None and rem_mtime > (loc_mtime + 2):
                    needs_down = True
                    reason = "server má novější verzi"

            if needs_down:
                rel_display = os.path.relpath(local_file, LOCAL_ROOT)
                if dry_run:
                    print(f"  🔍 [DRY-RUN] Bylo by staženo: {rel_display} ({reason})")
                    stats["updated"] += 1
                else:
                    print(f"  ⬇️  Stahuji: {rel_display} ({reason})...")
                    os.makedirs(os.path.dirname(local_file), exist_ok=True)
                    try:
                        with open(local_file, "wb") as f_out:
                            ftp.retrbinary(f"RETR {name}", f_out.write)
                        stats["updated"] += 1
                        stats["bytes_downloaded"] += os.path.getsize(local_file)
                    except Exception as ex:
                        print(f"    ❌ Chyba při stahování {name}: {ex}")
                        stats["errors"] += 1
            else:
                stats["up_to_date"] += 1

    return stats

def main():
    args = parse_arguments()
    print("=" * 65)
    print("🔄 JEDENÁCTKA - Synchronizace z testovacího serveru (FTP)")
    print("=" * 65)

    ftp = connect_ftp()
    start_time = time.time()

    print(f"\n📂 Serverový kořen: {BASE_REMOTE_DIR}")
    print(f"📁 Lokální složka:  {LOCAL_ROOT}")
    if args.dry_run:
        print("⚠️  Režim simulace (--dry-run) - žádné soubory nebudou měněny.")

    # 1. Synchronizace rozcestníku index.html
    stats = {"updated": 0, "up_to_date": 0, "bytes_downloaded": 0, "errors": 0}
    try:
        ftp.cwd(BASE_REMOTE_DIR)
        remote_index_size = None
        try:
            remote_index_size = ftp.size("index.html")
        except Exception:
            pass

        local_index = os.path.join(LOCAL_ROOT, "index.html")
        needs_index = False
        reason = ""
        if not os.path.exists(local_index):
            needs_index = True
            reason = "chybí lokálně"
        elif args.force:
            needs_index = True
            reason = "vynuceno"
        elif remote_index_size and remote_index_size != os.path.getsize(local_index):
            needs_index = True
            reason = f"velikost server: {remote_index_size} B vs lokální: {os.path.getsize(local_index)} B"

        if needs_index:
            if args.dry_run:
                print(f"  🔍 [DRY-RUN] Bylo by staženo: index.html ({reason})")
                stats["updated"] += 1
            else:
                print(f"  ⬇️  Stahuji: index.html ({reason})...")
                with open(local_index, "wb") as f:
                    ftp.retrbinary("RETR index.html", f.write)
                stats["updated"] += 1
                stats["bytes_downloaded"] += os.path.getsize(local_index)
        else:
            stats["up_to_date"] += 1
    except Exception as e:
        print(f"  ⚠️ Chyba při kontrole index.html: {e}")

    # 2. Synchronizace verzeA/
    print("\n🎨 Kontrola Variant A (verzeA/)...")
    stats_a = sync_remote_dir(
        ftp=ftp,
        remote_dir=f"{BASE_REMOTE_DIR}/verzeA",
        local_dir=os.path.join(LOCAL_ROOT, "verzeA"),
        force=args.force,
        html_only=args.html_only,
        dry_run=args.dry_run
    )

    # 3. Synchronizace verzeB/
    print("\n🎨 Kontrola Variant B (verzeB/)...")
    stats_b = sync_remote_dir(
        ftp=ftp,
        remote_dir=f"{BASE_REMOTE_DIR}/verzeB",
        local_dir=os.path.join(LOCAL_ROOT, "verzeB"),
        force=args.force,
        html_only=args.html_only,
        dry_run=args.dry_run
    )

    try:
        ftp.quit()
    except Exception:
        pass

    total_up = stats["updated"] + stats_a["updated"] + stats_b["updated"]
    total_same = stats["up_to_date"] + stats_a["up_to_date"] + stats_b["up_to_date"]
    total_bytes = stats["bytes_downloaded"] + stats_a["bytes_downloaded"] + stats_b["bytes_downloaded"]
    total_errors = stats["errors"] + stats_a["errors"] + stats_b["errors"]

    elapsed = time.time() - start_time
    mb_down = total_bytes / (1024 * 1024)

    print("\n" + "=" * 65)
    print("📊 VÝSLEDEK SYNCHRONIZACE:")
    print(f"  • Staženo / aktualizováno: {total_up} souborů ({mb_down:.2f} MB)")
    print(f"  • Beze změny (aktuální):   {total_same} souborů")
    if total_errors > 0:
        print(f"  • Chyby:                   {total_errors}")
    print(f"  • Doba běhu:               {elapsed:.1f} s")
    print("=" * 65)

    if total_up > 0:
        if args.dry_run:
            print("💡 Na serveru jsou novější změny. Spusťte bez --dry-run pro jejich stažení.")
        else:
            print("✨ Váš lokální kód byl úspěšně aktualizován na poslední publikovanou verzi!")
    else:
        print("✅ Váš lokální kód je již zcela aktuální se serverem.")

if __name__ == "__main__":
    main()
