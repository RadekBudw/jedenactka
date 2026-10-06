#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro automatický deploy webu na testovací FTP server (j4me.net).
Načítá přihlašovací údaje z lokálního souboru .env.
"""

import os
import sys
import argparse
import time
from ftplib import FTP, FTP_TLS, error_perm
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
FTP_REMOTE_DIR = os.getenv("FTP_REMOTE_DIR", "/web/11")
FTP_TLS_ENABLED = os.getenv("FTP_TLS", "false").lower() in ("true", "1", "yes")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Automatický deploy Jedenáctky na FTP.")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Nahrát vše: rozcestník index.html, verzi A i verzi B."
    )
    parser.add_argument(
        "--target",
        default="verzeA",
        help="Místní složka k nahrání (verzeA nebo verzeB). Ignorováno při --all."
    )
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Nahrát pouze HTML soubory (bleskový deploy bez obrázků)."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Vynutit nahrání všech souborů i když se velikost shoduje."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Pouze zkontrolovat spojení a vypsat soubory k nahrání, nic nenahrávat."
    )
    return parser.parse_args()

def check_env():
    missing = []
    if not FTP_HOST: missing.append("FTP_HOST")
    if not FTP_USER: missing.append("FTP_USER")
    if not FTP_PASS: missing.append("FTP_PASS")

    if missing:
        print("\n" + "=" * 60)
        print("❌ CHYBA: Chybí konfigurace v souboru .env!")
        print(f"Chybějící proměnné: {', '.join(missing)}")
        print("\nProsím vytvoř soubor .env v této složce podle .env.example:")
        print("FTP_HOST=ftp.j4me.net")
        print("FTP_USER=tve_jmeno")
        print("FTP_PASS=tve_heslo")
        print("FTP_REMOTE_DIR=/web/11")
        print("=" * 60 + "\n")
        sys.exit(1)

def ensure_remote_dir(ftp, remote_path):
    """Zajistí, že vzdálená složka existuje (vytvoří ji včetně podadresářů)."""
    parts = [p for p in remote_path.replace("\\", "/").split("/") if p]
    current = ""
    if remote_path.startswith("/"):
        current = "/"

    for part in parts:
        current = f"{current.rstrip('/')}/{part}"
        try:
            ftp.cwd(current)
        except error_perm:
            try:
                ftp.mkd(current)
                ftp.cwd(current)
            except Exception as e:
                print(f"  ⚠️ Varování při vytváření složky {current}: {e}")

def get_remote_file_size(ftp, filename):
    """Vrátí velikost souboru na FTP nebo None, pokud neexistuje / příkaz selže."""
    try:
        return ftp.size(filename)
    except Exception:
        return None

def upload_single_file(ftp, local_path, remote_dir, filename, args):
    """Nahraje jeden soubor do daného remote_dir."""
    ensure_remote_dir(ftp, remote_dir)
    file_size = os.path.getsize(local_path)

    remote_size = get_remote_file_size(ftp, filename)
    if not args.force and not filename.endswith(".html") and remote_size == file_size:
        print(f"  ⏩ Přeskočeno (beze změny): {filename}")
        return False, 0

    if args.dry_run:
        print(f"  [DRY-RUN] Bude nahráno: {filename} ({file_size / 1024:.1f} KB)")
        return True, file_size

    print(f"  ⬆️ Nahrávám: {filename} ({file_size / 1024:.1f} KB)...", end="", flush=True)
    with open(local_path, "rb") as f_in:
        ftp.storbinary(f"STOR {filename}", f_in)
    print(" OK")
    return True, file_size

def upload_directory_tree(ftp, local_dir, base_remote_dir, args):
    """Rekurzivně nahraje celou složku do vzdálené složky."""
    uploaded_count = 0
    skipped_count = 0
    total_bytes = 0

    for root, dirs, files in os.walk(local_dir):
        rel_dir = os.path.relpath(root, local_dir).replace("\\", "/")
        if rel_dir == ".":
            target_remote_dir = base_remote_dir
        else:
            target_remote_dir = f"{base_remote_dir.rstrip('/')}/{rel_dir}"

        ensure_remote_dir(ftp, target_remote_dir)

        for file in files:
            if args.html_only and not file.endswith(".html"):
                skipped_count += 1
                continue

            local_path = os.path.join(root, file)
            uploaded, b = upload_single_file(ftp, local_path, target_remote_dir, file, args)
            if uploaded:
                uploaded_count += 1
                total_bytes += b
            else:
                skipped_count += 1

    return uploaded_count, skipped_count, total_bytes

def main():
    args = parse_arguments()
    check_env()

    # Zjištění bázové cesty na serveru (např. /web/11)
    base_remote = FTP_REMOTE_DIR.rstrip("/")
    if base_remote.endswith("/verzeA") or base_remote.endswith("/verzeB"):
        base_remote = os.path.dirname(base_remote).replace("\\", "/")

    print("=" * 60)
    print(f"🚀 Deploy 11. oddíl vodních skautů -> {FTP_HOST}")
    if args.all:
        print("📦 Režim: KOMPLETNÍ DEPLOY (Rozcestník + Verze A + Verze B)")
        print(f"🌐 Cíl na serveru: {base_remote}")
    else:
        print(f"📁 Zdroj: {args.target}")
        print(f"🌐 Cíl na serveru: {base_remote}/{args.target}")

    if args.html_only:
        print("⚡ Režim: POUZE HTML SOUBORY")
    if args.force:
        print("🔄 Režim: FORCE (přepsat vše)")
    if args.dry_run:
        print("🔍 Režim: DRY-RUN (pouze test)")
    print("=" * 60)

    # Připojení k FTP
    print(f"\n🔌 Připojuji se k {FTP_HOST}:{FTP_PORT}...")
    try:
        if FTP_TLS_ENABLED:
            ftp = FTP_TLS()
            ftp.connect(FTP_HOST, FTP_PORT, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.prot_p()
            print("🔒 Připojeno přes FTPS (TLS).")
        else:
            ftp = FTP()
            ftp.connect(FTP_HOST, FTP_PORT, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            print("✅ Připojeno přes standardní FTP.")
    except Exception as e:
        print(f"❌ Selhalo připojení k FTP: {e}")
        sys.exit(1)

    start_time = time.time()
    total_uploaded = 0
    total_skipped = 0
    total_bytes = 0

    try:
        if args.all:
            # 1. Nahrání hlavního rozcestníku index.html
            root_index = os.path.abspath("index.html")
            if os.path.exists(root_index):
                print(f"\n📄 [1/3] Nahrávám rozcestník: index.html -> {base_remote}/index.html")
                up, b = upload_single_file(ftp, root_index, base_remote, "index.html", args)
                if up: total_uploaded += 1; total_bytes += b
                else: total_skipped += 1

            # 2. Nahrání Verze A
            dir_a = os.path.abspath("verzeA")
            if os.path.exists(dir_a):
                print(f"\n🎨 [2/3] Nahrávám Variantu A -> {base_remote}/verzeA")
                up, sk, b = upload_directory_tree(ftp, dir_a, f"{base_remote}/verzeA", args)
                total_uploaded += up; total_skipped += sk; total_bytes += b

            # 3. Nahrání Verze B
            dir_b = os.path.abspath("verzeB")
            if os.path.exists(dir_b):
                print(f"\n🏛️ [3/3] Nahrávám Variantu B -> {base_remote}/verzeB")
                up, sk, b = upload_directory_tree(ftp, dir_b, f"{base_remote}/verzeB", args)
                total_uploaded += up; total_skipped += sk; total_bytes += b

        else:
            # Nahrání konkrétní složky
            local_target_dir = os.path.abspath(args.target)
            if not os.path.exists(local_target_dir):
                print(f"❌ Chyba: Místní složka '{local_target_dir}' neexistuje!")
                ftp.quit()
                sys.exit(1)

            dest = f"{base_remote}/{args.target}"
            print(f"\n📁 Nahrávám {args.target} -> {dest}")
            up, sk, b = upload_directory_tree(ftp, local_target_dir, dest, args)
            total_uploaded += up; total_skipped += sk; total_bytes += b

    except Exception as e:
        print(f"\n❌ Chyba při nahrávání: {e}")
        ftp.quit()
        sys.exit(1)

    ftp.quit()
    elapsed = time.time() - start_time

    print("\n" + "=" * 60)
    print("🎉 DEPLOY DOKONČEN!")
    print(f"📊 Nahráno souborů: {total_uploaded} ({total_bytes / (1024 * 1024):.2f} MB)")
    print(f"⏩ Přeskočeno (identické fotky): {total_skipped}")
    print(f"⏱️ Čas: {elapsed:.2f} s")
    print("\n🌐 Živé odkazy:")
    print(f"  • Rozcestník: https://j4me.net/11/index.html")
    print(f"  • Varianta A: https://j4me.net/11/verzeA/index.html")
    print(f"  • Varianta B: https://j4me.net/11/verzeB/index.html")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
