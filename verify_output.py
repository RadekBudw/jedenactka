import re

for v in ['verzeA/index.html', 'verzeB/index.html', 'verzeA/vedeni.html', 'verzeB/vedeni.html']:
    with open(v, 'r', encoding='utf-8') as f:
        t = f.read()
    print(f"\n==================== {v} ====================")
    # 1. Zonerama images
    zr = re.findall(r'zonerama_\w+\.jpg', t)
    print(f"  Zonerama photo refs: {len(zr)} (unique: {set(zr)})")
    
    # 2. Logo emblem
    emblems = re.findall(r'logo_emblem\.png', t)
    print(f"  logo_emblem.png refs: {len(emblems)}")
    
    # 3. Header check
    header_m = re.search(r'<header[^>]*>.*?</header>', t, re.DOTALL)
    if header_m:
        header = header_m.group(0)
        has_junak = 'Junák' in header or 'junák' in header
        has_flag = 'Černo-žlutá vlajka 11. oddílu' in header
        print(f"  Header has Junák text: {has_junak}")
        print(f"  Header has flag next to Junák: {has_flag}")
        print(f"  Header has 'Loděnice Valcha': {'Loděnice Valcha' in header or 'loděnice Valcha' in header}")
    
    # 4. Loděnice Valcha across document
    lv = re.findall(r'loděnic[ea]\s+valch[ay]', t, re.I)
    print(f"  Total 'Loděnice Valcha' occurrences in page: {len(lv)}")
    if lv:
        print(f"    Sample: {lv[:3]}")
    
    # 5. Mobile menu close on click check
    has_close = 'mobileMenu' in t and 'classList.add(\'hidden\')' in t
    print(f"  Mobile menu closes on link click: {has_close}")
