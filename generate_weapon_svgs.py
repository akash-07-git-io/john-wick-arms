import os

img_dir = r"d:\Akash Files\Akash L Clg Documents\Web prg\john-wick-arms\images"
os.makedirs(img_dir, exist_ok=True)

weapons = [
    # Sidearms
    ("pit_viper.svg", "TTI JW4 PIT VIPER", "9x19mm Major", "Sidearms", "Single-Port Compensator & Taran Stippled Frame", "#D4AF37", "pistol"),
    ("combat_master_jw2.svg", "GLOCK 34 COMBAT MASTER", "9x19mm Parabellum", "Sidearms", "Taran Tactical Ported Slide & Fiber Optic", "#C5A059", "pistol"),
    ("sti_2011_jw3.svg", "TTI STI 2011 COMBAT MASTER", "9mm Major", "Sidearms", "Billet Steel 2011 Frame & Flared Magwell", "#D4AF37", "pistol"),
    ("hk_p30l.svg", "HECKLER & KOCH P30L", "9x19mm NATO", "Sidearms", "Custom Counterweight Compensator & Polygonal Rifling", "#A0AAB2", "pistol"),
    ("kimber_1911.svg", "KIMBER 1911 WARRIOR", ".45 ACP", "Sidearms", "Desert Tan Finish & G10 Tactical Grips (7 Rounds)", "#D2B48C", "pistol"),
    ("glock26.svg", "GLOCK 26 COMBAT MASTER", "9x19mm", "Sidearms", "Subcompact Concealed Carry Backup System", "#8A9EA7", "pistol"),

    # Shotguns
    ("benelli_m4.svg", "BENELLI M4 TACTICAL PORTED", "12-Gauge (3\" Magnum)", "Shotguns", "Auto-Regulating Gas System (ARGO) & Ghost Ring", "#D4AF37", "shotgun"),
    ("gen12_dragons_breath.svg", "GENESIS ARMS GEN-12", "12-Gauge Dragon's Breath", "Shotguns", "Short-Barrel Breacher Firing Incendiary Slugs", "#FF4500", "shotgun"),
    ("remington870.svg", "REMINGTON 870 BREACHER", "12-Gauge Tactical", "Shotguns", "Stand-Off Breaching Choke & Magpul SGA Stock", "#A0AAB2", "shotgun"),
    ("keltec_ksg.svg", "KEL-TEC KSG BULLPUP", "12-Gauge Dual-Tube", "Shotguns", "14+1 High-Capacity Bullpup Close Quarters Platform", "#8A9EA7", "shotgun"),

    # Submachine Guns
    ("sig_mpx.svg", "SIG MPX TTI SPEC", "9x19mm Subsonic", "Submachine Guns", "Subsonic Suppressed CQB System & Folding Arm Brace", "#D4AF37", "smg"),
    ("hk_mp5k.svg", "H&K MP5K-PDW", "9x19mm NATO", "Submachine Guns", "Closed-Bolt Roller-Delayed Blowback System", "#A0AAB2", "smg"),
    ("bt_apc9.svg", "B&T APC9 PRO-K", "9x19mm Parabellum", "Submachine Guns", "Swiss Hydraulic Buffer System & M-LOK Handguard", "#C5A059", "smg"),
    ("cz_scorpion.svg", "CZ SCORPION EVO 3 S1", "9x19mm Suppressed", "Submachine Guns", "Low-Profile Cold-Hammer Forged Barrel & Flash Can", "#8A9EA7", "smg"),

    # Rifles & Precision Platforms
    ("tti_tr1.svg", "TTI TR-1 ULTRALIGHT AR-15", "5.56x45mm NATO", "Rifles", "Trijicon AccuPoint 1-6x Scope & Offset RMR Optic", "#D4AF37", "rifle"),
    ("desert_tech_srs.svg", "DESERT TECH SRS-A1", "7.62x51mm / .308 Win", "Rifles", "Bullpup Precision Target Sniper System", "#C5A059", "rifle"),
    ("sig_mcx.svg", "SIG SAUER MCX VIRTUS", "5.56x45mm NATO", "Rifles", "Short-Stroke Gas Piston & Match Duo Trigger", "#A0AAB2", "rifle"),
    ("cheytac_m200.svg", "CHEYTAC M200 INTERVENTION", ".408 CheyTac", "Rifles", "Extreme Long-Range Anti-Materiel Precision (2000m+)", "#E5C158", "rifle")
]

