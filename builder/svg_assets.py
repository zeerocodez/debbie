# -*- coding: utf-8 -*-
"""
SVG Graphics & Fashion Art Asset Library for Debbie's Collection.
Self-contained, resolution-independent vector illustrations for products,
monogram visualizer, map, brand crest, and UI iconography.
"""

def get_product_svg(svg_id, width="100%", height="100%"):
    svgs = {
        # 1. Silk Kimono Loungewear Set
        "svg-silk-kimono": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="silk-grad-1" x1="60" y1="40" x2="260" y2="300" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFFDF9"/>
      <stop offset="40%" stop-color="#F5ECE4"/>
      <stop offset="100%" stop-color="#E5D3C5"/>
    </linearGradient>
    <linearGradient id="silk-shadow" x1="160" y1="40" x2="160" y2="300" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="rgba(196,130,117,0.1)"/>
      <stop offset="100%" stop-color="rgba(33,24,21,0.18)"/>
    </linearGradient>
    <linearGradient id="rose-piping" x1="100" y1="50" x2="220" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#C48275"/>
      <stop offset="100%" stop-color="#A5675B"/>
    </linearGradient>
  </defs>
  <!-- Background gentle shadow -->
  <ellipse cx="160" cy="295" rx="90" ry="14" fill="rgba(33,24,21,0.06)"/>
  
  <!-- Kimono Trousers -->
  <path d="M110 180 L100 285 Q100 288 105 288 L146 288 Q150 288 152 284 L160 215 L168 284 Q170 288 174 288 L215 288 Q220 288 220 285 L210 180 Z" fill="url(#silk-grad-1)" stroke="#D8C3B3" stroke-width="1.5"/>
  <path d="M160 215 L160 286" stroke="#C8B3A3" stroke-width="1.2" stroke-dasharray="3 3"/>
  <path d="M102 283 L144 283" stroke="url(#rose-piping)" stroke-width="2"/>
  <path d="M176 283 L218 283" stroke="url(#rose-piping)" stroke-width="2"/>
  
  <!-- Kimono Robe Body -->
  <path d="M90 70 L60 120 L88 135 L108 96 L108 200 Q160 210 212 200 L212 96 L232 135 L260 120 L230 70 Q160 54 90 70 Z" fill="url(#silk-grad-1)" stroke="#D8C3B3" stroke-width="1.5"/>
  <!-- Kimono Collar / Lapel Wrap -->
  <path d="M125 58 L185 150 L185 202 L165 202 L115 60 Z" fill="#FAF2EC" stroke="url(#rose-piping)" stroke-width="1.8"/>
  <path d="M195 58 L135 150 L135 170" stroke="url(#rose-piping)" stroke-width="1.8"/>
  
  <!-- Obi Sash Belt with bow -->
  <rect x="105" y="145" width="110" height="20" rx="3" fill="#C48275"/>
  <rect x="105" y="147" width="110" height="3" fill="#E8B5AC"/>
  <ellipse cx="160" cy="155" rx="14" ry="7" fill="#AF6E61"/>
  <!-- Hanging Belt ribbons -->
  <path d="M154 158 Q148 185 142 215 Q145 218 152 215 Q156 188 158 160 Z" fill="#C48275"/>
  <path d="M166 158 Q172 185 178 215 Q175 218 168 215 Q164 188 162 160 Z" fill="#AF6E61"/>
  
  <!-- Contrast Wide Sleeve Cuffs -->
  <path d="M60 120 L88 135" stroke="url(#rose-piping)" stroke-width="4"/>
  <path d="M260 120 L232 135" stroke="url(#rose-piping)" stroke-width="4"/>
  <!-- Monogram on chest crest -->
  <circle cx="138" cy="115" r="9" fill="rgba(196,130,117,0.15)"/>
  <text x="138" y="118" font-family="'Playfair Display', serif" font-size="7" font-weight="700" fill="#AA7C11" text-anchor="middle">DC</text>
  <!-- Fabric Sheen Highlight -->
  <path d="M116 100 Q124 130 128 144" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity="0.8"/>
</svg>''',

        # 2. Girls' Hand-Smocked Blossom Linen Dress
        "svg-linen-dress": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="dress-rose" x1="100" y1="60" x2="220" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FCEEEB"/>
      <stop offset="50%" stop-color="#F2D7D1"/>
      <stop offset="100%" stop-color="#E2B7AE"/>
    </linearGradient>
    <linearGradient id="smock-gold" x1="130" y1="100" x2="190" y2="135" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#AA7C11"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="290" rx="85" ry="12" fill="rgba(33,24,21,0.06)"/>
  
  <!-- Puffed Cap Sleeves -->
  <ellipse cx="106" cy="100" rx="20" ry="15" transform="rotate(-20 106 100)" fill="#F5DAD4" stroke="#D9AFA6" stroke-width="1.5"/>
  <ellipse cx="214" cy="100" rx="20" ry="15" transform="rotate(20 214 100)" fill="#F5DAD4" stroke="#D9AFA6" stroke-width="1.5"/>
  <path d="M88 108 Q96 114 104 110" stroke="#FFFFFF" stroke-width="2"/>
  <path d="M216 110 Q224 114 232 108" stroke="#FFFFFF" stroke-width="2"/>

  <!-- Bodice -->
  <path d="M125 78 Q160 84 195 78 L202 135 Q160 142 118 135 Z" fill="url(#dress-rose)" stroke="#D9AFA6" stroke-width="1.5"/>
  
  <!-- Hand-Smocked Geometric Embroidery Details -->
  <path d="M128 98 Q160 102 192 98" stroke="#AA7C11" stroke-width="1.5" stroke-dasharray="3 2"/>
  <path d="M126 107 Q160 112 194 107" stroke="#C48275" stroke-width="1.5" stroke-dasharray="4 2"/>
  <path d="M124 116 Q160 122 196 116" stroke="#AA7C11" stroke-width="1.5" stroke-dasharray="3 2"/>
  <path d="M122 125 Q160 131 198 125" stroke="#C48275" stroke-width="1.5" stroke-dasharray="4 2"/>
  <!-- Tiny embroidered rosebuds -->
  <circle cx="145" cy="107" r="2.5" fill="#C48275"/>
  <circle cx="160" cy="107" r="2.5" fill="#AA7C11"/>
  <circle cx="175" cy="107" r="2.5" fill="#C48275"/>

  <!-- Scalloped Peter Pan Collar -->
  <path d="M160 85 C146 85 130 76 128 66 C144 64 158 75 160 85 Z" fill="#FFFFFF" stroke="#D9AFA6" stroke-width="1.2"/>
  <path d="M160 85 C174 85 190 76 192 66 C176 64 162 75 160 85 Z" fill="#FFFFFF" stroke="#D9AFA6" stroke-width="1.2"/>
  <circle cx="160" cy="85" r="3" fill="#C48275"/>

  <!-- Gathered Flared A-Line Skirt -->
  <path d="M118 135 Q160 142 202 135 L242 265 Q160 282 78 265 Z" fill="url(#dress-rose)" stroke="#D9AFA6" stroke-width="1.5"/>
  
  <!-- Skirt Folds -->
  <path d="M135 140 Q130 200 120 268" stroke="rgba(196,130,117,0.3)" stroke-width="1.5"/>
  <path d="M160 142 Q160 200 160 272" stroke="rgba(196,130,117,0.4)" stroke-width="1.8"/>
  <path d="M185 140 Q190 200 200 268" stroke="rgba(196,130,117,0.3)" stroke-width="1.5"/>

  <!-- Scalloped French Lace Hem -->
  <path d="M78 265 Q94 274 110 266 Q126 276 142 268 Q160 278 178 268 Q194 276 210 266 Q226 274 242 265 L242 272 Q226 281 210 273 Q194 283 178 275 Q160 285 142 275 Q126 283 110 273 Q94 281 78 272 Z" fill="#FFFFFF" stroke="#D9C0B9" stroke-width="1"/>
  <!-- Velvet Sash & Back Bow Ribbon Tails -->
  <path d="M120 135 L200 135 L202 140 L118 140 Z" fill="#C48275"/>
  <path d="M198 140 Q215 165 224 195 Q218 196 210 175 Q205 155 198 140 Z" fill="#AF6E61"/>
</svg>''',

        # 3. Little Duke Navy Bespoke Blazer & Trouser Set
        "svg-boys-blazer": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="navy-grad" x1="90" y1="50" x2="230" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22304A"/>
      <stop offset="60%" stop-color="#182337"/>
      <stop offset="100%" stop-color="#0F1726"/>
    </linearGradient>
    <linearGradient id="brass-gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F5E4B2"/>
      <stop offset="50%" stop-color="#C29B38"/>
      <stop offset="100%" stop-color="#7A5D18"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="85" ry="12" fill="rgba(33,24,21,0.06)"/>
  
  <!-- Tailored Bermuda Shorts -->
  <path d="M120 180 L114 265 L152 265 L160 205 L168 265 L206 265 L200 180 Z" fill="#EAE3D9" stroke="#CFC5B8" stroke-width="1.5"/>
  <path d="M133 185 L133 260" stroke="#DDD4C7" stroke-width="1.2"/>
  <path d="M187 185 L187 260" stroke="#DDD4C7" stroke-width="1.2"/>
  <path d="M114 260 L152 260" stroke="#C4B7A6" stroke-width="3"/>
  <path d="M168 260 L206 260" stroke="#C4B7A6" stroke-width="3"/>

  <!-- Inner Dress Shirt & Silk Tie -->
  <path d="M142 56 L160 76 L178 56 Z" fill="#FFFFFF"/>
  <path d="M156 68 L164 68 L166 112 L160 120 L154 112 Z" fill="#C48275"/>

  <!-- Tailored Double Breasted Blazer Body -->
  <path d="M102 65 L68 125 L92 135 L106 100 L104 205 Q160 215 216 205 L214 100 L228 135 L252 125 L218 65 Q160 52 102 65 Z" fill="url(#navy-grad)" stroke="#121A28" stroke-width="1.5"/>
  
  <!-- Peaked Lapels -->
  <path d="M132 58 L114 108 L142 118 L126 150 L160 178 L194 150 L178 118 L206 108 L188 58 Q160 54 132 58 Z" fill="#283854" stroke="#121A28" stroke-width="1.2"/>

  <!-- Breast Pocket & Silk Pocket Square -->
  <path d="M122 118 L142 120 L142 124 L122 122 Z" fill="#182337"/>
  <path d="M126 118 L132 108 L138 119 Z" fill="#FBF8F5" stroke="#C48275" stroke-width="0.8"/>

  <!-- Crested Brass Buttons (Double Breasted 4-button setup) -->
  <circle cx="146" cy="148" r="4.5" fill="url(#brass-gold)" stroke="#59430E" stroke-width="0.8"/>
  <circle cx="174" cy="148" r="4.5" fill="url(#brass-gold)" stroke="#59430E" stroke-width="0.8"/>
  <circle cx="146" cy="172" r="4.5" fill="url(#brass-gold)" stroke="#59430E" stroke-width="0.8"/>
  <circle cx="174" cy="172" r="4.5" fill="url(#brass-gold)" stroke="#59430E" stroke-width="0.8"/>

  <!-- Flap Pockets -->
  <rect x="108" y="174" width="30" height="8" rx="2" fill="#1A253A" stroke="#121A28" stroke-width="1"/>
  <rect x="182" y="174" width="30" height="8" rx="2" fill="#1A253A" stroke="#121A28" stroke-width="1"/>
</svg>''',

        # 4. Monogrammed Royal Satin Pyjama Set
        "svg-satin-pj": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pj-rose" x1="80" y1="50" x2="240" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#F2D5CE"/>
      <stop offset="45%" stop-color="#E2B8AF"/>
      <stop offset="100%" stop-color="#C59388"/>
    </linearGradient>
    <linearGradient id="gold-pipe" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FCEAB8"/>
      <stop offset="100%" stop-color="#C29B38"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="88" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Trousers -->
  <path d="M112 175 L106 285 Q106 288 112 288 L148 288 L156 210 L164 288 L200 288 Q206 288 206 285 L200 175 Z" fill="url(#pj-rose)" stroke="#B78277" stroke-width="1.5"/>
  <path d="M106 284 L148 284" stroke="url(#gold-pipe)" stroke-width="2.5"/>
  <path d="M164 284 L206 284" stroke="url(#gold-pipe)" stroke-width="2.5"/>

  <!-- PJ Top Body -->
  <path d="M100 68 L64 125 L90 135 L108 98 L108 190 Q160 196 212 190 L212 98 L230 135 L256 125 L220 68 Q160 55 100 68 Z" fill="url(#pj-rose)" stroke="#B78277" stroke-width="1.5"/>

  <!-- Notch Lapel Collar with Gold Piping -->
  <path d="M130 62 L112 96 L134 104 L122 135 L160 162 L198 135 L186 104 L208 96 L190 62 Q160 58 130 62 Z" fill="#F8E5E1" stroke="url(#gold-pipe)" stroke-width="1.8"/>

  <!-- Center Placket & Mother of Pearl Buttons -->
  <line x1="160" y1="162" x2="160" y2="192" stroke="url(#gold-pipe)" stroke-width="1.5"/>
  <circle cx="160" cy="145" r="3" fill="#FFFFFF" stroke="#C29B38" stroke-width="0.8"/>
  <circle cx="160" cy="162" r="3" fill="#FFFFFF" stroke="#C29B38" stroke-width="0.8"/>
  <circle cx="160" cy="178" r="3" fill="#FFFFFF" stroke="#C29B38" stroke-width="0.8"/>

  <!-- Chest Pocket with Gold Monogram DC -->
  <rect x="120" y="115" width="24" height="24" rx="2" fill="#E8BDB4" stroke="url(#gold-pipe)" stroke-width="1.2"/>
  <line x1="120" y1="118" x2="144" y2="118" stroke="url(#gold-pipe)" stroke-width="1.5"/>
  <text x="132" y="132" font-family="'Playfair Display', serif" font-size="8" font-weight="700" fill="#AA7C11" text-anchor="middle">DC</text>

  <!-- Sleeve Cuffs -->
  <path d="M64 125 L90 135" stroke="url(#gold-pipe)" stroke-width="3"/>
  <path d="M256 125 L230 135" stroke="url(#gold-pipe)" stroke-width="3"/>

  <!-- Silk Sheen Highlights -->
  <path d="M180 110 Q192 140 196 175" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity="0.6"/>
</svg>''',

        # 5. Mini Akwa-Ibom Traditional Aso-Oke Attire
        "svg-aso-oke": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="coral-grad" x1="80" y1="40" x2="240" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#E86A58"/>
      <stop offset="50%" stop-color="#C84838"/>
      <stop offset="100%" stop-color="#8F2518"/>
    </linearGradient>
    <linearGradient id="asooke-gold" x1="100" y1="60" x2="220" y2="260" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FBE6A2"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#8E6B15"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="88" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Traditional Sokoto Trousers -->
  <path d="M120 180 L110 285 L148 285 L158 220 L168 285 L206 285 L196 180 Z" fill="#9C2C1F" stroke="#751A10" stroke-width="1.5"/>
  <path d="M110 280 L148 280" stroke="url(#asooke-gold)" stroke-width="3"/>
  <path d="M168 280 L206 280" stroke="url(#asooke-gold)" stroke-width="3"/>

  <!-- Mini Agbada / Tunic Body with Wide Flowing Cape Sleeves -->
  <path d="M60 100 Q160 65 260 100 L245 195 L208 190 L206 250 Q160 255 114 250 L112 190 L75 195 Z" fill="url(#coral-grad)" stroke="#6A160D" stroke-width="1.8"/>

  <!-- Geometric Aso-Oke Handwoven Stripes -->
  <path d="M80 115 L240 115" stroke="url(#asooke-gold)" stroke-width="2" stroke-dasharray="6 3"/>
  <path d="M75 135 L245 135" stroke="url(#asooke-gold)" stroke-width="2.5"/>
  <path d="M72 155 L248 155" stroke="url(#asooke-gold)" stroke-width="2" stroke-dasharray="6 3"/>

  <!-- Center Neckline & Intricate Gold Thread Filigree Medallion -->
  <path d="M135 78 Q160 100 185 78 L175 155 Q160 170 145 155 Z" fill="#751A10" stroke="url(#asooke-gold)" stroke-width="2"/>
  <circle cx="160" cy="122" r="14" fill="#8F2518" stroke="url(#asooke-gold)" stroke-width="2"/>
  <circle cx="160" cy="122" r="7" fill="url(#asooke-gold)"/>

  <!-- Akwa Ibom Coral Bead Royal Necklace -->
  <path d="M138 78 Q160 98 182 78" stroke="#FF5733" stroke-width="5" stroke-linecap="round" stroke-dasharray="1 8"/>
  <path d="M134 86 Q160 112 186 86" stroke="#D32F2F" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="1 7"/>

  <!-- Traditional Akwa Ibom Fila / Cap (Cap accent floating above or perched) -->
  <path d="M136 48 Q160 38 184 48 L188 64 Q160 60 132 64 Z" fill="url(#coral-grad)" stroke="url(#asooke-gold)" stroke-width="1.5"/>
  <line x1="134" y1="60" x2="186" y2="60" stroke="url(#asooke-gold)" stroke-width="2"/>
</svg>''',

        # 6. Ibom Atelier Waffle Knit Loungewear Set
        "svg-waffle-robe": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="waffle-grad" x1="100" y1="50" x2="220" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#F2EDE6"/>
      <stop offset="50%" stop-color="#E2D7CC"/>
      <stop offset="100%" stop-color="#C9BCB0"/>
    </linearGradient>
    <pattern id="waffle-pattern" width="6" height="6" patternUnits="userSpaceOnUse">
      <rect width="6" height="6" fill="transparent"/>
      <rect x="0.5" y="0.5" width="5" height="5" stroke="rgba(33,24,21,0.08)" stroke-width="0.8" fill="rgba(255,255,255,0.4)"/>
    </pattern>
  </defs>
  <ellipse cx="160" cy="295" rx="85" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Lounge Joggers -->
  <path d="M112 175 L106 285 Q106 288 112 288 L148 288 L156 215 L164 288 L200 288 Q206 288 206 285 L200 175 Z" fill="url(#waffle-grad)" stroke="#B5A597" stroke-width="1.5"/>
  <rect x="106" y="278" width="42" height="10" rx="3" fill="#D3C5B7"/>
  <rect x="164" y="278" width="42" height="10" rx="3" fill="#D3C5B7"/>

  <!-- Wrap Cardigan Robe -->
  <path d="M96 68 L60 120 L86 132 L106 95 L104 210 Q160 218 214 210 L212 95 L232 132 L258 120 L222 68 Q160 55 96 68 Z" fill="url(#waffle-grad)" stroke="#B5A597" stroke-width="1.5"/>
  
  <!-- Overlay Waffle Texture Pattern -->
  <path d="M104 95 L104 210 Q160 218 214 210 L212 95 Z" fill="url(#waffle-pattern)"/>

  <!-- Cozy Shawl Collar with Espresso Piping -->
  <path d="M130 62 Q145 105 178 155 L160 155 Q135 105 120 62 Z" fill="#D8CCC0" stroke="#8E7D73" stroke-width="1.2"/>
  <path d="M190 62 Q175 105 142 155 L160 155 Q185 105 200 62 Z" fill="#E4D9CE" stroke="#8E7D73" stroke-width="1.2"/>

  <!-- Waist Tie Belt -->
  <rect x="100" y="148" width="120" height="14" rx="3" fill="#A89688"/>
  <path d="M152 158 L146 220 L156 220 L160 160 Z" fill="#938173"/>

  <!-- Slouchy Deep Pockets -->
  <rect x="110" y="172" width="28" height="26" rx="4" fill="#DDD1C4" stroke="#B5A597" stroke-width="1.2"/>
  <rect x="180" y="172" width="28" height="26" rx="4" fill="#DDD1C4" stroke="#B5A597" stroke-width="1.2"/>
</svg>''',

        # 7. Princess Idara Tiered Tulle Ballgown
        "svg-tulle-ballgown": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="tulle-blush" x1="120" y1="60" x2="200" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFF5F2"/>
      <stop offset="50%" stop-color="#F9DED8"/>
      <stop offset="100%" stop-color="#EBBAB1"/>
    </linearGradient>
    <linearGradient id="gold-shimmer" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFF0C2"/>
      <stop offset="100%" stop-color="#D4AF37"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="95" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Satin Duchess Bodice -->
  <path d="M130 75 Q160 82 190 75 L196 130 Q160 136 124 130 Z" fill="url(#tulle-blush)" stroke="#DBADA4" stroke-width="1.5"/>

  <!-- Hand-sewn 3D Floral Appliqués on Bodice -->
  <circle cx="145" cy="95" r="5" fill="#FFFFFF" stroke="#C48275" stroke-width="1"/>
  <circle cx="145" cy="95" r="2" fill="url(#gold-shimmer)"/>
  <circle cx="160" cy="90" r="6" fill="#FFFFFF" stroke="#C48275" stroke-width="1"/>
  <circle cx="160" cy="90" r="2.5" fill="url(#gold-shimmer)"/>
  <circle cx="175" cy="96" r="5" fill="#FFFFFF" stroke="#C48275" stroke-width="1"/>
  <circle cx="175" cy="96" r="2" fill="url(#gold-shimmer)"/>

  <!-- Sweetheart Illusion Neckline with Pearls -->
  <path d="M136 78 Q160 92 184 78" stroke="url(#gold-shimmer)" stroke-width="1.5" stroke-dasharray="2 3"/>

  <!-- Waist Satin Sash -->
  <rect x="122" y="127" width="76" height="8" rx="2" fill="#C48275"/>

  <!-- Tier 1 Tulle Skirt -->
  <path d="M122 133 Q160 140 198 133 L216 180 Q160 195 104 180 Z" fill="rgba(249, 222, 216, 0.7)" stroke="#E8BDB4" stroke-width="1.2"/>
  <!-- Tier 2 Tulle Skirt -->
  <path d="M108 175 Q160 192 212 175 L234 230 Q160 248 86 230 Z" fill="rgba(242, 196, 187, 0.75)" stroke="#DEABA0" stroke-width="1.2"/>
  <!-- Tier 3 Tulle Skirt (Bottom Grand Flare) -->
  <path d="M88 225 Q160 245 232 225 L258 285 Q160 305 62 285 Z" fill="rgba(235, 186, 177, 0.85)" stroke="#D4998E" stroke-width="1.5"/>

  <!-- Sparkle Stars on Tulle -->
  <path d="M110 245 L113 250 L118 251 L114 255 L115 260 L110 257 L105 260 L106 255 L102 251 L107 250 Z" fill="#FFFFFF"/>
  <path d="M210 255 L212 259 L216 260 L213 263 L214 267 L210 265 L206 267 L207 263 L204 260 L208 259 Z" fill="#FFFFFF"/>
  <path d="M160 270 L162 274 L166 275 L163 278 L164 282 L160 280 L156 282 L157 278 L154 275 L158 274 Z" fill="url(#gold-shimmer)"/>
</svg>''',

        # 8. Organic Bamboo Baby Ribbed Romper & Bonnet
        "svg-bamboo-romper": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sage-grad" x1="100" y1="60" x2="220" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#E2EBE0"/>
      <stop offset="50%" stop-color="#C5D7C2"/>
      <stop offset="100%" stop-color="#9EB59B"/>
    </linearGradient>
    <pattern id="ribbed-lines" width="4" height="10" patternUnits="userSpaceOnUse">
      <line x1="2" y1="0" x2="2" y2="10" stroke="rgba(255,255,255,0.4)" stroke-width="1.2"/>
    </pattern>
  </defs>
  <ellipse cx="160" cy="295" rx="80" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Romper Body & Legs -->
  <path d="M120 100 L95 125 L110 140 L126 122 L124 235 L96 260 L116 276 L144 245 L160 250 L176 245 L204 276 L224 260 L196 235 L194 122 L210 140 L225 125 L200 100 Q160 92 120 100 Z" fill="url(#sage-grad)" stroke="#89A285" stroke-width="1.5"/>
  <path d="M120 100 L95 125 L110 140 L126 122 L124 235 L96 260 L116 276 L144 245 L160 250 L176 245 L204 276 L224 260 L196 235 L194 122 L210 140 L225 125 L200 100 Z" fill="url(#ribbed-lines)"/>

  <!-- Wooden Coconut Buttons on Henley Placket -->
  <rect x="154" y="98" width="12" height="52" rx="3" fill="#D2DEC0" stroke="#89A285" stroke-width="1"/>
  <circle cx="160" cy="108" r="3" fill="#6B4E3D"/>
  <circle cx="160" cy="122" r="3" fill="#6B4E3D"/>
  <circle cx="160" cy="136" r="3" fill="#6B4E3D"/>

  <!-- Matching Tie Bonnet (Posed resting above collar) -->
  <path d="M130 52 Q160 32 190 52 Q196 82 186 92 Q160 84 134 92 Q124 82 130 52 Z" fill="url(#sage-grad)" stroke="#89A285" stroke-width="1.5"/>
  <path d="M136 88 Q140 106 142 120" stroke="#9EB59B" stroke-width="1.8"/>
  <path d="M184 88 Q180 106 178 120" stroke="#9EB59B" stroke-width="1.8"/>
</svg>''',

        # 9. Little Gentleman Linen Suspender & Chino Set
        "svg-gentleman-set": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="mocha-linen" x1="110" y1="160" x2="210" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#C2AD9B"/>
      <stop offset="100%" stop-color="#9C8572"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="85" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Linen Suspender Shorts -->
  <path d="M116 160 L110 268 L150 268 L160 205 L170 268 L210 268 L204 160 Z" fill="url(#mocha-linen)" stroke="#87715F" stroke-width="1.5"/>
  
  <!-- White Grandad Collar Linen Shirt -->
  <path d="M106 72 L70 120 L94 130 L112 100 L112 165 Q160 168 208 165 L208 100 L226 130 L250 120 L214 72 Q160 62 106 72 Z" fill="#FDFBF9" stroke="#DDD4C8" stroke-width="1.5"/>
  <line x1="160" y1="78" x2="160" y2="165" stroke="#E5DDD2" stroke-width="1.5"/>
  <circle cx="160" cy="100" r="2.5" fill="#87715F"/>
  <circle cx="160" cy="120" r="2.5" fill="#87715F"/>
  <circle cx="160" cy="140" r="2.5" fill="#87715F"/>

  <!-- Leather & Elastic Suspenders (Y-Back Style over shoulders) -->
  <path d="M134 76 L134 164" stroke="#544133" stroke-width="4"/>
  <path d="M186 76 L186 164" stroke="#544133" stroke-width="4"/>
  <!-- Brass Adjuster Buckles -->
  <rect x="131" y="112" width="6" height="8" rx="1" fill="#C29B38"/>
  <rect x="183" y="112" width="6" height="8" rx="1" fill="#C29B38"/>

  <!-- Pre-tied Linen Bowtie -->
  <path d="M148 76 L160 82 L172 76 L168 88 L172 96 L160 90 L148 96 L152 88 Z" fill="#87715F" stroke="#544133" stroke-width="1"/>
  <circle cx="160" cy="86" r="3" fill="#695444"/>
</svg>''',

        # 10. Maman & Enfant Matching Silk Loungewear Duo
        "svg-mother-child-duo": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="duo-silk" x1="50" y1="40" x2="270" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FDF1ED"/>
      <stop offset="50%" stop-color="#F2D2CB"/>
      <stop offset="100%" stop-color="#DCABA1"/>
    </linearGradient>
  </defs>
  <ellipse cx="120" cy="295" rx="65" ry="10" fill="rgba(33,24,21,0.06)"/>
  <ellipse cx="230" cy="295" rx="45" ry="8" fill="rgba(33,24,21,0.06)"/>

  <!-- Adult Flowing Duster Robe (Left) -->
  <path d="M72 65 L40 120 L66 132 L84 95 L84 285 Q125 292 166 285 L166 95 L184 132 L210 120 L178 65 Q125 50 72 65 Z" fill="url(#duo-silk)" stroke="#C8978E" stroke-width="1.5"/>
  <path d="M105 58 L142 165 L142 286 L124 286 L92 59 Z" fill="#FBF0EC" stroke="#C48275" stroke-width="1.5"/>
  <rect x="80" y="152" width="90" height="12" rx="3" fill="#C48275"/>
  <circle cx="108" cy="115" r="7" fill="rgba(196,130,117,0.2)"/>
  <text x="108" y="117.5" font-family="'Playfair Display', serif" font-size="6" font-weight="700" fill="#AA7C11" text-anchor="middle">DC</text>

  <!-- Child Matching Miniature Kimono (Right) -->
  <path d="M198 140 L178 178 L196 186 L208 162 L208 285 Q232 290 256 285 L256 162 L268 186 L286 178 L266 140 Q232 130 198 140 Z" fill="url(#duo-silk)" stroke="#C8978E" stroke-width="1.5"/>
  <path d="M218 135 L242 205 L242 285 L230 285 L210 136 Z" fill="#FBF0EC" stroke="#C48275" stroke-width="1.5"/>
  <rect x="204" y="200" width="56" height="8" rx="2" fill="#C48275"/>
  <circle cx="222" cy="175" r="5" fill="rgba(196,130,117,0.2)"/>
  <text x="222" y="177" font-family="'Playfair Display', serif" font-size="4.5" font-weight="700" fill="#AA7C11" text-anchor="middle">DC</text>
</svg>''',

        # 11. Royal Plum Velvet Pageant Cape-Coat
        "svg-velvet-coat": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="plum-velvet" x1="100" y1="40" x2="220" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#5E1F3B"/>
      <stop offset="50%" stop-color="#46132A"/>
      <stop offset="100%" stop-color="#2D0A1A"/>
    </linearGradient>
    <linearGradient id="gold-filigree" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFEBB0"/>
      <stop offset="100%" stop-color="#C29B38"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="88" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Velvet Flared Coat Silhouette -->
  <path d="M125 65 L80 135 L106 148 L114 110 L102 275 Q160 286 218 275 L206 110 L214 148 L240 135 L195 65 Q160 55 125 65 Z" fill="url(#plum-velvet)" stroke="#220613" stroke-width="1.8"/>

  <!-- Quilted Satin Hem Border -->
  <path d="M102 265 Q160 276 218 265 L218 275 Q160 286 102 275 Z" fill="url(#gold-filigree)"/>

  <!-- Mandarin Collar with Gold Trim -->
  <path d="M136 60 Q160 66 184 60 L188 74 Q160 78 132 74 Z" fill="#380F22" stroke="url(#gold-filigree)" stroke-width="1.5"/>

  <!-- Ornate Frogged Gold Filigree Braiding Closures -->
  <g transform="translate(160, 95)">
    <circle cx="0" cy="0" r="4" fill="url(#gold-filigree)"/>
    <path d="M-24 -4 Q-12 -12 0 0 Q12 -12 24 -4 Q12 8 0 0 Q-12 8 -24 -4 Z" stroke="url(#gold-filigree)" stroke-width="1.5" fill="none"/>
  </g>
  <g transform="translate(160, 125)">
    <circle cx="0" cy="0" r="4" fill="url(#gold-filigree)"/>
    <path d="M-24 -4 Q-12 -12 0 0 Q12 -12 24 -4 Q12 8 0 0 Q-12 8 -24 -4 Z" stroke="url(#gold-filigree)" stroke-width="1.5" fill="none"/>
  </g>
  <g transform="translate(160, 155)">
    <circle cx="0" cy="0" r="4" fill="url(#gold-filigree)"/>
    <path d="M-24 -4 Q-12 -12 0 0 Q12 -12 24 -4 Q12 8 0 0 Q-12 8 -24 -4 Z" stroke="url(#gold-filigree)" stroke-width="1.5" fill="none"/>
  </g>
</svg>''',

        # 12. Tropical Riviera Pure Linen Camp Collar Shirt & Shorts
        "svg-camp-shirt": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="terra-linen" x1="100" y1="50" x2="220" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#EAA68C"/>
      <stop offset="60%" stop-color="#D68062"/>
      <stop offset="100%" stop-color="#BA5F40"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="85" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Resort Shorts -->
  <path d="M116 165 L108 265 L150 265 L160 210 L170 265 L212 265 L204 165 Z" fill="url(#terra-linen)" stroke="#9E4D31" stroke-width="1.5"/>
  <line x1="108" y1="172" x2="212" y2="172" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="3 3"/>

  <!-- Relaxed Camp Shirt -->
  <path d="M100 70 L60 115 L86 128 L108 96 L106 182 Q160 188 214 182 L212 96 L234 128 L260 115 L220 70 Q160 58 100 70 Z" fill="url(#terra-linen)" stroke="#9E4D31" stroke-width="1.5"/>

  <!-- Cuban Camp Collar (Open V-neck) -->
  <path d="M125 66 L112 102 L138 108 L160 135 L182 108 L208 102 L195 66 Z" fill="#F4BFA9" stroke="#9E4D31" stroke-width="1.2"/>

  <!-- Center Placket with Tortoiseshell Buttons -->
  <line x1="160" y1="135" x2="160" y2="182" stroke="#9E4D31" stroke-width="1.2"/>
  <circle cx="160" cy="148" r="2.8" fill="#4A2618"/>
  <circle cx="160" cy="164" r="2.8" fill="#4A2618"/>
</svg>''',

        # 13. Heritage Cashmere & Silk Personalized Swaddle Blanket
        "svg-blanket-monogram": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="swaddle-ivory" x1="80" y1="60" x2="240" y2="260" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFFDF9"/>
      <stop offset="50%" stop-color="#F5ECE4"/>
      <stop offset="100%" stop-color="#E4D3C5"/>
    </linearGradient>
    <linearGradient id="wreath-gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFEAA8"/>
      <stop offset="100%" stop-color="#C29B38"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="285" rx="90" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Folded Luxury Diamond Blanket Stack -->
  <path d="M160 65 L260 145 L160 225 L60 145 Z" fill="url(#swaddle-ivory)" stroke="#D4C2B2" stroke-width="1.8"/>
  <path d="M60 145 L160 225 L160 255 L60 175 Z" fill="#D8C5B5" stroke="#BAA594" stroke-width="1.5"/>
  <path d="M260 145 L160 225 L160 255 L260 175 Z" fill="#CBB6A5" stroke="#BAA594" stroke-width="1.5"/>

  <!-- Scalloped Satin Edging Along Diamond -->
  <path d="M160 65 L260 145 L160 225 L60 145 Z" stroke="url(#wreath-gold)" stroke-width="2.5" stroke-dasharray="6 4"/>

  <!-- Ornate Heraldic Laurel Wreath & Center Monogram -->
  <circle cx="160" cy="145" r="32" stroke="url(#wreath-gold)" stroke-width="1.5" stroke-dasharray="4 2" fill="rgba(255,255,255,0.7)"/>
  <!-- Laurel leaves -->
  <path d="M136 145 Q136 122 160 120 Q156 135 142 145" fill="url(#wreath-gold)"/>
  <path d="M184 145 Q184 122 160 120 Q164 135 178 145" fill="url(#wreath-gold)"/>
  <text x="160" y="152" font-family="'Playfair Display', serif" font-size="16" font-weight="700" fill="#AA7C11" text-anchor="middle">DC</text>
  <text x="160" y="165" font-family="'Plus Jakarta Sans', sans-serif" font-size="6" font-weight="600" letter-spacing="1" fill="#C48275" text-anchor="middle">ATELIER UYO</text>
</svg>''',

        # 14. Bespoke Silk Charmeuse Slip & Floor-Length Duster
        "svg-slip-duster": f'''<svg viewBox="0 0 320 320" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="charmeuse-esp" x1="100" y1="50" x2="220" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#3A2A24"/>
      <stop offset="50%" stop-color="#241915"/>
      <stop offset="100%" stop-color="#140C0A"/>
    </linearGradient>
    <linearGradient id="slip-champ" x1="120" y1="80" x2="200" y2="260" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFFDF9"/>
      <stop offset="100%" stop-color="#EAD9CC"/>
    </linearGradient>
  </defs>
  <ellipse cx="160" cy="295" rx="85" ry="12" fill="rgba(33,24,21,0.06)"/>

  <!-- Bias-cut Silk Slip Dress (Layered Underneath) -->
  <path d="M134 85 L144 110 L140 270 Q160 276 180 270 L176 110 L186 85 Z" fill="url(#slip-champ)" stroke="#D6C5B8" stroke-width="1.2"/>
  <line x1="140" y1="85" x2="144" y2="110" stroke="#C29B38" stroke-width="1"/>
  <line x1="180" y1="85" x2="176" y2="110" stroke="#C29B38" stroke-width="1"/>

  <!-- Floor-Length Duster Coat with Flared Lapels -->
  <path d="M96 68 L60 120 L86 132 L106 95 L100 285 Q160 292 220 285 L214 95 L234 132 L260 120 L224 68 Q160 52 96 68 Z" fill="url(#charmeuse-esp)" stroke="#110907" stroke-width="1.5"/>

  <!-- Flowing Front Open Drapes with Rose Gold Silk Facing -->
  <path d="M125 60 L140 180 L132 286 L108 286 L106 95 Z" fill="#45322C"/>
  <path d="M195 60 L180 180 L188 286 L212 286 L214 95 Z" fill="#45322C"/>

  <!-- Silk Sheen Line -->
  <path d="M112 110 Q118 160 116 230" stroke="rgba(255,255,255,0.25)" stroke-width="2" stroke-linecap="round"/>
</svg>'''
    }
    return svgs.get(svg_id, svgs["svg-silk-kimono"])


def get_studio_garment_svg(garment="pj", color="#F2D5CE", monogram="DC", thread="#C29B38", font_style="Playfair Display", placement="pocket"):
    """
    Dynamically renders the interactive Bespoke Studio garment vector
    with exact color, thread sheen, custom monogram initials, and selected typography.
    """
    font_family_css = f"'{font_style}', serif" if font_style != "Outfit" else "'Plus Jakarta Sans', sans-serif"
    return f'''<svg id="studio-live-svg" viewBox="0 0 340 340" width="100%" height="100%" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="garment-light" cx="50%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.25"/>
    </radialGradient>
    <filter id="thread-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="0.8" flood-color="rgba(0,0,0,0.3)"/>
    </filter>
  </defs>

  <ellipse cx="170" cy="310" rx="95" ry="12" fill="rgba(33,24,21,0.08)"/>

  <!-- Tailored Garment Base -->
  <path d="M106 72 L66 130 L94 142 L114 102 L112 210 Q170 218 228 210 L226 102 L246 142 L274 130 L234 72 Q170 58 106 72 Z" fill="{color}" stroke="rgba(0,0,0,0.18)" stroke-width="1.8"/>
  <!-- Highlight Shading -->
  <path d="M106 72 L66 130 L94 142 L114 102 L112 210 Q170 218 228 210 L226 102 L246 142 L274 130 L234 72 Q170 58 106 72 Z" fill="url(#garment-light)"/>

  <!-- Trousers / Bottom Hem (if set) -->
  <path d="M118 195 L112 300 Q112 304 118 304 L156 304 L165 230 L174 304 L212 304 Q218 304 218 300 L212 195 Z" fill="{color}" stroke="rgba(0,0,0,0.18)" stroke-width="1.8"/>
  <path d="M118 195 L112 300 Q112 304 118 304 L156 304 L165 230 L174 304 L212 304 Q218 304 218 300 L212 195 Z" fill="url(#garment-light)"/>
  <line x1="114" y1="298" x2="156" y2="298" stroke="{thread}" stroke-width="2.5"/>
  <line x1="174" y1="298" x2="216" y2="298" stroke="{thread}" stroke-width="2.5"/>

  <!-- Notch Lapel Collar with Embroidery Thread Piping -->
  <path d="M138 65 L118 102 L142 110 L128 145 L170 175 L212 145 L198 110 L222 102 L202 65 Q170 60 138 65 Z" fill="#FFFFFF" fill-opacity="0.15" stroke="{thread}" stroke-width="2"/>

  <!-- Placket and Buttons -->
  <line x1="170" y1="175" x2="170" y2="212" stroke="{thread}" stroke-width="1.5"/>
  <circle cx="170" cy="155" r="3.5" fill="#FFFFFF" stroke="{thread}" stroke-width="1"/>
  <circle cx="170" cy="175" r="3.5" fill="#FFFFFF" stroke="{thread}" stroke-width="1"/>
  <circle cx="170" cy="195" r="3.5" fill="#FFFFFF" stroke="{thread}" stroke-width="1"/>

  <!-- Pocket with Custom Monogram Embroidery -->
  <g id="monogram-pocket-group" transform="translate(126, 122)">
    <rect x="0" y="0" width="34" height="34" rx="3" fill="#FFFFFF" fill-opacity="0.2" stroke="{thread}" stroke-width="1.5"/>
    <line x1="0" y1="6" x2="34" y2="6" stroke="{thread}" stroke-width="1.5"/>
    <!-- Thread Stitch Dashes -->
    <rect x="2" y="2" width="30" height="30" rx="2" fill="none" stroke="{thread}" stroke-width="0.8" stroke-dasharray="2 2" opacity="0.7"/>
    <!-- Dynamic Monogram Text -->
    <text x="17" y="23" font-family="{font_family_css}" font-size="11" font-weight="700" letter-spacing="1" fill="{thread}" text-anchor="middle" filter="url(#thread-glow)">{monogram}</text>
  </g>
</svg>'''


def get_uyo_map_svg():
    """
    Renders an interactive high-fashion architectural street map of Uyo,
    Akwa Ibom State, highlighting 164 Udoumana Street, Aka Road, Nwaniba Road,
    and Ibom Plaza.
    """
    return '''<svg viewBox="0 0 460 360" width="100%" height="100%" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="map-bg" x1="0" y1="0" x2="460" y2="360" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FAF6F0"/>
      <stop offset="100%" stop-color="#EDE2D5"/>
    </linearGradient>
    <filter id="pin-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="rgba(33,24,21,0.25)"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="460" height="360" rx="16" fill="url(#map-bg)"/>

  <!-- Uyo City Street Grid Blocks -->
  <rect x="30" y="30" width="80" height="70" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>
  <rect x="130" y="30" width="110" height="70" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>
  <rect x="260" y="30" width="170" height="70" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>

  <rect x="30" y="125" width="80" height="90" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>
  <rect x="130" y="125" width="85" height="90" rx="8" fill="#FBF8F4" stroke="#E3D5C5" stroke-width="1"/>
  <rect x="240" y="125" width="190" height="90" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>

  <rect x="30" y="240" width="120" height="90" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>
  <rect x="175" y="240" width="120" height="90" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>
  <rect x="315" y="240" width="115" height="90" rx="8" fill="#F4ECE2" stroke="#E3D5C5" stroke-width="1"/>

  <!-- Major Arterial Roads in Uyo -->
  <!-- Aka Road -->
  <path d="M0 110 L460 110" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round"/>
  <path d="M0 110 L460 110" stroke="#C49E65" stroke-width="2" stroke-dasharray="8 6"/>

  <!-- Nwaniba / Oron Road Junction Axis -->
  <path d="M120 0 L120 360" stroke="#FFFFFF" stroke-width="14"/>
  <path d="M120 0 L120 360" stroke="#DDD1C2" stroke-width="1.5"/>

  <!-- Udoumana Street (Prominent Highlight) -->
  <path d="M225 360 L225 110 L280 0" stroke="#FFE9E4" stroke-width="18"/>
  <path d="M225 360 L225 110 L280 0" stroke="#C48275" stroke-width="3"/>

  <!-- Street Label Callouts -->
  <text x="18" y="104" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="700" fill="#756254" letter-spacing="1">AKA ROAD</text>
  <text x="375" y="104" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="700" fill="#756254" letter-spacing="1">IBOM PLAZA →</text>
  <text x="126" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="600" fill="#8E7D73">NWANIBA RD</text>
  <text x="235" y="280" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="800" fill="#C48275" letter-spacing="1.2">UDOUMANA STREET</text>

  <!-- Landmark: Ewet Housing Estate hint -->
  <text x="280" y="60" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="600" fill="#A89688">EWET HOUSING DIRECTION</text>

  <!-- 164 Udoumana Street Boutique Pin Marker -->
  <g transform="translate(225, 175)" filter="url(#pin-shadow)">
    <!-- Radar pulse circles -->
    <circle cx="0" cy="0" r="28" fill="#C48275" fill-opacity="0.18">
      <animate attributeName="r" values="16;34;16" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="fill-opacity" values="0.3;0;0.3" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="16" fill="#C48275" fill-opacity="0.3"/>
    
    <!-- Pin Body -->
    <path d="M0 -22 C-10 -22 -16 -14 -16 -4 C-16 8 0 22 0 22 C0 22 16 8 16 -4 C16 -14 10 -22 0 -22 Z" fill="#211815" stroke="#C29B38" stroke-width="2"/>
    <circle cx="0" cy="-6" r="6.5" fill="#C29B38"/>
    <text x="0" y="-3.5" font-family="'Playfair Display', serif" font-size="6" font-weight="700" fill="#211815" text-anchor="middle">DC</text>
  </g>

  <!-- Location Badge Card Overlay -->
  <g transform="translate(242, 142)">
    <rect width="180" height="62" rx="10" fill="#FFFFFF" stroke="#E5D8CC" stroke-width="1.2" filter="url(#pin-shadow)"/>
    <text x="14" y="22" font-family="'Playfair Display', serif" font-size="11" font-weight="700" fill="#211815">Debbie's Collection</text>
    <text x="14" y="38" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="600" fill="#C48275">164 Udoumana St, Uyo</text>
    <text x="14" y="50" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" fill="#8E7D73">Akwa Ibom State • Atelier & Boutique</text>
  </g>
</svg>'''

