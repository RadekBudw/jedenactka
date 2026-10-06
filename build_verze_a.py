# -*- coding: utf-8 -*-
import json, re, datetime
from build_data import leaders, h, TERMINOVNIK_BARKA, TERMINOVNIK_VLCATA, BLOG_POSTS, FAQ_ITEMS, get_version_meta_html, get_app_version, get_git_commit, save_version_json, update_index_html_version, get_search_modal_html, get_search_script_js

BUILD_TIMESTAMP = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

def get_navbar(is_subpage=False):
    prefix = "index.html" if is_subpage else ""
    return f"""
  <!-- TOP EMERGENCY / STATUS BAR -->
  <div class="bg-slate-950 text-slate-300 text-xs sm:text-sm py-2 px-4 border-b border-yellow-500/20">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
      <div class="flex items-center gap-2 text-center sm:text-left">
        <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-semibold text-xs border border-emerald-500/30">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Běží schůzky 2026/2027
        </span>
        <span class="text-xs sm:text-sm">Schůzky: <strong>Středa &amp; Čtvrtek 16:00 – 18:00</strong> na Valše</span>
      </div>
      <div class="flex items-center gap-3 text-xs">
        <a href="{prefix}#terminovnik" class="hover:text-yellow-400 transition-colors flex items-center gap-1.5">
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

  <!-- NAVIGATION -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- LOGO & BRAND -->
        <a href="{prefix}#" class="flex items-center gap-3.5 group">
          <div class="h-12 w-12 sm:h-14 sm:w-14 rounded-2xl bg-slate-900/5 p-1 flex items-center justify-center group-hover:scale-105 transition-transform duration-200 shrink-0">
            <img src="logo_emblem.png" alt="11. oddíl vodních skautů" class="h-full w-full object-contain filter drop-shadow-xs">
          </div>
          <div>
            <span class="block text-xl font-black tracking-tight text-brand-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-xs font-semibold text-slate-500">České Budějovice • Valcha</span>
          </div>
        </a>

        <!-- DESKTOP NAV -->
        <nav class="hidden lg:flex items-center gap-1">
          <a href="{prefix}#pro-rodice" class="px-3 py-2 rounded-xl text-sm font-bold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all flex items-center gap-1.5">
            <i class="fa-solid fa-heart-pulse text-amber-500 text-xs"></i> Pro rodiče
          </a>
          <a href="{prefix}#oddil" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">O oddílu</a>
          <a href="{prefix}#paluby" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">Naše paluby</a>
          <a href="{prefix}#terminovnik" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">Termínovník</a>
          <a href="{prefix}#aktuality" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">Aktuality</a>
          <a href="{"vedeni.html" if not is_subpage else "#"}" class="px-3 py-2 rounded-xl text-sm font-bold {"text-brand-sky bg-sky-50 shadow-xs" if is_subpage else "text-brand-blue hover:text-brand-sky hover:bg-slate-100"} transition-all flex items-center gap-1.5">
            <i class="fa-solid fa-users text-xs"></i> Vedení oddílu
          </a>
          <a href="{prefix}#klubovna" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">Valcha</a>
          <a href="{prefix}#kontakty" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">Kontakty</a>
        </nav>

        <!-- CTA, THEME TOGGLE & SEARCH -->
        <div class="hidden sm:flex items-center gap-2">
          <button onclick="openSearchModal()" class="p-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 dark:hover:bg-slate-700 transition-all shadow-xs cursor-pointer flex items-center justify-center gap-2 text-xs font-semibold" title="Vyhledávat na webu (Ctrl+K)" aria-label="Hledat na webu">
            <i class="fa-solid fa-magnifying-glass text-sm text-slate-500 dark:text-slate-400"></i>
            <span class="hidden xl:inline text-slate-500">Hledat...</span>
            <kbd class="hidden xl:inline-block px-1.5 py-0.5 text-[10px] bg-slate-100 dark:bg-slate-700 text-slate-400 rounded border border-slate-200 dark:border-slate-600 font-mono">Ctrl+K</kbd>
          </button>
          <button onclick="toggleTheme()" class="p-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-yellow-400 dark:hover:bg-slate-700 transition-all shadow-xs cursor-pointer flex items-center justify-center" title="Přepnout tmavý / světlý režim" aria-label="Přepnout režim">
            <i class="fa-solid fa-moon text-base text-slate-800 theme-toggle-icon"></i>
          </button>
          <a href="{prefix}#nabor" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm bg-gradient-to-r from-brand-gold to-brand-goldHover text-brand-navyDark shadow-md shadow-brand-gold/25 hover:shadow-lg hover:scale-[1.02] active:scale-[0.98] transition-all">
            <i class="fa-solid fa-compass text-base"></i>
            <span>Chci se přidat</span>
          </a>
        </div>

        <!-- MOBILE HAMBURGER, SEARCH & THEME TOGGLE -->
        <div class="flex items-center gap-1.5 lg:hidden">
          <button onclick="openSearchModal()" class="p-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 cursor-pointer" title="Hledat" aria-label="Hledat">
            <i class="fa-solid fa-magnifying-glass text-sm"></i>
          </button>
          <button onclick="toggleTheme()" class="p-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white hover:bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-yellow-400 dark:hover:bg-slate-700 cursor-pointer" title="Přepnout režim" aria-label="Přepnout režim">
            <i class="fa-solid fa-moon text-sm text-slate-800 theme-toggle-icon"></i>
          </button>
          <button id="mobileMenuBtn" type="button" class="p-2.5 rounded-xl text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 focus:outline-none" aria-label="Otevřít menu">
            <i class="fa-solid fa-bars text-2xl" id="menuIcon"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- MOBILE NAVIGATION DRAWER -->
    <div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-4 pt-3 pb-6 shadow-xl transition-all">
      <div class="mb-3">
        <button onclick="openSearchModal(); document.getElementById('mobileMenu').classList.add('hidden');" class="w-full flex items-center gap-3 px-4 py-3 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-sm font-medium border border-slate-200 dark:border-slate-700 text-left cursor-pointer">
          <i class="fa-solid fa-magnifying-glass text-slate-400 text-sm"></i>
          <span>Hledat na webu Jedenáctky...</span>
        </button>
      </div>
      <div class="flex flex-col gap-1 text-base font-semibold">
        <a href="{prefix}#pro-rodice" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-100 flex items-center gap-3 font-bold text-amber-700 dark:text-amber-400 bg-amber-50/50 dark:bg-amber-950/30">
          <i class="fa-solid fa-heart-pulse w-5 text-amber-500"></i> Pro rodiče (Rozpis schůzek & fotky)
        </a>
        <a href="{prefix}#oddil" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-3">
          <i class="fa-solid fa-anchor w-5 text-brand-sky"></i> O 11. oddílu vodních skautů
        </a>
        <a href="{prefix}#paluby" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-3">
          <i class="fa-solid fa-ship w-5 text-brand-sky"></i> Naše 3 paluby (vlčata, skauti, roveři)
        </a>
        <a href="{prefix}#terminovnik" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-3">
          <i class="fa-regular fa-calendar-check w-5 text-brand-sky"></i> Termínovník akcí & výprav
        </a>
        <a href="{prefix}#aktuality" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-3">
          <i class="fa-solid fa-newspaper w-5 text-brand-sky"></i> Aktuality z oddílu
        </a>
        <a href="vedeni.html" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-3 font-bold text-brand-sky">
          <i class="fa-solid fa-users w-5 text-brand-sky"></i> Celé vedení oddílu (34 vedoucích)
        </a>
        <a href="{prefix}#klubovna" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-3">
          <i class="fa-solid fa-house-chimney-water w-5 text-brand-sky"></i> Základna Valcha
        </a>
        <a href="{prefix}#kontakty" class="px-4 py-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-3">
          <i class="fa-solid fa-phone w-5 text-brand-sky"></i> Kontakty na kapitána & velitele
        </a>
        <div class="pt-3 border-t border-slate-100 dark:border-slate-800 mt-2 flex items-center justify-between px-2">
          <span class="text-xs font-bold text-slate-500 dark:text-slate-400">Režim zobrazení:</span>
          <button onclick="toggleTheme()" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-white dark:bg-slate-800 text-slate-800 dark:text-yellow-300 font-bold text-xs border border-slate-200 dark:border-slate-700 cursor-pointer">
            <i class="fa-solid fa-moon text-xs text-slate-800 theme-toggle-icon"></i>
            <span class="theme-toggle-text">Tmavý režim</span>
          </button>
        </div>
        <div class="pt-2">
          <a href="{prefix}#nabor" class="w-full py-3 rounded-xl font-bold text-center bg-brand-gold text-brand-navyDark block shadow-md">
            Chci do oddílu (Nábor chlapců)
          </a>
        </div>
      </div>
    </div>
  </header>
"""