def generate_svg(filename, title, caliber, category, feature, accent, gun_type):
    # Distinct SVG weapon silhouette drawing paths
    if gun_type == "pistol":
        silhouette = """
        <!-- Pistol Silhouette -->
        <g fill="none" stroke="{accent}" stroke-width="2.5" opacity="0.9">
            <!-- Slide -->
            <path d="M 120 130 L 340 130 L 340 165 L 310 165 L 305 175 L 230 175 L 220 170 L 120 170 Z" fill="#1A1C23" stroke="{accent}"/>
            <!-- Barrel & Compensator -->
            <rect x="340" y="135" width="40" height="25" rx="3" fill="#252932" stroke="{accent}"/>
            <circle cx="370" cy="147" r="5" fill="{accent}"/>
            <!-- Slide Serrations -->
            <line x1="140" y1="135" x2="140" y2="160" stroke="{accent}" stroke-width="2"/>
            <line x1="150" y1="135" x2="150" y2="160" stroke="{accent}" stroke-width="2"/>
            <line x1="160" y1="135" x2="160" y2="160" stroke="{accent}" stroke-width="2"/>
            <line x1="315" y1="135" x2="315" y2="160" stroke="{accent}" stroke-width="2"/>
            <line x1="325" y1="135" x2="325" y2="160" stroke="{accent}" stroke-width="2"/>
            <!-- Sights -->
            <rect x="130" y="122" width="12" height="8" fill="{accent}"/>
            <rect x="330" y="124" width="8" height="6" fill="#00FF66"/>
            <!-- Frame & Grip -->
            <path d="M 170 170 L 195 270 L 235 275 L 250 265 L 230 185 L 255 185 L 255 170 Z" fill="#16181F" stroke="{accent}"/>
            <!-- Trigger Guard & Trigger -->
            <path d="M 230 185 Q 260 215 285 180" fill="none" stroke="{accent}" stroke-width="2.5"/>
            <path d="M 250 183 Q 255 200 245 205" fill="none" stroke="{accent}" stroke-width="3"/>
            <!-- Stippling Grip Pattern -->
            <line x1="185" y1="200" x2="215" y2="200" stroke="{accent}" stroke-dasharray="2,3"/>
            <line x1="190" y1="220" x2="220" y2="220" stroke="{accent}" stroke-dasharray="2,3"/>
            <line x1="195" y1="240" x2="225" y2="240" stroke="{accent}" stroke-dasharray="2,3"/>
            <!-- Magwell Extension -->
            <polygon points="190,270 245,275 250,285 185,280" fill="{accent}" opacity="0.6"/>
        </g>
        """.format(accent=accent)
    elif gun_type == "shotgun":
        silhouette = """
        <!-- Shotgun Silhouette -->
        <g fill="none" stroke="{accent}" stroke-width="2.5" opacity="0.9">
            <!-- Stock -->
            <path d="M 50 180 L 110 160 L 150 170 L 150 210 L 90 220 L 50 200 Z" fill="#1A1C23" stroke="{accent}"/>
            <!-- Receiver -->
            <rect x="150" y="160" width="100" height="45" rx="3" fill="#252932" stroke="{accent}"/>
            <!-- Shell Ejection Port -->
            <rect x="175" y="168" width="45" height="18" fill="#101114" stroke="{accent}"/>
            <!-- Barrel & Mag Tube -->
            <rect x="250" y="165" width="180" height="18" fill="#1A1C23" stroke="{accent}"/>
            <rect x="250" y="185" width="170" height="14" fill="#1A1C23" stroke="{accent}"/>
            <!-- Breaching Muzzle Choke -->
            <rect x="430" y="162" width="22" height="24" fill="{accent}" opacity="0.8"/>
            <circle cx="440" cy="174" r="3" fill="#101114"/>
            <!-- Fore-end Pump / Handguard -->
            <rect x="270" y="180" width="80" height="24" rx="4" fill="#16181F" stroke="{accent}"/>
            <line x1="285" y1="180" x2="285" y2="204" stroke="{accent}"/>
            <line x1="305" y1="180" x2="305" y2="204" stroke="{accent}"/>
            <line x1="325" y1="180" x2="325" y2="204" stroke="{accent}"/>
            <!-- Trigger & Pistol Grip -->
            <path d="M 150 205 L 140 250 L 165 255 L 175 205 Z" fill="#16181F" stroke="{accent}"/>
            <path d="M 180 205 Q 195 225 210 205" fill="none" stroke="{accent}" stroke-width="2.5"/>
            <line x1="192" y1="205" x2="190" y2="218" stroke="{accent}" stroke-width="3"/>
            <!-- Ghost Ring Sight -->
            <circle cx="165" cy="152" r="5" fill="none" stroke="{accent}" stroke-width="2"/>
            <line x1="420" y1="165" x2="420" y2="155" stroke="{accent}" stroke-width="2"/>
        </g>
        """.format(accent=accent)
    elif gun_type == "smg":
        silhouette = """
        <!-- SMG Silhouette -->
        <g fill="none" stroke="{accent}" stroke-width="2.5" opacity="0.9">
            <!-- Folding Stock -->
            <line x1="60" y1="170" x2="140" y2="170" stroke="{accent}" stroke-width="3"/>
            <rect x="50" y="160" width="15" height="35" rx="3" fill="#1A1C23" stroke="{accent}"/>
            <!-- Receiver -->
            <path d="M 140 150 L 260 150 L 260 195 L 140 195 Z" fill="#252932" stroke="{accent}"/>
            <!-- Handguard & Rails -->
            <rect x="260" y="155" width="70" height="35" fill="#1A1C23" stroke="{accent}"/>
            <line x1="270" y1="160" x2="320" y2="160" stroke="{accent}" stroke-width="1.5" stroke-dasharray="3,3"/>
            <!-- Integrated Suppressor (Silencer) -->
            <rect x="330" y="152" width="105" height="40" rx="6" fill="#16181F" stroke="{accent}" stroke-width="2.5"/>
            <line x1="350" y1="152" x2="350" y2="192" stroke="{accent}" opacity="0.5"/>
            <line x1="380" y1="152" x2="380" y2="192" stroke="{accent}" opacity="0.5"/>
            <line x1="410" y1="152" x2="410" y2="192" stroke="{accent}" opacity="0.5"/>
            <!-- Curved Magazine -->
            <path d="M 230 195 L 210 270 L 235 275 L 255 195 Z" fill="#16181F" stroke="{accent}"/>
            <!-- Pistol Grip -->
            <path d="M 160 195 L 145 255 L 175 260 L 185 195 Z" fill="#16181F" stroke="{accent}"/>
            <!-- Trigger Guard -->
            <path d="M 185 195 Q 200 220 220 195" fill="none" stroke="{accent}" stroke-width="2"/>
            <!-- Optic / Red Dot Sight -->
            <rect x="180" y="132" width="40" height="18" rx="2" fill="#1A1C23" stroke="{accent}"/>
            <circle cx="200" cy="141" r="3" fill="#FF0055"/>
        </g>
        """.format(accent=accent)
    else: # rifle
        silhouette = """
        <!-- Rifle / Sniper Silhouette -->
        <g fill="none" stroke="{accent}" stroke-width="2.5" opacity="0.9">
            <!-- Stock / Chassis -->
            <path d="M 40 180 L 120 160 L 180 165 L 180 205 L 110 215 L 40 195 Z" fill="#1A1C23" stroke="{accent}"/>
            <line x1="60" y1="165" x2="60" y2="205" stroke="{accent}" stroke-width="3"/>
            <!-- Monolithic Upper Receiver -->
            <rect x="180" y="155" width="110" height="40" fill="#252932" stroke="{accent}"/>
            <!-- Free-Float M-LOK Rail Handguard -->
            <rect x="290" y="160" width="110" height="30" fill="#1A1C23" stroke="{accent}"/>
            <!-- Long Match Barrel -->
            <rect x="400" y="170" width="60" height="12" fill="#16181F" stroke="{accent}"/>
            <!-- Massive Muzzle Brake -->
            <polygon points="460,165 485,162 485,188 460,185" fill="{accent}"/>
            <circle cx="472" cy="175" r="3" fill="#101114"/>
            <!-- High-Power Precision Telemetry Scope -->
            <rect x="190" y="125" width="130" height="20" rx="3" fill="#16181F" stroke="{accent}"/>
            <circle cx="195" cy="135" r="7" fill="{accent}"/>
            <circle cx="315" cy="135" r="9" fill="{accent}"/>
            <rect x="215" y="145" width="12" height="10" fill="{accent}"/>
            <rect x="280" y="145" width="12" height="10" fill="{accent}"/>
            <!-- Magazine & Magwell -->
            <polygon points="230,195 240,260 265,260 260,195" fill="#16181F" stroke="{accent}"/>
            <!-- Ergonomic Sniper Grip -->
            <path d="M 175 195 L 160 250 L 190 255 L 200 195 Z" fill="#16181F" stroke="{accent}"/>
            <!-- Bipod Stood Up -->
            <line x1="380" y1="190" x2="360" y2="240" stroke="{accent}" stroke-width="2"/>
            <line x1="385" y1="190" x2="400" y2="240" stroke="{accent}" stroke-width="2"/>
        </g>
        """.format(accent=accent)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 320" width="100%" height="100%">
  <defs>
    <radialGradient id="bgGlow" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#1E2028"/>
      <stop offset="60%" stop-color="#121318"/>
      <stop offset="100%" stop-color="#0A0B0E"/>
    </radialGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F2D06B"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#8C6D1F"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="520" height="320" fill="url(#bgGlow)" rx="8"/>
  <rect width="516" height="316" x="2" y="2" fill="none" stroke="#2A2D37" stroke-width="1.5" rx="8"/>

  <!-- Tactical Grid overlay -->
  <g stroke="#1A1C24" stroke-width="1">
    <line x1="0" y1="80" x2="520" y2="80"/>
    <line x1="0" y1="160" x2="520" y2="160"/>
    <line x1="0" y1="240" x2="520" y2="240"/>
    <line x1="130" y1="0" x2="130" y2="320"/>
    <line x1="260" y1="0" x2="260" y2="320"/>
    <line x1="390" y1="0" x2="390" y2="320"/>
  </g>

  <!-- Continental High Table Seal Header -->
  <circle cx="48" cy="40" r="18" fill="none" stroke="{accent}" stroke-width="1.5"/>
  <circle cx="48" cy="40" r="14" fill="none" stroke="{accent}" stroke-width="0.8" stroke-dasharray="2,2"/>
  <text x="48" y="44" font-family="'Cinzel', serif, Times" font-size="11" fill="{accent}" font-weight="bold" text-anchor="middle">JW</text>

  <!-- Category & Caliber Tags -->
  <rect x="76" y="26" width="90" height="18" rx="3" fill="#1C1E26" stroke="{accent}" stroke-width="1"/>
  <text x="121" y="39" font-family="'Inter', sans-serif" font-size="9" fill="{accent}" font-weight="bold" text-anchor="middle">{category.upper()}</text>

  <rect x="172" y="26" width="120" height="18" rx="3" fill="#16181F" stroke="#3A3E4D" stroke-width="1"/>
  <text x="232" y="39" font-family="'Inter', sans-serif" font-size="9" fill="#9AA0B4" font-weight="600" text-anchor="middle">{caliber}</text>

  <text x="495" y="40" font-family="'Cinzel', serif" font-size="10" fill="{accent}" text-anchor="end" letter-spacing="2">CONTINENTAL ARMORY</text>

  <!-- Central Firearm Illustration -->
  {silhouette}

  <!-- Footer Specs & Details -->
  <rect x="16" y="278" width="488" height="28" rx="4" fill="#14161D" stroke="#252833"/>
  <text x="30" y="296" font-family="'Cinzel', serif" font-size="11" fill="#FFFFFF" font-weight="bold">{title}</text>
  <text x="490" y="296" font-family="'Inter', sans-serif" font-size="9.5" fill="{accent}" text-anchor="end">{feature}</text>
</svg>"""
    with open(os.path.join(img_dir, filename), "w", encoding="utf-8") as f:
        f.write(svg_content.strip())

for w in weapons:
    generate_svg(*w)

print(f"Generated {len(weapons)} high-definition weapon SVG illustrations successfully!")
