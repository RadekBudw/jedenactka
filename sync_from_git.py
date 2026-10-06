#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro synchronizaci nejnovější verze z GitHub repozitáře.
Umožňuje druhému správci webu (nebo komukoliv z týmu) stáhnout nejnovější změny
publikované do větve main.
"""

import subprocess
import sys
import os

# Zajištění UTF-8 výstupu na Windows konzoli
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def main():
    print("=" * 65)
    print("🔄 JEDENÁCTKA - Synchronizace z GitHubu (Testovací server)")
    print("=" * 65)

    # 1. Kontrola stavu
    ret, out, err = run_cmd("git status --porcelain")
    if out:
        print("⚠️  Máte neuložené lokální změny v těchto souborech:")
        for line in out.splitlines():
            print(f"   {line}")
        print("\n💡 Doporučujeme nejdříve změny uložit nebo odeslat do gitu.")

    print("\n🔌 Stahuji nejnovější změny z GitHubu (git pull)...")
    ret, out, err = run_cmd("git pull origin main")

    if ret == 0:
        if "Already up to date" in out or "Aktuální" in out or "Already up-to-date" in out:
            print("✅ Váš kód je již zcela aktuální se serverem GitHub.")
        else:
            print("✨ Úspěšně staženy nové změny z GitHubu:")
            print(out)
    else:
        print(f"❌ Chyba při synchronizaci: {err or out}")
        print("💡 Zkontrolujte připojení k internetu nebo přístupová práva.")
        sys.exit(1)

    print("\n" + "=" * 65)
    print("🌐 Aktuální testovací web na GitHub Pages:")
    print("   https://radekbudw.github.io/jedenactka/")
    print("=" * 65)

if __name__ == "__main__":
    main()
