#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kompletní build skript pro 11. oddíl vodních skautů ČB:
1. Vygeneruje Variantu A (index.html + vedeni.html)
2. Vygeneruje Variantu B (index.html + vedeni.html)
3. Uloží strojově čitelný version.json pro automatickou kontrolu
4. Aktualizuje kořenový rozcestník index.html s přesnou verzí a časem
"""

import sys
from build_verze_a import generate_index_a, generate_vedeni_a
from build_verze_b import generate_index_b, generate_vedeni_b
from build_data import save_version_json, update_index_html_version, get_app_version, get_git_commit

# Zajištění UTF-8 výstupu na Windows konzoli
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def main():
    print(f"🚀 Zahajuji kompletní sestavení webu...")
    print(f"   Verze: {get_app_version()} (commit {get_git_commit()})")

    print("\n[1/4] Generuji Variantu A...")
    generate_index_a()
    generate_vedeni_a()

    print("\n[2/4] Generuji Variantu B...")
    generate_index_b()
    generate_vedeni_b()

    print("\n[3/4] Ukládám metadata do version.json...")
    save_version_json()

    print("\n[4/4] Aktualizuji kořenový rozcestník index.html...")
    update_index_html_version()

    print(f"\n✅ Všechny stránky byly úspěšně vygenerovány ve verzi {get_app_version()}!")

if __name__ == "__main__":
    main()
