# -*- coding: utf-8 -*-
import re

print("=== Updating build_verze_a.py ===")
with open('build_verze_a.py', 'r', encoding='utf-8') as f:
    va = f.read()

# 1. Navbar in verze A
# Replace top bar text
va = va.replace('v loděnici Valcha</span>', 'na Valši</span>')

# Replace brand logo & remove Junák / flag
old_brand_a = """        <!-- LOGO & BRAND -->
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
        </a>"""

new_brand_a = """        <!-- LOGO & BRAND -->
        <a href="{prefix}#" class="flex items-center gap-3.5 group">
          <div class="h-12 w-12 sm:h-14 sm:w-14 rounded-2xl bg-slate-900/5 p-1 flex items-center justify-center group-hover:scale-105 transition-transform duration-200 shrink-0">
            <img src="{prefix}logo_emblem.png" alt="11. oddíl vodních skautů" class="h-full w-full object-contain filter drop-shadow-xs">
          </div>
          <div>
            <span class="block text-xl font-black tracking-tight text-brand-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-xs font-semibold text-slate-500">České Budějovice • Valcha</span>
          </div>
        </a>"""

if old_brand_a in va:
    va = va.replace(old_brand_a, new_brand_a)
    print("  [OK] verze A brand updated with real logo, no Junák text/flag")
else:
    print("  [FAIL] verze A old brand not matched!")

# Nav items in verze A
va = va.replace('>Loděnice</a>', '>Valcha</a>')
va = va.replace('Aktuality z loděnice', 'Aktuality z oddílu')
va = va.replace('Loděnice Valcha\n        </a>', 'Základna Valcha\n        </a>')
va = va.replace('Loděnice Valcha</a>', 'Základna Valcha</a>')
va = va.replace('Loděnice Valcha České Budějovice • V případě', 'Základna Valcha České Budějovice • V případě')
va = va.replace('České Budějovice • Loděnice Valcha', 'České Budějovice • Valcha')
va = va.replace('v loděnici na řece', 'na základně Valcha')
va = va.replace('alt="Skauti v loděnici na řece"', 'alt="Skauti na základně Valcha"')
va = va.replace('alt="Skauti v loděnici na řece" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">\n            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex items-end p-6">\n              <div class="text-white">\n                <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider">Loděnice Valcha</span>', 'alt="Skauti na základně Valcha" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">\n            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex items-end p-6">\n              <div class="text-white">\n                <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider">Základna Valcha</span>')

# Valcha section texts
va = va.replace('<!-- SEKCE: LODĚNICE VALCHA -->', '<!-- SEKCE: ZÁKLADNA VALCHA -->')
va = va.replace('Loděnice Valcha v Českých Budějovicích', 'Základna Valcha v Českých Budějovicích')
va = va.replace('Naše domovská loděnice se nachází v klidné lokalitě u vody nedaleko Malého jezu. Disponujeme hangárem pro oddílové pramice P550, kanoe a plachetnice, vytápěnými klubovnami pro zimní schůzky, dílnou i velkou travnatou loukou pro hry.',
                'Naše domovská základna Valcha se nachází v klidné lokalitě u vody nedaleko Malého jezu. Nejde pouze o loděnici – areál Valchy tvoří vytápěné klubovny pro celoroční schůzky, hangár pro oddílové pramice P550, kanoe i plachetnice, dílna a velká travnatá louka pro hry.')
va = va.replace('<strong>Adresa:</strong> Loděnice Valcha, České Budějovice', '<strong>Adresa:</strong> Základna Valcha, České Budějovice')
va = va.replace('title="Mapa Loděnice Valcha České Budějovice"', 'title="Mapa základny Valcha České Budějovice"')
va = va.replace('<span>Loděnice Valcha (11. oddíl)</span>', '<span>Základna Valcha (11. oddíl)</span>')
va = va.replace('Kudy k nám do loděnice', 'Kudy k nám na Valchu')
va = va.replace('Přímo u loděnice vede bezpečná páteřní cyklostezka podél řeky. Před loděnicí je prostor pro bezpečné zamčení kol.',
                'Přímo kolem Valchy vede bezpečná páteřní cyklostezka podél řeky. Před základnou je prostor pro bezpečné zamčení kol.')
