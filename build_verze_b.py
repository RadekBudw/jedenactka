# -*- coding: utf-8 -*-
import json, re, datetime
from build_data import leaders, h, TERMINOVNIK_BARKA, TERMINOVNIK_VLCATA, BLOG_POSTS, FAQ_ITEMS, get_version_meta_html, get_app_version, get_git_commit, save_version_json, update_index_html_version, get_search_modal_html, get_search_script_js

BUILD_TIMESTAMP = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

def get_navbar_b(is_subpage=False):
    prefix = "index.html" if is_subpage else ""
    return f"""
  <!-- TOP OFFICIAL SKAUT STATUS BAR -->
  <div class="bg-scout-navy text-slate-200 text-xs py-2 px-4 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
      <div class="flex items-center gap-2 text-center sm:text-left">
        <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold text-xs border border-emerald-500/30">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Běží schůzky 2026/2027
        </span>
        <span class="text-xs sm:text-sm">Schůzky: <strong>Středa &amp; Čtvrtek 16:00 – 18:00</strong> na Valše</span>
      </div>
      <div class="flex items-center gap-3 text-xs">
        <a href="{prefix}#terminovnik" class="hover:text-scout-cyan transition-colors flex items-center gap-1.5">
          <i class="fa-regular fa-calendar-check text-yellow-400"></i> Termínovník akcí
        </a>
        <span class="text-white/20">|</span>
        <a href="https://vaveha.cz" target="_blank" class="hover:text-white transition-colors flex items-center gap-1">
          <span>4. středisko VAVÉHA ČB</span>
          <i class="fa-solid fa-arrow-up-right-from-square text-[10px] text-slate-400"></i>
        </a>
      </div>
    </div>
  </div>

  <!-- MAIN HEADER -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- LOGO & BRAND -->
        <a href="{prefix}#" class="flex items-center gap-3.5 group">
          <div class="h-12 w-12 sm:h-14 sm:w-14 rounded-xl bg-slate-100 p-1 flex items-center justify-center group-hover:bg-slate-200 transition-colors shrink-0">
            <img src="logo_emblem.png" alt="11. oddíl vodních skautů" class="h-full w-full object-contain filter drop-shadow-xs">
          </div>
          <div>
            <span class="block text-xl font-bold tracking-tight text-scout-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-xs font-semibold text-scout-blue">České Budějovice • Valcha</span>
          </div>
        </a>

        <!-- DESKTOP MENU -->
        <nav class="hidden lg:flex items-center gap-5 text-sm font-semibold text-slate-700">
          <a href="{prefix}#pro-rodice" class="hover:text-scout-blue transition-colors flex items-center gap-1.5 font-bold text-amber-700">
            <i class="fa-solid fa-heart-pulse text-amber-500 text-xs"></i> Pro rodiče
          </a>
          <a href="{prefix}#oddil" class="hover:text-scout-blue transition-colors">O oddílu</a>
          <a href="{prefix}#paluby" class="hover:text-scout-blue transition-colors">Naše paluby</a>
          <a href="{prefix}#terminovnik" class="hover:text-scout-blue transition-colors">Termínovník</a>
          <a href="{prefix}#aktuality" class="hover:text-scout-blue transition-colors">Aktuality</a>
          <a href="{"vedeni.html" if not is_subpage else "#"}" class="{"text-scout-blue font-bold border-b-2 border-scout-blue pb-0.5" if is_subpage else "text-scout-blue hover:text-scout-navy font-bold"} transition-colors flex items-center gap-1">
            <i class="fa-solid fa-users text-xs"></i> Vedení oddílu
          </a>
          <a href="{prefix}#lodenice" class="hover:text-scout-blue transition-colors">Valcha</a>
          <a href="{prefix}#kontakty" class="hover:text-scout-blue transition-colors">Kontakty</a>
        </nav>

        <!-- CTA BUTTON, SEARCH & THEME TOGGLE -->
        <div class="hidden sm:flex items-center gap-2">
          <button onclick="openSearchModal()" class="p-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 dark:hover:bg-slate-700 transition-colors cursor-pointer flex items-center justify-center gap-2 text-xs font-semibold" title="Vyhledávat na webu (Ctrl+K)" aria-label="Hledat na webu">
            <i class="fa-solid fa-magnifying-glass text-sm text-slate-500 dark:text-slate-400"></i>
            <span class="hidden xl:inline text-slate-500">Hledat...</span>
            <kbd class="hidden xl:inline-block px-1.5 py-0.5 text-[10px] bg-slate-100 dark:bg-slate-700 text-slate-400 rounded border border-slate-200 dark:border-slate-600 font-mono">Ctrl+K</kbd>
          </button>
          <button onclick="toggleTheme()" class="p-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-yellow-400 dark:hover:bg-slate-700 transition-colors cursor-pointer flex items-center justify-center" title="Přepnout tmavý / světlý režim" aria-label="Přepnout režim">
            <i class="fa-solid fa-moon text-sm text-slate-800 theme-toggle-icon"></i>
          </button>
          <a href="{prefix}#nabor" class="px-5 py-2.5 rounded-lg text-sm font-bold bg-scout-blue text-white hover:bg-scout-navy shadow-sm transition-all flex items-center gap-2">
            <i class="fa-solid fa-user-plus text-xs"></i>
            <span>Nábor nových členů</span>
          </a>
        </div>

        <!-- HAMBURGER, SEARCH & THEME BUTTON -->
        <div class="flex items-center gap-1.5 lg:hidden">
          <button onclick="openSearchModal()" class="p-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 cursor-pointer" title="Hledat" aria-label="Hledat">
            <i class="fa-solid fa-magnifying-glass text-xs"></i>
          </button>
          <button onclick="toggleTheme()" class="p-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-yellow-400 dark:hover:bg-slate-700 cursor-pointer" title="Přepnout režim" aria-label="Přepnout režim">
            <i class="fa-solid fa-moon text-xs text-slate-800 theme-toggle-icon"></i>
          </button>
          <button id="mobileMenuBtnB" class="p-2 text-slate-700 dark:text-slate-200 hover:text-scout-blue focus:outline-none" aria-label="Menu">
            <i class="fa-solid fa-bars text-2xl"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- MOBILE MENU DRAWER -->
    <div id="mobileMenuB" class="hidden lg:hidden bg-slate-50 dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-4 py-4 space-y-2">
      <div class="mb-2">
        <button onclick="openSearchModal(); document.getElementById('mobileMenuB').classList.add('hidden');" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-xs font-medium border border-slate-200 dark:border-slate-700 text-left cursor-pointer">
          <i class="fa-solid fa-magnifying-glass text-slate-400 text-xs"></i>
          <span>Hledat na webu Jedenáctky...</span>
        </button>
      </div>
      <a href="{prefix}#pro-rodice" class="block px-3 py-2 rounded-lg font-bold text-amber-800 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/40 hover:bg-amber-100 flex items-center gap-2">
        <i class="fa-solid fa-heart-pulse text-amber-600"></i> Pro rodiče (Rozpis schůzek & fotky)
      </a>
      <a href="{prefix}#oddil" class="block px-3 py-2 rounded-lg font-semibold text-slate-800 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800">O 11. oddílu</a>
      <a href="{prefix}#paluby" class="block px-3 py-2 rounded-lg font-semibold text-slate-800 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800">Naše 3 paluby (vlčata, skauti, roveři)</a>
      <a href="{prefix}#terminovnik" class="block px-3 py-2 rounded-lg font-semibold text-slate-800 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800">Termínovník akcí & výprav</a>
      <a href="{prefix}#aktuality" class="block px-3 py-2 rounded-lg font-semibold text-slate-800 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800">Aktuality z oddílu</a>
      <a href="vedeni.html" class="block px-3 py-2 rounded-lg font-bold text-scout-blue hover:bg-slate-200 dark:hover:bg-slate-800">Vedení oddílu (34 vedoucích)</a>
      <a href="{prefix}#lodenice" class="block px-3 py-2 rounded-lg font-semibold text-slate-800 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800">Základna Valcha</a>
      <a href="{prefix}#kontakty" class="block px-3 py-2 rounded-lg font-semibold text-slate-800 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800">Kontakty</a>
      <div class="pt-2 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between px-1">
        <span class="text-xs font-bold text-slate-500 dark:text-slate-400">Režim zobrazení:</span>
        <button onclick="toggleTheme()" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-white dark:bg-slate-800 text-slate-800 dark:text-yellow-300 font-bold text-xs border border-slate-200 dark:border-slate-700 cursor-pointer">
          <i class="fa-solid fa-moon text-xs text-slate-800 theme-toggle-icon"></i>
          <span class="theme-toggle-text">Tmavý režim</span>
        </button>
      </div>
      <div class="pt-2">
        <a href="{prefix}#nabor" class="block text-center py-2.5 rounded-lg font-bold bg-scout-blue text-white">Nábor nových členů</a>
      </div>
    </div>
  </header>
"""

