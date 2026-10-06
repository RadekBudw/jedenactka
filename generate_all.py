# -*- coding: utf-8 -*-
import json, os, re

with open('leaders.json', encoding='utf-8') as f:
    leaders = json.load(f)

def h(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

TERMINOVNIK_BARKA = [
    {"date": "19.–20. 9.", "title": "Brigáda na Švýcaráku", "desc": "Pomoc správcům základny a příprava lodního materiálu na novou sezónu.", "type": "Práce & Zábava", "icon": "fa-hammer"},
    {"date": "28. 9.", "title": "Závod přes tři jezy (Praha)", "desc": "Celostátní vodácký závod historickým centrem Prahy. Naše posádky na startu!", "type": "Vodácký závod", "icon": "fa-trophy"},
    {"date": "10.–11. 10.", "title": "Přespání na Valše", "desc": "Noční loděnice, táborák, oddílová rada a první společné zážitky v loděnici.", "type": "Oddílovka", "icon": "fa-campground"},
    {"date": "24. 10.", "title": "Jednodenní podzimní výprava", "desc": "Pěší terénní výprava do jihočeské přírody spojená s hrou a orientací.", "type": "Výprava", "icon": "fa-compass"},
    {"date": "13.–14. 11.", "title": "Benediktýnka", "desc": "Tradiční vícedenní výprava s přespáním na chatě v lesích a noční etapovou hrou.", "type": "Víkendovka", "icon": "fa-fire"},
    {"date": "27.–28. 11.", "title": "Podzimní výprava", "desc": "Vícedenní putování posádek Bárky za každého počasí.", "type": "Víkendovka", "icon": "fa-person-hiking"},
    {"date": "27.–29. 12.", "title": "Oddílová Vánočka", "desc": "Vánoční zvyky, cukroví, dárky a bilancování uplynulého roku v teple klubovny.", "type": "Tradice", "icon": "fa-tree"},
    {"date": "16. 1.", "title": "Lezecká stěna Lanovka", "desc": "Zimní tělocvik na umělé lezecké stěně v Českých Budějovicích s lany a úvazky.", "type": "Sport", "icon": "fa-mountain"},
    {"date": "18.–21. 2.", "title": "Jarky (Jarní prázdniny)", "desc": "Čtyřdenní zimní expedice na sněhu s běžkami a zimními hrami.", "type": "Zimní expedice", "icon": "fa-snowflake"}
]

TERMINOVNIK_VLCATA = [
    {"date": "11.–13. 9.", "title": "Zahajovací výprava (Terčino údolí)", "desc": "Švýcarská chata, rozloučení se staršími vlčáky a jejich přechod do Bárky.", "type": "Výprava", "icon": "fa-compass"},
    {"date": "10. 10.", "title": "Podzimní jednodenka", "desc": "Sobotní dobrodružství v okolí Budějovic, hry a luštění šifer v lese.", "type": "Jednodenka", "icon": "fa-map"},
    {"date": "6.–7. 11.", "title": "Vlčácká přespávačka", "desc": "Noc v klubovně na Valše plná her, promítání a společného vaření.", "type": "Klubovna", "icon": "fa-bed"},
    {"date": "5. 12.", "title": "Mikulášská jednodenka", "desc": "Pátrání po stopách Mikuláše, čertovské stezky a nadílka pro šikovná vlčata.", "type": "Jednodenka", "icon": "fa-cookie-bite"},
    {"date": "27.–29. 12.", "title": "Vlčácká Vánočka", "desc": "Kouzlo Vánoc se smečkou, oddílové zvyky a vyhlášení nejlepších vlčat roku.", "type": "Tradice", "icon": "fa-tree"},
    {"date": "23. 1.", "title": "Zimní jednodenka", "desc": "Hry na sněhu, bobování a stopování zvěře v zimní krajině.", "type": "Jednodenka", "icon": "fa-snowflake"}
]

BLOG_POSTS = [
    {
        "title": "Zahajovací výprava v Terčině údolí",
        "date": "21. září 2026",
        "tag": "Toulavá smečka & Bárka",
        "desc": "Od pátku do neděle jsme byli na vlčácké výpravě na Švýcarské Chatě v Terčině údolí, kde se vlčácká paluba rozloučila s nejstaršími vlčáky, kteří posléze přešli do skautské paluby. Výprava byla stylizována do tématu záchrany dvou mimozemšťanů, kteří přistáli na Zemi. Večer jsme navíc měli interaktivní program o Helen Kellerové.",
        "img": "foto_2.jpg",
        "link": "https://jedenactka.skauting.cz/index.php/blog/"
    },
    {
        "title": "Závod přes tři jezy 2025 – Skauti na 5. místě!",
        "date": "15. listopadu 2025",
        "tag": "Vodácký závod",
        "desc": "Jako vodní skauti jsme nemohli chybět na tradičním závodě přes tři jezy v Praze, založeném v roce 1933. Posádky jsme nasadili hned do 4 kategorií: Skauti skončili na fantastickém 5. místě (Davído, Sekáč, Werran, Jojo, Pírko), Vlčata 15. místo, posádka do 18 let 7. místo a veteráni nad 18 let 11. místo!",
        "img": "foto_1.jpg",
        "link": "https://eu.zonerama.com/11skautskyoddil/Album/14180722"
    },
    {
        "title": "VVLnZ 2025 – Výprava Všech Lidí na Zemi",
        "date": "15. listopadu 2025",
        "tag": "Tradice & Rodiče",
        "desc": "Tradiční výprava všech lidí na zemi letos vedla malebným údolím okolo řeky Vltavy. Špekáčky, hry v přírodě, zpěv a hlavně vzácné shledání se starším vedením oddílu, bývalými členy i rodiči kluků. Děkujeme všem za skvělou účast a těšíme se zase za rok!",
        "img": "foto_4.jpg",
        "link": "https://eu.zonerama.com/11skautskyoddil/Album/14180805"
    },
    {
        "title": "Sraz jihočeských vodních skautů & Krčín",
        "date": "8. října 2025",
        "tag": "Vodní skauting",
        "desc": "O víkendu jsme pořádali sraz vodních skautů jihočeského kraje. Celá akce šla v duchu rybníkářství a potkali jsme i legendárního Jakuba Krčína. Na základně Lišky jsme se spojili s 2. oddílem Albatros, Přístavem Třináctka Opařany a 5. oddílem Stříbrné rybky.",
        "img": "foto_5.jpg",
        "link": "https://www.rajce.idnes.cz/rybky/album/luznicanka-2025"
    }
]

print("Loaded base datasets successfully.")
