import urllib.request, json, urllib.parse, ssl

ctx = ssl._create_unverified_context()
def search_osm(query):
    url = f'https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query)}&format=json&addressdetails=1'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = json.loads(urllib.request.urlopen(req, context=ctx).read().decode('utf-8'))
        print(f'=== OSM search: "{query}" ===')
        for r in res[:5]:
            print(f'  {r.get("display_name")}: lat={r.get("lat")}, lon={r.get("lon")}')
    except Exception as e:
        print(query, e)

search_osm('Valcha, České Budějovice')
search_osm('Skaut České Budějovice')
search_osm('loděnice České Budějovice')
