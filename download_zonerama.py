import os, urllib.request, ssl

ctx = ssl._create_unverified_context()
os.makedirs('zonerama_photos', exist_ok=True)

test_photos = [
    ('kanal_1', '622077767', 'Trénink na slalomovém kanále České Vrbné'),
    ('kanal_2', '622078363', 'Kajaky a kanoe na divoké vodě'),
    ('voda_1', '633496763', 'Společná voda 11. oddílu'),
    ('voda_2', '633496782', 'Pramice a vodácká výprava na řece'),
    ('voda_3', '633496771', 'Vodáci na řece Vltavě'),
    ('3jezy_1', '578833574', 'Závod Napříč Prahou přes tři jezy'),
    ('3jezy_2', '578833613', 'Posádka 11. oddílu na startu závodu'),
    ('tabor_1', '648696810', 'Letní tábor vodních skautů Labská Stráň'),
    ('tabor_2', '663923417', 'Táborový život a podsadové stany'),
    ('valcha_1', '673608923', 'Schůzka a zázemí na Valši')
]

for name, pid, caption in test_photos:
    target_path = os.path.join('zonerama_photos', f'{name}_{pid}.jpg')
    if not os.path.exists(target_path):
        url = f'https://eu.zonerama.com/photos/{pid}_1200x800_16.jpg'
        print(f"Downloading {pid} ({caption})...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req, context=ctx).read()
            with open(target_path, 'wb') as f:
                f.write(data)
            print(f"  OK! Size: {len(data)} bytes")
        except Exception as e:
            print(f"  Failed: {e}")
    else:
        print(f"Already exists: {target_path}")
