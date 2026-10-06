#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro kontrolu a porovnání verzí:
Porovná:
 1. Lokální stav na vašem počítači
 2. Vzdálený repozitář na GitHubu (co tam nahrál druhý správce)
 3. Živý testovací web na GitHub Pages (https://radekbudw.github.io/jedenactka/)
 4. Ostrý produkční web (https://jedenactka.skauting.cz/)
"""

import subprocess
import sys
import json
import re
import urllib.request
from build_data import get_app_version

# Zajištění UTF-8 výstupu na Windows konzoli
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

GH_PAGES_URL = "https://radekbudw.github.io/jedenactka/version.json"
GH_PAGES_HTML = "https://radekbudw.github.io/jedenactka/index.html"
WP_URL = "https://jedenactka.skauting.cz/"

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
        return res.returncode, res.stdout.strip()
    except Exception as e:
        return 1, str(e)

def get_local_commit():
    ret, out = run_cmd("git rev-parse --short HEAD")
    return out if ret == 0 else "neznámý"

def get_remote_git_commit():
    ret, out = run_cmd("git ls-remote origin main")
    if ret == 0 and out:
        parts = out.split()
        if parts:
            return parts[0][:7]
    return "nedostupný"

def get_gh_pages_version():
    try:
        req = urllib.request.Request(GH_PAGES_URL, headers={'User-Agent': 'Antigravity-Version-Checker'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('git_commit', 'neznámý'), data.get('build_display', ''), data.get('app_version', '')
    except Exception:
        # Fallback – načtení meta tagu z index.html
        try:
            req = urllib.request.Request(GH_PAGES_HTML, headers={'User-Agent': 'Antigravity-Version-Checker'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                html = resp.read().decode('utf-8', errors='replace')
                m_commit = re.search(r'<meta name="git-commit" content="([^"]+)"', html)
                m_time = re.search(r'<meta name="build-timestamp" content="([^"]+)"', html)
                m_ver = re.search(r'<meta name="app-version" content="([^"]+)"', html)
                commit = m_commit.group(1) if m_commit else "neznámý"
                time_str = m_time.group(1) if m_time else ""
                app_ver = m_ver.group(1) if m_ver else ""
                return commit, time_str, app_ver
        except Exception:
            return "nedostupný", "", ""

def check_wp_status():
    try:
        req = urllib.request.Request(WP_URL, headers={'User-Agent': 'Antigravity-Version-Checker'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='replace')
            if 'jedenactka-theme' in html:
                m_commit = re.search(r'<meta name="git-commit" content="([^"]+)"', html)
                commit = m_commit.group(1) if m_commit else "aktivní nová šablona"
                return f"Nová šablona ({commit})"
            elif 'twenty-twenty' in html.lower() or 'twentytwenty' in html.lower():
                return "Původní šablona Twenty Twenty (připraveno na deploy)"
            return "Dostupný (WordPress)"
    except Exception as e:
        return f"Nedostupný ({e})"

def main():
    print("=" * 70)
    print("🔍 JEDENÁCTKA - Porovnání a kontrola verzí napříč prostředími")
    print("=" * 70)

    local_version = get_app_version()
    local_commit = get_local_commit()
    remote_commit = get_remote_git_commit()
    gh_pages_commit, gh_pages_time, gh_pages_ver = get_gh_pages_version()
    wp_status = check_wp_status()

    # 1. Porovnání Lokální vs Vzdálený Git
    if local_commit == remote_commit:
        git_sync_status = "✅ 100% v souladu"
    else:
        git_sync_status = f"⚠️ Neshoda (Lokál: {local_commit} vs GitHub: {remote_commit})"

    # 2. Porovnání GitHub vs GitHub Pages
    if (gh_pages_ver and gh_pages_ver == local_version) or gh_pages_commit == remote_commit:
        pages_sync_status = "✅ 100% nasazeno naživo"
    elif gh_pages_commit == "nedostupný":
        pages_sync_status = "⏳ Zpracovává se nebo nedostupný"
    else:
        current_deployed = f"v{gh_pages_ver}" if gh_pages_ver else gh_pages_commit
        target_version = f"v{local_version}" if local_version else remote_commit
        pages_sync_status = f"🔄 Probíhá nasazení (Web má {current_deployed}, připraveno {target_version})"

    print(f"\n1️⃣  LOKÁLNÍ KÓD (váš počítač):")
    print(f"    • Verze:           {local_version} (commit {local_commit})")

    print(f"\n2️⃣  GITHUB REPOZITÁŘ (origin/main):")
    print(f"    • Git Commit:      {remote_commit}")
    print(f"    • Stav vůči vám:   {git_sync_status}")

    print(f"\n3️⃣  ŽIVÝ TESTOVACÍ WEB (GitHub Pages):")
    ver_text = f"{gh_pages_ver} ({gh_pages_commit})" if gh_pages_ver else gh_pages_commit
    time_text = f" • {gh_pages_time}" if gh_pages_time else ""
    print(f"    • Běžící verze:    {ver_text}{time_text}")
    print(f"    • Stav nasazení:   {pages_sync_status}")
    print(f"    • URL:             https://radekbudw.github.io/jedenactka/")

    print(f"\n4️⃣  OSTRÝ PRODUKČNÍ WEB (jedenactka.skauting.cz):")
    print(f"    • Aktuální stav:   {wp_status}")
    print(f"    • URL:             https://jedenactka.skauting.cz/")

    print("\n" + "=" * 70)
    if local_commit != remote_commit and remote_commit != "nedostupný":
        print("💡 Doporučení: Druhý správce nahrál na GitHub novější změny.")
        print("   Spusťte: python sync_from_git.py")
    else:
        print("✨ Váš lokální kód je zcela aktuální.")
    print("=" * 70)

if __name__ == "__main__":
    main()
