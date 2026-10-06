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

def get_search_index(prefix=""):
    items = [
        {
            "title": "Schůzky oddílu (Rozpis 2026/2027)",
            "desc": "Toulavá smečka (vlčata): Středa 16:00–18:00 • Bárka (vodní skauti): Čtvrtek 16:00–18:00 na loděnici Valcha.",
            "category": "Schůzky & Program",
            "url": f"{prefix}#pro-rodice",
            "icon": "fa-clock",
            "keywords": "schůzky středa čtvrtek kdy toulavá smečka bárka program časy"
        },
        {
            "title": "Loděnice a klubovna Valcha",
            "desc": "Stromovka 3, České Budějovice • GPS: 48.9720617N, 14.4690989E • Jak se k nám dostat na kole, pěšky i MHD.",
            "category": "Klubovna & Mapa",
            "url": f"{prefix}#klubovna",
            "icon": "fa-map-location-dot",
            "keywords": "valcha valši loděnice klubovna adresa kde mapa poloha stromovka gps doprava"
        },
        {
            "title": "Pro rodiče: Informace pro nováčky & fotogalerie",
            "desc": "Co s sebou na schůzky, oddílový kroj, platby, přihlášky a odkaz na kompletní fotogalerii na Zonerama.",
            "category": "Pro rodiče",
            "url": f"{prefix}#pro-rodice",
            "icon": "fa-heart-pulse",
            "keywords": "rodiče nováčci přihláška kroj poplatky vybavení co s sebou fotky zonerama galerie"
        },
        {
            "title": "Nábor nových členů do oddílu",
            "desc": "Přijímáme kluky i holky do vlčat (6–10 let) a skautů (11–15 let). Přijďte se podívat na nezávaznou zkušební schůzku!",
            "category": "Nábor",
            "url": f"{prefix}#nabor",
            "icon": "fa-user-plus",
            "keywords": "nábor přihláška noví členové chci se přidat zkušební schůzka jak se stát skautem"
        },
        {
            "title": "O 11. oddílu vodních skautů České Budějovice",
            "desc": "Historie oddílu od roku 1990, tradice černo-žluté vlajky, vodácká výchova a středisko VAVÉHA.",
            "category": "O oddílu",
            "url": f"{prefix}#oddil",
            "icon": "fa-anchor",
            "keywords": "o oddílu historie tradice vlajka černo žlutá vaveha středisko vodní skauting"
        },
        {
            "title": "Naše paluby (Vlčata, Skauti, Roveři, Klub)",
            "desc": "Toulavá smečka (6–10 let), Bárka (11–15 let), Roverská VěTeV (15+ let) a Klub 11. oddílu (dospělí a přátelé oddílu).",
            "category": "Paluby oddílu",
            "url": f"{prefix}#paluby",
            "icon": "fa-ship",
            "keywords": "paluby toulavá smečka vlčata bárka skauti větev roveři klub oddílu věkové kategorie družiny"
        },
        {
            "title": "Kontakty a vedení oddílu",
            "desc": "Kontaktní e-maily, telefonní čísla na kapitány a vedení jednotlivých palub, bankovní účet a IČO.",
            "category": "Kontakty",
            "url": f"{prefix}#kontakty",
            "icon": "fa-address-book",
            "keywords": "kontakty telefon email kapitán spojení kde nás najdete bankovní spojení transparentní účet"
        },
        {
            "title": "Kompletní tým vedení (34 vedoucích a rádců)",
            "desc": "Přehled všech 34 činovníků, rádců posádek, instruktorů a garantů se specializacemi a přezdívkami.",
            "category": "Vedení oddílu",
            "url": f"{'vedeni.html' if prefix == '' else prefix + 'vedeni.html'}",
            "icon": "fa-users",
            "keywords": "vedení vedoucí rádci činovníci rádce instruktor kapitán tým 34 vedoucích"
        }
    ]

    for ev in TERMINOVNIK_BARKA:
        items.append({
            "title": f"{ev['title']} ({ev['date']})",
            "desc": f"Bárka (vodní skauti) • {ev['desc']}",
            "category": "Termínovník: Bárka",
            "url": f"{prefix}#terminovnik",
            "icon": ev.get('icon', 'fa-calendar-day'),
            "keywords": f"{ev['title']} {ev['date']} {ev['desc']} bárka akce výprava termínovník"
        })

    for ev in TERMINOVNIK_VLCATA:
        items.append({
            "title": f"{ev['title']} ({ev['date']})",
            "desc": f"Toulavá smečka (vlčata) • {ev['desc']}",
            "category": "Termínovník: Vlčata",
            "url": f"{prefix}#terminovnik",
            "icon": ev.get('icon', 'fa-calendar-day'),
            "keywords": f"{ev['title']} {ev['date']} {ev['desc']} vlčata akce výprava termínovník"
        })

    for leader in leaders:
        nick = leader.get('nickname') or ''
        name = leader.get('name') or ''
        role = leader.get('role') or ''
        deck = leader.get('deck') or ''
        email = leader.get('email') or ''
        phone = leader.get('phone') or ''
        l_id = leader.get('id') or ''

        vedeni_url = 'vedeni.html' if prefix == '' else prefix + 'vedeni.html'
        target_url = f"{vedeni_url}#leader-{l_id}" if l_id else vedeni_url

        display_title = f"{nick} ({name})" if nick and nick != name else (nick or name)
        items.append({
            "title": display_title,
            "desc": f"{role} • Paluba: {deck}" + (f" • {email}" if email else ""),
            "category": "Vedení oddílu",
            "url": target_url,
            "icon": "fa-user-tag",
            "keywords": f"{nick} {name} {role} {deck} {email} {phone} vedoucí rádce kontakt"
        })

    return items

