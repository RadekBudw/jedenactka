import json

with open('vedeni_clean.json', 'r', encoding='utf-8') as f:
    leaders = json.load(f)

# -------------------------------------------------------------
# 1. GENERATE VERZE A: vedeni.html
# -------------------------------------------------------------

def render_cards_a(leaders):
    cards_html = []
    for l in leaders:
        avatar_img = f'<img src="{l["avatar"]}" alt="{l["name"]}" class="w-full h-full object-cover">' if l['avatar'] else f'<div class="w-full h-full bg-brand-navy flex items-center justify-center text-brand-gold font-bold text-2xl font-heading">{l["name"][0]}</div>'
        
        badge_color = 'bg-amber-100 text-amber-900 border-amber-200' if 'Toulavá' in l['paluba'] else ('bg-sky-100 text-brand-blue border-sky-200' if 'Bárka' in l['paluba'] else 'bg-slate-900 text-white border-slate-700')
        category_class = 'vlcata' if 'Toulavá' in l['paluba'] else ('skauti' if 'Bárka' in l['paluba'] else 'vedeni')
        
        phone_html = f'''<a href="tel:{l['phone'].replace(' ', '')}" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-slate-800 text-xs font-semibold border border-slate-200/80 transition-colors">
            <i class="fa-solid fa-phone text-brand-sky"></i> {l['phone']}
        </a>''' if l['phone'] else ''
        
        email_html = f'''<a href="mailto:{l['email']}" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-slate-800 text-xs font-semibold border border-slate-200/80 transition-colors">
            <i class="fa-solid fa-envelope text-brand-sky"></i> {l['email']}
        </a>''' if l['email'] else ''
        
        starosti_html = f'''<div class="text-xs text-slate-600 bg-slate-50 p-2.5 rounded-xl border border-slate-100">
            <strong class="block text-slate-900 text-[11px] uppercase tracking-wider mb-0.5 text-brand-navy">Má na starosti:</strong>
            {l['starosti']}
        </div>''' if l['starosti'] else ''
        
        kvalifikace_html = f'''<div class="text-[11px] text-slate-500 flex items-start gap-1.5 pt-1">
            <i class="fa-solid fa-award text-brand-gold mt-0.5 shrink-0"></i>
            <span><strong>Kvalifikace:</strong> {l['kvalifikace']}</span>
        </div>''' if l['kvalifikace'] else ''
        
        card = f'''
        <div class="leader-card {category_class} bg-white rounded-3xl p-6 shadow-md shadow-slate-200/50 border border-slate-200/80 hover:shadow-xl hover:border-brand-sky transition-all flex flex-col justify-between group">
          <div>
            <div class="flex items-start gap-4 mb-4">
              <div class="w-20 h-20 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white group-hover:scale-105 transition-transform bg-slate-100">
                {avatar_img}
              </div>
              <div>
                <span class="inline-block px-2.5 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider border mb-1 {badge_color}">
                  {l['paluba']}
                </span>
                <h3 class="text-lg font-black text-slate-900 font-heading leading-tight">{l['name']}</h3>
                <p class="text-xs font-bold text-brand-sky">{l['nickname'] if l['nickname'] else ''}</p>
                <p class="text-xs font-semibold text-slate-500 mt-0.5">{l['role']}</p>
              </div>
            </div>

            <div class="space-y-2 mt-2">
              {starosti_html}
              {kvalifikace_html}
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 flex flex-wrap gap-2">
            {phone_html}
            {email_html}
          </div>
        </div>
        '''
        cards_html.append(card)
    return '\n'.join(cards_html)

