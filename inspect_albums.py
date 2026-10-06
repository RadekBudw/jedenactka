import urllib.request, ssl, re, json, html

ctx = ssl._create_unverified_context()
def get_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    return urllib.request.urlopen(req, context=ctx).read().decode('utf-8', errors='ignore')

albums_to_check = [
    ('15374156', 'Kanál (divoká voda)'),
    ('15582766', 'Společná voda'),
    ('14180722', '3 Jezy Praha'),
    ('15758185', 'Tábor Labská Stráň'),
    ('14180805', 'Výprava'),
    ('16719506', 'Schůzky Valcha')
]

for aid, name in albums_to_check:
    page = get_url(f'https://eu.zonerama.com/11skautskyoddil/Album/{aid}')
    # Extract photos
    pids = list(dict.fromkeys(re.findall(r'photos/(\d+)_[^{}]*', page)))
    print(f"\nAlbum {aid} ({name}): found {len(pids)} photo IDs")
    print(f"  Sample IDs: {pids[:6]}")
