#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stahuje a aktualizuje seznam fotografií z oddílové fotogalerie Zonerama
ze složek za poslední 2 školní roky:
- 2025/2026: https://eu.zonerama.com/11skautskyoddil/2089661?count=21
- 2024/2025: https://eu.zonerama.com/11skautskyoddil/1522865?count=21

Výstup:
- zonerama_latest_photos.json (obsahuje ID, přímou CDN URL, název alba, tag a popis)
"""

import urllib.request
import re
import json
import os
import shutil
import sys

# Zajištění UTF-8 výstupu na Windows konzoli
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

FOLDERS = [
    {
        'year_label': '2025/2026',
        'folder_id': '2089661',
        'url': 'https://eu.zonerama.com/11skautskyoddil/2089661?count=21'
    },
    {
        'year_label': '2024/2025',
        'folder_id': '1522865',
        'url': 'https://eu.zonerama.com/11skautskyoddil/1522865?count=21'
    }
]

ALBUM_META = {
    '16719506': {
        'tag': 'Schůzky oddílu',
        'sub': 'Život na Valši',
        'desc': 'Pravidelný celoroční program družin v klubovně na Valši'
    },
    '15758185': {
        'tag': 'Letní tábor 2026',
        'sub': 'Labská Stráň',
        'desc': 'Čtrnáct dní nezapomenutelných zážitků, lezení a výzev v přírodě'
    },
    '15582766': {
        'tag': 'Společná voda 2026',
        'sub': 'Vodácká výprava',
        'desc': 'Sjíždění řeky na kánoích, peřeje a vodácká dobrodružství'
    },
    '15374156': {
        'tag': 'Slalomový kanál 2026',
        'sub': 'České Vrbné • divoká voda',
        'desc': 'Trénink pádlování, stability a peřejí na slalomové trati'
    },
    '14432662': {
        'tag': 'Vánoce na Švýcaráku',
        'sub': 'Zimní výprava',
        'desc': 'Tradiční vánoční setkání oddílu na srubové základně Švýcarák'
    },
    '14180805': {
        'tag': 'Podzimní výprava',
        'sub': 'Výprava všech lidí na zemi',
        'desc': 'Společné dobrodružství a lesní hry v podzimní přírodě'
    },
    '14180744': {
        'tag': 'Brigáda na Švýcaráku',
        'sub': 'Pomoc základně',
        'desc': 'Příprava dřeva na zimu, tábornické dovednosti a údržba chaty'
    },
    '14180722': {
        'tag': '3 Jezy Praha',
        'sub': 'Závod Napříč Prahou',
        'desc': 'Reprezentace posádky 11. oddílu na legendárním skautském závodě'
    }
}

JSON_PATH = os.path.join(os.path.dirname(__file__), 'zonerama_latest_photos.json')

def fetch_all_photos(save_file=True, timeout=10):
    all_photos = []
    for f in FOLDERS:
        req = urllib.request.Request(f['url'], headers={'User-Agent': HEADERS['User-Agent']})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                album_ids = list(dict.fromkeys(re.findall(r'/11skautskyoddil/Album/(\d+)', html)))
                for aid in album_ids:
                    slideshow_url = f'https://eu.zonerama.com/JSON/Slideshow_InitAlbum?albumId={aid}'
                    sreq = urllib.request.Request(slideshow_url, headers=HEADERS)
                    try:
                        with urllib.request.urlopen(sreq, timeout=timeout) as sresp:
                            raw = sresp.read()
                            sdata = json.loads(raw.decode('utf-8'))
                            title = sdata.get('title') or f"Album {aid}"
                            p_ids = sdata.get('photosId') or []
                            
                            meta = ALBUM_META.get(aid, {
                                'tag': title,
                                'sub': f'Zonerama {f["year_label"]}',
                                'desc': f'Fotografie z akce {title}'
                            })
                            
                            for pid in p_ids:
                                all_photos.append({
                                    'id': pid,
                                    'album_id': aid,
                                    'album_title': title,
                                    'tag': meta['tag'],
                                    'sub': meta['sub'],
                                    'title': meta['desc'],
                                    'year': f['year_label'],
                                    'src': f'https://eu.zonerama.com/photos/{pid}_1200x800_16.jpg',
                                    'link': f'https://eu.zonerama.com/11skautskyoddil/Photo/{aid}/{pid}'
                                })
                    except Exception as e:
                        print(f"Varování: Chyba při načítání alba {aid}: {e}")
        except Exception as e:
            print(f"Varování: Chyba při čtení složky {f['year_label']}: {e}")

    if all_photos and save_file:
        with open(JSON_PATH, 'w', encoding='utf-8') as out:
            json.dump(all_photos, out, ensure_ascii=False, indent=2)
        print(f"✅ Uloženo {len(all_photos)} fotek ze Zoneramy do {JSON_PATH}")
        copy_json_to_targets()
    return all_photos

def get_zonerama_photos():
    if os.path.exists(JSON_PATH):
        try:
            with open(JSON_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data:
                    return data
        except Exception:
            pass
    return fetch_all_photos(save_file=True)

def get_starter_pool(limit_per_album=5):
    photos = get_zonerama_photos()
    by_album = {}
    for p in photos:
        by_album.setdefault(p['album_id'], []).append(p)
    starter = []
    for aid, plist in by_album.items():
        starter.extend(plist[:limit_per_album])
    return starter

def copy_json_to_targets():
    base_dir = os.path.dirname(__file__)
    targets = [
        os.path.join(base_dir, 'verzeA', 'zonerama_latest_photos.json'),
        os.path.join(base_dir, 'verzeB', 'zonerama_latest_photos.json'),
        os.path.join(base_dir, 'wp_theme_build', 'zonerama_latest_photos.json')
    ]
    if not os.path.exists(JSON_PATH):
        return
    for tgt in targets:
        tdir = os.path.dirname(tgt)
        if os.path.exists(tdir):
            shutil.copy2(JSON_PATH, tgt)

if __name__ == '__main__':
    print("🔄 Spouštím synchronizaci fotek ze Zoneramy...")
    photos = fetch_all_photos(save_file=True)
    starter = get_starter_pool(5)
    print(f"Celkem fotek: {len(photos)}, velikost startovního poolu: {len(starter)}")
