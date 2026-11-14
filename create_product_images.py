"""
Generate high-fidelity, standalone SVG vector illustrations for all 12 products.
"""

import os

IMAGES_DIR = "application/images"
os.makedirs(IMAGES_DIR, exist_ok=True)

SVGS = {
    "headphones.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="hpBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </radialGradient>
    <linearGradient id="bandGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="metalGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#cbd5e1"/>
      <stop offset="50%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <linearGradient id="glowGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <filter id="hpShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="10" flood-opacity="0.15"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#hpBg)"/>
  
  <!-- Outer Headband -->
  <path d="M 100 220 A 110 110 0 0 1 300 220" fill="none" stroke="url(#bandGrad)" stroke-width="26" stroke-linecap="round" filter="url(#hpShadow)"/>
  <path d="M 125 180 A 90 90 0 0 1 275 180" fill="none" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
  
  <!-- Headband Soft Cushion -->
  <path d="M 130 160 A 85 85 0 0 1 270 160" fill="none" stroke="#1e293b" stroke-width="14" stroke-linecap="round"/>

  <!-- Left Hinge & Slider -->
  <rect x="94" y="200" width="16" height="35" rx="4" fill="url(#metalGrad)"/>
  <rect x="98" y="215" width="8" height="15" fill="#64748b"/>

  <!-- Right Hinge & Slider -->
  <rect x="290" y="200" width="16" height="35" rx="4" fill="url(#metalGrad)"/>
  <rect x="294" y="215" width="8" height="15" fill="#64748b"/>

  <!-- Left Earcup Assembly -->
  <g filter="url(#hpShadow)">
    <!-- Outer Cup -->
    <ellipse cx="102" cy="255" rx="36" ry="50" fill="url(#bandGrad)"/>
    <ellipse cx="102" cy="255" rx="30" ry="44" fill="url(#glowGrad)" opacity="0.3"/>
    <circle cx="102" cy="255" r="18" fill="url(#metalGrad)"/>
    <!-- LED Glow Ring -->
    <circle cx="102" cy="255" r="12" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <!-- Plush Pad -->
    <path d="M 118 215 C 130 230 130 280 118 295 C 110 295 106 280 106 255 C 106 230 110 215 118 215 Z" fill="#0f172a"/>
  </g>

  <!-- Right Earcup Assembly -->
  <g filter="url(#hpShadow)">
    <!-- Outer Cup -->
    <ellipse cx="298" cy="255" rx="36" ry="50" fill="url(#bandGrad)"/>
    <ellipse cx="298" cy="255" rx="30" ry="44" fill="url(#glowGrad)" opacity="0.3"/>
    <circle cx="298" cy="255" r="18" fill="url(#metalGrad)"/>
    <!-- LED Glow Ring -->
    <circle cx="298" cy="255" r="12" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <!-- Plush Pad -->
    <path d="M 282 215 C 270 230 270 280 282 295 C 290 295 294 280 294 255 C 294 230 290 215 282 215 Z" fill="#0f172a"/>
  </g>

  <!-- Wireless Audio Waves Badge -->
  <g transform="translate(180, 240)">
    <circle cx="20" cy="20" r="14" fill="#2563eb" opacity="0.1"/>
    <path d="M 12 20 Q 20 12 28 20 M 15 20 Q 20 15 25 20" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round"/>
  </g>
</svg>""",

    "laptop.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="laptopBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f5f3ff"/>
      <stop offset="100%" stop-color="#ede9fe"/>
    </radialGradient>
    <linearGradient id="screenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="40%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#312e81"/>
    </linearGradient>
    <linearGradient id="chassisGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="50%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <filter id="dropShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#laptopBg)"/>

  <!-- Screen Lid Assembly -->
  <g filter="url(#dropShadow)">
    <!-- Outer Bezel -->
    <rect x="70" y="80" width="260" height="175" rx="10" fill="#1e293b" stroke="#334155" stroke-width="2"/>
    <!-- Display Panel -->
    <rect x="80" y="90" width="240" height="155" rx="4" fill="url(#screenGrad)"/>
    
    <!-- Screen Content: Code / Data Waves Graphic -->
    <path d="M 85 200 Q 140 130 200 170 T 315 130 L 315 240 L 85 240 Z" fill="#6366f1" opacity="0.35"/>
    <path d="M 85 215 Q 150 160 220 190 T 315 160 L 315 240 L 85 240 Z" fill="#38bdf8" opacity="0.4"/>
    
    <!-- Code Lines Mockup -->
    <rect x="95" y="105" width="55" height="5" rx="2.5" fill="#38bdf8"/>
    <rect x="155" y="105" width="30" height="5" rx="2.5" fill="#f43f5e"/>
    <rect x="105" y="118" width="80" height="4" rx="2" fill="#cbd5e1" opacity="0.6"/>
    <rect x="105" y="128" width="60" height="4" rx="2" fill="#cbd5e1" opacity="0.6"/>

    <!-- Webcam & Sensor -->
    <circle cx="200" cy="85" r="2.5" fill="#0f172a"/>
    <circle cx="200" cy="85" r="1" fill="#38bdf8"/>
  </g>

  <!-- Laptop Base Chassis -->
  <g filter="url(#dropShadow)">
    <!-- Main Lower Deck -->
    <path d="M 40 255 L 70 255 L 330 255 L 360 255 L 345 285 L 55 285 Z" fill="url(#chassisGrad)"/>
    <rect x="40" y="254" width="320" height="3" fill="#cbd5e1"/>
    
    <!-- Keyboard Wells & Trackpad -->
    <rect x="95" y="258" width="210" height="12" rx="2" fill="#1e293b" opacity="0.85"/>
    <!-- Individual Key Visuals -->
    <line x1="105" y1="264" x2="295" y2="264" stroke="#475569" stroke-dasharray="8 3" stroke-width="3"/>
    
    <!-- Trackpad -->
    <rect x="170" y="272" width="60" height="10" rx="2" fill="#94a3b8" stroke="#64748b" stroke-width="0.8"/>
    <!-- Front Lip Notch -->
    <rect x="185" y="284" width="30" height="2" rx="1" fill="#475569"/>
  </g>
</svg>""",

    "smartwatch.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="watchBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#eef2ff"/>
      <stop offset="100%" stop-color="#e0e7ff"/>
    </radialGradient>
    <linearGradient id="strapGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="watchShadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#watchBg)"/>

  <!-- Top Silicone Strap -->
  <path d="M 155 40 L 245 40 L 235 130 L 165 130 Z" fill="url(#strapGrad)" filter="url(#watchShadow)"/>
  <!-- Strap Ribs -->
  <line x1="165" y1="65" x2="235" y2="65" stroke="#334155" stroke-width="2"/>
  <line x1="168" y1="85" x2="232" y2="85" stroke="#334155" stroke-width="2"/>
  <line x1="170" y1="105" x2="230" y2="105" stroke="#334155" stroke-width="2"/>

  <!-- Bottom Silicone Strap -->
  <path d="M 165 270 L 235 270 L 245 360 L 155 360 Z" fill="url(#strapGrad)" filter="url(#watchShadow)"/>
  <line x1="168" y1="295" x2="232" y2="295" stroke="#334155" stroke-width="2"/>
  <line x1="165" y1="315" x2="235" y2="315" stroke="#334155" stroke-width="2"/>
  <line x1="162" y1="335" x2="238" y2="335" stroke="#334155" stroke-width="2"/>

  <!-- Watch Chassis Outer -->
  <rect x="135" y="115" width="130" height="170" rx="36" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="2" filter="url(#watchShadow)"/>
  
  <!-- Digital Crown (Button) -->
  <rect x="264" y="150" width="8" height="28" rx="3" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>
  <!-- Secondary Button -->
  <rect x="264" y="195" width="6" height="35" rx="2" fill="#334155"/>

  <!-- Watch Screen OLED Surface -->
  <rect x="145" y="125" width="110" height="150" rx="28" fill="#000000"/>

  <!-- UI Displays: Time -->
  <text x="200" y="170" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="bold" fill="#ffffff" text-anchor="middle">10:42</text>
  <text x="200" y="188" font-family="sans-serif" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">THU, NOV 14</text>

  <!-- Activity Rings -->
  <circle cx="200" cy="225" r="22" fill="none" stroke="#334155" stroke-width="4"/>
  <circle cx="200" cy="225" r="22" fill="none" stroke="#22c55e" stroke-width="4" stroke-dasharray="100 40"/>
  <circle cx="200" cy="225" r="16" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="70 40"/>
  <circle cx="200" cy="225" r="10" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="40 30"/>

  <!-- Pulse Icon -->
  <path d="M 194 225 L 197 225 L 199 221 L 201 229 L 203 223 L 205 225 L 208 225" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-linecap="round"/>
</svg>""",

    "camera.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="camBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f0fdfa"/>
      <stop offset="100%" stop-color="#ccfbf1"/>
    </radialGradient>
    <linearGradient id="camBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <radialGradient id="lensOuter" cx="45%" cy="45%" r="55%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="70%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
    <radialGradient id="lensGlass" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="40%" stop-color="#0284c7"/>
      <stop offset="80%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#09090b"/>
    </radialGradient>
    <filter id="camShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="10" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#camBg)"/>

  <!-- Main Camera Body -->
  <rect x="75" y="125" width="250" height="165" rx="24" fill="url(#camBody)" stroke="#475569" stroke-width="2" filter="url(#camShadow)"/>
  
  <!-- Top Shutter Button -->
  <rect x="110" y="112" width="38" height="14" rx="3" fill="#dc2626"/>
  <rect x="113" y="110" width="32" height="4" rx="1.5" fill="#f87171"/>

  <!-- Textured Grips on side -->
  <rect x="85" y="145" width="14" height="125" rx="4" fill="#1e293b"/>
  <line x1="88" y1="155" x2="96" y2="155" stroke="#475569" stroke-width="2"/>
  <line x1="88" y1="165" x2="96" y2="165" stroke="#475569" stroke-width="2"/>
  <line x1="88" y1="175" x2="96" y2="175" stroke="#475569" stroke-width="2"/>
  <line x1="88" y1="185" x2="96" y2="185" stroke="#475569" stroke-width="2"/>

  <!-- Front Mini Display -->
  <rect x="115" y="150" width="75" height="50" rx="6" fill="#020617" stroke="#1e293b" stroke-width="1.5"/>
  <text x="152" y="172" font-family="sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">4K 60FPS</text>
  <text x="152" y="188" font-family="sans-serif" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">REC 00:14:28</text>

  <!-- Large Optical Lens Housing -->
  <g filter="url(#camShadow)">
    <circle cx="245" cy="205" r="56" fill="url(#lensOuter)" stroke="#475569" stroke-width="3"/>
    <circle cx="245" cy="205" r="44" fill="url(#lensGlass)"/>
    <!-- Lens Reflection Arcs -->
    <path d="M 220 180 A 32 32 0 0 1 270 180" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
    <path d="M 230 190 A 20 20 0 0 1 260 190" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
    <circle cx="258" cy="195" r="4" fill="#ffffff" opacity="0.8"/>
  </g>

  <!-- Recording LED Status Indicator -->
  <circle cx="120" cy="225" r="5" fill="#ef4444"/>
  <circle cx="120" cy="225" r="2" fill="#ffffff"/>
  <text x="132" y="228" font-family="sans-serif" font-size="9" font-weight="bold" fill="#94a3b8">ULTRA STABLE</text>
</svg>""",

    "tshirt.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="tshirtBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff1f2"/>
      <stop offset="100%" stop-color="#fee2e2"/>
    </radialGradient>
    <linearGradient id="teeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="50%" stop-color="#172554"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="teeShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity="0.18"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#tshirtBg)"/>

  <!-- Minimal Wooden Hanger Hook -->
  <path d="M 200 65 Q 210 50 200 40 Q 190 30 180 40 Q 170 55 195 65" fill="none" stroke="#b45309" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M 140 100 L 200 70 L 260 100" fill="none" stroke="#d97706" stroke-width="6" stroke-linecap="round"/>

  <!-- Main T-Shirt Body -->
  <path d="M 150 95 L 125 110 L 80 150 L 115 190 L 140 165 L 140 330 L 260 330 L 260 165 L 285 190 L 320 150 L 275 110 L 250 95 C 235 125 165 125 150 95 Z" fill="url(#teeGrad)" filter="url(#teeShadow)"/>

  <!-- Ribbed Collar -->
  <path d="M 150 95 C 165 125 235 125 250 95 C 235 105 165 105 150 95 Z" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
  
  <!-- Subtle Fabric Folds & Shading -->
  <path d="M 142 170 Q 170 210 160 325" fill="none" stroke="#1d4ed8" stroke-width="2" opacity="0.4"/>
  <path d="M 258 170 Q 230 210 240 325" fill="none" stroke="#1e40af" stroke-width="2" opacity="0.4"/>
  
  <!-- Sleeve Seams -->
  <path d="M 140 165 L 120 115" fill="none" stroke="#1d4ed8" stroke-width="1.5" stroke-dasharray="3 2"/>
  <path d="M 260 165 L 280 115" fill="none" stroke="#1d4ed8" stroke-width="1.5" stroke-dasharray="3 2"/>

  <!-- Minimal Brand Chest Tag -->
  <rect x="215" y="165" width="22" height="14" rx="2" fill="#2563eb" opacity="0.8"/>
  <text x="226" y="175" font-family="sans-serif" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">ZM</text>
</svg>""",

    "jeans.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="jeansBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f0f9ff"/>
      <stop offset="100%" stop-color="#e0f2fe"/>
    </radialGradient>
    <linearGradient id="denimGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1d4ed8"/>
      <stop offset="50%" stop-color="#1e40af"/>
      <stop offset="100%" stop-color="#172554"/>
    </linearGradient>
    <filter id="denimShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#jeansBg)"/>

  <!-- Denim Trouser Outline -->
  <g filter="url(#denimShadow)">
    <path d="M 130 75 L 270 75 L 265 140 L 255 350 L 210 350 L 200 170 L 190 350 L 145 350 L 135 140 Z" fill="url(#denimGrad)"/>
    
    <!-- Waistband & Belt Loops -->
    <rect x="130" y="75" width="140" height="18" fill="#1e3a8a" stroke="#ca8a04" stroke-width="1.5"/>
    <rect x="150" y="73" width="7" height="22" rx="1.5" fill="#172554"/>
    <rect x="196" y="73" width="7" height="22" rx="1.5" fill="#172554"/>
    <rect x="243" y="73" width="7" height="22" rx="1.5" fill="#172554"/>

    <!-- Brass Waist Button -->
    <circle cx="200" cy="84" r="5" fill="#eab308" stroke="#a16207" stroke-width="1"/>

    <!-- Fly Seam & Rivets -->
    <path d="M 200 93 L 200 135 Q 200 150 185 155" fill="none" stroke="#eab308" stroke-width="2" stroke-linecap="round"/>
    
    <!-- Left & Right Curved Pockets -->
    <path d="M 133 93 Q 155 93 165 115 L 160 135" fill="none" stroke="#eab308" stroke-width="2"/>
    <circle cx="165" cy="115" r="2.5" fill="#ca8a04"/>

    <path d="M 267 93 Q 245 93 235 115 L 240 135" fill="none" stroke="#eab308" stroke-width="2"/>
    <circle cx="235" cy="115" r="2.5" fill="#ca8a04"/>

    <!-- Contrast Leg Seams -->
    <line x1="172" y1="165" x2="175" y2="350" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
    <line x1="228" y1="165" x2="225" y2="350" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
    
    <!-- Bottom Hem Folds -->
    <rect x="145" y="344" width="45" height="6" fill="#172554" stroke="#eab308" stroke-width="1.2"/>
    <rect x="210" y="344" width="45" height="6" fill="#172554" stroke="#eab308" stroke-width="1.2"/>
  </g>
</svg>""",

    "jacket.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="jacketBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="100%" stop-color="#fef3c7"/>
    </radialGradient>
    <linearGradient id="fleeceGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <filter id="jktShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#jacketBg)"/>

  <!-- Main Fleece Silhouette -->
  <g filter="url(#jktShadow)">
    <path d="M 160 80 L 125 105 L 75 160 L 115 195 L 135 170 L 135 340 L 265 340 L 265 170 L 285 195 L 325 160 L 275 105 L 240 80 Z" fill="url(#fleeceGrad)"/>

    <!-- Stand-Up High Collar -->
    <path d="M 160 80 L 160 55 C 175 48 225 48 240 55 L 240 80 Z" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>

    <!-- Full Front Metal Zipper -->
    <line x1="200" y1="52" x2="200" y2="340" stroke="#cbd5e1" stroke-width="3"/>
    <rect x="196" y="90" width="8" height="14" rx="2" fill="#f59e0b"/>

    <!-- Contrast Chest Pocket -->
    <rect x="145" y="130" width="40" height="45" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <line x1="150" y1="138" x2="180" y2="138" stroke="#cbd5e1" stroke-width="2"/>
    <circle cx="180" cy="138" r="2.5" fill="#f59e0b"/>

    <!-- Side Hand-Warmer Pockets -->
    <path d="M 145 250 L 165 270" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
    <path d="M 255 250 L 235 270" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>

    <!-- Elastic Cuffs & Waistband -->
    <rect x="75" y="160" width="40" height="8" rx="2" fill="#0f172a" transform="rotate(-35 75 160)"/>
    <rect x="300" y="185" width="40" height="8" rx="2" fill="#0f172a" transform="rotate(35 300 185)"/>
    <rect x="135" y="334" width="130" height="7" fill="#0f172a"/>
  </g>
</svg>""",

    "clean_code.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bookBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fefce8"/>
      <stop offset="100%" stop-color="#fef08a"/>
    </radialGradient>
    <linearGradient id="coverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="50%" stop-color="#1e40af"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="bookShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="8" dy="14" stdDeviation="10" flood-opacity="0.25"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bookBg)"/>

  <!-- 3D Perspective Hardcover Book -->
  <g filter="url(#bookShadow)">
    <!-- Pages Block (Bottom Thickness) -->
    <path d="M 125 330 L 290 315 L 295 325 L 125 340 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <path d="M 290 95 L 305 105 L 295 325 L 290 315 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1"/>
    <!-- Page Edge Lines -->
    <line x1="295" y1="110" x2="292" y2="318" stroke="#94a3b8" stroke-dasharray="2 2"/>
    <line x1="300" y1="115" x2="294" y2="322" stroke="#94a3b8" stroke-dasharray="2 2"/>

    <!-- Front Cover -->
    <path d="M 110 75 L 290 95 L 290 315 L 110 330 Z" fill="url(#coverGrad)" stroke="#3b82f6" stroke-width="1.5"/>

    <!-- Spine -->
    <path d="M 95 90 L 110 75 L 110 330 L 95 345 Z" fill="#0f172a"/>

    <!-- Ribbon Bookmark -->
    <path d="M 200 95 L 200 345 L 208 335 L 216 345 L 216 95 Z" fill="#ef4444"/>

    <!-- Cover Art & Typography -->
    <text x="200" y="150" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="1.5">CLEAN CODE</text>
    <text x="200" y="172" font-family="sans-serif" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle" letter-spacing="0.5">&amp; SOFTWARE ARCHITECTURE</text>
    
    <!-- Geometric Tech Motif -->
    <circle cx="200" cy="225" r="30" fill="none" stroke="#60a5fa" stroke-width="2"/>
    <polygon points="200,205 220,235 180,235" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="200" cy="225" r="4" fill="#38bdf8"/>

    <!-- Author Badge -->
    <rect x="145" y="275" width="110" height="18" rx="4" fill="#1e293b"/>
    <text x="200" y="287" font-family="sans-serif" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">A HANDBOOK OF CRAFTSMANSHIP</text>
  </g>
</svg>""",

    "selenium_book.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="selBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f0fdf4"/>
      <stop offset="100%" stop-color="#dcfce7"/>
    </radialGradient>
    <linearGradient id="selCover" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="50%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
    <filter id="selShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="8" dy="14" stdDeviation="10" flood-opacity="0.25"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#selBg)"/>

  <!-- 3D Hardcover Book -->
  <g filter="url(#selShadow)">
    <!-- Page Block -->
    <path d="M 125 330 L 290 315 L 295 325 L 125 340 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <path d="M 290 95 L 305 105 L 295 325 L 290 315 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="295" y1="110" x2="292" y2="318" stroke="#94a3b8" stroke-dasharray="2 2"/>

    <!-- Front Cover -->
    <path d="M 110 75 L 290 95 L 290 315 L 110 330 Z" fill="url(#selCover)" stroke="#10b981" stroke-width="1.5"/>

    <!-- Spine -->
    <path d="M 95 90 L 110 75 L 110 330 L 95 345 Z" fill="#022c22"/>

    <!-- Cover Content -->
    <text x="200" y="145" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="1">TEST AUTOMATION</text>
    <text x="200" y="165" font-family="sans-serif" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">WITH SELENIUM &amp; PYTEST</text>
    
    <!-- Central Automation Browser Mockup -->
    <g transform="translate(150, 185)">
      <rect width="100" height="65" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <!-- Window Controls -->
      <circle cx="12" cy="12" r="3" fill="#ef4444"/>
      <circle cx="22" cy="12" r="3" fill="#f59e0b"/>
      <circle cx="32" cy="12" r="3" fill="#10b981"/>
      <line x1="42" y1="12" x2="88" y2="12" stroke="#334155" stroke-width="2"/>
      <!-- Checkmark Success Icon -->
      <circle cx="50" cy="40" r="14" fill="#10b981" opacity="0.2"/>
      <path d="M 43 40 L 48 45 L 57 35" fill="none" stroke="#34d399" stroke-width="3" stroke-linecap="round"/>
    </g>

    <!-- Badge -->
    <rect x="145" y="275" width="110" height="20" rx="4" fill="#022c22"/>
    <text x="200" y="288" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#a7f3d0" text-anchor="middle">PAGE OBJECT MODEL (POM)</text>
  </g>
</svg>""",

    "coffee_maker.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="coffeeBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff7ed"/>
      <stop offset="100%" stop-color="#ffedd5"/>
    </radialGradient>
    <linearGradient id="chromeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="40%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <filter id="machineShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#coffeeBg)"/>

  <!-- Espresso Machine Body -->
  <g filter="url(#machineShadow)">
    <!-- Top Warming Tray -->
    <rect x="110" y="80" width="180" height="15" rx="3" fill="url(#chromeGrad)"/>
    <line x1="125" y1="88" x2="275" y2="88" stroke="#475569" stroke-dasharray="6 3" stroke-width="2"/>

    <!-- Main Housing -->
    <rect x="115" y="95" width="170" height="145" fill="url(#chromeGrad)" stroke="#475569" stroke-width="1.5"/>

    <!-- Pressure Gauge Manometer -->
    <circle cx="200" cy="140" r="22" fill="#ffffff" stroke="#334155" stroke-width="2"/>
    <circle cx="200" cy="140" r="18" fill="none" stroke="#e2e8f0" stroke-width="1"/>
    <!-- Gauge Needle -->
    <line x1="200" y1="140" x2="208" y2="128" stroke="#dc2626" stroke-width="2" stroke-linecap="round"/>
    <circle cx="200" cy="140" r="2" fill="#0f172a"/>
    <text x="200" y="152" font-family="sans-serif" font-size="6" font-weight="bold" fill="#64748b" text-anchor="middle">15 BAR</text>

    <!-- Chrome Toggle Switches -->
    <rect x="140" y="132" width="16" height="16" rx="3" fill="#1e293b"/>
    <circle cx="148" cy="140" r="3" fill="#22c55e"/>
    
    <rect x="244" y="132" width="16" height="16" rx="3" fill="#1e293b"/>
    <circle cx="252" cy="140" r="3" fill="#eab308"/>

    <!-- Group Head & Portafilter -->
    <rect x="175" y="240" width="50" height="15" rx="2" fill="#1e293b"/>
    <!-- Portafilter Spout -->
    <path d="M 180 255 L 220 255 L 210 270 L 190 270 Z" fill="url(#chromeGrad)"/>
    <!-- Handle -->
    <rect x="220" y="245" width="60" height="12" rx="4" fill="#0f172a"/>

    <!-- Espresso Cup with Crema -->
    <path d="M 185 295 L 215 295 L 210 325 L 190 325 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <!-- Crema -->
    <ellipse cx="200" cy="298" rx="12" ry="3" fill="#78350f"/>
    <!-- Steam Swirls -->
    <path d="M 197 290 Q 200 280 196 275" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
    <path d="M 203 290 Q 206 280 202 275" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>

    <!-- Steam Wand -->
    <path d="M 260 240 L 270 290" fill="none" stroke="url(#chromeGrad)" stroke-width="5" stroke-linecap="round"/>

    <!-- Drip Tray Grid Base -->
    <rect x="110" y="325" width="180" height="25" rx="4" fill="#334155"/>
    <rect x="115" y="325" width="170" height="5" fill="#1e293b"/>
    <line x1="125" y1="327" x2="275" y2="327" stroke="#64748b" stroke-dasharray="4 2" stroke-width="2"/>
  </g>
</svg>""",

    "air_purifier.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="airBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </radialGradient>
    <linearGradient id="towerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#e2e8f0"/>
      <stop offset="35%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#cbd5e1"/>
    </linearGradient>
    <filter id="airShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity="0.18"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#airBg)"/>

  <!-- Tower Body -->
  <g filter="url(#airShadow)">
    <!-- Main Cylinder -->
    <rect x="140" y="90" width="120" height="240" rx="20" fill="url(#towerGrad)" stroke="#cbd5e1" stroke-width="1.5"/>

    <!-- Top Cap -->
    <ellipse cx="200" cy="90" rx="60" ry="14" fill="#0f172a"/>
    <ellipse cx="200" cy="90" rx="52" ry="10" fill="#1e293b"/>
    <!-- Glowing Air Quality Ring (Blue = Clean) -->
    <ellipse cx="200" cy="90" rx="42" ry="8" fill="none" stroke="#38bdf8" stroke-width="3"/>

    <!-- OLED Status Display on Front -->
    <circle cx="200" cy="140" r="22" fill="#020617" stroke="#334155" stroke-width="1.5"/>
    <circle cx="200" cy="140" r="20" fill="none" stroke="#22c55e" stroke-width="2"/>
    <text x="200" y="138" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">008</text>
    <text x="200" y="148" font-family="sans-serif" font-size="6" font-weight="bold" fill="#4ade80" text-anchor="middle">PM2.5</text>

    <!-- Perforated Intake Mesh -->
    <g fill="#94a3b8" opacity="0.6">
      <circle cx="160" cy="200" r="1.5"/><circle cx="170" cy="200" r="1.5"/><circle cx="180" cy="200" r="1.5"/><circle cx="190" cy="200" r="1.5"/><circle cx="200" cy="200" r="1.5"/><circle cx="210" cy="200" r="1.5"/><circle cx="220" cy="200" r="1.5"/><circle cx="230" cy="200" r="1.5"/><circle cx="240" cy="200" r="1.5"/>
      <circle cx="155" cy="210" r="1.5"/><circle cx="165" cy="210" r="1.5"/><circle cx="175" cy="210" r="1.5"/><circle cx="185" cy="210" r="1.5"/><circle cx="195" cy="210" r="1.5"/><circle cx="205" cy="210" r="1.5"/><circle cx="215" cy="210" r="1.5"/><circle cx="225" cy="210" r="1.5"/><circle cx="235" cy="210" r="1.5"/><circle cx="245" cy="210" r="1.5"/>
      <circle cx="160" cy="220" r="1.5"/><circle cx="170" cy="220" r="1.5"/><circle cx="180" cy="220" r="1.5"/><circle cx="190" cy="220" r="1.5"/><circle cx="200" cy="220" r="1.5"/><circle cx="210" cy="220" r="1.5"/><circle cx="220" cy="220" r="1.5"/><circle cx="230" cy="220" r="1.5"/><circle cx="240" cy="220" r="1.5"/>
      <circle cx="155" cy="230" r="1.5"/><circle cx="165" cy="230" r="1.5"/><circle cx="175" cy="230" r="1.5"/><circle cx="185" cy="230" r="1.5"/><circle cx="195" cy="230" r="1.5"/><circle cx="205" cy="230" r="1.5"/><circle cx="215" cy="230" r="1.5"/><circle cx="225" cy="230" r="1.5"/><circle cx="235" cy="230" r="1.5"/><circle cx="245" cy="230" r="1.5"/>
      <circle cx="160" cy="240" r="1.5"/><circle cx="170" cy="240" r="1.5"/><circle cx="180" cy="240" r="1.5"/><circle cx="190" cy="240" r="1.5"/><circle cx="200" cy="240" r="1.5"/><circle cx="210" cy="240" r="1.5"/><circle cx="220" cy="240" r="1.5"/><circle cx="230" cy="240" r="1.5"/><circle cx="240" cy="240" r="1.5"/>
      <circle cx="155" cy="250" r="1.5"/><circle cx="165" cy="250" r="1.5"/><circle cx="175" cy="250" r="1.5"/><circle cx="185" cy="250" r="1.5"/><circle cx="195" cy="250" r="1.5"/><circle cx="205" cy="250" r="1.5"/><circle cx="215" cy="250" r="1.5"/><circle cx="225" cy="250" r="1.5"/><circle cx="235" cy="250" r="1.5"/><circle cx="245" cy="250" r="1.5"/>
      <circle cx="160" cy="260" r="1.5"/><circle cx="170" cy="260" r="1.5"/><circle cx="180" cy="260" r="1.5"/><circle cx="190" cy="260" r="1.5"/><circle cx="200" cy="260" r="1.5"/><circle cx="210" cy="260" r="1.5"/><circle cx="220" cy="260" r="1.5"/><circle cx="230" cy="260" r="1.5"/><circle cx="240" cy="260" r="1.5"/>
      <circle cx="155" cy="270" r="1.5"/><circle cx="165" cy="270" r="1.5"/><circle cx="175" cy="270" r="1.5"/><circle cx="185" cy="270" r="1.5"/><circle cx="195" cy="270" r="1.5"/><circle cx="205" cy="270" r="1.5"/><circle cx="215" cy="270" r="1.5"/><circle cx="225" cy="270" r="1.5"/><circle cx="235" cy="270" r="1.5"/><circle cx="245" cy="270" r="1.5"/>
      <circle cx="160" cy="280" r="1.5"/><circle cx="170" cy="280" r="1.5"/><circle cx="180" cy="280" r="1.5"/><circle cx="190" cy="280" r="1.5"/><circle cx="200" cy="280" r="1.5"/><circle cx="210" cy="280" r="1.5"/><circle cx="220" cy="280" r="1.5"/><circle cx="230" cy="280" r="1.5"/><circle cx="240" cy="280" r="1.5"/>
    </g>

    <!-- Clean Air Flow Arrows -->
    <path d="M 130 80 Q 150 40 165 60" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" opacity="0.6"/>
    <path d="M 270 80 Q 250 40 235 60" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" opacity="0.6"/>
  </g>
</svg>""",

    "dutch_oven.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="ovenBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff1f2"/>
      <stop offset="100%" stop-color="#fecaca"/>
    </radialGradient>
    <radialGradient id="enamelGrad" cx="40%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="50%" stop-color="#e11d48"/>
      <stop offset="85%" stop-color="#be123c"/>
      <stop offset="100%" stop-color="#881337"/>
    </radialGradient>
    <linearGradient id="lidKnob" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#cbd5e1"/>
      <stop offset="50%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <filter id="ovenShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="14" stdDeviation="12" flood-opacity="0.22"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#ovenBg)"/>

  <!-- Dutch Oven Assembly -->
  <g filter="url(#ovenShadow)">
    <!-- Side Handles -->
    <path d="M 75 190 C 60 190 60 220 75 220 L 95 220 L 95 190 Z" fill="#881337" stroke="#4c0519" stroke-width="2"/>
    <path d="M 325 190 C 340 190 340 220 325 220 L 305 220 L 305 190 Z" fill="#881337" stroke="#4c0519" stroke-width="2"/>

    <!-- Pot Base -->
    <path d="M 90 185 C 90 280 120 310 200 310 C 280 310 310 280 310 185 Z" fill="url(#enamelGrad)" stroke="#9f1239" stroke-width="2"/>
    <!-- Specular Highlight on Pot -->
    <path d="M 115 200 C 115 260 135 285 180 295" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.35"/>

    <!-- Lid Rim -->
    <ellipse cx="200" cy="180" rx="112" ry="16" fill="#be123c" stroke="#881337" stroke-width="2"/>

    <!-- Domed Lid -->
    <path d="M 90 180 C 90 135 140 125 200 125 C 260 125 310 135 310 180 Z" fill="url(#enamelGrad)" stroke="#9f1239" stroke-width="1.5"/>
    <ellipse cx="200" cy="155" rx="75" ry="8" fill="none" stroke="#ffffff" stroke-width="2" opacity="0.35"/>

    <!-- Stainless Steel Knob Base & Handle -->
    <rect x="194" y="112" width="12" height="15" fill="#475569"/>
    <ellipse cx="200" cy="112" rx="18" ry="7" fill="url(#lidKnob)" stroke="#334155" stroke-width="1.5"/>
  </g>
</svg>"""
}

for fname, content in SVGS.items():
    fpath = os.path.join(IMAGES_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created: {fpath}")

print("All 12 product illustrations successfully generated!")

