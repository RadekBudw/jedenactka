import urllib.request, ssl, json
from bs4 import BeautifulSoup

ctx = ssl._create_unverified_context()
urls = {
    'oddil': 'https://jedenactka.skauting.cz/index.php/oddil/',
    'blog': 'https://jedenactka.skauting.cz/index.php/blog/',
    'rozpis_skauti': 'https://jedenactka.skauting.cz/index.php/barka/rozpis-schuzek-skautu/',
    'rozpis_vlcata': 'https://jedenactka.skauting.cz/index.php/toulava-smecka/rozpis-schuzek/',
    'skautske_maily': 'https://jedenactka.skauting.cz/index.php/barka/skautske-maily/',
    'terminovnik': 'https://jedenactka.skauting.cz/index.php/terminovnik/',
    'archiv_akci': 'https://jedenactka.skauting.cz/index.php/oddil/archiv-akci/',
    'vlcacke_fotky': 'https://jedenactka.skauting.cz/index.php/vlcacke-fotky/'
}

results = {}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as res:
            soup = BeautifulSoup(res.read(), 'html.parser')
            content = soup.find('main') or soup.find(class_=lambda c: c and 'entry-content' in c) or soup.body
            
            # extract text
            text = content.get_text('\n', strip=True) if content else ''
            # extract links
            links = []
            if content:
                for a in content.find_all('a'):
                    t = a.get_text(strip=True)
                    h = a.get('href')
                    if h and not h.startswith('#') and 'jedenactka.skauting.cz' not in h:
                        links.append({'text': t, 'href': h})
                    elif h and ('drive.google' in h or 'photos' in h or 'flickr' in h or 'docs.google' in h):
                        links.append({'text': t, 'href': h})
            
            results[name] = {
                'url': url,
                'text': text,
                'links': links
            }
            print(f'Done {name}')
    except Exception as e:
        print(f'Error {name}: {e}')

with open('subpages_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print('Saved all to subpages_data.json')