va = va.replace('K samotnému břehu loděnice je pěší zóna a zákaz vjezdu aut.', 'K samotné základně Valcha je pěší zóna a zákaz vjezdu aut.')
va = va.replace('přijďte se podívat do loděnice na Valše!', 'přijďte se podívat na Valchu!')
va = va.replace('Aktuality z loděnice &amp; výprav', 'Aktuality z oddílu &amp; výprav')

# Initial Hero image & tag in verze A
va = va.replace('<img id="heroImg" src="foto_1.jpg"', '<img id="heroImg" src="zonerama_2.jpg"')
va = va.replace('<span id="heroTag" class="text-xs font-bold text-yellow-300 uppercase tracking-wider">Trénink na Malši</span>', '<span id="heroTag" class="text-xs font-bold text-yellow-300 uppercase tracking-wider">Společná voda 2026</span>')
va = va.replace('<span id="heroSub" class="text-[11px] text-slate-400 font-medium">Pramice P550</span>', '<span id="heroSub" class="text-[11px] text-slate-400 font-medium">Sjíždění šlajsny na kánoi</span>')
va = va.replace('<p id="heroTitle" class="text-xs font-semibold text-slate-200 mt-1 leading-snug">Trénink posádek na řece Malši a Vltavě</p>', '<p id="heroTitle" class="text-xs font-semibold text-slate-200 mt-1 leading-snug">Vodácká dobrodružství & peřeje na řece</p>')

# Hero rotator array in verze A
old_hero_arr_a = """    const heroPhotos = [
      {{ src: "foto_1.jpg", tag: "Trénink na Malši", sub: "Pramice P550", title: "Trénink posádek na řece Malši a Vltavě" }},
      {{ src: "foto_3.jpg", tag: "Loděnice Valcha", sub: "Domovský přístav", title: "Život a schůzky na naší loděnici u Malého jezu" }},
      {{ src: "barka_2.jpg", tag: "Vlčata & Skauti", sub: "Chlapecký oddíl", title: "Společná parta, vodácký kroj a tradice Jedenáctky" }},
      {{ src: "upload_4.png", tag: "Expedice & Příroda", sub: "Víkendovky", title: "Pravidelné výpravy do přírody s batohy a pod celtu" }},
      {{ src: "foto_2.jpg", tag: "Toulavá smečka", sub: "Terčino údolí", title: "Zahajovací výprava a pasování vlčat do skautské Bárky" }},
      {{ src: "upload_1.jpg", tag: "Víkendová výprava", sub: "Hry v lese", title: "Dobrodružství a hry v jihočeské přírodě" }},
      {{ src: "foto_6.jpg", tag: "Vodácký výcvik", sub: "Řeka Malše", title: "Kormidlování, záchrana na vodě a týmová spolupráce" }}
    ];"""

new_hero_arr_a = """    // Fotografie čerpané z oddílové fotogalerie Zonerama za poslední rok
    const heroPhotos = [
      {{ src: "zonerama_2.jpg", tag: "Společná voda 2026", sub: "Sjíždění šlajsny na kánoi", title: "Vodácká dobrodružství & peřeje na řece" }},
      {{ src: "zonerama_1.jpg", tag: "Slalomový kanál 2026", sub: "České Vrbné • divoká voda", title: "Zázemí na vodě & trénink pádlování a stability" }},
      {{ src: "zonerama_3.jpg", tag: "3 Jezy Praha 2025", sub: "Závod Napříč Prahou", title: "Reprezentace posádky 11. oddílu na prestižním závodě" }},
      {{ src: "zonerama_5.jpg", tag: "Expedice na vodě", sub: "Společná výprava 11. oddílu", title: "Příroda, ticho a putování po jihočeských řekách" }},
      {{ src: "zonerama_valcha.jpg", tag: "Život na Valši", sub: "Klubovna a základna 11. oddílu", title: "Týmové hry v klubovně a celoroční program schůzek" }},
      {{ src: "zonerama_camp.jpg", tag: "Tábor Labská Stráň 2026", sub: "Lezení v pískovcích", title: "Čtrnáct dní nezapomenutelných zážitků a výzev v přírodě" }},
      {{ src: "zonerama_6.jpg", tag: "Kajaky v peřejích", sub: "České Vrbné", title: "Slalomový trénink mezi brankami na divoké vodě" }}
    ];"""

