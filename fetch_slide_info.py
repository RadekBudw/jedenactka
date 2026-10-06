import urllib.request, ssl, re, json
ctx = ssl._create_unverified_context()
url = 'https://eu.zonerama.com/11skautskyoddil/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8', errors='ignore')

slides = re.findall(r'<a href="https://eu\.zonerama\.com/11skautskyoddil/Photo/(\d+)/(\d+)"><img[^>]*data-image="([^"]+)"', html)
print('Found profile slides:', len(slides))
for album_id, photo_id, img_tpl in slides:
    print(f'Album: {album_id}, Photo: {photo_id}, Template: {img_tpl}')

# Let's inspect each album page to get the album title and date!
albums = list(set([s[0] for s in slides]))
print('\nUnique albums in featured slides:', albums)
for alb in albums:
    alb_url = f'https://eu.zonerama.com/11skautskyoddil/Album/{alb}'
    try:
        alb_req = urllib.request.Request(alb_url, headers={'User-Agent': 'Mozilla/5.0'})
        alb_html = urllib.request.urlopen(alb_req, context=ctx).read().decode('utf-8', errors='ignore')
        # Title of album
        title_m = re.search(r'<title>([^<]+)</title>', alb_html)
        title = title_m.group(1).replace(' | Zonerama.com', '') if title_m else alb
        # Date of album
        date_m = re.search(r'<span class="album-info-date">([^<]+)</span>', alb_html) or re.search(r'(\d{1,2}\.\s*\d{1,2}\.\s*\d{4})', alb_html)
        date = date_m.group(1) if date_m else ''
        print(f'Album {alb}: Title = "{title}", Date = "{date}"')
    except Exception as e:
        print(f'Album {alb} error:', e)
