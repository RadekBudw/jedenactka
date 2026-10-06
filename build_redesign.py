# -*- coding: utf-8 -*-
import json, os, re

with open('leaders.json', encoding='utf-8') as f:
    leaders = json.load(f)

# Helper to escape HTML
def h(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

# ==============================================================================
# 1. VERZE A: MODERNÍ FLOTILA (Bold, Maritime, Vibrant Navy & Yellow)
# ==============================================================================

def build_verze_a():
    # NAVIGATION HTML (Shared 100% identically between index.html and vedeni.html)
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
        <span class="text-xs sm:text-sm">Schůzky: <strong>Středa &amp; Čtvrtek 16:00 – 18:00</strong> v loděnici Valcha</span>
      </div>
      <div class="flex items-center gap-3 text-xs">
        <!-- ČERNO-ŽLUTÁ ODDÍLOVÁ VLAJKA -->
        <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-black text-yellow-400 font-bold text-[11px] border border-yellow-400/50 shadow-xs">
          <span class="w-3.5 h-2.5 inline-block rounded-xs border border-white/40 shadow-xs" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);"></span>
          <span>Černo-žlutá vlajka</span>
        </span>
        <span class="text-white/20">|</span>
        <a href="{prefix}#terminovnik" class="hover:text-yellow-400 transition-colors flex items-center gap-1">
          <i class="fa-regular fa-calendar-check text-yellow-400"></i> Termínovník akcí
        </a>
        <span class="text-white/20">|</span>
        <a href="https://vaveha.cz" target="_blank" class="hover:text-white transition-colors">4. středisko VAVÉHA ČB</a>
      </div>
    </div>
  </div>

  <!-- NAVIGATION -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- LOGO & BRAND -->
        <a href="{prefix}#" class="flex items-center gap-3.5 group">
          <div class="w-12 h-12 rounded-2xl bg-slate-950 flex items-center justify-center text-white shadow-md shadow-slate-900/30 group-hover:scale-105 transition-transform duration-200 border-2 border-yellow-400/80 relative overflow-hidden shrink-0">
            <div class="absolute -top-3 -right-3 w-8 h-8 bg-yellow-400 rotate-45 pointer-events-none"></div>
            <i class="fa-solid fa-anchor text-2xl text-yellow-400 relative z-10"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-brand-sky">Junák – český skaut</span>
              <span class="inline-flex w-3 h-2 rounded-xs border border-slate-400/60" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);" title="Černo-žlutá vlajka 11. oddílu"></span>
            </div>
            <span class="block text-xl font-black tracking-tight text-brand-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-[11px] font-medium text-slate-500 -mt-0.5">České Budějovice • Loděnice Valcha</span>
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
          <a href="{prefix}#klubovna" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">Loděnice</a>
          <a href="{prefix}#kontakty" class="px-3 py-2 rounded-xl text-sm font-semibold text-slate-700 hover:text-brand-blue hover:bg-slate-100 transition-all">Kontakty</a>
        </nav>

        <!-- CTA & SOCIAL -->
        <div class="hidden sm:flex items-center gap-3">
          <a href="{prefix}#nabor" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm bg-gradient-to-r from-brand-gold to-brand-goldHover text-brand-navyDark shadow-md shadow-brand-gold/25 hover:shadow-lg hover:scale-[1.02] active:scale-[0.98] transition-all">
            <i class="fa-solid fa-compass text-base"></i>
            <span>Chci se přidat</span>
          </a>
        </div>

        <!-- MOBILE HAMBURGER BUTTON -->
        <button id="mobileMenuBtn" type="button" class="lg:hidden p-2.5 rounded-xl text-slate-700 hover:bg-slate-100 focus:outline-none" aria-label="Otevřít menu">
          <i class="fa-solid fa-bars text-2xl" id="menuIcon"></i>
        </button>
      </div>
    </div>

    <!-- MOBILE NAVIGATION DRAWER -->
    <div id="mobileMenu" class="hidden lg:hidden bg-white border-b border-slate-200 px-4 pt-3 pb-6 shadow-xl transition-all">
      <div class="flex flex-col gap-1 text-base font-semibold">
        <a href="{prefix}#pro-rodice" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3 font-bold text-amber-700 bg-amber-50/50">
          <i class="fa-solid fa-heart-pulse w-5 text-amber-500"></i> Pro rodiče (Rozpis schůzek & fotky)
        </a>
        <a href="{prefix}#oddil" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3">
          <i class="fa-solid fa-anchor w-5 text-brand-sky"></i> O 11. oddílu vodních skautů
        </a>
        <a href="{prefix}#paluby" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3">
          <i class="fa-solid fa-ship w-5 text-brand-sky"></i> Naše 3 paluby (vlčata, skauti, roveři)
        </a>
        <a href="{prefix}#terminovnik" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3">
          <i class="fa-regular fa-calendar-check w-5 text-brand-sky"></i> Termínovník akcí & výprav
        </a>
        <a href="{prefix}#aktuality" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3">
          <i class="fa-solid fa-newspaper w-5 text-brand-sky"></i> Aktuality z loděnice
        </a>
        <a href="vedeni.html" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3 font-bold text-brand-sky">
          <i class="fa-solid fa-users w-5 text-brand-sky"></i> Celé vedení oddílu (34 vedoucích)
        </a>
        <a href="{prefix}#klubovna" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3">
          <i class="fa-solid fa-house-chimney-water w-5 text-brand-sky"></i> Loděnice Valcha
        </a>
        <a href="{prefix}#kontakty" class="px-4 py-3 rounded-xl hover:bg-slate-100 text-slate-800 flex items-center gap-3">
          <i class="fa-solid fa-phone w-5 text-brand-sky"></i> Kontakty na kapitána & velitele
        </a>
        <div class="pt-3 border-t border-slate-100 mt-2">
          <a href="{prefix}#nabor" class="w-full py-3 rounded-xl font-bold text-center bg-brand-gold text-brand-navyDark block shadow-md">
            Chci do oddílu (Nábor chlapců)
          </a>
        </div>
      </div>
    </div>
  </header>