if old_hero_arr_a in va:
    va = va.replace(old_hero_arr_a, new_hero_arr_a)
    print("  [OK] verze A heroPhotos updated with Zonerama photos")
else:
    print("  [FAIL] verze A old_hero_arr_a not matched!")

# Lodenice photos array in verze A
old_lodenice_arr_a = """    const lodenicePhotos = [
      {{ src: "foto_3.jpg", title: "Loděnice Valcha na břehu řeky Malše", tag: "Zázemí u řeky" }},
      {{ src: "foto_6.jpg", title: "Molo a trénink posádek na vodě", tag: "Vodácký výcvik" }},
      {{ src: "barka_1.jpg", title: "Lodní hangár a budova loděnice", tag: "Lodní hangár" }},
      {{ src: "barka_2.jpg", title: "Klubovny a travnaté prostranství", tag: "Zázemí pro hry" }},
      {{ src: "upload_2.png", title: "Pramice P550 a plachetnice Jedenáctky", tag: "Flotila lodí" }},
      {{ src: "upload_1.jpg", title: "Areál loděnice v přírodě u Malého jezu", tag: "Klidná lokalita" }},
      {{ src: "foto_1.jpg", title: "Vyplutí posádky na řeku z loděnice", tag: "Trénink na Malši" }},
      {{ src: "upload_4.png", title: "Příprava na výpravu z loděnice", tag: "Život v oddíle" }}
    ];"""

new_lodenice_arr_a = """    const lodenicePhotos = [
      {{ src: "zonerama_valcha.jpg", title: "Klubovny a život na Valši při schůzkách", tag: "Základna Valcha" }},
      {{ src: "zonerama_1.jpg", title: "Trénink na vodě a přístaviště u řeky", tag: "Vodácký výcvik" }},
      {{ src: "foto_3.jpg", title: "Základna Valcha na břehu řeky Malše", tag: "Zázemí u řeky" }},
      {{ src: "foto_6.jpg", title: "Molo a trénink posádek na vodě", tag: "Vodácký výcvik" }},
      {{ src: "barka_1.jpg", title: "Lodní hangár a budovy základny", tag: "Lodní hangár" }},
      {{ src: "barka_2.jpg", title: "Klubovny a travnaté prostranství", tag: "Zázemí pro hry" }},
      {{ src: "upload_2.png", title: "Pramice P550 a plachetnice Jedenáctky", tag: "Flotila lodí" }},
      {{ src: "upload_1.jpg", title: "Areál základny v přírodě u Malého jezu", tag: "Klidná lokalita" }}
    ];"""

if old_lodenice_arr_a in va:
    va = va.replace(old_lodenice_arr_a, new_lodenice_arr_a)
    print("  [OK] verze A lodenicePhotos updated")
else:
    print("  [FAIL] verze A old_lodenice_arr_a not matched!")

# Initial lodenice image
va = va.replace('src="foto_3.jpg" alt="Loděnice Valcha"', 'src="zonerama_valcha.jpg" alt="Základna Valcha"')
va = va.replace('Loděnice Valcha na břehu Malše', 'Klubovny a život na Valši při schůzkách')

# Footer in verze A
old_footer_a = """      <div class="flex items-center gap-3">
        <span class="w-4 h-3 rounded-xs border border-white/40" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);"></span>
        <span class="text-slate-300 font-bold">11. oddíl vodních skautů České Budějovice</span>
      </div>"""

new_footer_a = """      <div class="flex items-center gap-3">
        <img src="{prefix}logo_emblem.png" alt="11. oddíl vodních skautů" class="h-8 w-auto object-contain brightness-110">
        <span class="text-slate-300 font-bold">11. oddíl vodních skautů České Budějovice</span>
      </div>"""

va = va.replace(old_footer_a, new_footer_a)
print("  [OK] verze A footer updated with real logo emblem")

# Mobile menu toggle & close on link click in verze A
old_toggle_a = """    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenuBtn && mobileMenu) {{
      mobileMenuBtn.addEventListener('click', () => {{
        mobileMenu.classList.toggle('hidden');
      }});
    }}"""

new_toggle_a = """    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
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
    }}"""

va = va.replace(old_toggle_a, new_toggle_a)
print("  [OK] verze A mobile menu auto-close updated")

with open('build_verze_a.py', 'w', encoding='utf-8') as f:
    f.write(va)

