import urllib.request, ssl, re, json
ctx = ssl._create_unverified_context()
url = 'https://eu.zonerama.com/11skautskyoddil/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8', errors='ignore')

# Check script tags for data
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print('Total scripts:', len(scripts))
for i, s in enumerate(scripts):
    if 'photos' in s or 'Album' in s or 'Folder' in s:
        print(f'Script {i} contains keywords, len:', len(s))
        # let's look for json or array
        for line in s.split('\n'):
            if any(k in line for k in ['Album', 'Folder', 'photos', 'url', 'Id']):
                if len(line.strip()) < 300:
                    print('  ', line.strip())

# Check for API or JSON data inside HTML
api_calls = re.findall(r'https?://[^\s"\'<>]+(?:api|json|album)[^\s"\'<>]*', html, re.I)
print('API calls in html:', list(set(api_calls))[:10])