"""

    # Generate verzeA/index.html
    html_a = f"""<!DOCTYPE html>
<html lang="cs" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>11. oddíl vodních skautů České Budějovice | Moderní flotila</title>
  <meta name="description" content="Oficiální moderní prezentace 11. chlapeckého oddílu vodních skautů v Českých Budějovicích. Skauting, pramice, kanoe, dobrodružství pro kluky od 6 let.">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
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

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    .wave-bg {{
      background-image: radial-gradient(rgba(0, 168, 232, 0.15) 1px, transparent 0);
      background-size: 24px 24px;
    }}
    .badge-blur {{
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
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
          
          <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full bg-slate-950/90 badge-blur border border-yellow-400/40 text-xs sm:text-sm font-semibold shadow-lg">
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

          <!-- Action buttons -->
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

          <!-- Feature badges -->
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

        <!-- Right Hero Visual -->
        <div class="lg:col-span-5 relative">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white/20 aspect-[4/3] sm:aspect-[5/4] group">
            <img src="foto_1.jpg" alt="Skauti na pramici" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-gradient-to-t from-brand-navyDark/90 via-brand-navyDark/20 to-transparent"></div>
            
            <div class="absolute bottom-5 left-5 right-5 p-4 rounded-2xl bg-slate-950/80 backdrop-blur-md border border-yellow-400/30 text-white">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                  <span class="w-3 h-3 rounded-full bg-emerald-400 animate-ping"></span>
                  <span class="text-xs font-bold text-yellow-300 uppercase tracking-wider">Loděnice Valcha ČB</span>
                </div>
                <span class="text-[11px] text-slate-400">Pramice P550</span>
              </div>
              <p class="text-xs font-semibold text-slate-200 mt-1">Trénink posádek na řece Malši a Vltavě</p>
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
  <!-- SEKCE: PRO RODIČE (Rozpis schůzek, garanti, skautské maily, fotky, archivy) -->
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
          <p class="text-xs sm:text-sm text-slate-500">Loděnice Valcha České Budějovice • V případě neúčasti kontaktujte garanta daného dne.</p>
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
                <h4 class="font-bold text-slate-900 text-base font-heading">Matěj Bajgar</h4>
                <p class="text-xs font-black text-amber-600">Přezdívka: Myšák</p>
                <p class="text-[11px] text-slate-500 mt-0.5">Garant středeční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Toulavá smečka (6–10 let)</div>
              <p class="text-slate-500 text-[11px]">Příprava her, programu na vodě i v klubovně pro mladší kluky.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:778019042" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 font-bold text-xs transition-colors">
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
                <h4 class="font-bold text-slate-900 text-base font-heading">Jáchym Řehounek</h4>
                <p class="text-xs font-black text-amber-600">Přezdívka: Čáp</p>
                <p class="text-[11px] text-slate-500 mt-0.5">Garant čtvrteční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Toulavá smečka (6–10 let)</div>
              <p class="text-slate-500 text-[11px]">Omluvenky ze čtvrtečních schůzek a dotazy k programu vlčat.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:732405827" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 font-bold text-xs transition-colors">
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
                <h4 class="font-bold text-slate-900 text-base font-heading">Max Rosenthaler</h4>
                <p class="text-xs font-black text-brand-sky">Přezdívka: Werran</p>
                <p class="text-[11px] text-slate-500 mt-0.5">Garant středeční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Bárka (11–15 let)</div>
              <p class="text-slate-500 text-[11px]">Vodácký trénink, posádky skautů na řece Malši a Vltavě.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:728729518" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-sky-50 hover:bg-sky-100 text-brand-navy font-bold text-xs transition-colors">
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
              <img src="avatars/avatar_20.jpg" alt="František Kratochvíl – Franta" class="w-16 h-16 rounded-2xl object-cover shadow-sm border border-slate-200 shrink-0">
              <div>
                <h4 class="font-bold text-slate-900 text-base font-heading">František Kratochvíl</h4>
                <p class="text-xs font-black text-brand-sky">Přezdívka: Franta</p>
                <p class="text-[11px] text-slate-500 mt-0.5">Garant čtvrteční schůzky</p>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs space-y-1.5 mb-4">
              <div class="text-[11px] font-bold text-slate-700 uppercase">Bárka (11–15 let)</div>
              <p class="text-slate-500 text-[11px]">Příprava čtvrtečního programu skautů a koordinace posádek.</p>
            </div>
          </div>

          <div class="space-y-2 pt-3 border-t border-slate-100">
            <a href="tel:722320570" class="flex items-center justify-center gap-2 w-full py-2 px-3 rounded-xl bg-sky-50 hover:bg-sky-100 text-brand-navy font-bold text-xs transition-colors">
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
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: O 11. ODDÍLU (Autentický popis z původního webu, tradice, 4 paluby) -->
  <!-- ======================================================================== -->
  <section id="oddil" class="py-20 bg-slate-100 border-y border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        
        <div class="lg:col-span-7 space-y-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-yellow-400 text-slate-950 uppercase tracking-wider">
            <span class="w-2.5 h-2.5 rounded-full bg-slate-950"></span>
            Tradice od roku 1990 • 4. středisko VAVÉHA ČB
          </div>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-brand-navy font-heading tracking-tight leading-tight">
            Kdo jsme? <br>
            <span class="text-brand-blue">11. oddíl vodních skautů</span>
          </h2>
          <p class="text-slate-700 text-base leading-relaxed">
            Náš oddíl patří k tzv. <strong>vodním skautům</strong>. Jsme skauti, kteří do svého programu zahrnují také vodácké prvky – jízdu na pramicích P550, kanoích i plachetnicích. Sídlíme na vlastní loděnici Valcha na břehu Malše v Českých Budějovicích.
          </p>
          <p class="text-slate-600 text-sm leading-relaxed">
            Oddíl je podle věku chlapců rozdělen do čtyř částí (kterým u vodních skautů tradičně neříkáme oddíly, ale <strong>paluby</strong>): 
            První paluba pro nejmladší kluky se jmenuje <strong>Toulavá smečka</strong>, pro starší kluky <strong>Bárka</strong> a pro kluky od 16 let výše <strong>roverská VěTeV</strong>. Poslední „neoficiální“ palubou je <strong>Klub 11. oddílu</strong>, který sdružuje ke společným výletům z reality již bývalé vedoucí oddílu.
          </p>
          
          <!-- Oddílové pilíře -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="p-4 rounded-2xl bg-white border border-slate-200 shadow-sm flex items-start gap-3">
              <div class="w-10 h-10 rounded-xl bg-yellow-400/20 text-yellow-700 flex items-center justify-center shrink-0 text-lg">
                <i class="fa-solid fa-flag"></i>
              </div>
              <div>
                <h4 class="font-bold text-slate-900 text-sm font-heading">Černo-žlutá vlajka</h4>
                <p class="text-xs text-slate-500 mt-0.5">Naše oddílové barvy a žluté šátky symbolizují bratrství a soudržnost.</p>
              </div>
            </div>

            <div class="p-4 rounded-2xl bg-white border border-slate-200 shadow-sm flex items-start gap-3">
              <div class="w-10 h-10 rounded-xl bg-sky-100 text-brand-sky flex items-center justify-center shrink-0 text-lg">
                <i class="fa-solid fa-users-viewfinder"></i>
              </div>
              <div>
                <h4 class="font-bold text-slate-900 text-sm font-heading">Posádkový systém</h4>
                <p class="text-xs text-slate-500 mt-0.5">Posádky 6–8 chlapců, kde se mladší učí od starších samostatnosti a fair-play.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5 relative">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white aspect-[4/3] group">
            <img src="foto_3.jpg" alt="Skauti v loděnici na řece" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex items-end p-6">
              <div class="text-white">
                <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider">Loděnice Valcha</span>
                <p class="text-sm font-semibold text-slate-100">Pravidelné schůzky každou středu a čtvrtek</p>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Detailní rozpad 4 palub -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
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
  <!-- SEKCE: TERMÍNOVNÍK (Kalendář akcí Bárky i Toulavé smečky s přepínáním) -->
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

      <!-- FILTER TABS -->
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
      {"".join([f'''
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
      ''' for ev in TERMINOVNIK_BARKA])}
    </div>

    <!-- TERMINOVNIK GRID VLCATA (HIDDEN BY DEFAULT) -->
    <div id="gridVlcata" class="hidden grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {"".join([f'''
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
      ''' for ev in TERMINOVNIK_VLCATA])}
    </div>
  </section>

  <!-- ======================================================================== -->
  <!-- SEKCE: AKTUALITY Z LODĚNICE (Reálné články z blogu, 3 Jezy, VVLnZ) -->
  <!-- ======================================================================== -->
  <section id="aktuality" class="py-20 bg-slate-50 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
        <div>
          <span class="text-brand-sky font-bold text-xs uppercase tracking-wider">Z kroniky a dění v oddíle</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy font-heading mt-1">
            Aktuality z loděnice &amp; výprav
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
        {"".join([f'''
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
        ''' for post in BLOG_POSTS])}
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
  <!-- SEKCE: LODĚNICE VALCHA -->
  <!-- ======================================================================== -->
  <section id="klubovna" class="py-20 bg-slate-900 text-white relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-6 space-y-5">
          <span class="text-yellow-400 font-bold text-xs uppercase tracking-wider">Naše zázemí na řece Malši</span>
          <h2 class="text-3xl sm:text-4xl font-black font-heading">
            Loděnice Valcha v Českých Budějovicích
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Naše domovská loděnice se nachází v klidné lokalitě u vody nedaleko Malého jezu. Disponujeme hangárem pro oddílové pramice P550, kanoe a plachetnice, vytápěnými klubovnami pro zimní schůzky, dílnou i velkou travnatou loukou pro hry.
          </p>
          <div class="space-y-2 text-xs text-slate-300">
            <div class="flex items-center gap-2"><i class="fa-solid fa-location-dot text-yellow-400"></i> <strong>Adresa:</strong> Loděnice Valcha, České Budějovice</div>
            <div class="flex items-center gap-2"><i class="fa-solid fa-bus text-yellow-400"></i> <strong>Doprava:</strong> Zastávka MHD v docházkové vzdálenosti</div>
          </div>
        </div>

        <div class="lg:col-span-6 grid grid-cols-2 gap-4">
          <div class="rounded-2xl overflow-hidden aspect-[4/3] shadow-lg">
            <img src="barka_1.jpg" alt="Loděnice Valcha" class="w-full h-full object-cover">
          </div>
          <div class="rounded-2xl overflow-hidden aspect-[4/3] shadow-lg">
            <img src="barka_2.jpg" alt="Skauti v loděnici" class="w-full h-full object-cover">
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
          První tři schůzky jsou nezávazné a zdarma – přijďte se podívat do loděnice na Valše!
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
            Kapitán oddílu • Vůdce
          </span>
          <h3 class="text-xl font-extrabold text-slate-900 font-heading">Martin Hájek</h3>
          <p class="text-xs font-black text-brand-sky">Přezdívka: Hopík</p>
          
          <p class="text-xs text-slate-500 mt-3 px-2 leading-relaxed">
            Celkové vedení oddílu, tábory, oficiální záležitosti, nábor a komunikace se střediskem Vavéha.
          </p>
        </div>

        <div class="mt-6 pt-6 border-t border-slate-100 space-y-2 text-xs font-semibold">
          <a href="tel:733238774" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 text-brand-navy transition-all">
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
          <h3 class="text-xl font-extrabold text-slate-900 font-heading">David Hacker</h3>
          <p class="text-xs font-black text-amber-700">Přezdívka: Knedlík</p>
          
          <p class="text-xs text-slate-500 mt-3 px-2 leading-relaxed">
            Hlavní vedoucí Toulavé smečky (vlčata 6–10 let), příprava schůzek a víkendových výprav.
          </p>
        </div>

        <div class="mt-6 pt-6 border-t border-slate-100 space-y-2 text-xs font-semibold">
          <a href="mailto:knedlik@jedenactka.eu" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 text-brand-navy transition-all">
            <i class="fa-solid fa-envelope text-amber-600"></i>
            <span>knedlik@jedenactka.eu</span>
          </a>
          <span class="block text-[11px] text-slate-400 py-1">Garant schůzek viz sekce Pro rodiče</span>
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
          <h3 class="text-xl font-extrabold text-slate-900 font-heading">Vít Veltrubský</h3>
          <p class="text-xs font-black text-brand-sky">Přezdívka: Vodník / Slon</p>
          
          <p class="text-xs text-slate-500 mt-3 px-2 leading-relaxed">
            Důstojník skautské paluby Bárka (chlapci 11–15 let), vodácký výcvik, putovní výpravy na vodě a akce Bárky.
          </p>
        </div>

        <div class="mt-6 pt-6 border-t border-slate-100 space-y-2 text-xs font-semibold">
          <a href="mailto:vodnik@jedenactka.eu" class="flex items-center justify-center gap-2 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 text-brand-navy transition-all">
            <i class="fa-solid fa-envelope text-brand-sky"></i>
            <span>vodnik@jedenactka.eu</span>
          </a>
          <span class="block text-[11px] text-slate-400 py-1">Garanti schůzek Werran & Franta</span>
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
        <span class="w-4 h-3 rounded-xs border border-white/40" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);"></span>
        <span class="text-slate-300 font-bold">11. oddíl vodních skautů České Budějovice</span>
      </div>
      <p class="text-slate-500 text-center sm:text-right">
        Registrováno u Junák – český skaut, 4. středisko VAVÉHA České Budějovice.
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
  </script>
</body>
</html>
"""
    with open('verzeA/index.html', 'w', encoding='utf-8') as f:
        f.write(html_a)
    print("Wrote verzeA/index.html")

    # Generate verzeA/vedeni.html with IDENTICAL top bar & navbar
    # Render all 34 leader cards
    leader_cards = []
    for i, l in enumerate(leaders):
        raw = l.get('raw', [])
        name = l.get('name', '')
        avatar = f"avatars/avatar_{i+1}.jpg" if (i+1) <= 33 else "avatars/avatar_1.jpg"
        
        # Determine category
        cat = "all"
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

        # extract nick
        nick = ""
        for item in raw:
            if "–" in item and len(item.replace("–", "").strip()) > 0 and not any(k in item.lower() for k in ['kapitán', 'vůdce', 'důstojník', 'lodivod', 'garant']):
                nick = item.replace("–", "").strip()
                break
        if not nick and len(raw) > 2 and "–" in raw[1]:
            nick = raw[2].strip()

        # extract role
        role = ""
        for item in raw:
            if any(k in item.lower() for k in ['kapitán', 'vůdce', 'důstojník', 'garant', 'lodivod', 'zdravotník']):
                role = item.replace("–", "").strip()
                break
        if not role: role = "Lodivod"

        # extract phone & email
        phone = ""
        email = ""
        for item in raw:
            if "tel." in item.lower() or re.search(r'\d{3}\s*\d{3}\s*\d{3}', item):
                phone = item.replace("tel.:", "").replace("tel.", "").strip()
            if "@" in item:
                email = item.strip()

        # extra info
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
            contacts_html += f'<a href="tel:{phone.replace(" ", "")}" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-slate-800 text-xs font-semibold border border-slate-200/80 transition-colors"><i class="fa-solid fa-phone text-brand-sky"></i> {phone}</a> '
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
                <h3 class="text-base font-black text-slate-900 font-heading leading-tight">{h(name)}</h3>
                {f'<p class="text-xs font-black text-brand-sky">{h(nick)}</p>' if nick else ''}
                <p class="text-xs font-semibold text-slate-500 mt-0.5">{h(role)}</p>
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

    html_vedeni_a = f"""<!DOCTYPE html>
<html lang="cs" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vedení oddílu | 11. oddíl vodních skautů České Budějovice</title>
  
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
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
  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
  </style>
</head>
<body class="bg-[#F8FAFC] text-slate-800 antialiased selection:bg-brand-sky selection:text-white">

  {get_navbar(is_subpage=True)}

  <!-- HERO HEADER -->
  <section class="bg-gradient-to-br from-brand-navyDark via-brand-navy to-brand-blue text-white py-14 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto text-center space-y-4">
      <span class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-yellow-400 text-slate-950 uppercase tracking-wider">
        Tým za kormidlem Jedenáctky
      </span>
      <h1 class="text-3xl sm:text-5xl font-black font-heading tracking-tight">
        Kompletní vedení oddílu &amp; lodivodi
      </h1>
      <p class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto leading-relaxed">
        Náš oddíl stojí na desítkách obětavých dobrovolníků, vůdců, garantů schůzek a lodivodů, kteří pro kluky připravují program, tábory a výpravy.
      </p>

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
        <span class="w-4 h-3 rounded-xs border border-white/40" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);"></span>
        <span class="text-slate-300 font-bold">11. oddíl vodních skautů České Budějovice</span>
      </div>
      <p class="text-slate-500 text-center sm:text-right">
        Registrováno u Junák – český skaut, 4. středisko VAVÉHA České Budějovice.
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
  </script>
</body>
</html>
"""
    with open('verzeA/vedeni.html', 'w', encoding='utf-8') as f:
        f.write(html_vedeni_a)
    print("Wrote verzeA/vedeni.html")

build_verze_a()