print("\n=== Updating build_verze_b.py ===")
with open('build_verze_b.py', 'r', encoding='utf-8') as f:
    vb = f.read()

# 1. Navbar in verze B
vb = vb.replace('v loděnici Valcha</span>', 'na Valši</span>')

# Replace brand logo & remove Junák / flag
old_brand_b = """        <!-- LOGO & BRAND -->
        <a href="{prefix}#" class="flex items-center gap-3 group">
          <div class="w-12 h-12 rounded-xl bg-scout-blue text-white flex items-center justify-center text-2xl shadow-md group-hover:bg-scout-navy transition-colors relative overflow-hidden shrink-0">
            <div class="absolute -top-3 -right-3 w-7 h-7 bg-yellow-400 rotate-45 pointer-events-none"></div>
            <i class="fa-solid fa-anchor text-yellow-300 relative z-10"></i>
          </div>
          <div>
            <div class="flex items-center gap-1.5">
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Junák – český skaut</span>
              <span class="inline-flex w-3 h-2 rounded-xs border border-slate-300" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);" title="Černo-žlutá vlajka 11. oddílu"></span>
            </div>
            <span class="block text-xl font-bold tracking-tight text-scout-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-xs font-semibold text-scout-blue -mt-0.5">České Budějovice • Loděnice Valcha</span>
          </div>
        </a>"""

new_brand_b = """        <!-- LOGO & BRAND -->
        <a href="{prefix}#" class="flex items-center gap-3.5 group">
          <div class="h-12 w-12 sm:h-14 sm:w-14 rounded-xl bg-slate-100 p-1 flex items-center justify-center group-hover:bg-slate-200 transition-colors shrink-0">
            <img src="{prefix}logo_emblem.png" alt="11. oddíl vodních skautů" class="h-full w-full object-contain filter drop-shadow-xs">
          </div>
          <div>
            <span class="block text-xl font-bold tracking-tight text-scout-navy font-heading">11. oddíl vodních skautů</span>
            <span class="block text-xs font-semibold text-scout-blue">České Budějovice • Valcha</span>
          </div>
        </a>"""

if old_brand_b in vb:
    vb = vb.replace(old_brand_b, new_brand_b)
    print("  [OK] verze B brand updated with real logo, no Junák text/flag")
else:
    print("  [FAIL] verze B old brand not matched!")

# Nav items in verze B
vb = vb.replace('>Loděnice</a>', '>Valcha</a>')
vb = vb.replace('Aktuality z loděnice', 'Aktuality z oddílu')
vb = vb.replace('>Loděnice Valcha</a>', '>Základna Valcha</a>')
vb = vb.replace('České Budějovice • Loděnice Valcha', 'České Budějovice • Valcha')
vb = vb.replace('v loděnici Valcha', 'na Valši')
vb = vb.replace('na vodě a na loděnici', 'na vodě a na Valši')
vb = vb.replace('Sídlíme na loděnici Valcha', 'Sídlíme na základně Valcha')

# Valcha section texts in verze B
vb = vb.replace('<!-- SEKCE: LODĚNICE -->', '<!-- SEKCE: ZÁKLADNA VALCHA -->')
vb = vb.replace('Loděnice Valcha na řece Malši', 'Základna Valcha na řece Malši')
vb = vb.replace('Vlastní loděnice s hangárem na lodě, klubovnami, dílnou a přístupem k vodě u Malého jezu v Českých Budějovicích.',
                'Vlastní základna Valcha s hangárem na lodě, klubovnami, travnatou loukou, dílnou a přístupem k vodě u Malého jezu v Českých Budějovicích.')
vb = vb.replace('title="Mapa Loděnice Valcha České Budějovice"', 'title="Mapa základny Valcha České Budějovice"')
vb = vb.replace('<span>Loděnice Valcha (11. oddíl)</span>', '<span>Základna Valcha (11. oddíl)</span>')
vb = vb.replace('Kudy k nám do loděnice', 'Kudy k nám na Valchu')
vb = vb.replace('Cyklostezka vede přímo před loděnicí. K dispozici stojany na kola.',
                'Cyklostezka vede přímo kolem základny Valcha. K dispozici jsou stojany na kola.')