def get_search_modal_html(prefix=""):
    return f"""  <!-- MODAL VYHLEDÁVÁNÍ -->
  <div id="searchModal" class="fixed inset-0 z-[100] hidden bg-slate-950/75 backdrop-blur-sm flex items-start justify-center p-3 sm:p-6 md:pt-16 overflow-y-auto" onclick="if(event.target===this) closeSearchModal();">
    <div class="relative w-full max-w-2xl bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 overflow-hidden transform transition-all">
      
      <!-- HLAVIČKA FORMULÁŘE -->
      <form id="siteSearchForm" action="{prefix}index.html" method="get" class="flex items-center gap-3 px-5 py-4 border-b border-slate-100 dark:border-slate-800 bg-slate-50/60 dark:bg-slate-900/60" onsubmit="handleSearchSubmit(event)">
        <i class="fa-solid fa-magnifying-glass text-slate-400 text-lg"></i>
        <input id="siteSearchInput" type="search" name="s" placeholder="Hledat schůzky, Valchu, termíny, rádce, kontakty..." class="w-full bg-transparent text-slate-900 dark:text-white placeholder-slate-400 text-base sm:text-lg focus:outline-none" autocomplete="off" oninput="onSearchInput(this.value)">
        <button type="button" onclick="closeSearchModal()" class="p-1.5 rounded-xl text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 text-xs transition-colors cursor-pointer" title="Zavřít (Esc)">
          <kbd class="px-2 py-1 bg-white dark:bg-slate-800 rounded text-[11px] border border-slate-200 dark:border-slate-700 font-mono shadow-2xs">ESC</kbd>
        </button>
      </form>

      <!-- VÝSLEDKY & DOPORUČENÉ KATEGORIE -->
      <div id="searchResultsContainer" class="max-h-[60vh] overflow-y-auto p-4 sm:p-5 space-y-4">
        <!-- Vykresluje se dynamicky přes JS -->
      </div>

      <!-- ZÁPATÍ MODALU -->
      <div class="px-5 py-3.5 bg-slate-50 dark:bg-slate-950/60 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-xs text-slate-400">
        <div class="flex items-center gap-2">
          <span>Stiskem <kbd class="px-1.5 py-0.5 bg-white dark:bg-slate-800 border rounded font-mono text-[10px]">Enter</kbd> prohledáte celý archiv</span>
        </div>
        <button type="submit" form="siteSearchForm" class="text-brand-sky hover:underline font-bold inline-flex items-center gap-1 cursor-pointer">
          <span>Vyhledat</span>
          <i class="fa-solid fa-arrow-right text-[10px]"></i>
        </button>
      </div>

    </div>
  </div>"""

