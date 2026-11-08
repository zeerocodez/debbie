# -*- coding: utf-8 -*-
"""
Master Builder Script for Debbie's Collection E-Commerce Application.
Produces one complete, self-contained, offline-resilient index.html file.
"""
import os
import json
from builder.products_data import PRODUCTS
from builder.svg_assets import get_product_svg
from builder.app_html import (
    get_header_html,
    get_marquee_html,
    get_hero_html,
    get_categories_html,
    get_shop_catalog_html,
    get_atelier_html,
    get_reviews_html,
    get_boutique_visit_html,
    get_faq_html,
    get_footer_html,
    get_mobile_bottom_nav_html,
    get_modals_html
)
from builder.app_js import get_app_js

def build():
    # 1. Read CSS
    with open('builder/styles.css', 'r', encoding='utf-8') as f:
        css_content = f.read()

    # 2. Prepare SVGs dictionary for JS
    svg_map = {}
    for p in PRODUCTS:
        svg_map[p['svgId']] = get_product_svg(p['svgId'], '100%', '100%')

    # 3. Assemble HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Debbie's Collection | Children's Clothing & Bespoke Loungewear | 164 Udoumana Street, Uyo</title>
  <meta name="description" content="Discover Debbie's Collection at 164 Udoumana Street, Uyo, Akwa Ibom State. Hand-tailored children's couture, heirloom dresses, pleated tartan skirts, and bespoke made-to-measure loungewear.">
  <meta name="keywords" content="Debbie's Collection, Uyo fashion boutique, children clothing Uyo, bespoke loungewear Nigeria, Akwa Ibom kids fashion, Udoumana Street boutique, made to measure Nigerian couture">
  <meta name="author" content="Debbie's Collection">
  <meta name="theme-color" content="#211815">

  <!-- Open Graph -->
  <meta property="og:title" content="Debbie's Collection | Luxury Children's Wear & Bespoke Lounge">
  <meta property="og:description" content="Handcrafted elegance in Uyo, Akwa Ibom State. Made-to-measure heirloom children's fashion & bespoke loungewear.">
  <meta property="og:type" content="website">

  <!-- Fonts: Google Fonts with robust high-fashion fallbacks -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
{css_content}
  </style>

  <script>
    // Embedded Data Models
    window.DC_PRODUCTS = {json.dumps(PRODUCTS, ensure_ascii=False)};
    window.DC_SVGS = {json.dumps(svg_map, ensure_ascii=False)};
  </script>
</head>
<body>
  {get_header_html()}
  {get_marquee_html()}
  <main>
    {get_hero_html()}
    {get_categories_html()}
    {get_shop_catalog_html()}
    {get_atelier_html()}
    {get_reviews_html()}
    {get_boutique_visit_html()}
    {get_faq_html()}
  </main>
  {get_footer_html()}
  {get_mobile_bottom_nav_html()}
  {get_modals_html()}

  <script>
{get_app_js()}
  </script>
</body>
</html>
'''

    output_path = 'index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"Successfully generated {output_path} ({file_size_kb:.2f} KB)")

if __name__ == '__main__':
    build()