vb = vb.replace('K samotné loděnici je pěší zóna a zákaz vjezdu aut.', 'K samotné základně Valcha je pěší zóna a zákaz vjezdu aut.')
vb = vb.replace('Aktuality z loděnice &amp; výprav', 'Aktuality z oddílu &amp; výprav')

# Initial Hero image & tag in verze B
vb = vb.replace('<img id="heroImgB" src="foto_1.jpg"', '<img id="heroImgB" src="zonerama_2.jpg"')
vb = vb.replace('<span id="heroTagB" class="text-xs font-bold text-scout-blue uppercase tracking-wider">Trénink na Malši</span>', '<span id="heroTagB" class="text-xs font-bold text-scout-blue uppercase tracking-wider">Společná voda 2026</span>')
vb = vb.replace('<p id="heroTitleB" class="text-xs font-bold text-slate-800 mt-1 leading-snug">Trénink posádek na řece Malši a Vltavě</p>', '<p id="heroTitleB" class="text-xs font-bold text-slate-800 mt-1 leading-snug">Vodácká dobrodružství & peřeje na řece</p>')

# Hero rotator array in verze B
old_hero_arr_b = """    const heroPhotosB = [
      {{ src: "foto_1.jpg", tag: "Trénink na Malši", title: "Trénink posádek na řece Malši a Vltavě" }},
      {{ src: "foto_3.jpg", tag: "Loděnice Valcha", title: "Život a schůzky na naší loděnici u Malého jezu" }},
      {{ src: "barka_2.jpg", tag: "Vlčata & Skauti", title: "Společná parta, vodácký kroj a tradice Jedenáctky" }},
      {{ src: "upload_4.png", tag: "Expedice & Příroda", title: "Pravidelné výpravy do přírody s batohy a pod celtu" }},
      {{ src: "foto_2.jpg", tag: "Toulavá smečka", title: "Zahajovací výprava a pasování vlčat do skautské Bárky" }},
      {{ src: "upload_1.jpg", tag: "Víkendová výprava", title: "Dobrodružství a hry v jihočeské přírodě" }},
      {{ src: "foto_6.jpg", tag: "Vodácký výcvik", title: "Kormidlování, záchrana na vodě a týmová spolupráce" }}
    ];"""

new_hero_arr_b = """    // Fotografie čerpané z oddílové fotogalerie Zonerama za poslední rok
    const heroPhotosB = [
      {{ src: "zonerama_2.jpg", tag: "Společná voda 2026", title: "Vodácká dobrodružství & sjíždění šlajsny na kánoi" }},
      {{ src: "zonerama_1.jpg", tag: "Slalomový kanál 2026", title: "České Vrbné • trénink na divoké vodě a výcvik pádlování" }},
      {{ src: "zonerama_3.jpg", tag: "3 Jezy Praha 2025", title: "Posádka 11. oddílu na prestižním závodě Napříč Prahou" }},
      {{ src: "zonerama_5.jpg", tag: "Expedice na vodě", title: "Příroda a putování po jihočeských řekách" }},
      {{ src: "zonerama_valcha.jpg", tag: "Život na Valši", title: "Týmové hry v klubovně a celoroční program schůzek" }},
      {{ src: "zonerama_camp.jpg", tag: "Tábor Labská Stráň 2026", title: "Lezení ve skalách a táborové výzvy v přírodě" }},
      {{ src: "zonerama_6.jpg", tag: "Kajaky v peřejích", title: "Slalomový trénink mezi brankami na divoké vodě" }}
    ];"""

if old_hero_arr_b in vb:
    vb = vb.replace(old_hero_arr_b, new_hero_arr_b)
    print("  [OK] verze B heroPhotosB updated with Zonerama photos")
else:
    print("  [FAIL] verze B old_hero_arr_b not matched!")

# Lodenice photos array in verze B
old_lodenice_arr_b = """    const lodenicePhotosB = [
      {{ src: "foto_3.jpg", title: "Loděnice Valcha na břehu řeky Malše", tag: "Zázemí u řeky" }},
      {{ src: "foto_6.jpg", title: "Molo a trénink posádek na vodě", tag: "Vodácký výcvik" }},
      {{ src: "barka_1.jpg", title: "Lodní hangár a budova loděnice", tag: "Lodní hangár" }},
      {{ src: "barka_2.jpg", title: "Klubovny a travnaté prostranství", tag: "Zázemí pro hry" }},
      {{ src: "upload_2.png", title: "Pramice P550 a plachetnice Jedenáctky", tag: "Flotila lodí" }},
      {{ src: "upload_1.jpg", title: "Areál loděnice v přírodě u Malého jezu", tag: "Klidná lokalita" }},
      {{ src: "foto_1.jpg", title: "Vyplutí posádky na řeku z loděnice", tag: "Trénink na Malši" }},
      {{ src: "upload_4.png", title: "Příprava na výpravu z loděnice", tag: "Život v oddíle" }}
    ];"""

