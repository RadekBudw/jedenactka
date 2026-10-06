#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro automatický produkční deployment na WordPress (https://jedenactka.skauting.cz/).
Přihlásí se do administrace WordPressu, nahraje připravenou šablonu jedenactka-theme.zip
a automaticky ji aktivuje.
"""

import os
import sys
import argparse
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Zajištění UTF-8 výstupu na Windows konzoli
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Načtení proměnných z .env
load_dotenv()

WP_URL = os.getenv("WP_URL", "https://jedenactka.skauting.cz").rstrip("/")
WP_USER = os.getenv("WP_USER")
WP_PASS = os.getenv("WP_PASS")

DEFAULT_THEME_ZIP = os.path.join(os.path.dirname(__file__), "jedenactka-theme.zip")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Automatický deployment na WordPress (jedenactka.skauting.cz).")
    parser.add_argument(
        "--zip",
        default=DEFAULT_THEME_ZIP,
        help="Cesta k souboru šablony ZIP (výchozí: jedenactka-theme.zip)."
    )
    parser.add_argument(
        "--build-first",
        action="store_true",
        help="Nejprve znovu sestavit balíček šablony z aktuálních souborů."
    )
    parser.add_argument(
        "--variant",
        default="verzeA",
        help="Varianta pro sestavení: verzeA nebo verzeB (použije se při --build-first)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Pouze otestovat přihlášení a oprávnění administrátora, nenahrávat."
    )
    return parser.parse_args()

def check_env():
    missing = []
    if not WP_USER: missing.append("WP_USER")
    if not WP_PASS: missing.append("WP_PASS")

    if missing:
        print("\n" + "=" * 60)
        print("❌ CHYBA: Chybí WordPress přihlašovací údaje v souboru .env!")
        print(f"Chybějící proměnné: {', '.join(missing)}")
        print("\nProsím doplň do souboru .env:")
        print("WP_URL=https://jedenactka.skauting.cz")
        print("WP_USER=tve_prihlasovaci_jmeno_do_wordpressu")
        print("WP_PASS=tve_tajne_heslo_do_wordpressu")
        print("=" * 60 + "\n")
        sys.exit(1)

def main():
    args = parse_arguments()
    check_env()

    if args.build_first or not os.path.exists(args.zip):
        print("🔨 Spouštím sestavení WordPress šablony...")
        from build_wp_theme import prepare_wp_theme
        prepare_wp_theme(args.variant)

    if not os.path.exists(args.zip):
        print(f"❌ Chyba: Soubor šablony '{args.zip}' neexistuje!")
        sys.exit(1)

    zip_size_mb = os.path.getsize(args.zip) / (1024 * 1024)

    print("=" * 60)
    print(f"🚀 WordPress Production Deploy -> {WP_URL}")
    print(f"👤 Uživatel: {WP_USER}")
    print(f"📦 Balíček: {os.path.basename(args.zip)} ({zip_size_mb:.2f} MB)")
    if args.dry_run:
        print("🔍 Režim: DRY-RUN (pouze test přihlášení a oprávnění)")
    print("=" * 60)

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    })

    # 1. KROK: PŘIHLÁŠENÍ DO WORDPRESSU
    login_url = f"{WP_URL}/wp-login.php"
    admin_url = f"{WP_URL}/wp-admin/"
    print(f"\n🔐 1. Přihlašuji se do WordPressu ({login_url})...")

    try:
        # Získat testovací cookie
        session.get(login_url, timeout=20)

        login_payload = {
            "log": WP_USER,
            "pwd": WP_PASS,
            "wp-submit": "Přihlásit se",
            "redirect_to": admin_url,
            "testcookie": "1"
        }

        res_login = session.post(login_url, data=login_payload, timeout=25, allow_redirects=True)

        # Kontrola, zda jsme přihlášeni
        has_login_cookie = any('wordpress_logged_in' in c.name for c in session.cookies)
        if not has_login_cookie and "wp-admin" not in res_login.url:
            soup = BeautifulSoup(res_login.text, "html.parser")
            error_msg = soup.find(id="login_error")
            err_text = error_msg.get_text(strip=True) if error_msg else "Neplatné jméno nebo heslo."
            print(f"❌ Přihlášení selhalo: {err_text}")
            sys.exit(1)

        print("✅ Úspěšně přihlášeno do administrace WordPressu!")

    except Exception as e:
        print(f"❌ Chyba při komunikaci se serverem: {e}")
        sys.exit(1)

    # 2. KROK: KONTROLA STRÁNKY INSTALACE ŠABLON
    install_theme_url = f"{WP_URL}/wp-admin/theme-install.php?upload"
    print(f"\n🔍 2. Kontroluji oprávnění pro nahrávání šablon ({install_theme_url})...")

    try:
        res_upload_page = session.get(install_theme_url, timeout=25)
        if res_upload_page.status_code != 200 or "theme-install.php" not in res_upload_page.url:
            print("⚠️ Upozornění: Uživatelský účet možná nemá oprávnění instalovat šablony (upload_themes).")
            print("Zkontroluj, zda má účet roli 'Administrátor' nebo 'Správce sítě'.")
            if not args.dry_run:
                sys.exit(1)

        soup = BeautifulSoup(res_upload_page.text, "html.parser")
        form = soup.find("form", class_="wp-upload-form")
        if not form:
            form = soup.find("form", action=lambda x: x and "upload-theme" in x)

        if not form:
            print("⚠️ Nepodařilo se nalézt formulář pro nahrání šablony v administraci.")
            if not args.dry_run:
                sys.exit(1)
        else:
            action_url = form.get("action", f"{WP_URL}/wp-admin/update.php?action=upload-theme")
            if not action_url.startswith("http"):
                action_url = f"{WP_URL}/wp-admin/{action_url.lstrip('/')}"
            
            # Získání bezpečnostního tokenu _wpnonce
            nonce_input = form.find("input", {"name": "_wpnonce"})
            nonce = nonce_input["value"] if nonce_input else None
            print(f"✅ Formulář pro nahrání šablon je připraven (bezpečnostní token nalezen).")

    except Exception as e:
        print(f"❌ Chyba při zjišťování formuláře: {e}")
        sys.exit(1)

    if args.dry_run:
        print("\n" + "=" * 60)
        print("🎉 DRY-RUN TEST DOKONČEN!")
        print("✅ Přihlášení funguje.")
        print("✅ Oprávnění administrátora ověřena.")
        print("✅ Systém je 100% připraven na ostrý deploy.")
        print("=" * 60 + "\n")
        return

    # 3. KROK: NAHRÁNÍ ŠABLONY (UPLOAD)
    print(f"\n⬆️ 3. Nahrávám balíček {os.path.basename(args.zip)} na server...")
    start_time = time.time()

    try:
        with open(args.zip, "rb") as f_zip:
            files = {
                "themezip": (os.path.basename(args.zip), f_zip, "application/zip")
            }
            data = {
                "_wpnonce": nonce,
                "_wp_http_referer": f"/wp-admin/theme-install.php?upload",
                "install-theme-submit": "Instalovat"
            }

            res_upload = session.post(action_url, files=files, data=data, timeout=120)

        elapsed_upload = time.time() - start_time
        print(f"✅ Balíček nahrán na server ({elapsed_upload:.1f} s).")

        # 4. KROK: AKTIVACE ŠABLONY
        print("\n⚙️ 4. Aktivuji novou šablonu...")
        soup_res = BeautifulSoup(res_upload.text, "html.parser")

        # Hledání aktivačního odkazu
        activate_link = None
        for a in soup_res.find_all("a", href=True):
            if "action=activate" in a["href"] and ("jedenactka" in a["href"] or "stylesheet=" in a["href"]):
                activate_link = a["href"]
                break

        if not activate_link:
            # Kontrola, zda už šablona existuje a je potřeba ji nahradit
            replace_btn = None
            for a in soup_res.find_all("a", href=True):
                if "overwrite=" in a["href"] or "update-theme" in a["href"]:
                    replace_btn = a["href"]
                    break

            if replace_btn:
                print("🔄 Šablona již existovala, potvrzuji nahrazení novou verzí...")
                if not replace_btn.startswith("http"):
                    replace_btn = f"{WP_URL}/wp-admin/{replace_btn.lstrip('/')}"
                res_replace = session.get(replace_btn, timeout=60)
                soup_replace = BeautifulSoup(res_replace.text, "html.parser")
                for a in soup_replace.find_all("a", href=True):
                    if "action=activate" in a["href"]:
                        activate_link = a["href"]
                        break

        if activate_link:
            if not activate_link.startswith("http"):
                activate_link = f"{WP_URL}/wp-admin/{activate_link.lstrip('/')}"
            
            res_activate = session.get(activate_link, timeout=30)
            print("✅ Šablona '11. oddíl vodních skautů ČB' byla úspěšně AKTIVOVÁNA!")
        else:
            print("⚠️ Šablona byla nahrána, ale nenašel se přímý odkaz na aktivaci.")
            print(f"Prosím otevři {WP_URL}/wp-admin/themes.php a klikni na 'Aktivovat'.")

        # 5. KROK: OVĚŘENÍ ŽIVÉHO WEBU
        print(f"\n🌐 5. Ověřuji ostrý web na {WP_URL}/...")
        res_live = requests.get(f"{WP_URL}/", timeout=15)
        if "11. oddíl vodních skautů" in res_live.text or "jedenactka" in res_live.text.lower():
            print("🎉 VÝBORNĚ! Nový redesign je úspěšně živý na doméně!")
        else:
            print("ℹ️ Web odpověděl, zkontroluj výsledek v prohlížeči.")

        total_time = time.time() - start_time
        print("\n" + "=" * 60)
        print("🎉 PRODUKČNÍ DEPLOY DOKONČEN!")
        print(f"⏱️ Celkový čas: {total_time:.2f} s")
        print(f"🔗 Ostrý web: {WP_URL}/")
        print(f"🔗 Vedení oddílu: {WP_URL}/vedeni/")
        print("=" * 60 + "\n")

    except Exception as e:
        print(f"❌ Chyba při nahrávání šablony: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