# Build verzeA/index.html
def generate_index_a():
    barka_cards = "".join([f'''
      <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200/80 hover:border-brand-sky hover:shadow-md transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-black bg-sky-100 text-brand-blue">
              <i class="fa-solid {ev["icon"]}"></i> {ev["type"]}
            </span>
            <span class="text-xs font-bold text-slate-400">Bárka</span>
          </div>
          <div class="text-xl font-black font-heading text-brand-navy mt-1">{ev["title"]}</div>
          <div class="text-sm font-black text-brand-sky mt-0.5">{ev["date"]}</div>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">{ev["desc"]}</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-500 font-semibold">
          <span><i class="fa-solid fa-location-dot text-slate-400"></i> Dle propozic v mailu</span>
          <span class="text-brand-blue font-bold">@jedenactka.eu</span>
        </div>
      </div>
    ''' for ev in TERMINOVNIK_BARKA])

    vlcata_cards = "".join([f'''
      <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200/80 hover:border-amber-400 hover:shadow-md transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-black bg-amber-100 text-amber-900">
              <i class="fa-solid {ev["icon"]}"></i> {ev["type"]}
            </span>
            <span class="text-xs font-bold text-slate-400">Toulavá smečka</span>
          </div>
          <div class="text-xl font-black font-heading text-slate-900 mt-1">{ev["title"]}</div>
          <div class="text-sm font-black text-amber-600 mt-0.5">{ev["date"]}</div>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">{ev["desc"]}</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-500 font-semibold">
          <span><i class="fa-solid fa-location-dot text-slate-400"></i> Informace u garantů</span>
          <span class="text-amber-700 font-bold">Vlčata</span>
        </div>
      </div>
    ''' for ev in TERMINOVNIK_VLCATA])

    blog_cards = "".join([f'''
      <article class="bg-white rounded-3xl overflow-hidden shadow-sm border border-slate-200/80 hover:shadow-xl hover:border-brand-sky transition-all flex flex-col justify-between group">
        <div>
          <div class="aspect-[16/10] overflow-hidden bg-slate-100 relative">
            <img src="{post["img"]}" alt="{post["title"]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <span class="absolute top-3 left-3 px-2.5 py-1 rounded-lg text-[10px] font-black uppercase tracking-wider bg-slate-950/80 text-yellow-300 backdrop-blur-xs">
              {post["tag"]}
            </span>
          </div>
          <div class="p-5">
            <div class="text-[11px] font-semibold text-slate-400 mb-1 flex items-center gap-1.5">
              <i class="fa-regular fa-calendar text-brand-sky"></i> {post["date"]}
            </div>
            <h3 class="text-base font-black text-slate-900 font-heading leading-tight group-hover:text-brand-blue transition-colors">
              {post["title"]}
            </h3>
            <p class="text-xs text-slate-600 mt-2 line-clamp-4 leading-relaxed">
              {post["desc"]}
            </p>
          </div>
        </div>
        <div class="px-5 pb-5 pt-0">
          <a href="{post["link"]}" target="_blank" class="inline-flex items-center gap-1.5 text-xs font-bold text-brand-sky hover:text-brand-blue transition-colors">
            <span>Zobrazit fotky z akce</span>
            <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </a>
        </div>
      </article>
    ''' for post in BLOG_POSTS])

    faq_cards = "".join([f'''
      <div class="bg-white rounded-2xl border border-slate-200/90 shadow-sm overflow-hidden transition-all hover:border-brand-sky/60">
        <button onclick="toggleFaq({i})" class="w-full p-4 sm:p-5 text-left flex items-center justify-between gap-4 cursor-pointer select-none group" aria-expanded="false">
          <div class="flex items-center gap-3.5">
            <div class="w-10 h-10 rounded-xl bg-sky-50 text-brand-sky flex items-center justify-center text-base shrink-0 group-hover:scale-110 transition-transform">
              <i class="fa-solid {item["icon"]}"></i>
            </div>
            <span class="font-extrabold text-sm sm:text-base text-slate-900 font-heading group-hover:text-brand-blue transition-colors">
              {item["q"]}
            </span>
          </div>
          <div class="w-8 h-8 rounded-lg bg-slate-100 flex items-center justify-center shrink-0 group-hover:bg-sky-100 transition-colors">
            <i id="faqIcon{i}" class="fa-solid fa-chevron-down text-xs text-slate-500 group-hover:text-brand-sky transition-transform duration-300"></i>
          </div>
        </button>
        <div id="faqAns{i}" class="hidden px-5 pb-5 pt-1 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 bg-slate-50/50">
          <p>{item["a"]}</p>
        </div>
      </div>
    ''' for i, item in enumerate(FAQ_ITEMS)])

    html = f"""<!DOCTYPE html>
<html lang="cs" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>11. oddíl vodních skautů České Budějovice | Moderní flotila</title>
  <meta name="description" content="Oficiální moderní prezentace 11. chlapeckého oddílu vodních skautů v Českých Budějovicích. Skauting, pramice, kanoe, dobrodružství pro kluky od 6 let.">
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
            brand: {{
              navyDark: '#071527',
              navy: '#0C2340',
              blue: '#134074',
              sky: '#00A8E8',
              skyLight: '#E8F6FD',
              gold: '#FACC15',
              goldHover: '#EAB308',
              amberBadge: '#F59E0B'
            }}
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    .wave-bg {{
      background-image: radial-gradient(rgba(0, 168, 232, 0.15) 1px, transparent 0);
      background-size: 24px 24px;
    }}

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
      background-color: #f8fafc;
      color: #0f172a;
    }}

    /* Světlé sekce a karty - syté, perfektně čitelné texty */
    html:not(.dark) .bg-white p,
    html:not(.dark) .bg-slate-50 p,
    html:not(.dark) .bg-slate-100 p,
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

    html:not(.dark) .text-slate-900 {{
      color: #071527 !important;
    }}
    html:not(.dark) .text-brand-navy {{
      color: #0c2340 !important;
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
    /* TMMAVÉ BLOKY V DENNÍM REŽIMU (Hero, Gmail, Valcha, Nábor)  */
    /* V těchto sekcích MUSÍ text zůstat zářivě bílý / světlý!    */
    /* ========================================================= */
    html:not(.dark) section.bg-gradient-to-br,
    html:not(.dark) div.bg-gradient-to-br,
    html:not(.dark) div.bg-gradient-to-r,
    html:not(.dark) section.bg-slate-900,
    html:not(.dark) div.bg-slate-900,
    html:not(.dark) .bg-slate-950,
    html:not(.dark) footer.bg-slate-950 {{
      color: #ffffff;
    }}

    html:not(.dark) section.bg-gradient-to-br h1,
    html:not(.dark) section.bg-gradient-to-br h2,
    html:not(.dark) section.bg-gradient-to-br h3,
    html:not(.dark) div.bg-gradient-to-br h2,
    html:not(.dark) div.bg-gradient-to-br h3,
    html:not(.dark) div.bg-gradient-to-r h2,
    html:not(.dark) div.bg-gradient-to-r h3,
    html:not(.dark) section.bg-slate-900 h2,
    html:not(.dark) section.bg-slate-900 h3,
    html:not(.dark) div.bg-slate-900 h2,
    html:not(.dark) div.bg-slate-900 h3,
    html:not(.dark) section.bg-gradient-to-br strong,
    html:not(.dark) div.bg-gradient-to-br strong,
    html:not(.dark) div.bg-gradient-to-r strong,
    html:not(.dark) section.bg-slate-900 strong,
    html:not(.dark) div.bg-slate-900 strong {{
      color: #ffffff !important;
    }}

    html:not(.dark) section.bg-gradient-to-br p,
    html:not(.dark) div.bg-gradient-to-br p,
    html:not(.dark) div.bg-gradient-to-r p,
    html:not(.dark) section.bg-slate-900 p,
    html:not(.dark) div.bg-slate-900 p,
    html:not(.dark) footer.bg-slate-950 p {{
      color: #e2e8f0 !important;
    }}

    html:not(.dark) section.bg-gradient-to-br .text-slate-300,
    html:not(.dark) div.bg-gradient-to-br .text-slate-300,
    html:not(.dark) div.bg-gradient-to-r .text-slate-300,
    html:not(.dark) section.bg-slate-900 .text-slate-300,
    html:not(.dark) div.bg-slate-900 .text-slate-300,
    html:not(.dark) .bg-slate-950 .text-slate-300,
    html:not(.dark) footer.bg-slate-950 .text-slate-300 {{
      color: #cbd5e1 !important;
    }}

    html:not(.dark) section.bg-gradient-to-br .text-slate-200,
    html:not(.dark) div.bg-gradient-to-br .text-slate-200,
    html:not(.dark) div.bg-gradient-to-r .text-slate-200,
    html:not(.dark) section.bg-slate-900 .text-slate-200,
    html:not(.dark) div.bg-slate-900 .text-slate-200 {{
      color: #e2e8f0 !important;
    }}

    html:not(.dark) section.bg-gradient-to-br .text-slate-400,
    html:not(.dark) div.bg-gradient-to-br .text-slate-400,
    html:not(.dark) div.bg-gradient-to-r .text-slate-400,
    html:not(.dark) section.bg-slate-900 .text-slate-400,
    html:not(.dark) div.bg-slate-900 .text-slate-400,
    html:not(.dark) .bg-slate-950 .text-slate-400,
    html:not(.dark) footer.bg-slate-950 .text-slate-400 {{
      color: #94a3b8 !important;
    }}

    /* Tlačítka v Hero sekci v denním režimu */
    html:not(.dark) section.bg-gradient-to-br a.text-white {{
      color: #ffffff !important;
    }}

    /* ========================================================= */
    /* TMAVÝ REŽIM (NOČNÍ MOTIV)                                 */
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
    .dark #mobileMenu {{
      background-color: #0b1329 !important;
      border-color: #1e293b !important;
    }}
    .dark #mobileMenu a {{
      color: #e2e8f0 !important;
    }}
    .dark #mobileMenu a:hover {{
      background-color: #1e293b !important;
    }}
    
    /* Všechna světlá pozadí sekcí a bloků se v nočním režimu ztmaví */
    .dark section.bg-slate-100,
    .dark section.bg-slate-50,
    .dark section.bg-white,
    .dark #oddil,
    .dark #aktuality,
    .dark .bg-slate-100,
    .dark .bg-slate-100\\/80,
    .dark .bg-slate-50,
    .dark .bg-slate-50\\/50,
    .dark .bg-slate-50\\/60,
    .dark .bg-slate-200 {{
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
    .dark .text-slate-900 {{
      color: #ffffff !important;
    }}
    .dark .text-brand-blue {{
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
<body class="bg-[#F8FAFC] text-slate-800 antialiased selection:bg-brand-sky selection:text-white">

  {get_navbar(is_subpage=False)}

  <!-- HERO SECTION -->
  <section class="relative bg-gradient-to-br from-brand-navyDark via-brand-navy to-brand-blue text-white overflow-hidden py-16 sm:py-24 lg:py-28">
    <div class="absolute inset-0 wave-bg opacity-30"></div>
    <div class="absolute -right-20 -bottom-20 w-96 h-96 bg-brand-sky/20 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -left-20 top-0 w-80 h-80 bg-brand-gold/15 rounded-full blur-3xl pointer-events-none"></div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left Content -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          
          <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full bg-slate-950/90 border border-yellow-400/40 text-xs sm:text-sm font-semibold shadow-lg">
            <span class="w-5 h-3.5 inline-block rounded-xs border border-white/40 shadow-sm shrink-0" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);" title="Černo-žlutá oddílová vlajka"></span>
            <span class="text-white font-bold">11. oddíl vodních skautů</span>
            <span class="text-yellow-400 font-extrabold">• České Budějovice</span>
          </div>

          <h1 class="text-4xl sm:text-6xl lg:text-6xl font-black font-heading tracking-tight leading-[1.08]">
            Kde kluci objevují <br class="hidden sm:inline">
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-amber-300 to-yellow-400">vodu, odvahu</span> a celoživotní partu.
          </h1>

          <p class="text-base sm:text-lg text-slate-300 max-w-2xl mx-auto lg:mx-0 font-normal leading-relaxed">
            Chlapecký vodní skautský oddíl s tradicí v Českých Budějovicích. Učíme kluky samostatnosti, férovosti, jízdě na pramicích i plachetnicích a životu v přírodě pod černo-žlutou vlajkou.
          </p>

          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-2">
            <a href="#pro-rodice" class="w-full sm:w-auto px-7 py-4 rounded-2xl font-black text-base bg-gradient-to-r from-brand-gold to-brand-goldHover text-brand-navyDark shadow-xl shadow-brand-gold/25 hover:shadow-2xl hover:scale-105 active:scale-95 transition-all flex items-center justify-center gap-3">
              <i class="fa-solid fa-heart-pulse text-lg"></i>
              <span>Pro rodiče (Rozpis & fotky)</span>
            </a>
            <a href="#oddil" class="w-full sm:w-auto px-7 py-4 rounded-2xl font-bold text-base bg-white/10 hover:bg-white/15 text-white border border-white/20 hover:border-white/30 backdrop-blur-sm transition-all flex items-center justify-center gap-3">
              <i class="fa-solid fa-compass text-brand-sky"></i>
              <span>O našem oddílu</span>
            </a>
          </div>

          <div class="pt-6 border-t border-white/10 grid grid-cols-3 gap-3 text-left">
            <div>
              <span class="block text-2xl font-black font-heading text-yellow-300">4</span>
              <span class="text-xs text-slate-300 font-medium">Paluby od vlčat po rovery</span>
            </div>
            <div>
              <span class="block text-2xl font-black font-heading text-brand-sky">34</span>
              <span class="text-xs text-slate-300 font-medium">Zkušených vedoucích</span>
            </div>
            <div>
              <span class="block text-2xl font-black font-heading text-emerald-400">100%</span>
              <span class="text-xs text-slate-300 font-medium">Zážitky, voda & kamarádi</span>
            </div>
          </div>
        </div>

        <!-- Right Hero Visual with Rotating/Random Photos -->
        <div class="lg:col-span-5 relative">
          <div onclick="handleHeroClick()" class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white/20 hover:border-yellow-400/60 aspect-[4/3] sm:aspect-[5/4] group bg-slate-950 cursor-pointer select-none transition-all duration-300" title="Klikněte do fotky pro další snímek (nebo nechte běžet automatické střídání)">
            <img id="heroImg" src="zonerama_2.jpg" alt="11. oddíl vodních skautů" class="w-full h-full object-cover transition-opacity duration-500 group-hover:scale-105 transition-transform">
            <div class="absolute inset-0 bg-gradient-to-t from-brand-navyDark/95 via-brand-navyDark/30 to-transparent pointer-events-none"></div>

            <!-- Top live badge & shuffle button -->
            <div class="absolute top-4 left-4 right-4 flex items-center justify-between z-10">
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-yellow-400/30 text-[11px] font-bold text-yellow-300 shadow-md">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>Momentky z oddílu</span>
              </span>
              <button onclick="event.stopPropagation(); handleHeroClick()" type="button" class="px-3 py-1.5 rounded-xl bg-slate-950/85 hover:bg-slate-900 text-yellow-400 border border-yellow-400/50 hover:border-yellow-400 text-xs font-bold transition-all shadow-md cursor-pointer flex items-center gap-1.5 active:scale-95" title="Náhodně změnit fotografii v záhlaví">
                <i class="fa-solid fa-shuffle"></i>
                <span>Změnit fotku 🎲</span>
              </button>
            </div>
            
            <!-- Bottom caption card -->
            <div class="absolute bottom-3 left-3 right-3 sm:bottom-4 sm:left-4 sm:right-4 px-3.5 py-2 sm:px-4 sm:py-2.5 rounded-xl sm:rounded-2xl bg-slate-950/80 backdrop-blur-md border border-yellow-400/35 text-white shadow-lg z-10 transition-all group-hover:border-yellow-400/70">
              <div class="flex items-center justify-between gap-2">
                <span id="heroTag" class="text-[11px] sm:text-xs font-bold text-yellow-300 uppercase tracking-wider truncate">Společná voda 2026</span>
                <span id="heroSub" class="text-[10px] sm:text-[11px] text-slate-400 font-medium shrink-0">Sjíždění šlajsny na kánoi</span>
              </div>
              <p id="heroTitle" class="text-xs font-semibold text-slate-200 mt-0.5 leading-tight truncate sm:whitespace-normal">Vodácká dobrodružství & peřeje na řece</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- QUICK ANCHORS ROW -->
  <section class="relative -mt-7 z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <a href="#pro-rodice" class="bg-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-200/80 hover:border-amber-400 hover:-translate-y-1 transition-all group">
        <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-lg mb-2 group-hover:scale-110 transition-transform">
          <i class="fa-solid fa-heart-pulse"></i>
        </div>
        <h4 class="font-bold text-slate-900 text-sm font-heading group-hover:text-amber-600">Rozpis schůzek</h4>
        <p class="text-[11px] text-slate-500 mt-0.5">Garanti, kontakty a maily</p>
      </a>

      <a href="#terminovnik" class="bg-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-200/80 hover:border-brand-sky hover:-translate-y-1 transition-all group">
        <div class="w-10 h-10 rounded-xl bg-sky-50 text-brand-sky flex items-center justify-center text-lg mb-2 group-hover:scale-110 transition-transform">
          <i class="fa-regular fa-calendar-days"></i>
        </div>
        <h4 class="font-bold text-slate-900 text-sm font-heading group-hover:text-brand-blue">Kalendář akcí</h4>
        <p class="text-[11px] text-slate-500 mt-0.5">Výpravy, tábory & závody</p>
      </a>

      <a href="https://eu.zonerama.com/11skautskyoddil/" target="_blank" class="bg-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-200/80 hover:border-emerald-500 hover:-translate-y-1 transition-all group">
        <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-lg mb-2 group-hover:scale-110 transition-transform">
          <i class="fa-solid fa-camera"></i>
        </div>
        <h4 class="font-bold text-slate-900 text-sm font-heading group-hover:text-emerald-600">Fotogalerie oddílu</h4>
        <p class="text-[11px] text-slate-500 mt-0.5">Zonerama alba z akcí</p>
      </a>

      <a href="vedeni.html" class="bg-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-200/80 hover:border-brand-navy hover:-translate-y-1 transition-all group">
        <div class="w-10 h-10 rounded-xl bg-slate-100 text-brand-navy flex items-center justify-center text-lg mb-2 group-hover:scale-110 transition-transform">
          <i class="fa-solid fa-users"></i>
        </div>
        <h4 class="font-bold text-slate-900 text-sm font-heading group-hover:text-brand-navy">Vedení oddílu</h4>
        <p class="text-[11px] text-slate-500 mt-0.5">34 vedoucích a lodivodů</p>
      </a>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: PRO RODIČE -->
  <!-- ======================================================================== -->
  <section id="pro-rodice" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-900 uppercase tracking-wider mb-2">
        <i class="fa-solid fa-heart-pulse text-amber-600"></i> Informační servis pro rodiče
      </span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy font-heading">
        Vše důležité pro rodiče na jednom místě
      </h2>
      <p class="text-slate-600 mt-3 text-sm sm:text-base">
        Kdy a kde probíhají schůzky, na koho se obrátit s omluvou, jak fungují skautské maily i kde najdete heslované fotky kluků.
      </p>
    </div>

    <!-- 1. ROZPIS SCHŮZEK & GARANTI NA ROK 2026/2027 -->
    <div class="mb-14">
      <div class="flex items-center justify-between mb-6 flex-wrap gap-2">
        <div>
          <h3 class="text-xl sm:text-2xl font-black text-slate-900 font-heading flex items-center gap-2">
            <i class="fa-regular fa-clock text-brand-sky"></i>
            Rozpis schůzek & Garanti 2026/2027
          </h3>
          <p class="text-xs sm:text-sm text-slate-500">Základna Valcha České Budějovice • V případě neúčasti kontaktujte garanta daného dne.</p>
        </div>
        <span class="text-xs font-semibold px-3 py-1 rounded-lg bg-slate-100 text-slate-700 border border-slate-200">
          Čas: 16:00 – 18:00
        </span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Garant 1: Vlčata Středa -->
        <div class="bg-white rounded-3xl p-6 shadow-md border-2 border-amber-300 hover:shadow-xl transition-all flex flex-col justify-between relative overflow-hidden group">
          <div class="absolute top-0 right-0 w-20 h-20 bg-amber-100 rounded-bl-full pointer-events-none -mr-4 -mt-4"></div>
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-2.5 py-1 rounded-lg text-xs font-black bg-amber-500 text-slate-950 uppercase tracking-wider">
                Vlčata • Středa
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3.5 mb-4">
              <img src="avatars/avatar_4.jpg" alt="Matěj Bajgar – Myšák" class="w-16 h-16 rounded-2xl object-cover shadow-sm border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-lg font-heading">Myšák</h4>
                <p class="text-xs font-bold text-slate-600">Matěj Bajgar</p>
                <p class="text-[11px] text-amber-600 font-semibold mt-0.5">Garant středeční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Toulavá smečka (6–10 let)</div>
              <p class="text-slate-500 text-[11px]">Příprava her, programu na vodě i v klubovně pro mladší kluky.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:+420778019042" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 font-bold text-xs transition-colors">
              <i class="fa-solid fa-phone text-amber-600"></i> 778 019 042
            </a>
            <a href="mailto:matejb@jedenactka.eu" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-slate-50 hover:bg-slate-100 text-slate-700 font-semibold text-xs transition-colors">
              <i class="fa-solid fa-envelope text-slate-400"></i> matejb@jedenactka.eu
            </a>
          </div>
        </div>

        <!-- Garant 2: Vlčata Čtvrtek -->
        <div class="bg-white rounded-3xl p-6 shadow-md border-2 border-amber-300 hover:shadow-xl transition-all flex flex-col justify-between relative overflow-hidden group">
          <div class="absolute top-0 right-0 w-20 h-20 bg-amber-100 rounded-bl-full pointer-events-none -mr-4 -mt-4"></div>
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-2.5 py-1 rounded-lg text-xs font-black bg-amber-500 text-slate-950 uppercase tracking-wider">
                Vlčata • Čtvrtek
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3.5 mb-4">
              <img src="avatars/avatar_3.jpg" alt="Jáchym Řehounek – Čáp" class="w-16 h-16 rounded-2xl object-cover shadow-sm border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-lg font-heading">Čáp</h4>
                <p class="text-xs font-bold text-slate-600">Jáchym Řehounek</p>
                <p class="text-[11px] text-amber-600 font-semibold mt-0.5">Garant čtvrteční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Toulavá smečka (6–10 let)</div>
              <p class="text-slate-500 text-[11px]">Omluvenky ze čtvrtečních schůzek a dotazy k programu vlčat.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:+420732405827" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 font-bold text-xs transition-colors">
              <i class="fa-solid fa-phone text-amber-600"></i> 732 405 827
            </a>
            <a href="mailto:cap@jedenactka.eu" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-slate-50 hover:bg-slate-100 text-slate-700 font-semibold text-xs transition-colors">
              <i class="fa-solid fa-envelope text-slate-400"></i> cap@jedenactka.eu
            </a>
          </div>
        </div>

        <!-- Garant 3: Skauti Středa -->
        <div class="bg-white rounded-3xl p-6 shadow-md border-2 border-sky-300 hover:shadow-xl transition-all flex flex-col justify-between relative overflow-hidden group">
          <div class="absolute top-0 right-0 w-20 h-20 bg-sky-100 rounded-bl-full pointer-events-none -mr-4 -mt-4"></div>
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-2.5 py-1 rounded-lg text-xs font-black bg-brand-blue text-white uppercase tracking-wider">
                Skauti • Středa
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3.5 mb-4">
              <img src="avatars/avatar_19.jpg" alt="Max Rosenthaler – Werran" class="w-16 h-16 rounded-2xl object-cover shadow-sm border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-lg font-heading">Werran</h4>
                <p class="text-xs font-bold text-slate-600">Max Rosenthaler</p>
                <p class="text-[11px] text-brand-sky font-semibold mt-0.5">Garant středeční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Bárka (11–15 let)</div>
              <p class="text-slate-500 text-[11px]">Vodácký trénink, posádky skautů na řece Malši a Vltavě.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:+420728729518" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-sky-50 hover:bg-sky-100 text-brand-navy font-bold text-xs transition-colors">
              <i class="fa-solid fa-phone text-brand-sky"></i> 728 729 518
            </a>
            <a href="mailto:werran@jedenactka.eu" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-slate-50 hover:bg-slate-100 text-slate-700 font-semibold text-xs transition-colors">
              <i class="fa-solid fa-envelope text-slate-400"></i> werran@jedenactka.eu
            </a>
          </div>
        </div>

        <!-- Garant 4: Skauti Čtvrtek -->
        <div class="bg-white rounded-3xl p-6 shadow-md border-2 border-sky-300 hover:shadow-xl transition-all flex flex-col justify-between relative overflow-hidden group">
          <div class="absolute top-0 right-0 w-20 h-20 bg-sky-100 rounded-bl-full pointer-events-none -mr-4 -mt-4"></div>
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-2.5 py-1 rounded-lg text-xs font-black bg-brand-blue text-white uppercase tracking-wider">
                Skauti • Čtvrtek
              </span>
              <span class="text-xs font-bold text-slate-400">16:00 – 18:00</span>
            </div>
            
            <div class="flex items-center gap-3.5 mb-4">
              <img src="avatars/avatar_20.jpg" alt="František Kratochvíl – Fanda krátký" class="w-16 h-16 rounded-2xl object-cover shadow-sm border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-lg font-heading">Fanda krátký</h4>
                <p class="text-xs font-bold text-slate-600">František Kratochvíl</p>
                <p class="text-[11px] text-brand-sky font-semibold mt-0.5">Garant čtvrteční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Bárka (11–15 let)</div>
              <p class="text-slate-500 text-[11px]">Příprava čtvrtečního programu skautů a koordinace posádek.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:+420722320570" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-sky-50 hover:bg-sky-100 text-brand-navy font-bold text-xs transition-colors">
              <i class="fa-solid fa-phone text-brand-sky"></i> 722 320 570
            </a>
            <a href="mailto:franta@jedenactka.eu" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-slate-50 hover:bg-slate-100 text-slate-700 font-semibold text-xs transition-colors">
              <i class="fa-solid fa-envelope text-slate-400"></i> franta@jedenactka.eu
            </a>
          </div>
        </div>

      </div>
    </div>

    <!-- 2. SKAUTSKÉ MAILY (@jedenactka.eu) CALLOUT -->
    <div class="mb-14 rounded-3xl bg-gradient-to-r from-slate-900 via-brand-navyDark to-slate-900 text-white p-6 sm:p-8 border-2 border-yellow-400/50 shadow-xl relative overflow-hidden">
      <div class="absolute -right-10 -bottom-10 w-60 h-60 bg-yellow-400/10 rounded-full blur-2xl pointer-events-none"></div>
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        <div class="lg:col-span-8 space-y-3">
          <div class="flex items-center gap-2 text-yellow-400 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-envelope-circle-check text-base"></i>
            <span>Oddílová komunikace • Samostatnost pro skauty</span>
          </div>
          <h3 class="text-2xl sm:text-3xl font-black font-heading tracking-tight">
            Skautské maily na doméně <span class="text-yellow-300">@jedenactka.eu</span>
          </h3>
          <p class="text-slate-300 text-sm leading-relaxed">
            Protože věříme, že nedílnou součástí skautské výchovy je i <strong>výchova k zodpovědnosti a samostatnosti</strong>, využíváme ke komunikaci se skauty Gmail pod naší vlastní doménou <code class="px-2 py-0.5 rounded bg-white/10 text-yellow-300 font-mono text-xs">@jedenactka.eu</code>. 
            Adresy jsou skautům přiděleny při příchodu do Bárky a dostávají na ně veškeré informace o nadcházejících akcích, výpravách a aktualitách.
          </p>
          <div class="inline-flex items-center gap-3 p-3 rounded-xl bg-yellow-400/15 border border-yellow-400/30 text-yellow-200 text-xs font-semibold">
            <i class="fa-solid fa-triangle-exclamation text-yellow-400 text-base shrink-0"></i>
            <span><strong>Důležité pravidlo:</strong> „Jestli nechceš rozzlobit Trolla, kontroluj si mail alespoň jednou týdně!“</span>
          </div>
        </div>
        <div class="lg:col-span-4 flex flex-col items-center justify-center text-center p-4 rounded-2xl bg-white/5 border border-white/10">
          <div class="w-16 h-16 rounded-2xl bg-yellow-400 flex items-center justify-center text-slate-950 text-2xl font-black mb-3 shadow-lg">
            <i class="fa-brands fa-google"></i>
          </div>
          <span class="text-xs text-slate-300 font-medium">Přihlášení ke skautské schránce:</span>
          <a href="https://mail.google.com" target="_blank" class="mt-2 inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-xs bg-white text-slate-900 hover:bg-yellow-400 hover:text-slate-950 transition-all shadow-md">
            <span>Přejít na Gmail (@jedenactka.eu)</span>
            <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
          </a>
        </div>
      </div>
    </div>

    <!-- 3. RYCHLÉ ODKAZY PRO RODIČE: FOTKY, ZONERAMA, ARCHIV AKCÍ -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- Karta 1: Vlčácké fotky (heslované) -->
      <div class="bg-white rounded-3xl p-6 shadow-md border border-slate-200/80 hover:border-amber-400 hover:shadow-lg transition-all flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center text-xl mb-4">
            <i class="fa-solid fa-lock"></i>
          </div>
          <span class="text-[11px] font-bold uppercase tracking-wider text-amber-700 bg-amber-100/70 px-2 py-0.5 rounded">Chráněno heslem</span>
          <h4 class="text-lg font-black text-slate-900 font-heading mt-2">Vlčácké fotky</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Fotogalerie ze schůzek a výprav Toulavé smečky pro rodiče. Přístup je z důvodu ochrany soukromí chlapců zabezpečen heslem, které rodičům předávají garanti.
          </p>
        </div>
        <div class="mt-6 pt-4 border-t border-slate-100">
          <a href="https://jedenactka.skauting.cz/index.php/vlcacke-fotky/" target="_blank" class="w-full py-2.5 px-4 rounded-xl bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs flex items-center justify-center gap-2 transition-all shadow-sm">
            <i class="fa-solid fa-key text-xs"></i>
            <span>Vstoupit do Vlčáckých fotek</span>
          </a>
        </div>
      </div>

      <!-- Karta 2: Oddílová Zonerama -->
      <div class="bg-white rounded-3xl p-6 shadow-md border border-slate-200/80 hover:border-brand-sky hover:shadow-lg transition-all flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-sky-50 text-brand-sky flex items-center justify-center text-xl mb-4">
            <i class="fa-solid fa-images"></i>
          </div>
          <span class="text-[11px] font-bold uppercase tracking-wider text-brand-blue bg-sky-100/70 px-2 py-0.5 rounded">Veřejná fotobanka</span>
          <h4 class="text-lg font-black text-slate-900 font-heading mt-2">Zonerama fotogalerie</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Oficiální veřejná fotoalba z velkých akcí Jedenáctky – Závod 3 Jezy, letní tábory na řece, VVLnZ, brigády na Švýcaráku a krajské srazy vodních skautů.
          </p>
        </div>
        <div class="mt-6 pt-4 border-t border-slate-100">
          <a href="https://eu.zonerama.com/11skautskyoddil/" target="_blank" class="w-full py-2.5 px-4 rounded-xl bg-brand-blue hover:bg-brand-navy text-white font-bold text-xs flex items-center justify-center gap-2 transition-all shadow-sm">
            <i class="fa-solid fa-arrow-up-right-from-square text-xs"></i>
            <span>Otevřít Zonerama oddílu</span>
          </a>
        </div>
      </div>

      <!-- Karta 3: Archiv akcí & plakátky -->
      <div class="bg-white rounded-3xl p-6 shadow-md border border-slate-200/80 hover:border-emerald-500 hover:shadow-lg transition-all flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl mb-4">
            <i class="fa-solid fa-box-archive"></i>
          </div>
          <span class="text-[11px] font-bold uppercase tracking-wider text-emerald-700 bg-emerald-100/70 px-2 py-0.5 rounded">Historie & Kronika</span>
          <h4 class="text-lg font-black text-slate-900 font-heading mt-2">Archiv akcí & plakátků</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Kronika a originální výtvarné plakátky ke stažení z oddílových výprav, táborů a závodů od roku 2009. Prohlédněte si, čím vším oddíl žil.
          </p>
        </div>
        <div class="mt-6 pt-4 border-t border-slate-100">
          <a href="https://jedenactka.skauting.cz/index.php/oddil/archiv-akci/" target="_blank" class="w-full py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs flex items-center justify-center gap-2 transition-all shadow-sm">
            <i class="fa-solid fa-file-pdf text-xs"></i>
            <span>Zobrazit Archiv akcí</span>
          </a>
        </div>
      </div>

    </div>

    <!-- 4. ČASTO KLADENÉ OTÁZKY PRO RODIČE (FAQ) -->
    <div id="faq" class="mt-16 pt-12 border-t border-slate-200/80">
      <div class="text-center max-w-3xl mx-auto mb-10">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-sky-100 text-brand-blue uppercase tracking-wider mb-2">
          <i class="fa-solid fa-circle-question text-brand-sky"></i> Odpovědi na nejčastější dotazy
        </span>
        <h3 class="text-2xl sm:text-3xl font-black text-brand-navy font-heading">
          Často kladené otázky rodičů
        </h3>
        <p class="text-slate-600 mt-2 text-xs sm:text-sm">
          Zvažujete zápis syna k vodním skautům nebo už k nám chodí? Zde najdete odpovědi na otázky ohledně plavání, vybavení, financí i bezpečnosti.
        </p>
      </div>

      <div class="max-w-4xl mx-auto space-y-3">
        {faq_cards}
      </div>
    </div>

  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: O 11. ODDÍLU -->
  <!-- ======================================================================== -->
  <section id="oddil" class="py-20 bg-slate-100 dark:bg-slate-900 border-y border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        
        <div class="lg:col-span-7 space-y-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-yellow-400 text-slate-950 uppercase tracking-wider">
            <span class="w-2.5 h-2.5 rounded-full bg-slate-950"></span>
            Tradice od roku 1990 • 4. středisko VAVÉHA ČB
          </div>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-brand-navy dark:text-white font-heading tracking-tight leading-tight">
            Kdo jsme? <br>
            <span class="text-brand-blue dark:text-brand-sky">11. oddíl vodních skautů</span>
          </h2>
          <p class="text-slate-700 dark:text-slate-200 text-base leading-relaxed">
            Náš oddíl patří k tzv. <strong>vodním skautům</strong>. Jsme skauti, kteří do svého programu zahrnují také vodácké prvky – jízdu na pramicích P550, kanoích i plachetnicích. Sídlíme na vlastní loděnici Valcha na břehu Malše v Českých Budějovicích.
          </p>
          <p class="text-slate-600 dark:text-slate-300 text-sm leading-relaxed">
            Oddíl je podle věku chlapců rozdělen do čtyř částí (kterým u vodních skautů tradičně neříkáme oddíly, ale <strong>paluby</strong>): 
            První paluba pro nejmladší kluky se jmenuje <strong>Toulavá smečka</strong>, pro starší kluky <strong>Bárka</strong> a pro kluky od 16 let výše <strong>roverská VěTeV</strong>. Poslední „neoficiální“ palubou je <strong>Klub 11. oddílu</strong>, který sdružuje ke společným výletům z reality již bývalé vedoucí oddílu.
          </p>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm flex items-start gap-3">
              <div class="w-10 h-10 rounded-xl bg-yellow-400/20 text-yellow-700 dark:text-yellow-400 flex items-center justify-center shrink-0 text-lg">
                <i class="fa-solid fa-flag"></i>
              </div>
              <div>
                <h4 class="font-bold text-slate-900 dark:text-white text-sm font-heading">Černo-žlutá vlajka</h4>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Naše oddílové barvy a žluté šátky symbolizují bratrství a soudržnost.</p>
              </div>
            </div>

            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm flex items-start gap-3">
              <div class="w-10 h-10 rounded-xl bg-sky-100 dark:bg-sky-950/60 text-brand-sky flex items-center justify-center shrink-0 text-lg">
                <i class="fa-solid fa-users-viewfinder"></i>
              </div>
              <div>
                <h4 class="font-bold text-slate-900 dark:text-white text-sm font-heading">Posádkový systém</h4>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Posádky 6–8 chlapců, kde se mladší učí od starších samostatnosti a fair-play.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5 relative">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white dark:border-slate-800 aspect-[4/3] group">
            <img src="zonerama_valcha.jpg" alt="Skauti na základně Valcha" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex items-end p-6">
              <div class="text-white">
                <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider">Základna Valcha</span>
                <p class="text-sm font-semibold text-slate-100">Pravidelné schůzky každou středu a čtvrtek</p>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- 4 paluby -->
      <div id="paluby" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-4">
        
        <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200 hover:border-amber-400 transition-all flex flex-col justify-between">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-amber-50 p-2 mb-4 border border-amber-200 flex items-center justify-center">
              <img src="logo_vlcata.png" alt="Toulavá smečka" class="max-h-full object-contain">
            </div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-amber-700 bg-amber-100 px-2 py-0.5 rounded">1. Paluba • 6–10 let</span>
            <h3 class="text-xl font-black text-slate-900 font-heading mt-2">Toulavá smečka</h3>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Vlčata začínají veselou hrou. Učí se základy skautingu, pobytu v přírodě a první krůčky na vodě v bezpečí posádky.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-500 font-semibold flex items-center justify-between">
            <span>Schůzky: Středa / Čtvrtek</span>
            <span class="text-amber-600 font-bold">16:00 – 18:00</span>
          </div>
        </div>

        <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200 hover:border-brand-sky transition-all flex flex-col justify-between">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-sky-50 p-2 mb-4 border border-sky-200 flex items-center justify-center text-brand-sky text-2xl">
              <i class="fa-solid fa-anchor"></i>
            </div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-brand-blue bg-sky-100 px-2 py-0.5 rounded">2. Paluba • 11–15 let</span>
            <h3 class="text-xl font-black text-slate-900 font-heading mt-2">Bárka</h3>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Skauti se učí kormidlovat pramice, stavět tábor, přežít v přírodě, organizovat víkendové výpravy a získávají skautská jména.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-500 font-semibold flex items-center justify-between">
            <span>Schůzky: Středa / Čtvrtek</span>
            <span class="text-brand-sky font-bold">16:00 – 18:00</span>
          </div>
        </div>

        <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200 hover:border-emerald-500 transition-all flex flex-col justify-between">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-emerald-50 p-2 mb-4 border border-emerald-200 flex items-center justify-center">
              <img src="logo_vetev.png" alt="Roverská VěTeV" class="max-h-full object-contain">
            </div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">3. Paluba • 16+ let</span>
            <h3 class="text-xl font-black text-slate-900 font-heading mt-2">Roverská VěTeV</h3>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Roveři a rangers. Samostatné zahraniční expedice, náročné projekty, vodácké sjezdy divokých řek a pomoc s vedením oddílu.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-500 font-semibold flex items-center justify-between">
            <span>Akce & Expedice</span>
            <span class="text-emerald-600 font-bold">Víkendy</span>
          </div>
        </div>

        <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200 hover:border-purple-400 transition-all flex flex-col justify-between">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-purple-50 p-2 mb-4 border border-purple-200 flex items-center justify-center text-purple-600 text-2xl">
              <i class="fa-solid fa-mug-hot"></i>
            </div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-purple-700 bg-purple-100 px-2 py-0.5 rounded">4. Paluba • Bývalí vedoucí</span>
            <h3 class="text-xl font-black text-slate-900 font-heading mt-2">Klub 11. oddílu</h3>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Neoficiální paluba sdružující ke společným výletům z reality bývalé vedoucí a přátele Jedenáctky, kteří oddíl podporují.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-500 font-semibold flex items-center justify-between">
            <span>Srazy & Podpora</span>
            <span class="text-purple-600 font-bold">Trvale</span>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: TERMÍNOVNÍK -->
  <!-- ======================================================================== -->
  <section id="terminovnik" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
      <div>
        <span class="text-brand-sky font-bold text-xs uppercase tracking-wider">Kdy a kam vyrážíme</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy font-heading mt-1">
          Termínovník akcí & výprav
        </h2>
        <p class="text-slate-600 mt-2 text-sm max-w-xl">
          Aktuální přehled víkendovek, brigád, závodů a táborů. Vyberte palubu pro zobrazení programu.
        </p>
      </div>

      <div class="inline-flex p-1.5 rounded-2xl bg-slate-200/80 border border-slate-300">
        <button id="tabBarka" onclick="switchTerminovnik('barka')" class="px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-brand-navy text-white shadow-md transition-all">
          Bárka (Skauti)
        </button>
        <button id="tabVlcata" onclick="switchTerminovnik('vlcata')" class="px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm text-slate-700 hover:text-slate-950 transition-all">
          Toulavá smečka (Vlčata)
        </button>
      </div>
    </div>

    <!-- TERMINOVNIK GRID BARKA -->
    <div id="gridBarka" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {barka_cards}
    </div>

    <!-- TERMINOVNIK GRID VLCATA (HIDDEN BY DEFAULT) -->
    <div id="gridVlcata" class="hidden grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {vlcata_cards}
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: AKTUALITY Z LODĚNICE -->
  <!-- ======================================================================== -->
  <section id="aktuality" class="py-20 bg-slate-50 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
        <div>
          <span class="text-brand-sky font-bold text-xs uppercase tracking-wider">Z kroniky a dění v oddíle</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy font-heading mt-1">
            Aktuality z oddílu &amp; výprav
          </h2>
          <p class="text-slate-600 mt-2 text-sm max-w-xl">
            Čerstvé reportáže z našich závodů na vodě, vícedenních výprav a oddílového života.
          </p>
        </div>
        <a href="https://eu.zonerama.com/11skautskyoddil/" target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-xs bg-white hover:bg-slate-100 text-slate-800 border border-slate-200 shadow-sm transition-all">
          <span>Celá fotogalerie na Zonerama</span>
          <i class="fa-solid fa-arrow-up-right-from-square text-[10px] text-brand-sky"></i>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {blog_cards}
      </div>

    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: CO S SEBOU & VÝBAVA -->
  <!-- ======================================================================== -->
  <section id="co-s-sebou" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <span class="text-brand-sky font-bold text-xs uppercase tracking-wider">Výbava & Kroj</span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy font-heading mt-1">
        Co si sbalit na schůzku a na vodu
      </h2>
      <p class="text-slate-600 mt-2 text-sm">
        Přehledný seznam, se kterým váš kluk na nic nezapomene.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Schůzka -->
      <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
        <div class="w-12 h-12 rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center text-xl mb-4">
          <i class="fa-solid fa-pencil"></i>
        </div>
        <h3 class="text-lg font-bold text-slate-900 font-heading">Na běžnou schůzku</h3>
        <p class="text-xs text-slate-500 mt-1 mb-4">Základní výbava každou středu / čtvrtek</p>
        <ul class="space-y-2 text-xs text-slate-600">
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Skautský zápisník a tužka / propiska</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Oddílový žlutý šátek s turbánkem</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Uzlovačka (2–3 metry repšňůry)</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Lahev s pitím</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Sportovní oblečení & přezůvky do klubovny</li>
        </ul>
      </div>

      <!-- Na vodu -->
      <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
        <div class="w-12 h-12 rounded-2xl bg-sky-50 text-brand-sky flex items-center justify-center text-xl mb-4">
          <i class="fa-solid fa-vest-patches"></i>
        </div>
        <h3 class="text-lg font-bold text-slate-900 font-heading">Na vodu & pramici</h3>
        <p class="text-xs text-slate-500 mt-1 mb-4">Pro plavbu na řece v teplých měsících</p>
        <ul class="space-y-2 text-xs text-slate-600">
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Záchranná vesta (oddíl zapůjčí)</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Boty do vody s pevnou patou (ne pantofle!)</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Kompletní suché náhradní oblečení v igelitu</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Ručník a plavky</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Pokrývka hlavy proti slunci</li>
        </ul>
      </div>

      <!-- Víkendovka -->
      <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
        <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl mb-4">
          <i class="fa-solid fa-campground"></i>
        </div>
        <h3 class="text-lg font-bold text-slate-900 font-heading">Na víkendovou výpravu</h3>
        <p class="text-xs text-slate-500 mt-1 mb-4">Základ do batohu na cesty</p>
        <ul class="space-y-2 text-xs text-slate-600">
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Spacák & karimatka</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Pevná prošlápnutá obuv do lesa</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Ešus, lžíce a funkční čelovka</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Skautský kroj na zahájení a zakončení</li>
          <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-500"></i> Pláštěnka a teplé ponožky na noc</li>
        </ul>
      </div>

    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: ZÁKLADNA VALCHA -->
  <!-- ======================================================================== -->
  <section id="klubovna" class="py-20 bg-slate-900 text-white relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-6 space-y-5">
          <span class="text-yellow-400 font-bold text-xs uppercase tracking-wider">Naše zázemí na řece Malši</span>
          <h2 class="text-3xl sm:text-4xl font-black font-heading">
            Základna Valcha v Českých Budějovicích
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Naše domovská základna Valcha se nachází v klidné lokalitě u vody nedaleko Malého jezu. Nejde pouze o loděnici – areál Valchy tvoří vytápěné klubovny pro celoroční schůzky, hangár pro oddílové pramice P550, kanoe i plachetnice, dílna a velká travnatá louka pro hry.
          </p>
          <div class="space-y-2 text-xs text-slate-300">
            <div class="flex items-center gap-2"><i class="fa-solid fa-location-dot text-yellow-400"></i> <strong>Adresa:</strong> Základna Valcha, České Budějovice</div>
            <div class="flex items-center gap-2"><i class="fa-solid fa-bus text-yellow-400"></i> <strong>Doprava:</strong> Zastávka MHD v docházkové vzdálenosti</div>
          </div>
        </div>

        <div class="lg:col-span-6 space-y-3">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            
            <!-- Foto 1 -->
            <div onclick="handleLodeniceClick(1)" class="relative rounded-2xl overflow-hidden aspect-[4/3] shadow-lg border border-slate-700 hover:border-yellow-400 bg-slate-950 group cursor-pointer select-none transition-all duration-300" title="Klikněte do fotky pro změnu">
              <img id="lodeniceImg1" src="zonerama_valcha.jpg" alt="Základna Valcha" class="w-full h-full object-cover transition-opacity duration-300 group-hover:scale-105 transition-transform">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent flex flex-col justify-between p-3.5 pointer-events-none">
                <div class="flex justify-between items-start">
                  <span id="lodeniceTag1" class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-yellow-400 text-slate-950 shadow-xs">Zázemí u řeky</span>
                  <span class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-slate-900/80 text-[10px] text-yellow-300 opacity-80 group-hover:opacity-100 transition-opacity">
                    <i class="fa-solid fa-hand-pointer text-[9px]"></i> Klikni
                  </span>
                </div>
                <div>
                  <p id="lodeniceTitle1" class="text-xs font-bold text-white leading-tight">Klubovny a život na Valše při schůzkách</p>
                </div>
              </div>
            </div>

            <!-- Foto 2 -->
            <div onclick="handleLodeniceClick(2)" class="relative rounded-2xl overflow-hidden aspect-[4/3] shadow-lg border border-slate-700 hover:border-yellow-400 bg-slate-950 group cursor-pointer select-none transition-all duration-300" title="Klikněte do fotky pro změnu">
              <img id="lodeniceImg2" src="foto_6.jpg" alt="Zázemí oddílu" class="w-full h-full object-cover transition-opacity duration-300 group-hover:scale-105 transition-transform">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent flex flex-col justify-between p-3.5 pointer-events-none">
                <div class="flex justify-between items-start">
                  <span id="lodeniceTag2" class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-sky-400 text-slate-950 shadow-xs">Vodácký výcvik</span>
                  <span class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-slate-900/80 text-[10px] text-sky-300 opacity-80 group-hover:opacity-100 transition-opacity">
                    <i class="fa-solid fa-hand-pointer text-[9px]"></i> Klikni
                  </span>
                </div>
                <div>
                  <p id="lodeniceTitle2" class="text-xs font-bold text-white leading-tight">Molo a trénink posádek</p>
                </div>
              </div>
            </div>

          </div>

          <!-- Ovládací lišta pro náhodnou změnu fotek -->
          <div class="flex items-center justify-between pt-1 text-xs text-slate-400">
            <span class="flex items-center gap-1.5 text-[11px]">
              <i class="fa-solid fa-shuffle text-yellow-400"></i>
              Fotky se automaticky náhodně střídají
            </span>
            <button onclick="randomizeLodenicePhotos()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-yellow-400 font-bold text-xs border border-slate-700 hover:border-yellow-400/50 transition-all cursor-pointer">
              <i class="fa-solid fa-dice"></i>
              <span>Náhodná fotka</span>
            </button>
          </div>
        </div>

      </div>

      <!-- INTERAKTIVNÍ MAPA & NAVIGACE K VALŠE -->
      <div class="mt-14 pt-10 border-t border-slate-800">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          
          <!-- Left: OpenStreetMap Interactive Embed -->
          <div class="lg:col-span-7 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-map-location-dot"></i> Interaktivní mapa základny Valcha
              </span>
              <span class="text-[11px] text-slate-400 font-medium">Stromovka 3, České Budějovice</span>
            </div>

            <div class="relative rounded-2xl overflow-hidden shadow-2xl border-2 border-slate-700 bg-slate-950 aspect-[16/10] sm:aspect-[16/9]">
              <iframe 
                title="Mapa základny Valcha České Budějovice"
                class="w-full h-full border-0 filter contrast-105" 
                src="https://www.openstreetmap.org/export/embed.html?bbox=14.4621%2C48.9675%2C14.4761%2C48.9765&amp;layer=mapnik&amp;marker=48.9720617%2C14.4690989"
                loading="lazy">
              </iframe>
              <div class="absolute top-3 left-3 px-3 py-1.5 rounded-xl bg-slate-950/90 backdrop-blur-md border border-yellow-400/40 text-white text-xs font-bold shadow-lg pointer-events-none flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-yellow-400 animate-pulse"></span>
                <span>Základna Valcha (11. oddíl)</span>
              </div>
            </div>

            <!-- Rychlá navigační tlačítka -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-1">
              <a href="https://mapy.cz/zakladni?q=48.9720617N%2C+14.4690989E" target="_blank" class="flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-yellow-400 hover:bg-yellow-300 text-slate-950 font-black text-xs transition-all shadow-md">
                <i class="fa-solid fa-diamond-turn-right text-sm"></i>
                <span>Navigovat v Mapy.cz</span>
              </a>
              <a href="https://www.google.com/maps/search/?api=1&query=48.9720617,14.4690989" target="_blank" class="flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white border border-white/20 font-bold text-xs transition-all">
                <i class="fa-brands fa-google text-sm text-yellow-400"></i>
                <span>Google Maps</span>
              </a>
              <a href="https://idos.idnes.cz/ceskebudejovice/spojeni/" target="_blank" class="flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-sky-500/20 hover:bg-sky-500/30 text-sky-300 border border-sky-400/30 font-bold text-xs transition-all">
                <i class="fa-solid fa-bus text-sm"></i>
                <span>Spojení MHD (IDOS)</span>
              </a>
            </div>
          </div>

          <!-- Right: Průvodce příchodem & praktické rady pro rodiče -->
          <div class="lg:col-span-5 bg-slate-950/80 rounded-2xl p-6 border border-slate-800 space-y-4">
            <h3 class="text-lg font-black text-white font-heading flex items-center gap-2">
              <i class="fa-solid fa-route text-yellow-400"></i> Kudy k nám na Valchu
            </h3>

            <div class="space-y-3.5 text-xs text-slate-300">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-yellow-400/10 text-yellow-400 flex items-center justify-center shrink-0 text-sm mt-0.5">
                  <i class="fa-solid fa-location-dot"></i>
                </div>
                <div>
                  <strong class="text-white block">Adresa &amp; GPS</strong>
                  <span>Stromovka 3 (Valcha), 370 01 České Budějovice</span><br>
                  <code class="text-yellow-300 font-mono text-[11px]">48.9720617° N, 14.4690989° E</code>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-sky-400/10 text-brand-sky flex items-center justify-center shrink-0 text-sm mt-0.5">
                  <i class="fa-solid fa-bus"></i>
                </div>
                <div>
                  <strong class="text-white block">Městská hromadná doprava (MHD)</strong>
                  <span>Zastávka <em>Výstaviště</em> nebo <em>U Parku</em>. Odtud je to klidná pěší procházka parkem Stromovka cca 5–7 minut podél vody.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-emerald-400/10 text-emerald-400 flex items-center justify-center shrink-0 text-sm mt-0.5">
                  <i class="fa-solid fa-bicycle"></i>
                </div>
                <div>
                  <strong class="text-white block">Na kole a pěšky</strong>
                  <span>Přímo kolem Valchy vede bezpečná páteřní cyklostezka podél řeky. Před základnou je prostor pro bezpečné zamčení kol.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-amber-400/10 text-amber-400 flex items-center justify-center shrink-0 text-sm mt-0.5">
                  <i class="fa-solid fa-square-parking"></i>
                </div>
                <div>
                  <strong class="text-white block">Autem &amp; Parkování pro rodiče</strong>
                  <span>Parkování v ulici Stromovka / Na Zlaté stoce. Upozornění: K samotné základně Valcha je pěší zóna a zákaz vjezdu aut.</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: NÁBOR NOVÝCH ČLENŮ -->
  <!-- ======================================================================== -->
  <section id="nabor" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-gradient-to-br from-brand-navy via-brand-blue to-slate-900 rounded-3xl p-8 sm:p-12 text-white shadow-2xl relative overflow-hidden">
      <div class="max-w-3xl space-y-4">
        <span class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-yellow-400 text-slate-950 uppercase tracking-wider">
          Nábor chlapců do oddílu
        </span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading leading-tight">
          Hledáte pro syna partu správných kamarádů?
        </h2>
        <p class="text-slate-200 text-sm sm:text-base leading-relaxed">
          Přijímáme chlapce od 6 do 10 let do Toulavé smečky (vlčata) i starší kluky od 11 do 14 let do Bárky (skauti). 
          První tři schůzky jsou nezávazné a zdarma – přijďte se podívat na Valchu!
        </p>
        <div class="pt-4 flex flex-wrap gap-4">
          <a href="#kontakty" class="px-6 py-3.5 rounded-xl font-black text-sm bg-yellow-400 text-slate-950 hover:bg-yellow-300 transition-all shadow-lg">
            Kontaktovat kapitána oddílu
          </a>
          <a href="#pro-rodice" class="px-6 py-3.5 rounded-xl font-bold text-sm bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all">
            Časy schůzek a garanti
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: KONTAKTY & KLÍČOVÉ VEDENÍ ODDÍLU (SE SKUTEČNÝMI PROFILOVÝMI FOTKAMI) -->
  <!-- ======================================================================== -->
  <section id="kontakty" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <span class="text-brand-sky font-bold text-xs uppercase tracking-wider">Lidé za kormidlem</span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy font-heading mt-1">
        Vedení oddílu &amp; Klíčové kontakty
      </h2>
      <p class="text-slate-600 mt-2 text-sm">
        Potřebujete poradit? Zde jsou přímé kontakty na kapitána oddílu a důstojníky jednotlivých palub.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
      
      <!-- Kontakt 1: Kapitán Hopík -->
      <div class="bg-white rounded-3xl p-7 shadow-lg border border-slate-200/80 text-center relative group flex flex-col justify-between">
        <div>
          <div class="w-24 h-24 mx-auto rounded-2xl overflow-hidden shadow-md border-2 border-yellow-400 mb-4 bg-slate-100">
            <img src="avatars/avatar_1.jpg" alt="Martin Hájek – Hopík" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
          </div>
          <span class="inline-block px-3 py-1 rounded-full text-[11px] font-black bg-slate-900 text-yellow-300 uppercase tracking-wider mb-2">
            Kapitán oddílu
          </span>
          <h3 class="text-2xl font-black text-slate-900 font-heading">Hopík</h3>
          <p class="text-xs font-bold text-slate-600">Martin Hájek</p>
          
          <p class="text-xs text-slate-500 mt-3 px-2 leading-relaxed">
            Celkové vedení oddílu, tábory, oficiální záležitosti, nábor a komunikace se střediskem Vavéha.
          </p>
        </div>

        <div class="mt-6 pt-6 border-t border-slate-100 space-y-2 text-xs font-semibold">
          <a href="tel:+420733238774" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 text-brand-navy transition-all">
            <i class="fa-solid fa-phone text-brand-sky"></i>
            <span>733 238 774</span>
          </a>
          <a href="mailto:hopik@jedenactka.eu" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 text-brand-navy transition-all">
            <i class="fa-solid fa-envelope text-brand-sky"></i>
            <span>hopik@jedenactka.eu</span>
          </a>
        </div>
      </div>

      <!-- Kontakt 2: Vlčata Knedlík -->
      <div class="bg-white rounded-3xl p-7 shadow-lg border border-slate-200/80 text-center relative group flex flex-col justify-between">
        <div>
          <div class="w-24 h-24 mx-auto rounded-2xl overflow-hidden shadow-md border-2 border-amber-400 mb-4 bg-slate-100">
            <img src="avatars/avatar_2.jpg" alt="David Hacker – Knedlík" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
          </div>
          <span class="inline-block px-3 py-1 rounded-full text-[11px] font-black bg-amber-100 text-amber-900 uppercase tracking-wider mb-2">
            Důstojník Toulavé smečky
          </span>
          <h3 class="text-2xl font-black text-slate-900 font-heading">Knedlík</h3>
          <p class="text-xs font-bold text-slate-600">David Hacker</p>
          
          <p class="text-xs text-slate-500 mt-3 px-2 leading-relaxed">
            Hlavní vedoucí Toulavé smečky (vlčata 6–10 let), příprava schůzek a víkendových výprav.
          </p>
        </div>

        <div class="mt-6 pt-6 border-t border-slate-100 space-y-2 text-xs font-semibold">
          <a href="tel:+420604458758" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 transition-all">
            <i class="fa-solid fa-phone text-amber-600"></i>
            <span>604 458 758</span>
          </a>
          <a href="mailto:knedlik@jedenactka.eu" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 text-brand-navy transition-all">
            <i class="fa-solid fa-envelope text-amber-600"></i>
            <span>knedlik@jedenactka.eu</span>
          </a>
          <span class="block text-[11px] text-slate-400 py-0.5">Garant schůzek viz sekce Pro rodiče</span>
        </div>
      </div>

      <!-- Kontakt 3: Skauti Vodník -->
      <div class="bg-white rounded-3xl p-7 shadow-lg border border-slate-200/80 text-center relative group flex flex-col justify-between">
        <div>
          <div class="w-24 h-24 mx-auto rounded-2xl overflow-hidden shadow-md border-2 border-sky-400 mb-4 bg-slate-100">
            <img src="avatars/avatar_17.jpg" alt="Vít Veltrubský – Vodník" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
          </div>
          <span class="inline-block px-3 py-1 rounded-full text-[11px] font-black bg-sky-100 text-brand-blue uppercase tracking-wider mb-2">
            Důstojník Bárky
          </span>
          <h3 class="text-2xl font-black text-slate-900 font-heading">Vodník / Slon</h3>
          <p class="text-xs font-bold text-slate-600">Vít Veltrubský</p>
          
          <p class="text-xs text-slate-500 mt-3 px-2 leading-relaxed">
            Důstojník skautské paluby Bárka (chlapci 11–15 let), vodácký výcvik, putovní výpravy na vodě a akce Bárky.
          </p>
        </div>

        <div class="mt-6 pt-6 border-t border-slate-100 space-y-2 text-xs font-semibold">
          <a href="tel:+420724687854" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-sky-50 hover:bg-sky-100 text-brand-navy transition-all">
            <i class="fa-solid fa-phone text-brand-sky"></i>
            <span>724 687 854</span>
          </a>
          <a href="mailto:vodnik@jedenactka.eu" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 text-brand-navy transition-all">
            <i class="fa-solid fa-envelope text-brand-sky"></i>
            <span>vodnik@jedenactka.eu</span>
          </a>
          <span class="block text-[11px] text-slate-400 py-0.5">Garanti schůzek Werran & Fanda krátký</span>
        </div>
      </div>

    </div>

    <!-- VELKÝ BANNER PRO PŘECHOD NA CELÉ VEDENÍ ODDÍLU (34 VEDOUCÍCH) -->
    <div class="rounded-3xl bg-slate-900 p-8 sm:p-10 text-white text-center sm:text-left flex flex-col sm:flex-row items-center justify-between gap-6 shadow-xl border-2 border-yellow-400/40">
      <div class="space-y-2 max-w-2xl">
        <span class="text-xs font-bold uppercase tracking-wider text-yellow-400">Kompletní tým Jedenáctky</span>
        <h3 class="text-2xl sm:text-3xl font-black font-heading">
          Chcete vidět celé vedení oddílu?
        </h3>
        <p class="text-slate-300 text-xs sm:text-sm">
          Náš oddíl tvoří 34 obětavých vedoucích, garantů schůzek a lodivodů. Podívejte se na jejich profily, kvalifikace a funkce.
        </p>
      </div>
      <a href="vedeni.html" class="px-8 py-4 rounded-2xl font-black text-sm bg-gradient-to-r from-yellow-400 to-amber-500 text-slate-950 hover:scale-105 active:scale-95 transition-all shadow-lg shrink-0 flex items-center gap-3">
        <i class="fa-solid fa-users text-lg"></i>
        <span>Zobrazit všech 34 vedoucích & lodivodů</span>
        <i class="fa-solid fa-arrow-right text-xs"></i>
      </a>
    </div>

  </section>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-slate-400 text-xs py-12 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <img src="logo_emblem.png" alt="11. oddíl vodních skautů" class="h-8 w-auto object-contain brightness-110">
        <span class="text-slate-300 font-bold">11. oddíl vodních skautů České Budějovice</span>
      </div>
      <p class="text-slate-500 text-center sm:text-right flex flex-col sm:flex-row items-center justify-end gap-1.5 sm:gap-2">
        <span class="text-slate-400">Verze: {get_app_version()} ({get_git_commit()})</span>
        <span class="hidden sm:inline text-slate-700">•</span>
        <span class="text-slate-400">Aktualizováno: {BUILD_TIMESTAMP}</span>
        <span class="hidden sm:inline text-slate-700">•</span>
        <span>Registrováno u Junák – český skaut, 4. středisko VAVÉHA České Budějovice.</span>
      </p>
    </div>
  </footer>

  <script>
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenuBtn && mobileMenu) {{
      mobileMenuBtn.addEventListener('click', () => {{
        mobileMenu.classList.toggle('hidden');
      }});
      mobileMenu.querySelectorAll('a').forEach(link => {{
        link.addEventListener('click', () => {{
          mobileMenu.classList.add('hidden');
        }});
      }});
    }}

    // Termínovník tabs switcher
    function switchTerminovnik(tab) {{
      const gridBarka = document.getElementById('gridBarka');
      const gridVlcata = document.getElementById('gridVlcata');
      const tabBarka = document.getElementById('tabBarka');
      const tabVlcata = document.getElementById('tabVlcata');

      if (tab === 'barka') {{
        gridBarka.classList.remove('hidden');
        gridBarka.classList.add('grid');
        gridVlcata.classList.add('hidden');
        gridVlcata.classList.remove('grid');

        tabBarka.className = "px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-brand-navy text-white shadow-md transition-all";
        tabVlcata.className = "px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm text-slate-700 hover:text-slate-950 transition-all";
      }} else {{
        gridVlcata.classList.remove('hidden');
        gridVlcata.classList.add('grid');
        gridBarka.classList.add('hidden');
        gridBarka.classList.remove('grid');

        tabVlcata.className = "px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-brand-navy text-white shadow-md transition-all";
        tabBarka.className = "px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm text-slate-700 hover:text-slate-950 transition-all";
      }}
    }}

    // FAQ accordion toggle
    function toggleFaq(idx) {{
      const ans = document.getElementById('faqAns' + idx);
      const icon = document.getElementById('faqIcon' + idx);
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
    const lodenicePhotos = [
      {{ src: "zonerama_valcha.jpg", title: "Klubovny a život na Valše při schůzkách", tag: "Základna Valcha" }},
      {{ src: "zonerama_1.jpg", title: "Trénink na vodě a přístaviště u řeky", tag: "Vodácký výcvik" }},
      {{ src: "foto_3.jpg", title: "Základna Valcha na břehu řeky Malše", tag: "Zázemí u řeky" }},
      {{ src: "foto_6.jpg", title: "Molo a trénink posádek na vodě", tag: "Vodácký výcvik" }},
      {{ src: "barka_1.jpg", title: "Lodní hangár a budovy základny", tag: "Lodní hangár" }},
      {{ src: "barka_2.jpg", title: "Klubovny a travnaté prostranství", tag: "Zázemí pro hry" }},
      {{ src: "upload_2.png", title: "Pramice P550 a plachetnice Jedenáctky", tag: "Flotila lodí" }},
      {{ src: "upload_1.jpg", title: "Areál základny v přírodě u Malého jezu", tag: "Klidná lokalita" }}
    ];

    let currentLodeniceIdx1 = Math.floor(Math.random() * lodenicePhotos.length);
    let currentLodeniceIdx2 = (currentLodeniceIdx1 + 1) % lodenicePhotos.length;

    function randomizeSingleLodenice(slot) {{
      if (slot === 1) {{
        let newIdx1 = Math.floor(Math.random() * lodenicePhotos.length);
        while ((newIdx1 === currentLodeniceIdx1 || newIdx1 === currentLodeniceIdx2) && lodenicePhotos.length > 2) {{
          newIdx1 = Math.floor(Math.random() * lodenicePhotos.length);
        }}
        currentLodeniceIdx1 = newIdx1;
        applySingleLodenicePhoto(1);
      }} else {{
        let newIdx2 = Math.floor(Math.random() * lodenicePhotos.length);
        while ((newIdx2 === currentLodeniceIdx2 || newIdx2 === currentLodeniceIdx1) && lodenicePhotos.length > 2) {{
          newIdx2 = Math.floor(Math.random() * lodenicePhotos.length);
        }}
        currentLodeniceIdx2 = newIdx2;
        applySingleLodenicePhoto(2);
      }}
    }}

    function handleLodeniceClick(slot) {{
      randomizeSingleLodenice(slot);
      startLodeniceTimer();
    }}

    function randomizeLodenicePhotos() {{
      let newIdx1 = Math.floor(Math.random() * lodenicePhotos.length);
      while (newIdx1 === currentLodeniceIdx1 && lodenicePhotos.length > 1) {{
        newIdx1 = Math.floor(Math.random() * lodenicePhotos.length);
      }}
      currentLodeniceIdx1 = newIdx1;
      
      let newIdx2 = Math.floor(Math.random() * lodenicePhotos.length);
      while ((newIdx2 === currentLodeniceIdx1 || newIdx2 === currentLodeniceIdx2) && lodenicePhotos.length > 2) {{
        newIdx2 = Math.floor(Math.random() * lodenicePhotos.length);
      }}
      currentLodeniceIdx2 = newIdx2;

      applyLodenicePhotos();
    }}

    function applySingleLodenicePhoto(slot) {{
      if (slot === 1) {{
        const img1 = document.getElementById('lodeniceImg1');
        const title1 = document.getElementById('lodeniceTitle1');
        const tag1 = document.getElementById('lodeniceTag1');
        if (img1) {{
          img1.style.opacity = '0.2';
          setTimeout(() => {{
            img1.src = lodenicePhotos[currentLodeniceIdx1].src;
            img1.alt = lodenicePhotos[currentLodeniceIdx1].title;
            if (title1) title1.textContent = lodenicePhotos[currentLodeniceIdx1].title;
            if (tag1) tag1.textContent = lodenicePhotos[currentLodeniceIdx1].tag;
            img1.style.opacity = '1';
          }}, 180);
        }}
      }} else {{
        const img2 = document.getElementById('lodeniceImg2');
        const title2 = document.getElementById('lodeniceTitle2');
        const tag2 = document.getElementById('lodeniceTag2');
        if (img2) {{
          img2.style.opacity = '0.2';
          setTimeout(() => {{
            img2.src = lodenicePhotos[currentLodeniceIdx2].src;
            img2.alt = lodenicePhotos[currentLodeniceIdx2].title;
            if (title2) title2.textContent = lodenicePhotos[currentLodeniceIdx2].title;
            if (tag2) tag2.textContent = lodenicePhotos[currentLodeniceIdx2].tag;
            img2.style.opacity = '1';
          }}, 180);
        }}
      }}
    }}

    function applyLodenicePhotos() {{
      applySingleLodenicePhoto(1);
      applySingleLodenicePhoto(2);
    }}

    let lodeniceTimer = null;
    function startLodeniceTimer() {{
      if (lodeniceTimer) clearInterval(lodeniceTimer);
      lodeniceTimer = setInterval(() => {{
        randomizeLodenicePhotos();
      }}, 4000);
    }}

    // Hero záhlaví - náhodné a automatické střídání fotografií
    // Fotografie čerpané z oddílové fotogalerie Zonerama za poslední rok
    const heroPhotos = [
      {{ src: "zonerama_2.jpg", tag: "Společná voda 2026", sub: "Sjíždění šlajsny na kánoi", title: "Vodácká dobrodružství & peřeje na řece" }},
      {{ src: "zonerama_1.jpg", tag: "Slalomový kanál 2026", sub: "České Vrbné • divoká voda", title: "Zázemí na vodě & trénink pádlování a stability" }},
      {{ src: "zonerama_3.jpg", tag: "3 Jezy Praha 2025", sub: "Závod Napříč Prahou", title: "Reprezentace posádky 11. oddílu na prestižním závodě" }},
      {{ src: "zonerama_5.jpg", tag: "Expedice na vodě", sub: "Společná výprava 11. oddílu", title: "Příroda, ticho a putování po jihočeských řekách" }},
      {{ src: "zonerama_valcha.jpg", tag: "Život na Valše", sub: "Klubovna a základna 11. oddílu", title: "Týmové hry v klubovně a celoroční program schůzek" }},
      {{ src: "zonerama_camp.jpg", tag: "Tábor Labská Stráň 2026", sub: "Lezení v pískovcích", title: "Čtrnáct dní nezapomenutelných zážitků a výzev v přírodě" }},
      {{ src: "zonerama_6.jpg", tag: "Kajaky v peřejích", sub: "České Vrbné", title: "Slalomový trénink mezi brankami na divoké vodě" }},
      {{ src: "zonerama_hero_1.jpg", tag: "Vánoce na Švýcaráku", sub: "Zimní výprava v lesích", title: "Tradiční vánoční setkání oddílu na srubové základně Švýcarák" }},
      {{ src: "zonerama_hero_2.jpg", tag: "Vánoce na Švýcaráku", sub: "Prskavky & stromeček", title: "Kouzlo Vánoc, oddílové zvyky a dárky v zasněžených lesích" }},
      {{ src: "zonerama_hero_3.jpg", tag: "Výprava všech lidí na zemi", sub: "Podzimní výprava", title: "Společné dobrodružství a setkání generací vodních skautů" }},
      {{ src: "zonerama_hero_4.jpg", tag: "Výprava všech lidí na zemi", sub: "Táborový oheň v přírodě", title: "Špekáčky, kytary a přátelství v údolí řeky Vltavy" }},
      {{ src: "zonerama_hero_5.jpg", tag: "Brigáda na Švýcaráku", sub: "Pomoc základně", title: "Příprava palivového dříví na zimu a údržba oddílového srubu" }},
      {{ src: "zonerama_hero_6.jpg", tag: "3 Jezy Praha 2025", sub: "Start pod Vyšehradem", title: "Reprezentace 11. oddílu na legendárním závodě Napříč Prahou" }},
      {{ src: "zonerama_hero_7.jpg", tag: "3 Jezy Praha 2025", sub: "Šlajsna na Vltavě", title: "Průjezd vorovou propustí v peřejích historického centra Prahy" }},
      {{ src: "zonerama_hero_8.jpg", tag: "Slalomový kanál 2026", sub: "České Vrbné • divoká voda", title: "Trénink pádlování a stability posádek mezi brankami" }},
      {{ src: "zonerama_hero_9.jpg", tag: "Společná voda 2026", sub: "Flotila na řece Vltavě", title: "Putování na kanoích po jihočeských řekách a vodácká kamarádství" }},
      {{ src: "zonerama_hero_10.jpg", tag: "Tábor Labská Stráň 2026", sub: "Lezení v pískovcích", title: "Skalní lezení, lanové techniky a odvaha v Labském kaňonu" }}
    ];

    let currentHeroIdx = Math.floor(Math.random() * heroPhotos.length);

    function renderHeroDots() {{
      const container = document.getElementById('heroDots');
      if (!container) return;
      container.innerHTML = heroPhotos.map((_, i) => `
        <button onclick="event.stopPropagation(); setHeroPhoto(${{i}})" class="h-1.5 rounded-full transition-all cursor-pointer ${{i === currentHeroIdx ? 'w-6 bg-yellow-400' : 'w-2 bg-white/30 hover:bg-white/60'}}" title="Fotka ${{i+1}}"></button>
      `).join('');
    }}

    function setHeroPhoto(idx) {{
      currentHeroIdx = idx;
      applyHeroPhoto();
      startHeroTimer();
    }}

    function randomizeHeroPhoto() {{
      let newIdx = Math.floor(Math.random() * heroPhotos.length);
      while (newIdx === currentHeroIdx && heroPhotos.length > 1) {{
        newIdx = Math.floor(Math.random() * heroPhotos.length);
      }}
      currentHeroIdx = newIdx;
      applyHeroPhoto();
    }}

    function handleHeroClick() {{
      randomizeHeroPhoto();
      startHeroTimer();
    }}

    function applyHeroPhoto() {{
      const img = document.getElementById('heroImg');
      const tag = document.getElementById('heroTag');
      const sub = document.getElementById('heroSub');
      const title = document.getElementById('heroTitle');

      if (img) {{
        img.style.opacity = '0.2';
        setTimeout(() => {{
          const item = heroPhotos[currentHeroIdx];
          img.src = item.src;
          img.alt = item.title;
          if (tag) tag.textContent = item.tag;
          if (sub) sub.textContent = item.sub;
          if (title) title.textContent = item.title;
          img.style.opacity = '1';
          renderHeroDots();
        }}, 200);
      }}
    }}

    let heroTimer = null;
    function startHeroTimer() {{
      if (heroTimer) clearInterval(heroTimer);
      heroTimer = setInterval(() => {{
        randomizeHeroPhoto();
      }}, 5000);
    }}

    // Spustit náhodnou fotku hned při načtení a zapnout rotaci
    applyHeroPhoto();
    startHeroTimer();

    // Spustit náhodné fotky loděnice a zapnout rotaci
    randomizeLodenicePhotos();
    startLodeniceTimer();

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
    with open('verzeA/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully generated verzeA/index.html")

# Build verzeA/vedeni.html
def generate_vedeni_a():
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
            badge_color = "bg-slate-900 text-white"
            filter_cat = "vedeni"
        elif "toulav" in raw_str or "smečk" in raw_str or any(n in raw_str for n in ['myšák', 'čáp', 'knedlík', 'kraken', 'sponzor', 'rusalka', 'achilles', 'sisi', 'bobr', 'medůza', 'tulák', 'ríša', 'trasher', 'jerhi', 'venda']):
            badge_text = "Toulavá smečka (vlčata)"
            badge_color = "bg-amber-100 text-amber-900 border-amber-300"
            filter_cat = "vlcata"
        else:
            badge_text = "Bárka (skauti)"
            badge_color = "bg-sky-100 text-brand-blue border-sky-300"
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

        extra_html = "".join([f'<div class="text-[11px] text-slate-600 bg-slate-50 p-2 rounded-xl border border-slate-100 mt-1.5">{ex}</div>' for ex in extra])

        contacts_html = ""
        if phone:
            clean_digits = re.sub(r'[^0-9+]', '', phone)
            if not clean_digits.startswith('+'):
                clean_digits = f'+420{clean_digits}'
            contacts_html += f'<a href="tel:{clean_digits}" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-slate-800 text-xs font-semibold border border-slate-200/80 transition-colors"><i class="fa-solid fa-phone text-brand-sky"></i> {phone}</a> '
        if email:
            contacts_html += f'<a href="mailto:{email}" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-slate-800 text-xs font-semibold border border-slate-200/80 transition-colors"><i class="fa-solid fa-envelope text-brand-sky"></i> {email}</a>'

        card = f"""
        <div class="leader-card {filter_cat} bg-white rounded-3xl p-6 shadow-md shadow-slate-200/50 border border-slate-200/80 hover:shadow-xl hover:border-brand-sky transition-all flex flex-col justify-between group">
          <div>
            <div class="flex items-start gap-4 mb-3">
              <div class="w-18 h-18 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white group-hover:scale-105 transition-transform bg-slate-100" style="width: 72px; height: 72px;">
                <img src="{avatar}" alt="{h(name)}" class="w-full h-full object-cover">
              </div>
              <div>
                <span class="inline-block px-2.5 py-0.5 rounded-md text-[10px] font-black uppercase tracking-wider border mb-1 {badge_color}">
                  {badge_text}
                </span>
                <h3 class="text-lg font-black text-slate-900 font-heading leading-tight">{h(nick if nick else name)}</h3>
                {f'<p class="text-xs font-bold text-slate-700 mt-0.5">{h(name)}</p>' if nick else ''}
                <p class="text-[11px] font-semibold text-brand-sky mt-0.5">{h(role)}</p>
              </div>
            </div>

            <div class="space-y-1 mt-2">
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
            brand: {{
              navyDark: '#071527',
              navy: '#0C2340',
              blue: '#134074',
              sky: '#00A8E8',
              skyLight: '#E8F6FD',
              gold: '#FACC15',
              goldHover: '#EAB308'
            }}
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}

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
      background-color: #f8fafc;
      color: #0f172a;
    }}
    html:not(.dark) .leader-card p,
    html:not(.dark) .bg-white p,
    html:not(.dark) .bg-slate-50 p {{
      color: #1e293b;
    }}
    html:not(.dark) .text-slate-900 {{
      color: #071527 !important;
    }}
    html:not(.dark) .text-brand-navy {{
      color: #0c2340 !important;
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
    html:not(.dark) section.bg-gradient-to-br {{
      color: #ffffff;
    }}
    html:not(.dark) section.bg-gradient-to-br h1,
    html:not(.dark) section.bg-gradient-to-br strong,
    html:not(.dark) .bg-slate-950 strong,
    html:not(.dark) .bg-slate-900 strong,
    html:not(.dark) footer.bg-slate-950 strong {{
      color: #ffffff !important;
    }}
    html:not(.dark) .bg-slate-950 p,
    html:not(.dark) .bg-slate-900 p,
    html:not(.dark) footer.bg-slate-950 p,
    html:not(.dark) section.bg-gradient-to-br p {{
      color: #e2e8f0 !important;
    }}
    html:not(.dark) .bg-slate-950 span.text-slate-300,
    html:not(.dark) .bg-slate-900 span.text-slate-300,
    html:not(.dark) footer.bg-slate-950 span.text-slate-300,
    html:not(.dark) section.bg-gradient-to-br span.text-slate-300,
    html:not(.dark) section.bg-gradient-to-br .text-slate-300 {{
      color: #cbd5e1 !important;
    }}
    html:not(.dark) .bg-slate-950 span.text-slate-400,
    html:not(.dark) .bg-slate-900 span.text-slate-400,
    html:not(.dark) footer.bg-slate-950 span.text-slate-400,
    html:not(.dark) footer.bg-slate-950 p.text-slate-400,
    html:not(.dark) footer.bg-slate-950 p.text-slate-500,
    html:not(.dark) section.bg-gradient-to-br span.text-slate-400 {{
      color: #94a3b8 !important;
    }}

    /* ========================================================= */
    /* TMAVÝ REŽIM PRO VEDENÍ                                    */
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
    .dark #mobileMenu {{
      background-color: #0b1329 !important;
      border-color: #1e293b !important;
    }}
    .dark #mobileMenu a {{
      color: #e2e8f0 !important;
    }}
    .dark #mobileMenu a:hover {{
      background-color: #1e293b !important;
    }}
    .dark .bg-white {{
      background-color: #0f1c34 !important;
      border-color: #1e2e4a !important;
      color: #f1f5f9 !important;
    }}
    .dark .bg-slate-50,
    .dark .bg-slate-100,
    .dark .bg-slate-200 {{
      background-color: #162544 !important;
      border-color: #243b66 !important;
      color: #e2e8f0 !important;
    }}
    .dark .border-white {{
      border-color: #1e2e4a !important;
    }}
    .dark h1, .dark h2, .dark h3, .dark h4, .dark h5, .dark h6, .dark strong {{
      color: #ffffff !important;
    }}
    .dark .text-brand-navy,
    .dark .text-slate-900 {{
      color: #ffffff !important;
    }}
    .dark .text-brand-blue,
    .dark .text-brand-sky {{
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
    .dark .filter-btn:not(.active) {{
      background-color: #162544 !important;
      border-color: #243b66 !important;
      color: #e2e8f0 !important;
    }}
    .dark .filter-btn.active {{
      background-color: #0284c7 !important;
      color: #ffffff !important;
      border-color: #0284c7 !important;
    }}
  </style>
</head>
<body class="bg-[#F8FAFC] text-slate-800 antialiased selection:bg-brand-sky selection:text-white">

  {get_navbar(is_subpage=True)}

  <!-- HERO HEADER -->
  <section class="bg-gradient-to-br from-brand-navyDark via-brand-navy to-brand-blue text-white py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto space-y-4">
      
      <!-- DROBEČKOVÁ NAVIGACE / NÁVRAT NA HLAVNÍ STRÁNKU -->
      <div class="flex items-center justify-between flex-wrap gap-2 pb-3 border-b border-white/10 text-xs">
        <a href="index.html" class="inline-flex items-center gap-2 font-bold text-yellow-400 hover:text-white transition-colors bg-white/10 hover:bg-white/20 px-3 py-1.5 rounded-full border border-white/15">
          <i class="fa-solid fa-arrow-left text-[11px]"></i>
          <span>Zpět na hlavní stránku oddílu</span>
        </a>
        <span class="text-slate-400">Podstránka webu • Varianta A</span>
      </div>

      <div class="text-center pt-2 space-y-3">
        <span class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-yellow-400 text-slate-950 uppercase tracking-wider">
          Tým za kormidlem Jedenáctky
        </span>
        <h1 class="text-3xl sm:text-5xl font-black font-heading tracking-tight">
          Kompletní vedení oddílu &amp; lodivodi
        </h1>
        <p class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto leading-relaxed">
          Náš oddíl stojí na desítkách obětavých dobrovolníků, vůdců, garantů schůzek a lodivodů, kteří pro kluky připravují program, tábory a výpravy.
        </p>
      </div>

      <!-- FILTER CONTROLS -->
      <div class="pt-4 flex flex-wrap items-center justify-center gap-2">
        <button onclick="filterLeaders('all')" class="leader-filter active px-5 py-2.5 rounded-xl text-xs font-bold bg-brand-gold text-brand-navyDark shadow-md transition-all" data-filter="all">
          Všichni vedoucí (34)
        </button>
        <button onclick="filterLeaders('vlcata')" class="leader-filter px-5 py-2.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all" data-filter="vlcata">
          Toulavá smečka (vlčata)
        </button>
        <button onclick="filterLeaders('skauti')" class="leader-filter px-5 py-2.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all" data-filter="skauti">
          Bárka (skauti)
        </button>
        <button onclick="filterLeaders('vedeni')" class="leader-filter px-5 py-2.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all" data-filter="vedeni">
          Vůdcové oddílu
        </button>
      </div>
    </div>
  </section>

  <!-- LEADERS GRID -->
  <main class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="leadersGrid">
      {"".join(leader_cards)}
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-slate-400 text-xs py-12 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <img src="logo_emblem.png" alt="11. oddíl vodních skautů" class="h-8 w-auto object-contain brightness-110">
        <span class="text-slate-300 font-bold">11. oddíl vodních skautů České Budějovice</span>
      </div>
      <p class="text-slate-500 text-center sm:text-right flex flex-col sm:flex-row items-center justify-end gap-1.5 sm:gap-2">
        <span class="text-slate-400">Verze: {get_app_version()} ({get_git_commit()})</span>
        <span class="hidden sm:inline text-slate-700">•</span>
        <span class="text-slate-400">Aktualizováno: {BUILD_TIMESTAMP}</span>
        <span class="hidden sm:inline text-slate-700">•</span>
        <span>Registrováno u Junák – český skaut, 4. středisko VAVÉHA České Budějovice.</span>
      </p>
    </div>
  </footer>

  <script>
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenuBtn && mobileMenu) {{
      mobileMenuBtn.addEventListener('click', () => {{
        mobileMenu.classList.toggle('hidden');
      }});
      mobileMenu.querySelectorAll('a').forEach(link => {{
        link.addEventListener('click', () => {{
          mobileMenu.classList.add('hidden');
        }});
      }});
    }}

    function filterLeaders(cat) {{
      const cards = document.querySelectorAll('.leader-card');
      const btns = document.querySelectorAll('.leader-filter');

      btns.forEach(btn => {{
        if (btn.getAttribute('data-filter') === cat) {{
          btn.className = "leader-filter active px-5 py-2.5 rounded-xl text-xs font-bold bg-brand-gold text-brand-navyDark shadow-md transition-all";
        }} else {{
          btn.className = "leader-filter px-5 py-2.5 rounded-xl text-xs font-bold bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all";
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
    with open('verzeA/vedeni.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully generated verzeA/vedeni.html")

generate_index_a()
generate_vedeni_a()
save_version_json()
update_index_html_version()