html_verze_a = f'''<!DOCTYPE html>
<html lang="cs" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kompletní vedení oddílu a lodivodi | 11. oddíl vodních skautů ČB</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              navy: '#0B2545',
              navyDark: '#061527',
              blue: '#134074',
              sky: '#00A8E8',
              gold: '#F5A623',
              goldHover: '#E09214',
              sand: '#F7F9FB'
            }}
          }},
          fontFamily: {{
            heading: ['Outfit', 'sans-serif'],
            body: ['"Plus Jakarta Sans"', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
  </style>
</head>
<body class="bg-[#F8FAFC] text-slate-800 antialiased selection:bg-brand-sky selection:text-white">

  <!-- TOP BAR -->
  <div class="bg-brand-navyDark text-slate-300 text-xs sm:text-sm py-2 px-4 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
      <div class="flex items-center gap-2">
        <a href="index.html" class="hover:text-brand-sky flex items-center gap-1.5 font-semibold text-white">
          <i class="fa-solid fa-arrow-left"></i> Zpět na hlavní stránku
        </a>
      </div>
      <div class="text-xs text-slate-400">11. oddíl vodních skautů České Budějovice</div>
    </div>
  </div>

  <!-- NAVIGATION -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <a href="index.html" class="flex items-center gap-3.5 group">
          <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-brand-blue to-brand-navy flex items-center justify-center text-white shadow-md shadow-brand-navy/15">
            <i class="fa-solid fa-anchor text-2xl text-brand-gold"></i>
          </div>
          <div>
            <span class="block text-xs font-bold uppercase tracking-wider text-brand-sky">Junák – český skaut</span>
            <span class="block text-xl font-black tracking-tight text-brand-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-[11px] font-medium text-slate-500 -mt-0.5">Vedení oddílu & Lodivodi</span>
          </div>
        </a>

        <nav class="hidden lg:flex items-center gap-2">
          <a href="index.html#paluby" class="px-3.5 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100">Paluby</a>
          <a href="index.html#terminovnik" class="px-3.5 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100">Kalendář</a>
          <a href="index.html#co-s-sebou" class="px-3.5 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100">Výbava</a>
          <a href="vedeni.html" class="px-3.5 py-2 rounded-xl text-sm font-bold text-brand-sky bg-sky-50">Vedení oddílu</a>
          <a href="index.html#kontakty" class="px-3.5 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100">Kontakty</a>
        </nav>

        <a href="index.html#nabor" class="px-5 py-2.5 rounded-xl font-bold text-sm bg-brand-gold text-brand-navyDark shadow-md hover:brightness-105 transition-all">
          Chci se přidat
        </a>
      </div>
    </div>
  </header>

  <!-- HERO HEADER -->
  <section class="bg-gradient-to-br from-brand-navyDark via-brand-navy to-brand-blue text-white py-14 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto text-center space-y-4">
      <span class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-white/10 text-brand-gold border border-white/15 uppercase tracking-wider">
        Tým za kormidlem Jedenáctky
      </span>
      <h1 class="text-3xl sm:text-5xl font-black font-heading tracking-tight">
        Kompletní vedení oddílu & lodivodi
      </h1>
      <p class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto leading-relaxed">
        Náš oddíl stojí na desítkách obětavých dobrovolníků, vůdců, garantů schůzek a lodivodů, kteří pro kluky připravují program, tábory a výpravy.
      </p>

      <!-- FILTER CONTROLS -->
      <div class="pt-6 flex flex-wrap items-center justify-center gap-2">
        <button onclick="filterLeaders('all')" class="leader-filter active px-5 py-2.5 rounded-xl text-xs font-bold bg-brand-gold text-brand-navyDark shadow-md transition-all" data-filter="all">
          Všichni vedoucí (34)
        </button>
        <button onclick="filterLeaders('vlcata')" class="leader-filter px-5 py-2.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all" data-filter="vlcata">
          Toulavá smečka (vlčata)
        </button>
        <button onclick="filterLeaders('skauti')" class="leader-filter px-5 py-2.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all" data-filter="skauti">
          Bárka (skauti)
        </button>
      </div>
    </div>
  </section>

  <!-- LEADERS GRID -->
  <main class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="leadersGrid">
      {render_cards_a(leaders)}
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-brand-navyDark text-slate-400 text-xs py-10 border-t border-white/10 text-center">
    <p>© 2026 11. oddíl vodních skautů České Budějovice • Junák – český skaut, z. s.</p>
    <a href="index.html" class="inline-block mt-2 text-brand-sky hover:underline font-semibold">&larr; Zpět na hlavní stránku</a>
  </footer>

  <script>
    function filterLeaders(category) {{
      document.querySelectorAll('.leader-filter').forEach(btn => {{
        if (btn.dataset.filter === category) {{
          btn.className = 'leader-filter active px-5 py-2.5 rounded-xl text-xs font-bold bg-brand-gold text-brand-navyDark shadow-md transition-all';
        }} else {{
          btn.className = 'leader-filter px-5 py-2.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all';
        }}
      }});

      document.querySelectorAll('.leader-card').forEach(card => {{
        if (category === 'all' || card.classList.contains(category)) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>
'''