new_lodenice_arr_b = """    const lodenicePhotosB = [
      {{ src: "zonerama_valcha.jpg", title: "Klubovny a život na Valši při schůzkách", tag: "Základna Valcha" }},
      {{ src: "zonerama_1.jpg", title: "Trénink na vodě a přístaviště u řeky", tag: "Vodácký výcvik" }},
      {{ src: "foto_3.jpg", title: "Základna Valcha na břehu řeky Malše", tag: "Zázemí u řeky" }},
      {{ src: "foto_6.jpg", title: "Molo a trénink posádek na vodě", tag: "Vodácký výcvik" }},
      {{ src: "barka_1.jpg", title: "Lodní hangár a budova základny", tag: "Lodní hangár" }},
      {{ src: "barka_2.jpg", title: "Klubovny a travnaté prostranství", tag: "Zázemí pro hry" }},
      {{ src: "upload_2.png", title: "Pramice P550 a plachetnice Jedenáctky", tag: "Flotila lodí" }},
      {{ src: "upload_1.jpg", title: "Areál základny v přírodě u Malého jezu", tag: "Klidná lokalita" }}
    ];"""

if old_lodenice_arr_b in vb:
    vb = vb.replace(old_lodenice_arr_b, new_lodenice_arr_b)
    print("  [OK] verze B lodenicePhotosB updated")
else:
    print("  [FAIL] verze B old_lodenice_arr_b not matched!")

# Initial lodenice image in verze B
vb = vb.replace('id="lodeniceImg1B" src="foto_3.jpg" alt="Loděnice Valcha"', 'id="lodeniceImg1B" src="zonerama_valcha.jpg" alt="Základna Valcha"')
vb = vb.replace('id="lodeniceImg2B" src="foto_6.jpg" alt="Loděnice Valcha"', 'id="lodeniceImg2B" src="zonerama_1.jpg" alt="Vodácký trénink"')
vb = vb.replace('<p id="lodeniceTitle1B" class="text-xs font-bold text-white leading-tight">Loděnice Valcha na břehu Malše</p>', '<p id="lodeniceTitle1B" class="text-xs font-bold text-white leading-tight">Klubovny a život na Valši při schůzkách</p>')

# Footer in verze B
old_footer_b = """      <div class="flex items-center gap-2">
        <span class="w-3.5 h-2.5 inline-block rounded-xs border border-white/40 shadow-xs" style="background: linear-gradient(135deg, #000 50%, #facc15 50%);"></span>
        <span class="font-bold text-white">11. oddíl vodních skautů České Budějovice</span>
      </div>"""

new_footer_b = """      <div class="flex items-center gap-2">
        <img src="{prefix}logo_emblem.png" alt="11. oddíl vodních skautů" class="h-7 w-auto object-contain brightness-110">
        <span class="font-bold text-white">11. oddíl vodních skautů České Budějovice</span>
      </div>"""

vb = vb.replace(old_footer_b, new_footer_b)
print("  [OK] verze B footer updated with real logo emblem")

# Mobile menu toggle & close on link click in verze B
old_toggle_b = """    const mobileMenuBtnB = document.getElementById('mobileMenuBtnB');
    const mobileMenuB = document.getElementById('mobileMenuB');
    if (mobileMenuBtnB && mobileMenuB) {{
      mobileMenuBtnB.addEventListener('click', () => {{
        mobileMenuB.classList.toggle('hidden');
      }});
    }}"""

new_toggle_b = """    const mobileMenuBtnB = document.getElementById('mobileMenuBtnB');
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
    }}"""

vb = vb.replace(old_toggle_b, new_toggle_b)
print("  [OK] verze B mobile menu auto-close updated")

with open('build_verze_b.py', 'w', encoding='utf-8') as f:
    f.write(vb)

print("\n=== Done updating builder scripts! ===")