def get_search_script_js(prefix="", is_subpage=False):
    search_data_json = json.dumps(get_search_index(prefix), ensure_ascii=False)
    return f"""  <script>
    // Search data index
    const SEARCH_INDEX = {search_data_json};

    function removeAccents(str) {{
      return (str || '').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
    }}

    function openSearchModal(initialQuery = '') {{
      const modal = document.getElementById('searchModal');
      const input = document.getElementById('siteSearchInput');
      if (!modal || !input) return;

      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';

      if (initialQuery) {{
        input.value = initialQuery;
      }}
      input.focus();
      onSearchInput(input.value);
    }}

    function closeSearchModal() {{
      const modal = document.getElementById('searchModal');
      if (!modal) return;
      modal.classList.add('hidden');
      document.body.style.overflow = '';
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        closeSearchModal();
      }}
      // Ctrl+K nebo Cmd+K nebo klávesa /
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {{
        e.preventDefault();
        openSearchModal();
      }}
      if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {{
        e.preventDefault();
        openSearchModal();
      }}
    }});

    function onSearchInput(query) {{
      const container = document.getElementById('searchResultsContainer');
      if (!container) return;

      const q = removeAccents(query.trim());

      if (!q) {{
        // Výchozí stav – doporučené rychlé odkazy a kategorie
        container.innerHTML = `
          <div class="space-y-4">
            <div class="text-xs font-bold uppercase tracking-wider text-slate-400">Rychlé volby & doporučené sekce</div>
            <div class="flex flex-wrap gap-2">
              <button type="button" onclick="quickFillSearch('schůzky')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 transition-colors cursor-pointer">🕒 Schůzky 2026/27</button>
              <button type="button" onclick="quickFillSearch('Valcha')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 transition-colors cursor-pointer">⚓ Loděnice Valcha</button>
              <button type="button" onclick="quickFillSearch('termínovník')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 transition-colors cursor-pointer">📅 Termínovník výprav</button>
              <button type="button" onclick="quickFillSearch('Hopík')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 transition-colors cursor-pointer">👤 Hopík (kapitán)</button>
              <button type="button" onclick="quickFillSearch('Toulavá smečka')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 transition-colors cursor-pointer">🐺 Vlčata</button>
              <button type="button" onclick="quickFillSearch('Bárka')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 transition-colors cursor-pointer">⛵ Skauti (Bárka)</button>
            </div>
            
            <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800">
              <div class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Časté dotazy</div>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm">
                <a href="{prefix}#pro-rodice" onclick="closeSearchModal()" class="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 hover:bg-sky-50 dark:hover:bg-slate-800 transition-all flex items-center gap-3">
                  <div class="w-8 h-8 rounded-xl bg-amber-100 dark:bg-amber-950/60 text-amber-600 flex items-center justify-center shrink-0">
                    <i class="fa-solid fa-heart-pulse text-xs"></i>
                  </div>
                  <div>
                    <div class="font-bold text-slate-800 dark:text-slate-200 text-xs">Informace pro rodiče</div>
                    <div class="text-[11px] text-slate-400">Rozpis, vybavení, fotky</div>
                  </div>
                </a>
                <a href="{prefix}#klubovna" onclick="closeSearchModal()" class="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 hover:bg-sky-50 dark:hover:bg-slate-800 transition-all flex items-center gap-3">
                  <div class="w-8 h-8 rounded-xl bg-sky-100 dark:bg-sky-950/60 text-brand-sky flex items-center justify-center shrink-0">
                    <i class="fa-solid fa-map-location-dot text-xs"></i>
                  </div>
                  <div>
                    <div class="font-bold text-slate-800 dark:text-slate-200 text-xs">Kde je loděnice Valcha?</div>
                    <div class="text-[11px] text-slate-400">Stromovka 3, mapa & GPS</div>
                  </div>
                </a>
              </div>
            </div>
          </div>
        `;
        return;
      }}

      // Filtrace indexu
      const matches = SEARCH_INDEX.filter(item => {{
        const fullText = removeAccents(`${{item.title}} ${{item.desc}} ${{item.category}} ${{item.keywords || ''}}`);
        return fullText.includes(q);
      }});

      if (matches.length === 0) {{
        container.innerHTML = `
          <div class="text-center py-8 px-4">
            <div class="w-12 h-12 mx-auto mb-3 rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-400">
              <i class="fa-solid fa-magnifying-glass text-base"></i>
            </div>
            <div class="font-bold text-slate-800 dark:text-slate-200 text-sm mb-1">Žádné okamžité výsledky pro „${{query}}“</div>
            <div class="text-xs text-slate-400 max-w-sm mx-auto mb-4">Zkuste zkontrolovat překlep, použít obecnější slovo nebo stisknout Enter pro prohledání celého archivu článků.</div>
            <button type="submit" form="siteSearchForm" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold bg-brand-sky text-white hover:bg-sky-500 transition-colors">
              <span>Hledat v celém archivu</span>
              <i class="fa-solid fa-arrow-right text-[10px]"></i>
            </button>
          </div>
        `;
        return;
      }}

      // Vykreslení výsledků
      let html = `<div class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Nalezeno ${{matches.length}} výsledků pro „${{query}}“:</div>`;
      html += `<div class="space-y-2">`;
      matches.slice(0, 10).forEach(m => {{
        html += `
          <a href="${{m.url}}" onclick="closeSearchModal()" class="block p-3 sm:p-3.5 rounded-2xl bg-slate-50/80 dark:bg-slate-800/60 hover:bg-sky-50/80 dark:hover:bg-slate-800 border border-slate-100 dark:border-slate-800 hover:border-sky-200 dark:hover:border-slate-700 transition-all group">
            <div class="flex items-start gap-3">
              <div class="w-8 h-8 rounded-xl bg-white dark:bg-slate-700 border border-slate-200/60 dark:border-slate-600 flex items-center justify-center text-brand-sky shrink-0 group-hover:scale-105 transition-transform">
                <i class="fa-solid ${{m.icon || 'fa-arrow-right'}} text-xs"></i>
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-2 mb-1">
                  <span class="px-2 py-0.5 rounded-md bg-white dark:bg-slate-700 text-[10px] font-bold text-slate-500 dark:text-slate-300 border border-slate-200/60 dark:border-slate-600">${{m.category}}</span>
                </div>
                <div class="font-bold text-slate-900 dark:text-white text-sm group-hover:text-brand-sky transition-colors truncate">${{m.title}}</div>
                <div class="text-xs text-slate-500 dark:text-slate-400 line-clamp-2 mt-0.5">${{m.desc}}</div>
              </div>
              <i class="fa-solid fa-chevron-right text-slate-300 dark:text-slate-600 group-hover:text-brand-sky text-xs self-center"></i>
            </div>
          </a>
        `;
      }});
      html += `</div>`;
      container.innerHTML = html;
    }}

    function quickFillSearch(term) {{
      const input = document.getElementById('siteSearchInput');
      if (input) {{
        input.value = term;
        input.focus();
        onSearchInput(term);
      }}
    }}

    function handleSearchSubmit(e) {{
      const query = document.getElementById('siteSearchInput')?.value.trim();
      // Pokud máme WordPress prostředí, nebráníme odeslání formuláře (?s=query)
      if (window.location.search || window.location.pathname.includes('/wordpress') || document.querySelector('meta[name="generator"][content*="WordPress"]')) {{
        return true;
      }}
      // Statické demo na GitHub Pages: pokud byl nalezen výsledek, přesměrujeme na první shodu
      const q = removeAccents(query);
      if (q) {{
        const matches = SEARCH_INDEX.filter(item => removeAccents(`${{item.title}} ${{item.desc}} ${{item.keywords || ''}}`).includes(q));
        if (matches.length > 0) {{
          e.preventDefault();
          closeSearchModal();
          window.location.href = matches[0].url;
          return false;
        }}
      }}
      return true;
    }}
  </script>"""

print("Datasets ready.")