with open('verzeA/vedeni.html', 'w', encoding='utf-8') as f:
    f.write(html_verze_a)

print('Generated verzeA/vedeni.html successfully!')

# -------------------------------------------------------------
# 2. GENERATE VERZE B: vedeni.html
# -------------------------------------------------------------

def render_cards_b(leaders):
    cards_html = []
    for l in leaders:
        avatar_img = f'<img src="{l["avatar"]}" alt="{l["name"]}" class="w-full h-full object-cover">' if l['avatar'] else f'<div class="w-full h-full bg-scout-navy flex items-center justify-center text-white font-bold text-2xl font-heading">{l["name"][0]}</div>'
        category_class = 'vlcata' if 'Toulavá' in l['paluba'] else ('skauti' if 'Bárka' in l['paluba'] else 'vedeni')
        badge_color = 'bg-amber-100 text-amber-900' if 'Toulavá' in l['paluba'] else ('bg-scout-lightBlue text-scout-blue' if 'Bárka' in l['paluba'] else 'bg-slate-800 text-white')
        
        phone_html = f'''<div><i class="fa-solid fa-phone text-scout-blue w-4"></i> <a href="tel:{l['phone'].replace(' ', '')}" class="hover:underline">{l['phone']}</a></div>''' if l['phone'] else ''
        email_html = f'''<div><i class="fa-solid fa-envelope text-scout-blue w-4"></i> <a href="mailto:{l['email']}" class="hover:underline">{l['email']}</a></div>''' if l['email'] else ''
        
        starosti_html = f'''<p class="text-xs text-slate-600 mt-2"><strong class="text-slate-800">Má na starosti:</strong> {l['starosti']}</p>''' if l['starosti'] else ''
        kvalifikace_html = f'''<p class="text-[11px] text-slate-500 mt-1"><strong class="text-slate-700">Kvalifikace:</strong> {l['kvalifikace']}</p>''' if l['kvalifikace'] else ''
        
        card = f'''
        <div class="leader-card-b {category_class} bg-white border border-slate-200 rounded-xl p-5 shadow-sm hover:border-scout-blue transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start gap-4 mb-3">
              <div class="w-16 h-16 rounded-xl overflow-hidden shrink-0 border border-slate-200 bg-slate-100">
                {avatar_img}
              </div>
              <div>
                <span class="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded {badge_color}">
                  {l['paluba']}
                </span>
                <h3 class="text-base font-bold text-scout-navy font-heading mt-1 leading-tight">{l['name']}</h3>
                <p class="text-xs font-semibold text-scout-blue">{l['nickname'] if l['nickname'] else ''}</p>
                <p class="text-xs text-slate-500">{l['role']}</p>
              </div>
            </div>
            {starosti_html}
            {kvalifikace_html}
          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 text-xs font-medium space-y-1">
            {phone_html}
            {email_html}
          </div>
        </div>
        '''
        cards_html.append(card)
    return '\n'.join(cards_html)