# Build verzeB/index.html
def generate_index_b():
    barka_cards = "".join([f'''
      <div class="bg-white rounded-2xl p-5 shadow-sm border border-slate-200 hover:border-scout-blue hover:shadow transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-xs font-bold bg-sky-100 text-scout-blue">
              <i class="fa-solid {ev["icon"]}"></i> {ev["type"]}
            </span>
            <span class="text-xs font-semibold text-slate-400">Bárka</span>
          </div>
          <h4 class="text-base font-bold text-scout-navy mt-1 font-heading">{ev["title"]}</h4>
          <div class="text-xs font-bold text-scout-cyan mt-0.5">{ev["date"]}</div>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">{ev["desc"]}</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-500">
          <span><i class="fa-solid fa-location-dot text-slate-400"></i> Dle propozic</span>
          <span class="text-scout-blue font-semibold">@jedenactka.eu</span>
        </div>
      </div>
    ''' for ev in TERMINOVNIK_BARKA])

    vlcata_cards = "".join([f'''
      <div class="bg-white rounded-2xl p-5 shadow-sm border border-slate-200 hover:border-amber-400 hover:shadow transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-xs font-bold bg-amber-100 text-amber-900">
              <i class="fa-solid {ev["icon"]}"></i> {ev["type"]}
            </span>
            <span class="text-xs font-semibold text-slate-400">Toulavá smečka</span>
          </div>
          <h4 class="text-base font-bold text-slate-900 mt-1 font-heading">{ev["title"]}</h4>
          <div class="text-xs font-bold text-amber-700 mt-0.5">{ev["date"]}</div>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">{ev["desc"]}</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-500">
          <span><i class="fa-solid fa-location-dot text-slate-400"></i> Informace u garantů</span>
          <span class="text-amber-800 font-semibold">Vlčata</span>
        </div>
      </div>
    ''' for ev in TERMINOVNIK_VLCATA])

    blog_cards = "".join([f'''
      <article class="bg-white rounded-2xl overflow-hidden shadow-sm border border-slate-200 hover:shadow-md hover:border-scout-blue transition-all flex flex-col justify-between group">
        <div>
          <div class="aspect-[16/10] overflow-hidden bg-slate-100 relative">
            <img src="{post["img"]}" alt="{post["title"]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-scout-navy text-white">
              {post["tag"]}
            </span>
          </div>
          <div class="p-4">
            <div class="text-[11px] font-semibold text-slate-400 mb-1 flex items-center gap-1.5">
              <i class="fa-regular fa-calendar text-scout-blue"></i> {post["date"]}
            </div>
            <h4 class="text-sm font-bold text-scout-navy font-heading leading-snug group-hover:text-scout-blue transition-colors">
              {post["title"]}
            </h4>
            <p class="text-xs text-slate-600 mt-2 line-clamp-3 leading-relaxed">
              {post["desc"]}
            </p>
          </div>
        </div>
        <div class="px-4 pb-4 pt-0">
          <a href="{post["link"]}" target="_blank" class="inline-flex items-center gap-1 text-xs font-bold text-scout-blue hover:text-scout-navy transition-colors">
            <span>Fotky z akce</span>
            <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </a>
        </div>
      </article>
    ''' for post in BLOG_POSTS])

    faq_cards_b = "".join([f'''
      <div class="bg-white rounded-xl border border-slate-200 shadow-2xs overflow-hidden hover:border-scout-blue transition-colors">
        <button onclick="toggleFaqB({i})" class="w-full p-4 sm:p-5 text-left flex items-center justify-between gap-4 cursor-pointer select-none group" aria-expanded="false">
          <div class="flex items-center gap-3">
            <span class="w-8 h-8 rounded-lg bg-sky-50 text-scout-blue flex items-center justify-center text-sm shrink-0">
              <i class="fa-solid {item["icon"]}"></i>
            </span>
            <span class="font-bold text-sm sm:text-base text-scout-navy font-heading group-hover:text-scout-blue transition-colors">
              {item["q"]}
            </span>
          </div>
          <span class="text-slate-400 group-hover:text-scout-blue transition-colors shrink-0">
            <i id="faqIconB{i}" class="fa-solid fa-chevron-down text-xs transition-transform duration-300"></i>
          </span>
        </button>
        <div id="faqAnsB{i}" class="hidden px-5 pb-5 pt-1 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 bg-slate-50/60">
          <p>{item["a"]}</p>
        </div>
      </div>
    ''' for i, item in enumerate(FAQ_ITEMS)])

    html = f"""<!DOCTYPE html>
<html lang="cs" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>11. oddíl vodních skautů České Budějovice | Junák – český skaut</title>
{get_version_meta_html()}
  
  <script>
    if (localStorage.theme === 'dark') {{
      document.documentElement.classList.add('dark');
    }} else {{
      document.documentElement.classList.remove('dark');
    }}
  </script>

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            scout: {{
              blue: '#005080',
              navy: '#002D5A',
              cyan: '#009BE0',
              sand: '#F4F6F8',
              sandDark: '#E5E9EE'
            }}
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700;800&family=The+Sans:wght@700;800&display=swap" rel="stylesheet">

  <style>
    body {{ font-family: 'Source Sans 3', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'The Sans', 'Source Sans 3', sans-serif; }}

    /* Plynulý přechod při přepnutí motivu */
    html.theme-transition,
    html.theme-transition *,
    html.theme-transition *:before,
    html.theme-transition *:after {{
      transition: background-color 0.25s ease, border-color 0.25s ease, color 0.15s ease !important;
    }}

    /* ========================================================= */
    /* DENNÍ REŽIM - VYSOKÝ KONTRAST A MAXIMÁLNÍ ČITELNOST       */
    /* ========================================================= */
    html:not(.dark) body {{
      background-color: #f8f9fa;
      color: #0f172a;
    }}

    /* Světlé sekce a karty - syté, perfektně čitelné texty */
    html:not(.dark) .bg-white p,
    html:not(.dark) .bg-slate-50 p,
    html:not(.dark) .bg-slate-100 p,
    html:not(.dark) .bg-scout-sand p,
    html:not(.dark) #pro-rodice p,
    html:not(.dark) #oddil p,
    html:not(.dark) #paluby p,
    html:not(.dark) #terminovnik p,
    html:not(.dark) #aktuality p,
    html:not(.dark) #faq p,
    html:not(.dark) #vybava p,
    html:not(.dark) #kontakty p {{
      color: #1e293b;
    }}

    html:not(.dark) .text-scout-navy {{
      color: #002d5a !important;
    }}
    html:not(.dark) .text-slate-900 {{
      color: #071527 !important;
    }}
    html:not(.dark) .text-slate-800 {{
      color: #0f172a !important;
    }}
    html:not(.dark) .text-slate-700 {{
      color: #0f172a !important;
    }}
    html:not(.dark) .text-slate-600 {{
      color: #1e293b !important;
    }}
    html:not(.dark) .text-slate-500 {{
      color: #334155 !important;
    }}
    html:not(.dark) .text-slate-400 {{
      color: #475569 !important;
    }}

    /* ========================================================= */
    /* TMAVÉ BLOKY V DENNÍM REŽIMU (Gmail, Valcha, Nábor, Footer) */
    /* ========================================================= */
    html:not(.dark) .bg-slate-950,
    html:not(.dark) .bg-slate-900,
    html:not(.dark) footer.bg-slate-950,
    html:not(.dark) .bg-scout-navy,
    html:not(.dark) div.bg-gradient-to-r {{
      color: #ffffff;
    }}
    html:not(.dark) .bg-scout-navy h1,
    html:not(.dark) .bg-scout-navy h2,
    html:not(.dark) .bg-scout-navy h3,
    html:not(.dark) div.bg-gradient-to-r h2,
    html:not(.dark) div.bg-gradient-to-r h3,
    html:not(.dark) .bg-slate-900 h2,
    html:not(.dark) .bg-slate-900 h3,
    html:not(.dark) .bg-scout-navy strong,
    html:not(.dark) div.bg-gradient-to-r strong,
    html:not(.dark) .bg-slate-900 strong,
    html:not(.dark) footer.bg-slate-950 strong {{
      color: #ffffff !important;
    }}
    html:not(.dark) .bg-scout-navy p,
    html:not(.dark) div.bg-gradient-to-r p,
    html:not(.dark) .bg-slate-900 p,
    html:not(.dark) footer.bg-slate-950 p {{
      color: #e2e8f0 !important;
    }}
    html:not(.dark) .bg-scout-navy .text-slate-300,
    html:not(.dark) div.bg-gradient-to-r .text-slate-300,
    html:not(.dark) .bg-slate-900 .text-slate-300,
    html:not(.dark) .bg-slate-950 .text-slate-300,
    html:not(.dark) footer.bg-slate-950 .text-slate-300 {{
      color: #cbd5e1 !important;
    }}
    html:not(.dark) .bg-scout-navy .text-slate-400,
    html:not(.dark) div.bg-gradient-to-r .text-slate-400,
    html:not(.dark) .bg-slate-900 .text-slate-400,
    html:not(.dark) .bg-slate-950 .text-slate-400,
    html:not(.dark) footer.bg-slate-950 .text-slate-400 {{
      color: #94a3b8 !important;
    }}

    /* ========================================================= */
    /* TMAVÝ REŽIM - KOMPLETNÍ BAREVNÁ PALETA PRO NOČNÍ MOTIV    */
    /* ========================================================= */
    .dark {{
      color-scheme: dark;
    }}
    .dark body {{
      background-color: #070e1d !important;
      color: #f1f5f9 !important;
    }}
    .dark header {{
      background-color: rgba(7, 14, 29, 0.95) !important;
      border-color: rgba(30, 41, 59, 0.8) !important;
    }}
    .dark nav a {{
      color: #cbd5e1 !important;
    }}
    .dark nav a:hover {{
      background-color: rgba(30, 41, 59, 0.8) !important;
      color: #38bdf8 !important;
    }}
    .dark #mobileMenuB {{
      background-color: #0b1329 !important;
      border-color: #1e293b !important;
    }}
    .dark #mobileMenuB a {{
      color: #e2e8f0 !important;
    }}
    .dark #mobileMenuB a:hover {{
      background-color: #1e293b !important;
    }}
    
    /* Všechna světlá pozadí sekcí a bloků se v nočním režimu ztmaví */
    .dark section.bg-slate-100,
    .dark section.bg-slate-50,
    .dark section.bg-white,
    .dark section.bg-scout-sand,
    .dark #oddil,
    .dark #aktuality,
    .dark #lodenice,
    .dark .bg-slate-100,
    .dark .bg-slate-100\\/80,
    .dark .bg-slate-50,
    .dark .bg-slate-50\\/50,
    .dark .bg-slate-50\\/60,
    .dark .bg-slate-200,
    .dark .bg-scout-sand,
    .dark .bg-scout-sandDark {{
      background-color: #0b1528 !important;
      border-color: #1e2e4a !important;
      color: #e2e8f0 !important;
    }}

    /* Karty a boxy v nočním režimu */
    .dark .bg-white {{
      background-color: #0f1c34 !important;
      border-color: #1e2e4a !important;
      color: #f1f5f9 !important;
    }}

    /* Rámečky fotek */
    .dark .border-white {{
      border-color: #1e2e4a !important;
    }}

    /* Titulky a texty */
    .dark h1, .dark h2, .dark h3, .dark h4, .dark h5, .dark h6 {{
      color: #ffffff !important;
    }}
    .dark strong {{
      color: #ffffff !important;
    }}
    .dark .text-brand-navy,
    .dark .text-scout-navy,
    .dark .text-slate-900 {{
      color: #ffffff !important;
    }}
    .dark .text-brand-blue,
    .dark .text-scout-blue,
    .dark .text-scout-cyan {{
      color: #38bdf8 !important;
    }}
    .dark .text-slate-800 {{
      color: #f1f5f9 !important;
    }}
    .dark .text-slate-700 {{
      color: #e2e8f0 !important;
    }}
    .dark .text-slate-600 {{
      color: #cbd5e1 !important;
    }}
    .dark .text-slate-500,
    .dark .text-slate-400 {{
      color: #94a3b8 !important;
    }}

    /* Textové barvy ikon a odznaků */
    .dark .text-yellow-700 {{
      color: #facc15 !important;
    }}
    .dark .text-amber-700, .dark .text-amber-800, .dark .text-amber-900 {{
      color: #fbbf24 !important;
    }}
    .dark .text-emerald-700, .dark .text-emerald-800, .dark .text-emerald-900 {{
      color: #34d399 !important;
    }}

    /* Rámečky */
    .dark .border-slate-100,
    .dark .border-slate-200,
    .dark .border-slate-300 {{
      border-color: #1e2e4a !important;
    }}

    /* Barevné akcentové boxíky v kartách */
    .dark .bg-amber-50,
    .dark .bg-amber-50\\/50,
    .dark .bg-amber-100 {{
      background-color: rgba(245, 158, 11, 0.15) !important;
      border-color: rgba(245, 158, 11, 0.3) !important;
      color: #fbbf24 !important;
    }}
    .dark .bg-sky-50,
    .dark .bg-sky-100 {{
      background-color: rgba(14, 165, 233, 0.15) !important;
      border-color: rgba(14, 165, 233, 0.3) !important;
      color: #38bdf8 !important;
    }}
    .dark .bg-emerald-50,
    .dark .bg-emerald-100 {{
      background-color: rgba(16, 185, 129, 0.15) !important;
      border-color: rgba(16, 185, 129, 0.3) !important;
      color: #34d399 !important;
    }}
    .dark .bg-purple-50,
    .dark .bg-purple-100 {{
      background-color: rgba(168, 85, 247, 0.15) !important;
      border-color: rgba(168, 85, 247, 0.3) !important;
      color: #c084fc !important;
    }}

    /* Tlačítka a odkazy s bg-slate-50 nebo bg-slate-100 (kontakty, maily, telefony) */
    .dark a.bg-slate-50,
    .dark a.bg-slate-100,
    .dark a.bg-white,
    .dark button.bg-slate-100,
    .dark button.bg-white {{
      background-color: #162544 !important;
      border-color: #243b66 !important;
      color: #e2e8f0 !important;
    }}
    .dark a.bg-slate-50:hover,
    .dark a.bg-slate-100:hover,
    .dark a.bg-white:hover,
    .dark button.bg-slate-100:hover,
    .dark button.bg-white:hover {{
      background-color: #1e3560 !important;
      color: #ffffff !important;
    }}
  </style>
</head>
<body class="bg-[#F8F9FA] text-slate-800 antialiased selection:bg-scout-blue selection:text-white">

  {get_navbar_b(is_subpage=False)}

  <!-- HERO SECTION -->
  <section class="bg-white border-b border-slate-200 py-12 sm:py-16 lg:py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <div class="lg:col-span-7 space-y-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-scout-sand border border-slate-200 text-xs font-bold text-scout-navy">
            <span class="w-3.5 h-2.5 inline-block rounded-xs border border-slate-300 shadow-2xs" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);"></span>
            <span>Černo-žlutá oddílová vlajka • 4. středisko VAVÉHA ČB</span>
          </div>

          <h1 class="text-3xl sm:text-5xl lg:text-5xl font-extrabold text-scout-navy font-heading tracking-tight leading-tight">
            11. oddíl vodních skautů <br>
            <span class="text-scout-blue">České Budějovice</span>
          </h1>

          <p class="text-base sm:text-lg text-slate-600 leading-relaxed max-w-2xl">
            Jsme chlapecký vodní skautský oddíl s dlouholetou tradicí. Učíme kluky samostatnosti, spolupráci v posádce, jízdě na pramicích i plachetnicích a pravidlům fair-play na Valše.
          </p>

          <div class="flex flex-col sm:flex-row items-center gap-3 pt-2">
            <a href="#pro-rodice" class="w-full sm:w-auto px-6 py-3.5 rounded-lg text-sm font-bold bg-scout-blue text-white hover:bg-scout-navy shadow-sm transition-all flex items-center justify-center gap-2">
              <i class="fa-solid fa-heart-pulse"></i>
              <span>Pro rodiče (Rozpis schůzek & fotky)</span>
            </a>
            <a href="#oddil" class="w-full sm:w-auto px-6 py-3.5 rounded-lg text-sm font-bold bg-scout-sand hover:bg-slate-200 text-scout-navy border border-slate-300 transition-all flex items-center justify-center gap-2">
              <i class="fa-solid fa-compass text-scout-blue"></i>
              <span>O našem oddílu</span>
            </a>
          </div>

          <div class="pt-4 border-t border-slate-100 grid grid-cols-3 gap-4 text-xs text-slate-600">
            <div><strong>4</strong> paluby dle věku</div>
            <div><strong>34</strong> vedoucích &amp; lodivodů</div>
            <div><strong>100%</strong> skautské hodnoty</div>
          </div>
        </div>

        <div class="lg:col-span-5 relative">
          <div onclick="handleHeroClickB()" class="rounded-2xl overflow-hidden shadow-lg border border-slate-200 hover:border-scout-blue aspect-[4/3] group bg-slate-900 relative cursor-pointer select-none transition-all duration-300" title="Klikněte do fotky pro další snímek (nebo nechte běžet automatické střídání)">
            <img id="heroImgB" src="zonerama_2.jpg" alt="11. oddíl vodních skautů" class="w-full h-full object-cover transition-opacity duration-500 group-hover:scale-105 transition-transform">
            <div class="absolute inset-0 bg-gradient-to-t from-scout-navy/90 via-transparent to-transparent flex flex-col justify-between p-4 pointer-events-none">
              <div class="flex justify-between items-start pointer-events-auto">
                <span id="heroTagB" class="text-xs font-bold uppercase px-2.5 py-1 rounded bg-scout-blue text-white shadow-xs">Trénink na Malši</span>
                <button onclick="event.stopPropagation(); handleHeroClickB()" type="button" class="px-2.5 py-1 rounded bg-white/90 hover:bg-white text-scout-navy font-bold text-xs shadow transition-all cursor-pointer flex items-center gap-1 active:scale-95" title="Náhodně změnit fotografii v záhlaví">
                  <i class="fa-solid fa-shuffle text-scout-blue"></i>
                  <span>Další fotka 🎲</span>
                </button>
              </div>
              <div class="flex items-center justify-between">
                <p id="heroTitleB" class="text-sm font-bold text-white leading-snug">Trénink posádek na řece Malši a Vltavě</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- QUICK ACTION ROW -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-6">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
      <a href="#pro-rodice" class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 hover:border-scout-blue transition-all">
        <div class="text-amber-600 font-bold text-xs"><i class="fa-solid fa-clock"></i> Schůzky</div>
        <div class="text-sm font-bold text-slate-800 mt-1">Středa &amp; Čtvrtek</div>
        <div class="text-[11px] text-slate-500">16:00 – 18:00 Valcha</div>
      </a>
      <a href="#terminovnik" class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 hover:border-scout-blue transition-all">
        <div class="text-scout-blue font-bold text-xs"><i class="fa-regular fa-calendar"></i> Výpravy</div>
        <div class="text-sm font-bold text-slate-800 mt-1">Termínovník akcí</div>
        <div class="text-[11px] text-slate-500">Víkendovky &amp; závody</div>
      </a>
      <a href="https://eu.zonerama.com/11skautskyoddil/" target="_blank" class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 hover:border-scout-blue transition-all">
        <div class="text-emerald-600 font-bold text-xs"><i class="fa-solid fa-images"></i> Fotogalerie</div>
        <div class="text-sm font-bold text-slate-800 mt-1">Zonerama alba</div>
        <div class="text-[11px] text-slate-500">Fotky z akcí</div>
      </a>
      <a href="vedeni.html" class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 hover:border-scout-blue transition-all">
        <div class="text-scout-navy font-bold text-xs"><i class="fa-solid fa-users"></i> Vedení</div>
        <div class="text-sm font-bold text-slate-800 mt-1">34 vedoucích</div>
        <div class="text-[11px] text-slate-500">Profily &amp; kontakty</div>
      </a>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: PRO RODIČE -->
  <!-- ======================================================================== -->
  <section id="pro-rodice" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-12">
      <span class="text-xs font-bold uppercase tracking-wider text-amber-800 bg-amber-100 px-3 py-1 rounded-md">
        Informační servis pro rodiče
      </span>
      <h2 class="text-3xl font-extrabold text-scout-navy font-heading mt-2">
        Vše důležité pro rodiče chlapců
      </h2>
      <p class="text-slate-600 text-sm mt-2">
        Rozpis schůzek, kontakty na garanty jednotlivých dnů, skautské e-maily a fotoarchivy.
      </p>
    </div>

    <!-- 1. ROZPIS SCHŮZEK & GARANTI -->
    <div class="mb-12">
      <div class="flex items-center justify-between mb-4 flex-wrap gap-2">
        <h3 class="text-lg font-bold text-scout-navy font-heading flex items-center gap-2">
          <i class="fa-regular fa-clock text-scout-blue"></i>
          Rozpis schůzek na rok 2026/2027
        </h3>
        <span class="text-xs font-bold text-slate-600 bg-slate-100 px-3 py-1 rounded border border-slate-200">
          Čas schůzek: 16:00 – 18:00
        </span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
        
        <!-- Garant 1: Vlčata Středa -->
        <div class="bg-white rounded-xl p-5 shadow-sm border border-slate-200 hover:border-amber-400 transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-100 text-amber-900">
                Vlčata • Středa
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3 mb-3">
              <img src="avatars/avatar_4.jpg" alt="Matěj Bajgar – Myšák" class="w-14 h-14 rounded-xl object-cover border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-sm font-heading">Myšák</h4>
                <p class="text-xs font-semibold text-slate-700">Matěj Bajgar</p>
                <p class="text-[11px] text-slate-500">Garant středeční schůzky</p>
              </div>
            </div>

            <p class="text-xs text-slate-600 mb-3 bg-slate-50 p-2 rounded">
              Toulavá smečka (6–10 let). Omluvenky ze středečních schůzek.
            </p>
          </div>

          <div class="space-y-1.5 pt-3 border-t border-slate-100 text-xs">
            <a href="tel:+420778019042" class="flex items-center justify-center gap-2 py-1.5 rounded bg-amber-50 text-amber-900 font-bold hover:bg-amber-100 transition-colors">
              <i class="fa-solid fa-phone text-xs"></i> 778 019 042
            </a>
            <a href="mailto:matejb@jedenactka.eu" class="flex items-center justify-center gap-2 py-1.5 rounded bg-slate-50 text-slate-700 hover:bg-slate-100 transition-colors">
              <i class="fa-solid fa-envelope text-xs text-slate-400"></i> matejb@jedenactka.eu
            </a>
          </div>
        </div>

        <!-- Garant 2: Vlčata Čtvrtek -->
        <div class="bg-white rounded-xl p-5 shadow-sm border border-slate-200 hover:border-amber-400 transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-100 text-amber-900">
                Vlčata • Čtvrtek
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3 mb-3">
              <img src="avatars/avatar_3.jpg" alt="Jáchym Řehounek – Čáp" class="w-14 h-14 rounded-xl object-cover border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-sm font-heading">Čáp</h4>
                <p class="text-xs font-semibold text-slate-700">Jáchym Řehounek</p>
                <p class="text-[11px] text-slate-500">Garant čtvrteční schůzky</p>
              </div>
            </div>

            <p class="text-xs text-slate-600 mb-3 bg-slate-50 p-2 rounded">
              Toulavá smečka (6–10 let). Omluvenky ze čtvrtečních schůzek.
            </p>
          </div>

          <div class="space-y-1.5 pt-3 border-t border-slate-100 text-xs">
            <a href="tel:+420732405827" class="flex items-center justify-center gap-2 py-1.5 rounded bg-amber-50 text-amber-900 font-bold hover:bg-amber-100 transition-colors">
              <i class="fa-solid fa-phone text-xs"></i> 732 405 827
            </a>
            <a href="mailto:cap@jedenactka.eu" class="flex items-center justify-center gap-2 py-1.5 rounded bg-slate-50 text-slate-700 hover:bg-slate-100 transition-colors">
              <i class="fa-solid fa-envelope text-xs text-slate-400"></i> cap@jedenactka.eu
            </a>
          </div>
        </div>

        <!-- Garant 3: Skauti Středa -->
        <div class="bg-white rounded-xl p-5 shadow-sm border border-slate-200 hover:border-scout-blue transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-100 text-scout-blue">
                Skauti • Středa
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3 mb-3">
              <img src="avatars/avatar_19.jpg" alt="Max Rosenthaler – Werran" class="w-14 h-14 rounded-xl object-cover border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-sm font-heading">Werran</h4>
                <p class="text-xs font-semibold text-slate-700">Max Rosenthaler</p>
                <p class="text-[11px] text-slate-500">Garant středeční schůzky</p>
              </div>
            </div>

            <p class="text-xs text-slate-600 mb-3 bg-slate-50 p-2 rounded">
              Bárka (11–15 let). Schůzky skautů na vodě a na Valše.
            </p>
          </div>

          <div class="space-y-1.5 pt-3 border-t border-slate-100 text-xs">
            <a href="tel:+420728729518" class="flex items-center justify-center gap-2 py-1.5 rounded bg-sky-50 text-scout-navy font-bold hover:bg-sky-100 transition-colors">
              <i class="fa-solid fa-phone text-xs"></i> 728 729 518
            </a>
            <a href="mailto:werran@jedenactka.eu" class="flex items-center justify-center gap-2 py-1.5 rounded bg-slate-50 text-slate-700 hover:bg-slate-100 transition-colors">
              <i class="fa-solid fa-envelope text-xs text-slate-400"></i> werran@jedenactka.eu
            </a>
          </div>
        </div>

        <!-- Garant 4: Skauti Čtvrtek -->
        <div class="bg-white rounded-xl p-5 shadow-sm border border-slate-200 hover:border-scout-blue transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-100 text-scout-blue">
                Skauti • Čtvrtek
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3 mb-3">
              <img src="avatars/avatar_20.jpg" alt="František Kratochvíl – Fanda krátký" class="w-14 h-14 rounded-xl object-cover border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-sm font-heading">Fanda krátký</h4>
                <p class="text-xs font-semibold text-slate-700">František Kratochvíl</p>
                <p class="text-[11px] text-slate-500">Garant čtvrteční schůzky</p>
              </div>
            </div>

            <p class="text-xs text-slate-600 mb-3 bg-slate-50 p-2 rounded">
              Bárka (11–15 let). Čtvrteční posádkový program skautů.
            </p>
          </div>

          <div class="space-y-1.5 pt-3 border-t border-slate-100 text-xs">
            <a href="tel:+420722320570" class="flex items-center justify-center gap-2 py-1.5 rounded bg-sky-50 text-scout-navy font-bold hover:bg-sky-100 transition-colors">
              <i class="fa-solid fa-phone text-xs"></i> 722 320 570
            </a>
            <a href="mailto:franta@jedenactka.eu" class="flex items-center justify-center gap-2 py-1.5 rounded bg-slate-50 text-slate-700 hover:bg-slate-100 transition-colors">
              <i class="fa-solid fa-envelope text-xs text-slate-400"></i> franta@jedenactka.eu
            </a>
          </div>
        </div>

      </div>
    </div>

    <!-- 2. SKAUTSKÉ MAILY -->
    <div class="mb-12 bg-scout-sand border border-slate-300 rounded-2xl p-6 sm:p-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        <div class="lg:col-span-8 space-y-2">
          <span class="text-xs font-bold uppercase tracking-wider text-scout-blue">Samostatnost a komunikace</span>
          <h3 class="text-xl font-bold text-scout-navy font-heading">
            Skautské e-maily pod doménou @jedenactka.eu
          </h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
            Protože věříme, že nedílnou součástí skautské výchovy je i výchova k zodpovědnosti a samostatnosti, využíváme ke komunikaci se skauty Gmail pod vlastní doménou <code class="font-mono bg-white px-1.5 py-0.5 rounded text-scout-navy font-bold">@jedenactka.eu</code>. 
            Adresy jsou skautům přiděleny při příchodu do Bárky a dostávají na ně veškeré informace o akcích.
          </p>
          <div class="pt-1 text-xs font-semibold text-amber-900 bg-amber-100/70 p-2.5 rounded-lg border border-amber-200">
            <i class="fa-solid fa-circle-exclamation text-amber-600 mr-1"></i>
            <em>„Jestli nechceš rozzlobit Trolla, kontroluj si mail alespoň jednou týdně!“</em>
          </div>
        </div>
        <div class="lg:col-span-4 text-center">
          <a href="https://mail.google.com" target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-xs font-bold bg-scout-blue text-white hover:bg-scout-navy transition-all shadow-sm">
            <span>Přihlášení do Gmailu (@jedenactka.eu)</span>
            <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
          </a>
        </div>
      </div>
    </div>

    <!-- 3. FOTOARCHIVY A ODKAZY -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <span class="text-[10px] font-bold uppercase text-amber-800 bg-amber-100 px-2 py-0.5 rounded">Pro rodiče vlčat</span>
          <h4 class="text-base font-bold text-slate-900 font-heading mt-2">Vlčácké fotky</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed">
            Sekce chráněná heslem pro rodiče kluků z Toulavé smečky. Heslo sdělují garanti na schůzkách.
          </p>
        </div>
        <a href="https://jedenactka.skauting.cz/index.php/vlcacke-fotky/" target="_blank" class="mt-4 w-full py-2 rounded-lg bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs text-center block">
          <i class="fa-solid fa-lock text-xs mr-1"></i> Vstoupit do fotogalerie
        </a>
      </div>

      <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <span class="text-[10px] font-bold uppercase text-scout-blue bg-sky-100 px-2 py-0.5 rounded">Veřejná fotobanka</span>
          <h4 class="text-base font-bold text-slate-900 font-heading mt-2">Zonerama 11. oddílu</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed">
            Fotoalba z velkých akcí: 3 Jezy, letní tábory na řece, VVLnZ a srazy vodních skautů.
          </p>
        </div>
        <a href="https://eu.zonerama.com/11skautskyoddil/" target="_blank" class="mt-4 w-full py-2 rounded-lg bg-scout-blue hover:bg-scout-navy text-white font-bold text-xs text-center block">
          <i class="fa-solid fa-arrow-up-right-from-square text-xs mr-1"></i> Otevřít Zonerama
        </a>
      </div>

      <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <span class="text-[10px] font-bold uppercase text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded">Kronika</span>
          <h4 class="text-base font-bold text-slate-900 font-heading mt-2">Archiv akcí &amp; plakátků</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed">
            Historické plakátky a kroniky výprav a táborů oddílu od roku 2009 ke stažení.
          </p>
        </div>
        <a href="https://jedenactka.skauting.cz/index.php/oddil/archiv-akci/" target="_blank" class="mt-4 w-full py-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs text-center block border border-slate-300">
          <i class="fa-solid fa-file-pdf text-xs mr-1"></i> Zobrazit archiv
        </a>
      </div>

    </div>

    <!-- 4. ČASTO KLADENÉ OTÁZKY PRO RODIČE (FAQ) -->
    <div id="faq" class="mt-14 pt-10 border-t border-slate-200">
      <div class="text-center max-w-2xl mx-auto mb-8">
        <span class="text-xs font-bold uppercase tracking-wider text-scout-blue bg-sky-50 px-3 py-1 rounded-md">
          Dotazy &amp; Odpovědi
        </span>
        <h3 class="text-2xl font-extrabold text-scout-navy font-heading mt-2">
          Často kladené otázky rodičů
        </h3>
        <p class="text-slate-600 text-xs sm:text-sm mt-1">
          Vše podstatné o bezpečnosti, plavání, vybavení a fungování oddílu pro nové i stávající rodiče.
        </p>
      </div>

      <div class="max-w-3xl mx-auto space-y-2.5">
        {faq_cards_b}
      </div>
    </div>

  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: O ODDÍLU -->
  <!-- ======================================================================== -->
  <section id="oddil" class="py-16 bg-white dark:bg-slate-900 border-y border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center mb-12">
        <div class="lg:col-span-7 space-y-4">
          <span class="text-xs font-bold text-scout-blue uppercase tracking-wider">O 11. oddílu</span>
          <h2 class="text-3xl font-extrabold text-scout-navy font-heading">
            Vodní skauting v Českých Budějovicích
          </h2>
          <p class="text-slate-700 text-sm leading-relaxed">
            Náš oddíl patří k tzv. <strong>vodním skautům</strong>. Do programu zahrnujeme klasické skautské dovednosti obohacené o vodáctví – jízdu na pramicích P550, kanoích a plachetnicích. Sídlíme na základně Valcha u řeky Malše.
          </p>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
            Oddíl je podle věku rozdělen do čtyř částí (kterým říkáme <strong>paluby</strong>): 
            <strong>Toulavá smečka</strong> (vlčata 6–10 let), <strong>Bárka</strong> (skauti 11–15 let), <strong>Roverská VěTeV</strong> (od 16 let) a <strong>Klub 11. oddílu</strong> (bývalí vedoucí a přátelé oddílu). 
            První dvě paluby jsou děleny do posádek po 6–8 chlapcích, kteří se scházejí jednou týdně na dvouhodinových schůzkách.
          </p>
          <div class="p-3 bg-scout-sand rounded-xl border border-slate-200 text-xs text-slate-700">
            <strong>Oddílové barvy:</strong> Černo-žlutá vlajka 11. oddílu a žluté skautské šátky.
          </div>
        </div>

        <div class="lg:col-span-5">
          <img src="zonerama_valcha.jpg" alt="Základna Valcha" class="rounded-xl shadow-md border border-slate-200 w-full aspect-[4/3] object-cover">
        </div>
      </div>

      <!-- 4 PALUBY GRID -->
      <div id="paluby" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        <div class="p-5 rounded-xl border border-slate-200 bg-slate-50">
          <img src="logo_vlcata.png" alt="Vlčata" class="h-10 mb-3 object-contain">
          <div class="text-[11px] font-bold text-amber-700 uppercase">1. Paluba (6–10 let)</div>
          <h3 class="text-base font-bold text-slate-900 font-heading mt-1">Toulavá smečka</h3>
          <p class="text-xs text-slate-600 mt-1">Hry, poznávání přírody a první zkušenosti v posádce.</p>
        </div>

        <div class="p-5 rounded-xl border border-slate-200 bg-slate-50">
          <div class="w-10 h-10 rounded-lg bg-sky-100 text-scout-blue flex items-center justify-center text-xl mb-3">
            <i class="fa-solid fa-anchor"></i>
          </div>
          <div class="text-[11px] font-bold text-scout-blue uppercase">2. Paluba (11–15 let)</div>
          <h3 class="text-base font-bold text-slate-900 font-heading mt-1">Bárka</h3>
          <p class="text-xs text-slate-600 mt-1">Vodácký výcvik, vícedenní výpravy a samostatnost.</p>
        </div>

        <div class="p-5 rounded-xl border border-slate-200 bg-slate-50">
          <img src="logo_vetev.png" alt="Roveři" class="h-10 mb-3 object-contain">
          <div class="text-[11px] font-bold text-emerald-700 uppercase">3. Paluba (16+ let)</div>
          <h3 class="text-base font-bold text-slate-900 font-heading mt-1">Roverská VěTeV</h3>
          <p class="text-xs text-slate-600 mt-1">Zahraniční expedice, náročné projekty a služba.</p>
        </div>

        <div class="p-5 rounded-xl border border-slate-200 bg-slate-50">
          <div class="w-10 h-10 rounded-lg bg-purple-100 text-purple-700 flex items-center justify-center text-xl mb-3">
            <i class="fa-solid fa-mug-hot"></i>
          </div>
          <div class="text-[11px] font-bold text-purple-700 uppercase">4. Paluba (Bývalí vedoucí)</div>
          <h3 class="text-base font-bold text-slate-900 font-heading mt-1">Klub 11. oddílu</h3>
          <p class="text-xs text-slate-600 mt-1">Společná setkání bývalých vedoucích a podpora oddílu.</p>
        </div>

      </div>

    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: TERMÍNOVNÍK -->
  <!-- ======================================================================== -->
  <section id="terminovnik" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
      <div>
        <span class="text-xs font-bold text-scout-blue uppercase tracking-wider">Harmonogram</span>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-scout-navy font-heading">
          Termínovník akcí &amp; výprav
        </h2>
      </div>

      <div class="inline-flex p-1 rounded-lg bg-slate-200 border border-slate-300">
        <button id="tabBarkaB" onclick="switchTerminovnikB('barka')" class="px-4 py-2 rounded-md font-bold text-xs bg-scout-navy text-white transition-all">
          Bárka (Skauti)
        </button>
        <button id="tabVlcataB" onclick="switchTerminovnikB('vlcata')" class="px-4 py-2 rounded-md font-bold text-xs text-slate-700 hover:text-slate-900 transition-all">
          Toulavá smečka (Vlčata)
        </button>
      </div>
    </div>

    <!-- BARKA -->
    <div id="gridBarkaB" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {barka_cards}
    </div>

    <!-- VLCATA -->
    <div id="gridVlcataB" class="hidden grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {vlcata_cards}
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: AKTUALITY -->
  <!-- ======================================================================== -->
  <section id="aktuality" class="py-16 bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between mb-8">
        <div>
          <span class="text-xs font-bold text-scout-blue uppercase tracking-wider">Ze života oddílu</span>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-scout-navy font-heading">
            Aktuality z oddílu &amp; výprav
          </h2>
        </div>
        <a href="https://eu.zonerama.com/11skautskyoddil/" target="_blank" class="text-xs font-bold text-scout-blue hover:text-scout-navy flex items-center gap-1">
          <span>Celá fotogalerie na Zonerama</span>
          <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
        {blog_cards}
      </div>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: VYBAVENÍ -->
  <!-- ======================================================================== -->
  <section id="vybaveni" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-2xl mx-auto mb-10">
      <span class="text-xs font-bold text-scout-blue uppercase tracking-wider">Výbava</span>
      <h2 class="text-2xl sm:text-3xl font-extrabold text-scout-navy font-heading">
        Co s sebou na schůzku a na vodu
      </h2>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="p-5 rounded-xl border border-slate-200 bg-white">
        <h4 class="font-bold text-scout-navy text-sm font-heading mb-2"><i class="fa-solid fa-pencil text-amber-600 mr-1.5"></i> Na běžnou schůzku</h4>
        <ul class="text-xs text-slate-600 space-y-1.5">
          <li>• Zápisník a tužka</li>
          <li>• Žlutý oddílový šátek</li>
          <li>• Uzlovačka (2–3 m)</li>
          <li>• Pití v lahvi</li>
          <li>• Přezůvky do klubovny</li>
        </ul>
      </div>

      <div class="p-5 rounded-xl border border-slate-200 bg-white">
        <h4 class="font-bold text-scout-navy text-sm font-heading mb-2"><i class="fa-solid fa-vest-patches text-scout-blue mr-1.5"></i> Na vodu</h4>
        <ul class="text-xs text-slate-600 space-y-1.5">
          <li>• Záchranná vesta (půjčí oddíl)</li>
          <li>• Pevné boty do vody</li>
          <li>• Náhradní oblečení v igelitu</li>
          <li>• Ručník &amp; plavky</li>
          <li>• Čepice proti slunci</li>
        </ul>
      </div>

      <div class="p-5 rounded-xl border border-slate-200 bg-white">
        <h4 class="font-bold text-scout-navy text-sm font-heading mb-2"><i class="fa-solid fa-campground text-emerald-600 mr-1.5"></i> Na výpravu</h4>
        <ul class="text-xs text-slate-600 space-y-1.5">
          <li>• Spacák a karimatka</li>
          <li>• Pevná obuv do terénu</li>
          <li>• Ešus, lžíce, čelovka</li>
          <li>• Skautský kroj</li>
          <li>• Pláštěnka</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: ZÁKLADNA VALCHA -->
  <!-- ======================================================================== -->
  <section id="lodenice" class="py-16 bg-scout-sand dark:bg-slate-900 border-y border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-6 space-y-3">
          <span class="text-xs font-bold text-scout-blue uppercase">Zázemí</span>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-scout-navy font-heading">
            Základna Valcha na řece Malši
          </h2>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
            Vlastní základna Valcha s hangárem na lodě, klubovnami, travnatou loukou, dílnou a přístupem k vodě u Malého jezu v Českých Budějovicích.
          </p>
        </div>
        <div class="lg:col-span-6 space-y-3">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            
            <!-- Foto 1 -->
            <div onclick="handleLodeniceClickB(1)" class="relative rounded-xl overflow-hidden aspect-[4/3] shadow border border-slate-300 hover:border-scout-blue bg-slate-900 group cursor-pointer select-none transition-all duration-300" title="Klikněte do fotky pro změnu">
              <img id="lodeniceImg1B" src="zonerama_valcha.jpg" alt="Základna Valcha" class="w-full h-full object-cover transition-opacity duration-300 group-hover:scale-105 transition-transform">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-transparent to-transparent flex flex-col justify-between p-3 pointer-events-none">
                <div class="flex justify-between items-start">
                  <span id="lodeniceTag1B" class="text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-scout-navy text-white">Zázemí u řeky</span>
                  <span class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-slate-900/80 text-[10px] text-white opacity-80 group-hover:opacity-100 transition-opacity">
                    <i class="fa-solid fa-hand-pointer text-[9px]"></i> Klikni
                  </span>
                </div>
                <p id="lodeniceTitle1B" class="text-xs font-bold text-white leading-tight">Klubovny a život na Valše při schůzkách</p>
              </div>
            </div>

            <!-- Foto 2 -->
            <div onclick="handleLodeniceClickB(2)" class="relative rounded-xl overflow-hidden aspect-[4/3] shadow border border-slate-300 hover:border-scout-blue bg-slate-900 group cursor-pointer select-none transition-all duration-300" title="Klikněte do fotky pro změnu">
              <img id="lodeniceImg2B" src="zonerama_1.jpg" alt="Vodácký trénink" class="w-full h-full object-cover transition-opacity duration-300 group-hover:scale-105 transition-transform">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-transparent to-transparent flex flex-col justify-between p-3 pointer-events-none">
                <div class="flex justify-between items-start">
                  <span id="lodeniceTag2B" class="text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-scout-blue text-white">Vodácký výcvik</span>
                  <span class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-slate-900/80 text-[10px] text-white opacity-80 group-hover:opacity-100 transition-opacity">
                    <i class="fa-solid fa-hand-pointer text-[9px]"></i> Klikni
                  </span>
                </div>
                <p id="lodeniceTitle2B" class="text-xs font-bold text-white leading-tight">Molo a trénink posádek</p>
              </div>
            </div>

          </div>

          <div class="flex items-center justify-between pt-1 text-xs text-slate-500">
            <span class="flex items-center gap-1.5 text-[11px]">
              <i class="fa-solid fa-shuffle text-scout-blue"></i>
              Fotky loděnice se automaticky náhodně mění
            </span>
            <button onclick="randomizeLodenicePhotosB()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white hover:bg-slate-100 text-scout-blue font-bold text-xs border border-slate-300 shadow-2xs transition-all cursor-pointer">
              <i class="fa-solid fa-dice"></i>
              <span>Náhodná fotka</span>
            </button>
          </div>
        </div>
      </div>

      <!-- INTERAKTIVNÍ MAPA & NAVIGACE K VALŠE -->
      <div class="mt-12 pt-8 border-t border-slate-300">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          
          <!-- Left: OpenStreetMap Interactive Embed -->
          <div class="lg:col-span-7 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-scout-blue uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-map-location-dot"></i> Interaktivní mapa základny Valcha
              </span>
              <span class="text-[11px] text-slate-500 font-medium">Stromovka 3, České Budějovice</span>
            </div>

            <div class="relative rounded-xl overflow-hidden shadow-md border border-slate-300 bg-slate-900 aspect-[16/10] sm:aspect-[16/9]">
              <iframe 
                title="Mapa základny Valcha České Budějovice"
                class="w-full h-full border-0 filter contrast-105" 
                src="https://www.openstreetmap.org/export/embed.html?bbox=14.4621%2C48.9675%2C14.4761%2C48.9765&amp;layer=mapnik&amp;marker=48.9720617%2C14.4690989"
                loading="lazy">
              </iframe>
              <div class="absolute top-3 left-3 px-3 py-1.5 rounded-lg bg-scout-navy/90 backdrop-blur-md text-white text-xs font-bold shadow pointer-events-none flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>Základna Valcha (11. oddíl)</span>
              </div>
            </div>

            <!-- Rychlá navigační tlačítka -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-1">
              <a href="https://mapy.cz/zakladni?q=48.9720617N%2C+14.4690989E" target="_blank" class="flex items-center justify-center gap-2 px-3 py-2 rounded-lg bg-scout-blue hover:bg-scout-navy text-white font-bold text-xs transition-colors shadow-2xs">
                <i class="fa-solid fa-diamond-turn-right text-xs"></i>
                <span>Navigovat v Mapy.cz</span>
              </a>
              <a href="https://www.google.com/maps/search/?api=1&query=48.9720617,14.4690989" target="_blank" class="flex items-center justify-center gap-2 px-3 py-2 rounded-lg bg-white hover:bg-slate-100 text-slate-800 border border-slate-300 font-bold text-xs transition-colors">
                <i class="fa-brands fa-google text-xs text-scout-blue"></i>
                <span>Google Maps</span>
              </a>
              <a href="https://idos.idnes.cz/ceskebudejovice/spojeni/" target="_blank" class="flex items-center justify-center gap-2 px-3 py-2 rounded-lg bg-scout-sand hover:bg-slate-200 text-scout-navy border border-slate-300 font-bold text-xs transition-colors">
                <i class="fa-solid fa-bus text-xs"></i>
                <span>Spojení MHD (IDOS)</span>
              </a>
            </div>
          </div>

          <!-- Right: Průvodce příchodem & praktické rady pro rodiče -->
          <div class="lg:col-span-5 bg-white rounded-xl p-5 border border-slate-300 shadow-2xs space-y-3.5">
            <h3 class="text-base font-bold text-scout-navy font-heading flex items-center gap-2">
              <i class="fa-solid fa-route text-scout-blue"></i> Kudy k nám na Valchu
            </h3>

            <div class="space-y-3 text-xs text-slate-600">
              <div class="flex items-start gap-2.5">
                <div class="w-7 h-7 rounded-md bg-sky-50 text-scout-blue flex items-center justify-center shrink-0 text-xs mt-0.5">
                  <i class="fa-solid fa-location-dot"></i>
                </div>
                <div>
                  <strong class="text-slate-900 block">Adresa &amp; GPS</strong>
                  <span>Stromovka 3 (Valcha), 370 01 České Budějovice</span><br>
                  <code class="text-slate-800 font-mono text-[11px]">48.9720617° N, 14.4690989° E</code>
                </div>
              </div>

              <div class="flex items-start gap-2.5">
                <div class="w-7 h-7 rounded-md bg-amber-50 text-amber-700 flex items-center justify-center shrink-0 text-xs mt-0.5">
                  <i class="fa-solid fa-bus"></i>
                </div>
                <div>
                  <strong class="text-slate-900 block">Městská doprava (MHD)</strong>
                  <span>Zastávka <em>Výstaviště</em> nebo <em>U Parku</em>. Cca 5–7 min pěšky parkem Stromovka podél vody.</span>
                </div>
              </div>

              <div class="flex items-start gap-2.5">
                <div class="w-7 h-7 rounded-md bg-emerald-50 text-emerald-700 flex items-center justify-center shrink-0 text-xs mt-0.5">
                  <i class="fa-solid fa-bicycle"></i>
                </div>
                <div>
                  <strong class="text-slate-900 block">Na kole a pěšky</strong>
                  <span>Páteřní cyklostezka vede přímo před Valchou. K dispozici stojany na kola.</span>
                </div>
              </div>

              <div class="flex items-start gap-2.5">
                <div class="w-7 h-7 rounded-md bg-slate-100 text-slate-700 flex items-center justify-center shrink-0 text-xs mt-0.5">
                  <i class="fa-solid fa-square-parking"></i>
                </div>
                <div>
                  <strong class="text-slate-900 block">Autem &amp; Parkování</strong>
                  <span>Parkování v ulici Stromovka / Na Zlaté stoce. K samotné základně Valcha je pěší zóna a zákaz vjezdu aut.</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: NÁBOR -->
  <!-- ======================================================================== -->
  <section id="nabor" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <div class="bg-scout-navy rounded-2xl p-8 sm:p-12 text-white">
      <h2 class="text-2xl sm:text-3xl font-extrabold font-heading">
        Nábor chlapců do oddílu
      </h2>
      <p class="text-slate-300 text-xs sm:text-sm max-w-xl mx-auto mt-2">
        Přijímáme chlapce od 6 do 14 let. První tři schůzky jsou nezávazné. Přijďte se podívat!
      </p>
      <div class="mt-6 flex justify-center gap-3">
        <a href="#kontakty" class="px-5 py-2.5 rounded-lg bg-yellow-400 text-slate-950 font-bold text-xs hover:bg-yellow-300">
          Kontaktovat vůdce oddílu
        </a>
        <a href="#pro-rodice" class="px-5 py-2.5 rounded-lg bg-white/10 text-white font-bold text-xs hover:bg-white/20 border border-white/20">
          Časy schůzek &amp; garanti
        </a>
      </div>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: KONTAKTY S REÁLNÝMI FOTKAMI -->
  <!-- ======================================================================== -->
  <section id="kontakty" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-2xl mx-auto mb-10">
      <span class="text-xs font-bold text-scout-blue uppercase tracking-wider">Kontakty</span>
      <h2 class="text-2xl sm:text-3xl font-extrabold text-scout-navy font-heading">
        Vedení oddílu &amp; Klíčové kontakty
      </h2>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
      
      <!-- Hopík -->
      <div class="bg-white rounded-xl p-6 border border-slate-200 shadow-sm text-center flex flex-col justify-between">
        <div>
          <img src="avatars/avatar_1.jpg" alt="Martin Hájek – Hopík" class="w-20 h-20 mx-auto rounded-xl object-cover border-2 border-scout-blue mb-3">
          <span class="text-[10px] font-bold uppercase text-white bg-scout-navy px-2 py-0.5 rounded">Kapitán oddílu</span>
          <h3 class="text-base font-bold text-slate-900 font-heading mt-2">Hopík</h3>
          <p class="text-xs font-semibold text-slate-700">Martin Hájek</p>
          <p class="text-xs text-slate-500 mt-2">Celkové vedení oddílu a oficiální komunikace.</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-100 text-xs space-y-1.5">
          <div><a href="tel:+420733238774" class="text-slate-700 hover:text-scout-blue font-semibold inline-flex items-center gap-1.5"><i class="fa-solid fa-phone text-scout-blue"></i> 733 238 774</a></div>
          <div><a href="mailto:hopik@jedenactka.eu" class="text-slate-700 hover:text-scout-blue font-semibold inline-flex items-center gap-1.5"><i class="fa-solid fa-envelope text-scout-blue"></i> hopik@jedenactka.eu</a></div>
        </div>
      </div>

      <!-- Knedlík -->
      <div class="bg-white rounded-xl p-6 border border-slate-200 shadow-sm text-center flex flex-col justify-between">
        <div>
          <img src="avatars/avatar_2.jpg" alt="David Hacker – Knedlík" class="w-20 h-20 mx-auto rounded-xl object-cover border-2 border-amber-400 mb-3">
          <span class="text-[10px] font-bold uppercase text-amber-900 bg-amber-100 px-2 py-0.5 rounded">Důstojník Toulavé smečky</span>
          <h3 class="text-base font-bold text-slate-900 font-heading mt-2">Knedlík</h3>
          <p class="text-xs font-semibold text-slate-700">David Hacker</p>
          <p class="text-xs text-slate-500 mt-2">Hlavní vedoucí Toulavé smečky (vlčata 6–10 let).</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-100 text-xs space-y-1.5">
          <div><a href="tel:+420604458758" class="text-slate-700 hover:text-amber-600 font-semibold inline-flex items-center gap-1.5"><i class="fa-solid fa-phone text-amber-600"></i> 604 458 758</a></div>
          <div><a href="mailto:knedlik@jedenactka.eu" class="text-slate-700 hover:text-amber-600 font-semibold inline-flex items-center gap-1.5"><i class="fa-solid fa-envelope text-amber-600"></i> knedlik@jedenactka.eu</a></div>
          <div class="text-[11px] text-slate-400">Garanti schůzek viz sekce Pro rodiče</div>
        </div>
      </div>

      <!-- Vodník -->
      <div class="bg-white rounded-xl p-6 border border-slate-200 shadow-sm text-center flex flex-col justify-between">
        <div>
          <img src="avatars/avatar_17.jpg" alt="Vít Veltrubský – Vodník" class="w-20 h-20 mx-auto rounded-xl object-cover border-2 border-sky-400 mb-3">
          <span class="text-[10px] font-bold uppercase text-scout-blue bg-sky-100 px-2 py-0.5 rounded">Důstojník Bárky</span>
          <h3 class="text-base font-bold text-slate-900 font-heading mt-2">Vodník / Slon</h3>
          <p class="text-xs font-semibold text-slate-700">Vít Veltrubský</p>
          <p class="text-xs text-slate-500 mt-2">Důstojník skautské paluby Bárka (chlapci 11–15 let).</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-100 text-xs space-y-1.5">
          <div><a href="tel:+420724687854" class="text-slate-700 hover:text-scout-blue font-semibold inline-flex items-center gap-1.5"><i class="fa-solid fa-phone text-scout-blue"></i> 724 687 854</a></div>
          <div><a href="mailto:vodnik@jedenactka.eu" class="text-slate-700 hover:text-scout-blue font-semibold inline-flex items-center gap-1.5"><i class="fa-solid fa-envelope text-scout-blue"></i> vodnik@jedenactka.eu</a></div>
          <div class="text-[11px] text-slate-400">Garanti schůzek Werran &amp; Fanda krátký</div>
        </div>
      </div>

    </div>

    <!-- BANNER TO VEDENI.HTML -->
    <div class="p-6 rounded-xl bg-scout-sand border border-slate-300 text-center flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="text-left">
        <h4 class="font-bold text-scout-navy text-sm font-heading">Kompletní vedení oddílu (34 vedoucích a lodivodů)</h4>
        <p class="text-xs text-slate-600">Prohlédněte si profily, kvalifikace a funkce všech vedoucích Jedenáctky.</p>
      </div>
      <a href="vedeni.html" class="px-5 py-2.5 rounded-lg text-xs font-bold bg-scout-blue text-white hover:bg-scout-navy transition-all shrink-0">
        Zobrazit všech 34 vedoucích &rarr;
      </a>
    </div>

  </section>

  <!-- FOOTER -->
  <footer class="bg-scout-navy text-slate-300 text-xs py-8 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4">
      <div class="flex items-center gap-2">
        <img src="logo_emblem.png" alt="11. oddíl vodních skautů" class="h-7 w-auto object-contain brightness-110">
        <span class="font-bold text-white">11. oddíl vodních skautů České Budějovice</span>
      </div>
      <div class="text-slate-400 text-center sm:text-right flex flex-col sm:flex-row items-center justify-end gap-1.5 sm:gap-2">
        <span class="text-slate-300">Verze: {get_app_version()} ({get_git_commit()})</span>
        <span class="hidden sm:inline text-slate-600">•</span>
        <span class="text-slate-300">Aktualizováno: {BUILD_TIMESTAMP}</span>
        <span class="hidden sm:inline text-slate-600">•</span>
        <span>Registrováno u Junák – český skaut, 4. středisko VAVÉHA České Budějovice.</span>
      </div>
    </div>
  </footer>

  <script>
    const mobileMenuBtnB = document.getElementById('mobileMenuBtnB');
    const mobileMenuB = document.getElementById('mobileMenuB');
    if (mobileMenuBtnB && mobileMenuB) {{
      mobileMenuBtnB.addEventListener('click', () => {{
        mobileMenuB.classList.toggle('hidden');
      }});
      mobileMenuB.querySelectorAll('a').forEach(link => {{
        link.addEventListener('click', () => {{
          mobileMenuB.classList.add('hidden');
        }});
      }});
    }}

    function switchTerminovnikB(tab) {{
      const gridBarka = document.getElementById('gridBarkaB');
      const gridVlcata = document.getElementById('gridVlcataB');
      const tabBarka = document.getElementById('tabBarkaB');
      const tabVlcata = document.getElementById('tabVlcataB');

      if (tab === 'barka') {{
        gridBarka.classList.remove('hidden');
        gridBarka.classList.add('grid');
        gridVlcata.classList.add('hidden');
        gridVlcata.classList.remove('grid');

        tabBarka.className = "px-4 py-2 rounded-md font-bold text-xs bg-scout-navy text-white transition-all";
        tabVlcata.className = "px-4 py-2 rounded-md font-bold text-xs text-slate-700 hover:text-slate-900 transition-all";
      }} else {{
        gridVlcata.classList.remove('hidden');
        gridVlcata.classList.add('grid');
        gridBarka.classList.add('hidden');
        gridBarka.classList.remove('grid');

        tabVlcata.className = "px-4 py-2 rounded-md font-bold text-xs bg-scout-navy text-white transition-all";
        tabBarka.className = "px-4 py-2 rounded-md font-bold text-xs text-slate-700 hover:text-slate-900 transition-all";
      }}
    }}

    // FAQ accordion toggle
    function toggleFaqB(idx) {{
      const ans = document.getElementById('faqAnsB' + idx);
      const icon = document.getElementById('faqIconB' + idx);
      if (!ans) return;
      const isHidden = ans.classList.contains('hidden');
      if (isHidden) {{
        ans.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
      }} else {{
        ans.classList.add('hidden');
        if (icon) icon.classList.remove('rotate-180');
      }}
    }}

    // Základna Valcha - náhodné střídání existujících fotek
    const lodenicePhotosB = [
      {{ src: "zonerama_valcha.jpg", title: "Klubovny a život na Valše při schůzkách", tag: "Základna Valcha" }},
      {{ src: "zonerama_1.jpg", title: "Trénink na vodě a přístaviště u řeky", tag: "Vodácký výcvik" }},
      {{ src: "foto_3.jpg", title: "Základna Valcha na břehu řeky Malše", tag: "Zázemí u řeky" }},
      {{ src: "foto_6.jpg", title: "Molo a trénink posádek na vodě", tag: "Vodácký výcvik" }},
      {{ src: "barka_1.jpg", title: "Lodní hangár a budova základny", tag: "Lodní hangár" }},
      {{ src: "barka_2.jpg", title: "Klubovny a travnaté prostranství", tag: "Zázemí pro hry" }},
      {{ src: "upload_2.png", title: "Pramice P550 a plachetnice Jedenáctky", tag: "Flotila lodí" }},
      {{ src: "upload_1.jpg", title: "Areál základny v přírodě u Malého jezu", tag: "Klidná lokalita" }}
    ];

    let currentLodeniceIdx1B = Math.floor(Math.random() * lodenicePhotosB.length);
    let currentLodeniceIdx2B = (currentLodeniceIdx1B + 1) % lodenicePhotosB.length;

    function randomizeSingleLodeniceB(slot) {{
      if (slot === 1) {{
        let newIdx1 = Math.floor(Math.random() * lodenicePhotosB.length);
        while ((newIdx1 === currentLodeniceIdx1B || newIdx1 === currentLodeniceIdx2B) && lodenicePhotosB.length > 2) {{
          newIdx1 = Math.floor(Math.random() * lodenicePhotosB.length);
        }}
        currentLodeniceIdx1B = newIdx1;
        applySingleLodenicePhotoB(1);
      }} else {{
        let newIdx2 = Math.floor(Math.random() * lodenicePhotosB.length);
        while ((newIdx2 === currentLodeniceIdx2B || newIdx2 === currentLodeniceIdx1B) && lodenicePhotosB.length > 2) {{
          newIdx2 = Math.floor(Math.random() * lodenicePhotosB.length);
        }}
        currentLodeniceIdx2B = newIdx2;
        applySingleLodenicePhotoB(2);
      }}
    }}

    function handleLodeniceClickB(slot) {{
      randomizeSingleLodeniceB(slot);
      startLodeniceTimerB();
    }}

    function randomizeLodenicePhotosB() {{
      let newIdx1 = Math.floor(Math.random() * lodenicePhotosB.length);
      while (newIdx1 === currentLodeniceIdx1B && lodenicePhotosB.length > 1) {{
        newIdx1 = Math.floor(Math.random() * lodenicePhotosB.length);
      }}
      currentLodeniceIdx1B = newIdx1;
      
      let newIdx2 = Math.floor(Math.random() * lodenicePhotosB.length);
      while ((newIdx2 === currentLodeniceIdx1B || newIdx2 === currentLodeniceIdx2B) && lodenicePhotosB.length > 2) {{
        newIdx2 = Math.floor(Math.random() * lodenicePhotosB.length);
      }}
      currentLodeniceIdx2B = newIdx2;

      applyLodenicePhotosB();
    }}

    function getAssetUrlB(url) {{
      if (!url) return '';
      if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('/') || url.startsWith('data:')) return url;
      const base = (typeof window.WP_THEME_URI !== 'undefined') ? window.WP_THEME_URI : '';
      return base + url;
    }}

    function applySingleLodenicePhotoB(slot) {{
      if (slot === 1) {{
        const img1 = document.getElementById('lodeniceImg1B');
        const title1 = document.getElementById('lodeniceTitle1B');
        const tag1 = document.getElementById('lodeniceTag1B');
        if (img1) {{
          img1.style.opacity = '0.2';
          setTimeout(() => {{
            img1.src = getAssetUrlB(lodenicePhotosB[currentLodeniceIdx1B].src);
            img1.alt = lodenicePhotosB[currentLodeniceIdx1B].title;
            if (title1) title1.textContent = lodenicePhotosB[currentLodeniceIdx1B].title;
            if (tag1) tag1.textContent = lodenicePhotosB[currentLodeniceIdx1B].tag;
            img1.style.opacity = '1';
          }}, 180);
        }}
      }} else {{
        const img2 = document.getElementById('lodeniceImg2B');
        const title2 = document.getElementById('lodeniceTitle2B');
        const tag2 = document.getElementById('lodeniceTag2B');
        if (img2) {{
          img2.style.opacity = '0.2';
          setTimeout(() => {{
            img2.src = getAssetUrlB(lodenicePhotosB[currentLodeniceIdx2B].src);
            img2.alt = lodenicePhotosB[currentLodeniceIdx2B].title;
            if (title2) title2.textContent = lodenicePhotosB[currentLodeniceIdx2B].title;
            if (tag2) tag2.textContent = lodenicePhotosB[currentLodeniceIdx2B].tag;
            img2.style.opacity = '1';
          }}, 180);
        }}
      }}
    }}

    function applyLodenicePhotosB() {{
      applySingleLodenicePhotoB(1);
      applySingleLodenicePhotoB(2);
    }}

    let lodeniceTimerB = null;
    function startLodeniceTimerB() {{
      if (lodeniceTimerB) clearInterval(lodeniceTimerB);
      lodeniceTimerB = setInterval(() => {{
        randomizeLodenicePhotosB();
      }}, 4000);
    }}

    // Hero záhlaví - náhodné a automatické střídání fotografií
    // Fotografie čerpané z oddílové fotogalerie Zonerama za poslední rok
    const heroPhotosB = [
      {{ src: "zonerama_2.jpg", tag: "Společná voda 2026", title: "Vodácká dobrodružství & sjíždění šlajsny na kánoi" }},
      {{ src: "zonerama_1.jpg", tag: "Slalomový kanál 2026", title: "České Vrbné • trénink na divoké vodě a výcvik pádlování" }},
      {{ src: "zonerama_3.jpg", tag: "3 Jezy Praha 2025", title: "Posádka 11. oddílu na prestižním závodě Napříč Prahou" }},
      {{ src: "zonerama_5.jpg", tag: "Expedice na vodě", title: "Příroda a putování po jihočeských řekách" }},
      {{ src: "zonerama_valcha.jpg", tag: "Život na Valše", title: "Týmové hry v klubovně a celoroční program schůzek" }},
      {{ src: "zonerama_camp.jpg", tag: "Tábor Labská Stráň 2026", title: "Lezení ve skalách a táborové výzvy v přírodě" }},
      {{ src: "zonerama_6.jpg", tag: "Kajaky v peřejích", title: "Slalomový trénink mezi brankami na divoké vodě" }},
      {{ src: "zonerama_hero_1.jpg", tag: "Vánoce na Švýcaráku", title: "Tradiční vánoční setkání oddílu na srubové základně Švýcarák" }},
      {{ src: "zonerama_hero_2.jpg", tag: "Vánoce na Švýcaráku", title: "Kouzlo Vánoc, oddílové zvyky a dárky v zasněžených lesích" }},
      {{ src: "zonerama_hero_3.jpg", tag: "Výprava všech lidí", title: "Společné dobrodružství a setkání generací vodních skautů" }},
      {{ src: "zonerama_hero_4.jpg", tag: "Výprava všech lidí", title: "Špekáčky, kytary a přátelství v údolí řeky Vltavy" }},
      {{ src: "zonerama_hero_5.jpg", tag: "Brigáda na Švýcaráku", title: "Příprava palivového dříví na zimu a údržba oddílového srubu" }},
      {{ src: "zonerama_hero_6.jpg", tag: "3 Jezy Praha 2025", title: "Reprezentace 11. oddílu na legendárním závodě Napříč Prahou" }},
      {{ src: "zonerama_hero_7.jpg", tag: "3 Jezy Praha 2025", title: "Průjezd vorovou propustí v peřejích historického centra Prahy" }},
      {{ src: "zonerama_hero_8.jpg", tag: "Slalomový kanál 2026", title: "Trénink pádlování a stability posádek mezi brankami" }},
      {{ src: "zonerama_hero_9.jpg", tag: "Společná voda 2026", title: "Putování na kanoích po jihočeských řekách a vodácká kamarádství" }},
      {{ src: "zonerama_hero_10.jpg", tag: "Tábor Labská Stráň 2026", title: "Skalní lezení, lanové techniky a odvaha v Labském kaňonu" }}
    ];

    let currentHeroIdxB = Math.floor(Math.random() * heroPhotosB.length);

    function randomizeHeroPhotoB() {{
      let newIdx = Math.floor(Math.random() * heroPhotosB.length);
      while (newIdx === currentHeroIdxB && heroPhotosB.length > 1) {{
        newIdx = Math.floor(Math.random() * heroPhotosB.length);
      }}
      currentHeroIdxB = newIdx;
      applyHeroPhotoB();
    }}

    function handleHeroClickB() {{
      randomizeHeroPhotoB();
      startHeroTimerB();
    }}

    function applyHeroPhotoB() {{
      const img = document.getElementById('heroImgB');
      const tag = document.getElementById('heroTagB');
      const title = document.getElementById('heroTitleB');

      if (img) {{
        img.style.opacity = '0.2';
        setTimeout(() => {{
          const item = heroPhotosB[currentHeroIdxB];
          img.src = getAssetUrlB(item.src);
          img.alt = item.title;
          if (tag) tag.textContent = item.tag;
          if (title) title.textContent = item.title;
          img.style.opacity = '1';
        }}, 200);
      }}
    }}

    let heroTimerB = null;
    function startHeroTimerB() {{
      if (heroTimerB) clearInterval(heroTimerB);
      heroTimerB = setInterval(() => {{
        randomizeHeroPhotoB();
      }}, 5000);
    }}

    // Spustit náhodnou fotku v záhlaví hned při načtení a zapnout rotaci
    applyHeroPhotoB();
    startHeroTimerB();

    // Spustit náhodné fotky loděnice a zapnout rotaci
    randomizeLodenicePhotosB();
    startLodeniceTimerB();

    // Přepínač tmavého / světlého režimu s localStorage
    function toggleTheme() {{
      document.documentElement.classList.add('theme-transition');
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.theme = isDark ? 'dark' : 'light';
      updateThemeIcons();
      setTimeout(() => {{
        document.documentElement.classList.remove('theme-transition');
      }}, 300);
    }}

    function updateThemeIcons() {{
      const isDark = document.documentElement.classList.contains('dark');
      document.querySelectorAll('.theme-toggle-icon').forEach(icon => {{
        if (isDark) {{
          icon.className = 'fa-solid fa-sun text-yellow-400 theme-toggle-icon';
        }} else {{
          icon.className = 'fa-solid fa-moon text-slate-800 theme-toggle-icon';
        }}
      }});
      document.querySelectorAll('.theme-toggle-text').forEach(t => {{
        t.textContent = isDark ? 'Světlý režim' : 'Tmavý režim';
      }});
    }}
    updateThemeIcons();
  </script>

{get_search_modal_html()}
{get_search_script_js()}
</body>
</html>
"""
    with open('verzeB/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully generated verzeB/index.html")

# Build verzeB/vedeni.html
def generate_vedeni_b():
    leader_cards = []
    for i, l in enumerate(leaders):
        raw = l.get('raw', [])
        name = l.get('name', '')
        avatar = f"avatars/avatar_{i+1}.jpg" if (i+1) <= 34 else "avatars/avatar_1.jpg"
        
        # Specifická oprava pro Šamana (Mag. iur. Christopher Alexander De La Cruz)
        if name.startswith('Mag. iur.') or i == 29:
            name = 'Mag. iur. Christopher Alexander De La Cruz'
            nick = 'Šaman'
            role = 'Lodivod • Manažer tabulkových systémů'
        else:
            nick = ""
            for item in raw:
                if "–" in item and len(item.replace("–", "").strip()) > 0 and not any(k in item.lower() for k in ['kapitán', 'vůdce', 'důstojník', 'lodivod', 'garant']):
                    nick = item.replace("–", "").strip()
                    break
            if not nick and len(raw) > 2 and "–" in raw[1]:
                nick = raw[2].strip()

            role = ""
            for item in raw:
                if any(k in item.lower() for k in ['kapitán', 'vůdce', 'důstojník', 'garant', 'lodivod', 'zdravotník']):
                    role = item.replace("–", "").strip()
                    break
            if not role: role = "Lodivod"

        raw_str = " ".join(raw).lower()
        if "kapitán" in raw_str or "vůdce" in raw_str:
            badge_text = "Vedení oddílu"
            badge_color = "bg-scout-navy text-white"
            filter_cat = "vedeni"
        elif "toulav" in raw_str or "smečk" in raw_str or any(n in raw_str for n in ['myšák', 'čáp', 'knedlík', 'kraken', 'sponzor', 'rusalka', 'achilles', 'sisi', 'bobr', 'medůza', 'tulák', 'ríša', 'trasher', 'jerhi', 'venda']):
            badge_text = "Toulavá smečka (vlčata)"
            badge_color = "bg-amber-100 text-amber-900 border-amber-300"
            filter_cat = "vlcata"
        else:
            badge_text = "Bárka (skauti)"
            badge_color = "bg-sky-100 text-scout-blue border-sky-300"
            filter_cat = "skauti"

        phone = ""
        email = ""
        for item in raw:
            if "tel." in item.lower() or re.search(r'\d{3}\s*\d{3}\s*\d{3}', item):
                phone = item.replace("tel.:", "").replace("tel.", "").strip()
            if "@" in item:
                email = item.strip()

        extra = []
        for j, item in enumerate(raw):
            if "má na starosti:" in item.lower() and j+1 < len(raw):
                extra.append(f"<strong>Má na starosti:</strong> {h(raw[j+1])}")
            if "kvalifikace:" in item.lower() and j+1 < len(raw):
                extra.append(f"<strong>Kvalifikace:</strong> {h(raw[j+1])}")
            if "pozice:" in item.lower() or "pozice" in item.lower() and j+1 < len(raw):
                extra.append(f"<strong>Funkce:</strong> {h(raw[j+1].replace(':', '').strip())}")

        extra_html = "".join([f'<div class="text-[11px] text-slate-600 bg-slate-50 p-2 rounded border border-slate-200 mt-1">{ex}</div>' for ex in extra])

        contacts_html = ""
        if phone:
            clean_digits = re.sub(r'[^0-9+]', '', phone)
            if not clean_digits.startswith('+'):
                clean_digits = f'+420{clean_digits}'
            contacts_html += f'<a href="tel:{clean_digits}" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-semibold transition-colors"><i class="fa-solid fa-phone text-scout-blue"></i> {phone}</a> '
        if email:
            contacts_html += f'<a href="mailto:{email}" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-semibold transition-colors"><i class="fa-solid fa-envelope text-scout-blue"></i> {email}</a>'

        card = f"""
        <div class="leader-card-b {filter_cat} bg-white rounded-xl p-5 shadow-sm border border-slate-200 hover:border-scout-blue hover:shadow transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-start gap-3 mb-3">
              <div class="w-16 h-16 rounded-lg overflow-hidden shrink-0 border border-slate-200 bg-slate-100">
                <img src="{avatar}" alt="{h(name)}" class="w-full h-full object-cover">
              </div>
              <div>
                <span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider border mb-1 {badge_color}">
                  {badge_text}
                </span>
                <h3 class="text-base font-bold text-scout-navy font-heading leading-tight">{h(nick if nick else name)}</h3>
                {f'<p class="text-xs font-semibold text-slate-700 mt-0.5">{h(name)}</p>' if nick else ''}
                <p class="text-[11px] font-medium text-scout-blue mt-0.5">{h(role)}</p>
              </div>
            </div>

            <div class="space-y-1">
              {extra_html}
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 flex flex-wrap gap-2">
            {contacts_html}
          </div>
        </div>
        """
        leader_cards.append(card)

    html = f"""<!DOCTYPE html>
<html lang="cs" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vedení oddílu | 11. oddíl vodních skautů České Budějovice</title>
{get_version_meta_html()}
  
  <script>
    if (localStorage.theme === 'dark') {{
      document.documentElement.classList.add('dark');
    }} else {{
      document.documentElement.classList.remove('dark');
    }}
  </script>

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            scout: {{
              blue: '#005080',
              navy: '#002D5A',
              cyan: '#009BE0',
              sand: '#F4F6F8',
              sandDark: '#E5E9EE'
            }}
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700;800&family=The+Sans:wght@700;800&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Source Sans 3', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'The Sans', 'Source Sans 3', sans-serif; }}

    /* Plynulý přechod při přepnutí motivu */
    html.theme-transition,
    html.theme-transition *,
    html.theme-transition *:before,
    html.theme-transition *:after {{
      transition: background-color 0.25s ease, border-color 0.25s ease, color 0.15s ease !important;
    }}

    /* ========================================================= */
    /* DENNÍ REŽIM - VYSOKÝ KONTRAST A MAXIMÁLNÍ ČITELNOST       */
    /* ========================================================= */
    html:not(.dark) body {{
      background-color: #f8f9fa;
      color: #0f172a;
    }}
    html:not(.dark) .leader-card-b p,
    html:not(.dark) .bg-white p,
    html:not(.dark) .bg-slate-50 p {{
      color: #1e293b;
    }}
    html:not(.dark) .text-scout-navy {{
      color: #002d5a !important;
    }}
    html:not(.dark) .text-slate-900 {{
      color: #071527 !important;
    }}
    html:not(.dark) .text-slate-800 {{
      color: #0f172a !important;
    }}
    html:not(.dark) .text-slate-700 {{
      color: #0f172a !important;
    }}
    html:not(.dark) .text-slate-600 {{
      color: #1e293b !important;
    }}
    html:not(.dark) .text-slate-500 {{
      color: #334155 !important;
    }}
    html:not(.dark) .text-slate-400 {{
      color: #475569 !important;
    }}

    /* Zachování světlého textu v tmavých blocích v denním režimu */
    html:not(.dark) .bg-slate-950,
    html:not(.dark) .bg-slate-900,
    html:not(.dark) footer.bg-slate-950,
    html:not(.dark) .bg-scout-navy {{
      color: #ffffff;
    }}
    html:not(.dark) .bg-scout-navy h1,
    html:not(.dark) .bg-scout-navy strong,
    html:not(.dark) .bg-slate-950 strong,
    html:not(.dark) .bg-slate-900 strong,
    html:not(.dark) footer.bg-slate-950 strong {{
      color: #ffffff !important;
    }}
    html:not(.dark) .bg-slate-950 p,
    html:not(.dark) .bg-slate-900 p,
    html:not(.dark) footer.bg-slate-950 p,
    html:not(.dark) .bg-scout-navy p {{
      color: #e2e8f0 !important;
    }}
    html:not(.dark) .bg-slate-950 span.text-slate-300,
    html:not(.dark) .bg-slate-900 span.text-slate-300,
    html:not(.dark) footer.bg-slate-950 span.text-slate-300,
    html:not(.dark) .bg-scout-navy span.text-slate-300,
    html:not(.dark) .bg-scout-navy .text-slate-300 {{
      color: #cbd5e1 !important;
    }}
    html:not(.dark) .bg-slate-950 span.text-slate-400,
    html:not(.dark) .bg-slate-900 span.text-slate-400,
    html:not(.dark) footer.bg-slate-950 span.text-slate-400,
    html:not(.dark) footer.bg-slate-950 p.text-slate-400,
    html:not(.dark) footer.bg-slate-950 p.text-slate-500,
    html:not(.dark) .bg-scout-navy span.text-slate-400,
    html:not(.dark) .bg-scout-navy .text-slate-400 {{
      color: #94a3b8 !important;
    }}
    html:not(.dark) .bg-slate-950 strong,
    html:not(.dark) .bg-slate-900 strong,
    html:not(.dark) footer.bg-slate-950 strong,
    html:not(.dark) .bg-scout-navy strong {{
      color: #ffffff !important;
    }}

    /* ========================================================= */
    /* TMAVÝ REŽIM PRO VEDENÍ B                                  */
    /* ========================================================= */
    .dark {{
      color-scheme: dark;
    }}
    .dark body {{
      background-color: #070e1d !important;
      color: #f1f5f9 !important;
    }}
    .dark header {{
      background-color: rgba(11, 21, 40, 0.95) !important;
      border-color: rgba(30, 41, 59, 0.8) !important;
    }}
    .dark nav a {{
      color: #cbd5e1 !important;
    }}
    .dark nav a:hover {{
      color: #38bdf8 !important;
    }}
    .dark #mobileMenuB {{
      background-color: #0f1c34 !important;
      border-color: #1e293b !important;
    }}
    .dark #mobileMenuB a {{
      color: #e2e8f0 !important;
    }}
    .dark #mobileMenuB a:hover {{
      background-color: #1e2e4a !important;
    }}
    .dark section.bg-scout-sand {{
      background-color: #0b1528 !important;
      border-color: #1e2e4a !important;
    }}
    .dark .bg-white {{
      background-color: #0f1c34 !important;
      border-color: #1e2e4a !important;
      color: #f1f5f9 !important;
    }}
    .dark .bg-slate-50,
    .dark .bg-slate-100,
    .dark .bg-slate-200,
    .dark .bg-scout-sand,
    .dark .bg-scout-sandDark {{
      background-color: #162544 !important;
      border-color: #243b66 !important;
      color: #e2e8f0 !important;
    }}
    .dark h1, .dark h2, .dark h3, .dark h4, .dark h5, .dark h6, .dark strong {{
      color: #ffffff !important;
    }}
    .dark .text-scout-navy,
    .dark .text-slate-900 {{
      color: #ffffff !important;
    }}
    .dark .text-scout-blue,
    .dark .text-scout-cyan {{
      color: #38bdf8 !important;
    }}
    .dark .text-slate-800 {{
      color: #f1f5f9 !important;
    }}
    .dark .text-slate-700 {{
      color: #e2e8f0 !important;
    }}
    .dark .text-slate-600 {{
      color: #cbd5e1 !important;
    }}
    .dark .text-slate-500,
    .dark .text-slate-400 {{
      color: #94a3b8 !important;
    }}
    .dark .border-slate-100,
    .dark .border-slate-200,
    .dark .border-slate-300 {{
      border-color: #1e2e4a !important;
    }}
    .dark a.bg-slate-50,
    .dark a.bg-slate-100,
    .dark a.bg-white,
    .dark button.bg-slate-100,
    .dark button.bg-white {{
      background-color: #162544 !important;
      border-color: #243b66 !important;
      color: #e2e8f0 !important;
    }}
    .dark a.bg-slate-50:hover,
    .dark a.bg-slate-100:hover,
    .dark a.bg-white:hover,
    .dark button.bg-slate-100:hover,
    .dark button.bg-white:hover {{
      background-color: #1e3560 !important;
      color: #ffffff !important;
    }}
    .dark .filter-btn-b:not(.active) {{
      background-color: #162544 !important;
      border-color: #243b66 !important;
      color: #e2e8f0 !important;
    }}
    .dark .filter-btn-b.active {{
      background-color: #009BE0 !important;
      color: #ffffff !important;
      border-color: #009BE0 !important;
    }}
  </style>
</head>
<body class="bg-[#F8F9FA] text-slate-800 antialiased selection:bg-scout-blue selection:text-white">

  {get_navbar_b(is_subpage=True)}

  <!-- PAGE HEADER -->
  <section class="bg-scout-sand border-b border-slate-200 py-10 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto space-y-3">
      
      <!-- DROBEČKOVÁ NAVIGACE / NÁVRAT -->
      <div class="flex items-center justify-between flex-wrap gap-2 pb-2 border-b border-slate-300/80 text-xs">
        <a href="index.html" class="inline-flex items-center gap-1.5 font-bold text-scout-blue hover:text-scout-navy transition-colors">
          <i class="fa-solid fa-arrow-left text-[11px]"></i>
          <span>Zpět na hlavní stránku oddílu</span>
        </a>
        <span class="text-slate-500">Podstránka webu • Varianta B</span>
      </div>

      <div class="text-center pt-1 space-y-2">
        <span class="text-scout-blue font-bold text-xs uppercase tracking-wider">Tým vedoucích</span>
        <h1 class="text-3xl sm:text-4xl font-extrabold text-scout-navy font-heading">
          Vedení 11. oddílu, garanti schůzek a lodivodi
        </h1>
        <p class="text-slate-600 text-sm max-w-2xl mx-auto">
          Strukturovaný přehled všech 34 dospělých a roverů, kteří se podílejí na přípravě programu pro vlčata a skauty Jedenáctky.
        </p>
      </div>

      <!-- FILTERS -->
      <div class="pt-4 flex flex-wrap justify-center gap-2">
        <button onclick="filterLeadersB('all')" class="filter-btn-b active px-4 py-2 rounded-lg text-xs font-bold bg-scout-navy text-white" data-filter="all">Všichni (34)</button>
        <button onclick="filterLeadersB('vlcata')" class="filter-btn-b px-4 py-2 rounded-lg text-xs font-bold bg-white text-slate-700 border border-slate-300" data-filter="vlcata">Toulavá smečka (vlčata)</button>
        <button onclick="filterLeadersB('skauti')" class="filter-btn-b px-4 py-2 rounded-lg text-xs font-bold bg-white text-slate-700 border border-slate-300" data-filter="skauti">Bárka (skauti)</button>
        <button onclick="filterLeadersB('vedeni')" class="filter-btn-b px-4 py-2 rounded-lg text-xs font-bold bg-white text-slate-700 border border-slate-300" data-filter="vedeni">Vůdcové oddílu</button>
      </div>
    </div>
  </section>

  <!-- LEADERS GRID -->
  <main class="py-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="leadersGridB">
      {"".join(leader_cards)}
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-scout-navy text-slate-300 text-xs py-8 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4">
      <div class="flex items-center gap-2">
        <img src="logo_emblem.png" alt="11. oddíl vodních skautů" class="h-7 w-auto object-contain brightness-110">
        <span class="font-bold text-white">11. oddíl vodních skautů České Budějovice</span>
      </div>
      <div class="text-slate-400 text-center sm:text-right flex flex-col sm:flex-row items-center justify-end gap-1.5 sm:gap-2">
        <span class="text-slate-300">Verze: {get_app_version()} ({get_git_commit()})</span>
        <span class="hidden sm:inline text-slate-600">•</span>
        <span class="text-slate-300">Aktualizováno: {BUILD_TIMESTAMP}</span>
        <span class="hidden sm:inline text-slate-600">•</span>
        <span>Registrováno u Junák – český skaut, 4. středisko VAVÉHA České Budějovice.</span>
      </div>
    </div>
  </footer>

  <script>
    const mobileMenuBtnB = document.getElementById('mobileMenuBtnB');
    const mobileMenuB = document.getElementById('mobileMenuB');
    if (mobileMenuBtnB && mobileMenuB) {{
      mobileMenuBtnB.addEventListener('click', () => {{
        mobileMenuB.classList.toggle('hidden');
      }});
      mobileMenuB.querySelectorAll('a').forEach(link => {{
        link.addEventListener('click', () => {{
          mobileMenuB.classList.add('hidden');
        }});
      }});
    }}

    function filterLeadersB(cat) {{
      const cards = document.querySelectorAll('.leader-card-b');
      const btns = document.querySelectorAll('.filter-btn-b');

      btns.forEach(btn => {{
        if (btn.getAttribute('data-filter') === cat) {{
          btn.className = "filter-btn-b active px-4 py-2 rounded-lg text-xs font-bold bg-scout-navy text-white";
        }} else {{
          btn.className = "filter-btn-b px-4 py-2 rounded-lg text-xs font-bold bg-white text-slate-700 border border-slate-300";
        }}
      }});

      cards.forEach(card => {{
        if (cat === 'all') {{
          card.classList.remove('hidden');
        }} else if (card.classList.contains(cat)) {{
          card.classList.remove('hidden');
        }} else {{
          card.classList.add('hidden');
        }}
      }});
    }}

    // Přepínač tmavého / světlého režimu s localStorage
    function toggleTheme() {{
      document.documentElement.classList.add('theme-transition');
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.theme = isDark ? 'dark' : 'light';
      updateThemeIcons();
      setTimeout(() => {{
        document.documentElement.classList.remove('theme-transition');
      }}, 300);
    }}

    function updateThemeIcons() {{
      const isDark = document.documentElement.classList.contains('dark');
      document.querySelectorAll('.theme-toggle-icon').forEach(icon => {{
        if (isDark) {{
          icon.className = 'fa-solid fa-sun text-yellow-400 theme-toggle-icon';
        }} else {{
          icon.className = 'fa-solid fa-moon text-slate-800 theme-toggle-icon';
        }}
      }});
      document.querySelectorAll('.theme-toggle-text').forEach(t => {{
        t.textContent = isDark ? 'Světlý režim' : 'Tmavý režim';
      }});
    }}
    updateThemeIcons();
  </script>

{get_search_modal_html(prefix="")}
{get_search_script_js(prefix="", is_subpage=True)}
</body>
</html>
"""
    with open('verzeB/vedeni.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully generated verzeB/vedeni.html")

generate_index_b()
generate_vedeni_b()
save_version_json()
update_index_html_version()

