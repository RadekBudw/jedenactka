import urllib.request
import os
import sys
from PIL import Image
import io

# Zajištění UTF-8 výstupu
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

photos_to_download = [
    {
        'filename': 'zonerama_hero_1.jpg',
        'id': 588905967,
        'tag': 'Vánoce na Švýcaráku',
        'sub': 'Zimní výprava v Novohradských horách',
        'title': 'Tradiční vánoční setkání oddílu na srubové základně Švýcarák'
    },
    {
        'filename': 'zonerama_hero_2.jpg',
        'id': 588905978,
        'tag': 'Vánoce na Švýcaráku',
        'sub': 'Prskavky & vánoční stromeček',
        'title': 'Kouzlo Vánoc, oddílové zvyky a dárky v zasněžených lesích'
    },
    {
        'filename': 'zonerama_hero_3.jpg',
        'id': 578837518,
        'tag': 'Výprava všech lidí na zemi',
        'sub': 'Podzimní výprava',
        'title': 'Společné dobrodružství a setkání generací vodních skautů'
    },
    {
        'filename': 'zonerama_hero_4.jpg',
        'id': 578837504,
        'tag': 'Výprava všech lidí na zemi',
        'sub': 'Táborový oheň v přírodě',
        'title': 'Špekáčky, kytary a přátelství v údolí řeky Vltavy'
    },
    {
        'filename': 'zonerama_hero_5.jpg',
        'id': 578835269,
        'tag': 'Brigáda na Švýcaráku',
        'sub': 'Pomoc základně',
        'title': 'Příprava palivového dříví na zimu a údržba oddílového srubu'
    },
    {
        'filename': 'zonerama_hero_6.jpg',
        'id': 578833613,
        'tag': '3 Jezy Praha 2025',
        'sub': 'Start posádky pod Vyšehradem',
        'title': 'Reprezentace 11. oddílu na legendárním závodě Napříč Prahou'
    },
    {
        'filename': 'zonerama_hero_7.jpg',
        'id': 578833750,
        'tag': '3 Jezy Praha 2025',
        'sub': 'Šlajsna na Staroměstském jezu',
        'title': 'Průjezd vorovou propustí v peřejích historického centra Prahy'
    },
    {
        'filename': 'zonerama_hero_8.jpg',
        'id': 622078363,
        'tag': 'Slalomový kanál 2026',
        'sub': 'České Vrbné • divoká voda',
        'title': 'Trénink pádlování a stability posádek mezi brankami'
    },
    {
        'filename': 'zonerama_hero_9.jpg',
        'id': 633496771,
        'tag': 'Společná voda 2026',
        'sub': 'Flotila na řece Vltavě',
        'title': 'Putování na kanoích po jihočeských řekách a vodácká kamarádství'
    },
    {
        'filename': 'zonerama_hero_10.jpg',
        'id': 648696810,
        'tag': 'Tábor Labská Stráň 2026',
        'sub': 'Lezení v pískovcích',
        'title': 'Skalní lezení, lanové techniky a odvaha v Labském kaňonu'
    }
]

targets = ['verzeA', 'verzeB']

for item in photos_to_download:
    url = f"https://eu.zonerama.com/photos/{item['id']}_1200x800_16.jpg"
    print(f"Stahuji {item['filename']} (ID {item['id']})...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        raw_bytes = resp.read()
    
    # Optimize with Pillow
    img = Image.open(io.BytesIO(raw_bytes))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    out_buf = io.BytesIO()
    img.save(out_buf, format='JPEG', quality=85, optimize=True, progressive=True)
    optimized_bytes = out_buf.getvalue()
    
    orig_kb = len(raw_bytes) // 1024
    opt_kb = len(optimized_bytes) // 1024
    print(f"  Optimalizováno: {orig_kb} KB -> {opt_kb} KB (úspora {orig_kb - opt_kb} KB)")
    
    for t in targets:
        dest_path = os.path.join(t, item['filename'])
        with open(dest_path, 'wb') as f:
            f.write(optimized_bytes)
        print(f"  -> Uloženo do {dest_path}")

print("\nHotovo! Všech 10 fotek staženo a optimalizováno.")
