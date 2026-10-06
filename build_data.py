import json, re, datetime, subprocess, os

with open('leaders.json', encoding='utf-8') as f:
    leaders = json.load(f)

def h(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def get_git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "780deb9"

def get_git_commit_count():
    try:
        return int(subprocess.check_output(["git", "rev-list", "--count", "HEAD"], stderr=subprocess.DEVNULL).decode().strip())
    except Exception:
        return 8

def get_app_version():
    try:
        status = subprocess.check_output(["git", "status", "--porcelain"], stderr=subprocess.DEVNULL).decode().strip()
        count = get_git_commit_count()
        if status:
            count += 1
        return f"1.2.{count}"
    except Exception:
        return "1.2.9"

def get_version_meta_html():
    commit = get_git_commit()
    version = get_app_version()
    now = datetime.datetime.now()
    iso_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"""  <!-- NEVIDITELNÉ METADATA VERZOVÁNÍ -->
  <meta name="app-version" content="{version}">
  <meta name="build-timestamp" content="{iso_time}">
  <meta name="git-commit" content="{commit}">
  <meta name="generator" content="Antigravity / 11. oddíl vodních skautů ČB">
  <!-- JEDENACTKA_VERSION: ver={version} git={commit} time={iso_time} -->"""

def save_version_json():
    version = get_app_version()
    commit = get_git_commit()
    now = datetime.datetime.now()
    data = {
        "app_version": version,
        "git_commit": commit,
        "build_timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "build_display": now.strftime("%d.%m.%Y %H:%M")
    }
    with open('version.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_index_html_version():
    try:
        if not os.path.exists('index.html'):
            return
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        version = get_app_version()
        commit = get_git_commit()
        now = datetime.datetime.now()
        iso_time = now.strftime("%Y-%m-%d %H:%M:%S")
        disp_time = now.strftime("%d.%m.%Y %H:%M")

        meta_replacement = f"""  <!-- NEVIDITELNÉ METADATA VERZOVÁNÍ -->
  <meta name="app-version" content="{version}">
  <meta name="build-timestamp" content="{iso_time}">
  <meta name="git-commit" content="{commit}">
  <meta name="generator" content="Antigravity / 11. oddíl vodních skautů ČB">
  <!-- JEDENACTKA_VERSION: ver={version} git={commit} time={iso_time} -->"""

        content = re.sub(
            r'  <!-- NEVIDITELNÉ METADATA VERZOVÁNÍ -->.*?<!-- JEDENACTKA_VERSION:[^>]*-->',
            meta_replacement,
            content,
            flags=re.DOTALL
        )

        content = re.sub(
            r'<span class="text-slate-400">Verze:[^<]*</span>',
            f'<span class="text-slate-400">Verze: {version} ({commit})</span>',
            content
        )
        content = re.sub(
            r'<span class="text-slate-400">Aktualizováno:[^<]*</span>',
            f'<span class="text-slate-400">Aktualizováno: {disp_time}</span>',
            content
        )

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Chyba při aktualizaci index.html: {e}")


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

FAQ_ITEMS = [
    {
        "q": "Musí syn umět hned plavat, když nastupuje k vodním skautům?",
        "a": "Nemusí být závodní plavec ani mistr ve vodě. Na všech vodáckých aktivitách (pramice P550, kanoe) mají všichni chlapci povinně certifikované záchranné plovací vesty s vysokým výtlakem, a to bez výjimky. V začátcích se s vodou seznamují v klidných úsecích řeky a pod přímým dohledem dospělých kormidelníků. Plavecké dovednosti i jistotu na vodě rozvíjíme postupně a bezpečně.",
        "icon": "fa-life-ring"
    },
    {
        "q": "Jak probíhají první schůzky a lze si oddíl nezávazně vyzkoušet?",
        "a": "Ano, přesně tak to doporučujeme! První 2 až 3 schůzky jsou pro každého nováčka zcela nezávazné a zdarma. Kluk si vezme běžné sportovní oblečení, přijde se podívat do loděnice na Valše, zapojí se do her a pozná svou budoucí posádku. Teprve když se rozhodne pokračovat, domluvíte se s kapitánem na registraci.",
        "icon": "fa-compass"
    },
    {
        "q": "Kolik stojí členství a jaká je finanční náročnost oddílu?",
        "a": "Skauting patří k finančně nejdostupnějším volnočasovým aktivitám. Roční členský příspěvek (registrace) činí přibližně 1 200 – 1 500 Kč za celý školní rok (zahrnuje pojištění, metodické materiály i celoroční provoz loděnice). Běžné víkendové výpravy stojí cca 200–450 Kč (jízdné a jídlo) a třítýdenní letní tábor na řece bývá zlomkem ceny běžných komerčních táborů.",
        "icon": "fa-coins"
    },
    {
        "q": "Jaké vybavení a oblečení musíme synovi koupit do začátku?",
        "a": "Do začátku synovi nekupujte nic speciálního! Na schůzky stačí pohodlné sportovní oblečení a přezůvky do klubovny, v teplých měsících boty do vody s pevnou patou, ručník a náhradní suché tričko. Záchranné vesty, pramice i pádla plně zapůjčuje oddíl. Vlastní vodácký kroj a oddílový žlutý šátek se pořizuje až po několika měsících před skautským slibem.",
        "icon": "fa-shirt"
    },
    {
        "q": "Kdo se o kluky stará a jaká je kvalifikace vedoucích?",
        "a": "O kluky se stará stabilní tým 34 zkušených vedoucích a lodivodů. Naši vedoucí procházejí akreditovaným vzdělávacím systémem Junáka – mají čekatelské a vůdcovské zkoušky a kapitánské zkoušky pro vedení plavidel na vodních cestách. Na vícedenních výpravách a táborech je vždy přítomen zdravotník zotavovacích akcí (ZZA akreditovaný MŠMT).",
        "icon": "fa-user-shield"
    },
    {
        "q": "Jaká jsou pravidla ohledně mobilních telefonů a elektroniky?",
        "a": "Učíme kluky vnímat svět kolem sebe, přírodu, vodu a kamarády z očí do očí. Během schůzek i víkendových výprav proto platí pravidlo, že mobilní telefony odpočívají vypnuté v batohu. Rodiče mají v případě potřeby vždy přímý telefonní kontakt na garanta schůzky nebo vedoucího výpravy.",
        "icon": "fa-mobile-screen"
    },
    {
        "q": "V čem se vodní skauti liší od klasických (suchozemských)?",
        "a": "Máme stejné skautské hodnoty a desatero zákonů, ale naším živlem je řeka. Místo oddílů máme paluby (Toulavá smečka, Bárka, Roverská VěTeV) a místo družin posádky. Učíme se kormidlovat legendární pramice P550, vázat námořní uzly, sjíždět jezy a tábořit na břehu řeky. Nosíme modré vodácké kroje a oddílové žluté šátky.",
        "icon": "fa-anchor"
    }
]

print("Datasets ready.")