html_verze_b = f'''<!DOCTYPE html>
<html lang="cs" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vedení 11. oddílu | Junák – český skaut České Budějovice</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Roboto+Slab:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            scout: {{
              navy: '#002B49',
              blue: '#0062A3',
              lightBlue: '#E6F0F8',
              cyan: '#009FE3',
              sand: '#F7F7F7'
            }}
          }},
          fontFamily: {{
            heading: ['"Roboto Slab"', 'serif'],
            body: ['Inter', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{ font-family: 'Inter', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Roboto Slab', serif; }}
  </style>
</head>
<body class="bg-white text-slate-800 antialiased selection:bg-scout-blue selection:text-white">

  <!-- TOP OFFICIAL SKAUT BAR -->
  <div class="bg-scout-navy text-slate-200 text-xs py-2 px-4 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
      <a href="index.html" class="hover:text-white flex items-center gap-2">
        <i class="fa-solid fa-arrow-left text-scout-cyan"></i> Zpět na úvodní stránku
      </a>
      <span class="text-slate-300">4. středisko VAVÉHA České Budějovice</span>
    </div>
  </div>

  <!-- MAIN HEADER -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <a href="index.html" class="flex items-center gap-3 group">
          <div class="w-12 h-12 rounded-xl bg-scout-blue text-white flex items-center justify-center text-2xl">
            <i class="fa-solid fa-anchor"></i>
          </div>
          <div>
            <span class="block text-xl font-bold tracking-tight text-scout-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-xs font-semibold text-scout-blue -mt-0.5">Kompletní vedení oddílu</span>
          </div>
        </a>

        <nav class="hidden lg:flex items-center gap-6 text-sm font-semibold text-slate-700">
          <a href="index.html#o-nas" class="hover:text-scout-blue">O oddílu</a>
          <a href="index.html#paluby" class="hover:text-scout-blue">Paluby</a>
          <a href="index.html#harmonogram" class="hover:text-scout-blue">Kalendář akcí</a>
          <a href="index.html#vybaveni" class="hover:text-scout-blue">Vybavení</a>
          <a href="vedeni.html" class="text-scout-blue font-bold">Vedení</a>
          <a href="index.html#kontakty" class="hover:text-scout-blue">Kontakty</a>
        </nav>

        <a href="index.html#nabor" class="px-5 py-2.5 rounded-lg text-sm font-bold bg-scout-blue text-white hover:bg-scout-navy">
          Nábor
        </a>
      </div>
    </div>
  </header>

  <!-- PAGE HEADER -->
  <section class="bg-scout-sand border-b border-slate-200 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto text-center space-y-3">
      <span class="text-scout-blue font-bold text-xs uppercase tracking-wider">Tým vedoucích</span>
      <h1 class="text-3xl sm:text-4xl font-extrabold text-scout-navy font-heading">
        Vedení 11. oddílu, garanti schůzek a lodivodi
      </h1>
      <p class="text-slate-600 text-sm max-w-2xl mx-auto">
        Strukturovaný přehled všech dospělých a roverů, kteří se podílejí na přípravě programu pro vlčata a skauty.
      </p>

      <!-- FILTERS -->
      <div class="pt-4 flex flex-wrap justify-center gap-2">
        <button onclick="filterLeadersB('all')" class="filter-btn-b active px-4 py-2 rounded-lg text-xs font-bold bg-scout-navy text-white" data-filter="all">Všichni (34)</button>
        <button onclick="filterLeadersB('vlcata')" class="filter-btn-b px-4 py-2 rounded-lg text-xs font-bold bg-white text-slate-700 border border-slate-300" data-filter="vlcata">Toulavá smečka (vlčata)</button>
        <button onclick="filterLeadersB('skauti')" class="filter-btn-b px-4 py-2 rounded-lg text-xs font-bold bg-white text-slate-700 border border-slate-300" data-filter="skauti">Bárka (skauti)</button>
      </div>
    </div>
  </section>

  <!-- CARDS GRID -->
  <main class="py-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="leadersGridB">
      {render_cards_b(leaders)}
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-100 border-t border-slate-200 text-slate-500 text-xs py-8 text-center">
    <p>© 2026 11. oddíl vodních skautů České Budějovice • Junák – český skaut, z. s.</p>
    <a href="index.html" class="inline-block mt-1 text-scout-blue hover:underline font-semibold">&larr; Zpět na úvodní stránku</a>
  </footer>

  <script>
    function filterLeadersB(category) {{
      document.querySelectorAll('.filter-btn-b').forEach(btn => {{
        if (btn.dataset.filter === category) {{
          btn.className = 'filter-btn-b active px-4 py-2 rounded-lg text-xs font-bold bg-scout-navy text-white';
        }} else {{
          btn.className = 'filter-btn-b px-4 py-2 rounded-lg text-xs font-bold bg-white text-slate-700 border border-slate-300';
        }}
      }});

      document.querySelectorAll('.leader-card-b').forEach(card => {{
        if (category === 'all' || card.classList.contains(category)) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>
'''

with open('verzeB/vedeni.html', 'w', encoding='utf-8') as f:
    f.write(html_verze_b)

print('Generated verzeB/vedeni.html successfully!')
