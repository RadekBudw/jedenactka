#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generátor WordPress šablony pro 11. oddíl vodních skautů České Budějovice.
Převede statickou verzi (Varianta A nebo B) na kompletní, samostatnou WordPress šablonu
a zabalí ji do instalačního archivu jedenactka-theme.zip.

Obsahuje:
- front-page.php (hlavní responzivní stránka oddílu)
- page-vedeni.php (stránka s 34 vedoucími oddílu, filtry a kontakty)
- page.php (univerzální šablona pro stávající podstránky jako /vlcacke-fotky/ a /oddil/archiv-akci/)
- single.php (šablona pro jednotlivé aktuality/články)
- index.php (fallback šablona)
- functions.php (automatické nastavení, podpora title-tagu, Gutenberg stylů a stránky vedení)
- plnou podporu wp_head() a wp_footer() pro pluginy (např. Google Drive Galerie, hesla)
"""

import os
import sys
import re
import shutil
import zipfile
from build_data import get_app_version

# Zajištění UTF-8 výstupu na Windows konzoli
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

THEME_SLUG = "jedenactka-theme"
THEME_NAME = "11. oddíl vodních skautů ČB - Moderní flotila"
THEME_DIR = os.path.join(os.path.dirname(__file__), "wp_theme_build")
OUTPUT_ZIP = os.path.join(os.path.dirname(__file__), "jedenactka-theme.zip")

# CSS pravidla pro WordPress Gutenberg bloky, heslem chráněné stránky a obecný obsah
WP_CONTENT_STYLES = """
    /* ========================================================= */
    /* WORDPRESS OBSAH, GUTENBERG BLOKY A FORMULÁŘ PRO HESLO    */
    /* ========================================================= */
    .entry-content { font-size: 1rem; line-height: 1.75; }
    .entry-content p { margin-bottom: 1.25rem; }
    .entry-content h1, .entry-content h2, .entry-content h3, .entry-content h4 {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      color: #0f172a;
      margin-top: 2rem;
      margin-bottom: 1rem;
    }
    .dark .entry-content h1, .dark .entry-content h2, .dark .entry-content h3, .dark .entry-content h4 {
      color: #ffffff !important;
    }
    .entry-content h2 { font-size: 1.625rem; }
    .entry-content h3 { font-size: 1.25rem; }
    .entry-content ul { list-style-type: disc; margin-left: 1.75rem; margin-bottom: 1.25rem; }
    .entry-content ol { list-style-type: decimal; margin-left: 1.75rem; margin-bottom: 1.25rem; }
    .entry-content li { margin-bottom: 0.35rem; }
    .entry-content a { color: #0284c7; text-decoration: underline; font-weight: 600; }
    .entry-content a:hover { color: #0369a1; }
    .dark .entry-content a { color: #38bdf8; }
    .dark .entry-content a:hover { color: #facc15; }
    .entry-content img { border-radius: 1rem; max-width: 100%; height: auto; margin: 1.5rem 0; }
    .entry-content table { width: 100%; border-collapse: collapse; margin-bottom: 1.5rem; }
    .entry-content th, .entry-content td { padding: 0.75rem 1rem; border: 1px solid #e2e8f0; text-align: left; }
    .dark .entry-content th, .dark .entry-content td { border-color: #334155; }
    .entry-content th { background-color: #f8fafc; font-weight: 700; }
    .dark .entry-content th { background-color: #1e293b; color: #ffffff; }

    /* Gutenberg Button Blocks (např. stažení plakátků v Archivu akcí) */
    .entry-content .wp-block-button { margin-bottom: 1rem; }
    .entry-content .wp-block-button__link {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.65rem 1.25rem;
      border-radius: 0.75rem;
      font-weight: 700;
      font-size: 0.875rem;
      background: #0284c7;
      color: #ffffff !important;
      text-decoration: none !important;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      transition: all 0.2s ease;
    }
    .entry-content .wp-block-button__link:hover {
      background: #0369a1;
      transform: translateY(-1px);
      box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }

    /* Formulář pro heslo (např. Vlčácké fotky chráněné heslem) */
    .post-password-form {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 1.25rem;
      padding: 1.75rem;
      max-width: 34rem;
      margin: 1.5rem 0;
    }
    .dark .post-password-form {
      background: #0f1c34;
      border-color: #1e2e4a;
    }
    .post-password-form p { margin-bottom: 0.75rem; }
    .post-password-form label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    .post-password-form input[type="password"] {
      padding: 0.625rem 1rem;
      border-radius: 0.75rem;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      color: #0f172a;
      outline: none;
      width: 100%;
      max-width: 18rem;
      margin-bottom: 0.85rem;
      display: block;
    }
    .dark .post-password-form input[type="password"] {
      background: #162544;
      border-color: #243b66;
      color: #ffffff;
    }
    .post-password-form input[type="password"]:focus {
      border-color: #0284c7;
      box-shadow: 0 0 0 2px rgba(2, 132, 199, 0.25);
    }
    .post-password-form input[type="submit"] {
      padding: 0.65rem 1.5rem;
      border-radius: 0.75rem;
      font-weight: 700;
      background: #facc15;
      color: #071527;
      border: none;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(250, 204, 21, 0.3);
      transition: all 0.2s ease;
    }
    .post-password-form input[type="submit"]:hover {
      background: #eab308;
      transform: translateY(-1px);
    }
"""

def prepare_wp_theme(source_dir="verzeA"):
    source_dir = os.path.abspath(source_dir)
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Zdrojová složka {source_dir} neexistuje.")

    print(f"📦 Příprava WordPress šablony ze složky: {source_dir}")

    # 1. Vyčistit cílovou složku pro sestavení
    if os.path.exists(THEME_DIR):
        shutil.rmtree(THEME_DIR)
    os.makedirs(THEME_DIR, exist_ok=True)

    # 2. Zkopírovat všechny obrázky a složky (avatary, fotky, loga)
    for item in os.listdir(source_dir):
        s_item = os.path.join(source_dir, item)
        d_item = os.path.join(THEME_DIR, item)
        if os.path.isdir(s_item):
            shutil.copytree(s_item, d_item)
        elif item.lower().endswith(('.jpg', '.jpeg', '.png', '.svg', '.webp', '.gif', '.ico')):
            shutil.copy2(s_item, d_item)

    # 3. Vytvořit style.css s hlavičkou šablony
    style_css_content = f"""/*
Theme Name: {THEME_NAME}
Theme URI: https://jedenactka.skauting.cz/
Author: 11. oddíl vodních skautů České Budějovice
Author URI: https://jedenactka.skauting.cz/
Description: Oficiální moderní a responzivní WordPress šablona 11. oddílu vodních skautů České Budějovice.
Version: {get_app_version()}
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Text Domain: jedenactka
*/
"""
    with open(os.path.join(THEME_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(style_css_content)

    # 4. Vytvořit functions.php
    functions_php_content = """<?php
/**
 * 11. oddíl vodních skautů - Theme Functions
 */

if (!defined('ABSPATH')) {
    exit;
}

function jedenactka_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('responsive-embeds');
    add_theme_support('align-wide');

    // Automatické vytvoření stránky 'vedeni' při aktivaci šablony, pokud ještě neexistuje
    if (!get_page_by_path('vedeni')) {
        wp_insert_post(array(
            'post_title'     => 'Vedení oddílu',
            'post_name'      => 'vedeni',
            'post_status'    => 'publish',
            'post_type'      => 'page',
            'page_template'  => 'page-vedeni.php',
            'comment_status' => 'closed'
        ));
    }
}
add_action('after_switch_theme', 'jedenactka_setup');

// Směrování pro podstránku vedení
add_filter('template_include', function($template) {
    if (is_page('vedeni') || (isset($_GET['stranka']) && $_GET['stranka'] === 'vedeni')) {
        $vedeni_template = locate_template(array('page-vedeni.php'));
        if (!empty($vedeni_template)) {
            return $vedeni_template;
        }
    }
    return $template;
});
"""
    with open(os.path.join(THEME_DIR, "functions.php"), "w", encoding="utf-8") as f:
        f.write(functions_php_content)

    # Načíst index.html a vedeni.html
    with open(os.path.join(source_dir, "index.html"), "r", encoding="utf-8") as f:
        index_html = f.read()

    with open(os.path.join(source_dir, "vedeni.html"), "r", encoding="utf-8") as f:
        vedeni_html = f.read()

    # 5. Převedení index.html -> front-page.php
    wp_front = adapt_html_to_wp(index_html, is_subpage=False)
    with open(os.path.join(THEME_DIR, "front-page.php"), "w", encoding="utf-8") as f:
        f.write(wp_front)

    # 6. Převedení vedeni.html -> page-vedeni.php
    wp_vedeni = "<?php\n/*\nTemplate Name: Vedení oddílu\n*/\n?>\n" + adapt_html_to_wp(vedeni_html, is_subpage=True)
    with open(os.path.join(THEME_DIR, "page-vedeni.php"), "w", encoding="utf-8") as f:
        f.write(wp_vedeni)

    # 7. Vytvoření univerzální šablony page.php (pro /vlcacke-fotky/, /oddil/archiv-akci/ a další existující podstránky)
    wp_page = generate_wp_page_template(vedeni_html)
    with open(os.path.join(THEME_DIR, "page.php"), "w", encoding="utf-8") as f:
        f.write(wp_page)

    # 8. Vytvoření šablony single.php (pro jednotlivé články/aktuality)
    with open(os.path.join(THEME_DIR, "single.php"), "w", encoding="utf-8") as f:
        f.write(wp_page)

    # 9. Vytvoření fallback index.php
    index_php_content = """<?php
/**
 * Fallback Template
 */
if (is_front_page()) {
    include get_template_directory() . '/front-page.php';
} else {
    include get_template_directory() . '/page.php';
}
"""
    with open(os.path.join(THEME_DIR, "index.php"), "w", encoding="utf-8") as f:
        f.write(index_php_content)

    # 10. Screenshot šablony (použijeme koka_preview.png nebo logo)
    screenshot_src = os.path.join(os.path.dirname(__file__), "koka_preview.png")
    if os.path.exists(screenshot_src):
        shutil.copy2(screenshot_src, os.path.join(THEME_DIR, "screenshot.png"))

    # 11. Zabalení do ZIP archivu
    print(f"🗜️ Balím do ZIP archivu: {OUTPUT_ZIP}...")
    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(THEME_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, THEME_DIR)
                # Uložit do podsložky 'jedenactka-theme/...' pro čisté rozbalení ve WordPressu
                zip_arcname = os.path.join(THEME_SLUG, rel_path)
                zipf.write(file_path, zip_arcname)

    size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 * 1024)
    print(f"✅ HOTOVO! Vytvořen instalační balíček: {OUTPUT_ZIP} ({size_mb:.2f} MB)")
    return OUTPUT_ZIP

def adapt_html_to_wp(html_content, is_subpage=False):
    """Nahradí statické relativní odkazy a cesty za dynamické WordPress funkce a doplní wp_head a wp_footer."""
    # Odstranění statického <title> tagu – WordPress si ho generuje sám přes add_theme_support('title-tag')
    html_content = re.sub(r'<title>.*?</title>', '<!-- Title managed dynamically by WordPress -->', html_content, flags=re.DOTALL)

    # Vložení <?php wp_head(); ?> před </head>
    if '</head>' in html_content:
        html_content = html_content.replace('</head>', '<?php wp_head(); ?>\n</head>')

    # Vložení <?php wp_footer(); ?> před </body>
    if '</body>' in html_content:
        html_content = html_content.replace('</body>', '<?php wp_footer(); ?>\n</body>')

    # Nahrazení odkazů na vedeni.html
    html_content = re.sub(r'href=["\']vedeni\.html["\']', 'href="<?php echo home_url(\'/vedeni/\'); ?>"', html_content)

    # Nahrazení odkazů na hlavní stránku
    if is_subpage:
        html_content = re.sub(r'href=["\']index\.html#(.*?)["\']', 'href="<?php echo home_url(\'/\'); ?>#\\1"', html_content)
        html_content = re.sub(r'href=["\']index\.html["\']', 'href="<?php echo home_url(\'/\'); ?>"', html_content)
        html_content = re.sub(r'href=["\']#["\']', 'href="<?php echo home_url(\'/vedeni/\'); ?>"', html_content)

    # Nahrazení obrázků (src="cesta.jpg|png|svg")
    def replace_src(match):
        attr = match.group(1)
        val = match.group(2)
        if val.startswith(('http://', 'https://', '//', 'data:')):
            return match.group(0)
        return f'{attr}="<?php echo get_template_directory_uri(); ?>/{val}"'

    html_content = re.sub(r'(src)=["\']([^"\']+)["\']', replace_src, html_content)

    return html_content

def generate_wp_page_template(vedeni_html):
    """
    Vygeneruje univerzální WordPress page.php šablonu převzetím hlavičky a patičky z vedeni.html,
    ale s vloženým dynamickým tělem pro zobrazení libovolné WordPress stránky (fotky, archiv akcí, články atd.).
    """
    h_end = vedeni_html.find('</header>') + len('</header>')
    f_start = vedeni_html.find('<!-- FOOTER -->')
    if f_start == -1:
        f_start = vedeni_html.find('<footer')

    header_raw = vedeni_html[:h_end]
    footer_raw = vedeni_html[f_start:]

    # Doplnit WordPress styly do <style> v hlavičce
    if '</style>' in header_raw:
        header_raw = header_raw.replace('</style>', WP_CONTENT_STYLES + '\n  </style>')

    body_content = """
  <!-- HLAVNÍ OBSAH PODSTRÁNKY -->
  <main class="min-h-screen py-8 sm:py-12 px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto">
    <!-- DROBEČKOVÁ NAVIGACE / NÁVRAT NA ÚVOD -->
    <div class="mb-6 flex items-center justify-between gap-4">
      <a href="<?php echo home_url('/'); ?>" class="inline-flex items-center gap-2 text-sm font-bold text-slate-500 hover:text-brand-sky dark:text-slate-400 dark:hover:text-amber-400 transition-colors">
        <i class="fa-solid fa-arrow-left text-xs"></i>
        <span>Zpět na hlavní stránku oddílu</span>
      </a>
      <span class="text-xs text-slate-400 font-semibold hidden sm:inline">11. oddíl vodních skautů České Budějovice</span>
    </div>

    <!-- KARTA S OBSAHEM STRÁNKY -->
    <article class="bg-white dark:bg-slate-900 rounded-3xl p-6 sm:p-10 shadow-sm border border-slate-200/80 dark:border-slate-800">
      <header class="mb-8 border-b border-slate-100 dark:border-slate-800 pb-6">
        <h1 class="text-3xl sm:text-4xl font-black text-slate-900 dark:text-white font-heading tracking-tight">
          <?php the_title(); ?>
        </h1>
      </header>

      <div class="entry-content text-slate-700 dark:text-slate-200 leading-relaxed">
        <?php
        if ( have_posts() ) :
            while ( have_posts() ) : the_post();
                the_content();
            endwhile;
        else :
            echo '<p>Žádný obsah nebyl nalezen.</p>';
        endif;
        ?>
      </div>
    </article>
  </main>
"""

    full_page = header_raw + "\n" + body_content + "\n" + footer_raw
    return adapt_html_to_wp(full_page, is_subpage=True)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "verzeA"
    prepare_wp_theme(target)
