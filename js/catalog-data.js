// ============================================================
// John Wick & Co. Arms - Tactical Armory Catalog Data
// ============================================================

const catalogData = [
  // ------------------ SIDEARMS ------------------
  {
    id: "jw-01",
    name: "TTI JW4 Pit Viper 9mm",
    category: "Sidearms",
    price: 7500,
    priceDisplay: "$7,500",
    caliber: "9x19mm Major",
    capacity: "21+1 Rounds",
    barrelLength: "5.0 in Match-Grade",
    effectiveRange: "50 meters",
    image: "images/pit_viper.jpg",
    description: "The crown jewel of Taran Tactical Innovations, built specifically for John Wick in Chapter 4. Features a single-port compensator, extreme-engineering lite-speed fire control group, and titanium-nitrided fangs.",
    specs: {
      action: "Single Action Only (SAO)",
      sights: "Trijicon SRO Ready with Fiber Optic Front",
      finish: "Diamond-Like Carbon (DLC) Black & Gold TiN",
      weight: "38 oz (Unloaded)"
    }
  },
  {
    id: "jw-02",
    name: "TTI Combat Master Glock 34",
    category: "Sidearms",
    price: 6800,
    priceDisplay: "$6,800",
    caliber: "9x19mm Parabellum",
    capacity: "22+1 Extended Rounds",
    barrelLength: "5.3 in Ionbond Bronze",
    effectiveRange: "50 meters",
    image: "images/combat_master_jw2.jpg",
    description: "Custom combat modification by TTI used in the Rome catacombs in Chapter 2. Hand-stippled grip, flared competition magwell, lightened slide with combat serrations, and tuned 3.5 lb trigger pull.",
    specs: {
      action: "Safe Action Striker-Fired",
      sights: "TTI Fiber Optic Target Sights",
      finish: "Matte Black Cerakote with Bronze Barrel",
      weight: "26 oz"
    }
  },
  {
    id: "jw-03",
    name: "TTI STI 2011 Combat Master",
    category: "Sidearms",
    price: 7200,
    priceDisplay: "$7,200",
    caliber: "9mm Major",
    capacity: "22+1 Rounds",
    barrelLength: "5.4 in Bull Barrel",
    effectiveRange: "60 meters",
    image: "images/sti_2011_jw3.jpg",
    description: "Featured in the iconic Continental shootout in Chapter 3. Built on an STI double-stack 2011 frame with a match bull barrel, oversized magazine release, and ambidextrous safety levers.",
    specs: {
      action: "Single Action 2011 Match",
      sights: "Adjustable Target Rear, Green Fiber Front",
      finish: "DLC Coated Steel Frame",
      weight: "39 oz"
    }
  },
  {
    id: "jw-04",
    name: "Heckler & Koch P30L Compensated",
    category: "Sidearms",
    price: 3800,
    priceDisplay: "$3,800",
    caliber: "9x19mm NATO",
    capacity: "15+1 Rounds",
    barrelLength: "4.45 in with Counterweight",
    effectiveRange: "45 meters",
    image: "images/hk_p30l.jpg",
    description: "John Wick's legendary primary sidearm from Chapter 1. Fitted with a custom match aluminum counterweight compensator, ambidextrous slide controls, and interchangeable ergonomic grip modules.",
    specs: {
      action: "DA/SA with Rear Decocking Button",
      sights: "Superluminova Night Sights",
      finish: "Corrosion-Proof Hostile Environment Nitro-Carburized",
      weight: "27.5 oz"
    }
  },
  {
    id: "jw-05",
    name: "Kimber 1911 Warrior .45 ACP",
    category: "Sidearms",
    price: 4200,
    priceDisplay: "$4,200",
    caliber: ".45 ACP",
    capacity: "7+1 Single-Stack",
    barrelLength: "5.0 in Stainless Steel",
    effectiveRange: "50 meters",
    image: "images/kimber_1911.jpg",
    description: "Gifted to John Wick by the Bowery King with exactly seven rounds in Chapter 2. Features desert tan KimPro finish, G10 tactical grips, tactical accessory rail, and Novak night sights.",
    specs: {
      action: "Single Action 1911",
      sights: "Novak Tritium 3-Dot Night Sights",
      finish: "Desert Tan KimPro II",
      weight: "39 oz"
    }
  },
  {
    id: "jw-06",
    name: "Glock 26 Combat Master Backup",
    category: "Sidearms",
    price: 2900,
    priceDisplay: "$2,900",
    caliber: "9x19mm Parabellum",
    capacity: "12+1 Rounds",
    barrelLength: "3.42 in Subcompact",
    effectiveRange: "30 meters",
    image: "images/glock26.jpg",
    description: "Concealed tactical backup pistol worn in an ankle holster. Upgraded by the Sommelier with a tungsten guide rod, undercut trigger guard, and match trigger package.",
    specs: {
      action: "Striker Fired",
      sights: "Low-Profile Tritium Sights",
      finish: "Tenifer Matte Black",
      weight: "21.5 oz"
    }
  },

  // ------------------ SHOTGUNS ------------------
  {
    id: "jw-07",
    name: "Benelli M4 Tactical Ported",
    category: "Shotguns",
    price: 5400,
    priceDisplay: "$5,400",
    caliber: "12-Gauge (3 in Magnum)",
    capacity: "8+1 Shells",
    barrelLength: "18.5 in Ported Barrel",
    effectiveRange: "40 meters",
    image: "images/benelli_m4.jpg",
    description: "The Sommelier's premier recommendation: 'Italian classic, auto-regulating gas-operated system, textured grip, and short pull.' Customized with ported barrel, enlarged bolt release, and match loading port.",
    specs: {
      action: "ARGO (Auto-Regulating Gas-Operated) Semi-Auto",
      sights: "Ghost Ring Iron Sights & Picatinny Rail",
      finish: "Anodized Black & Phosphated Steel",
      weight: "7.8 lbs"
    }
  },
  {
    id: "jw-08",
    name: "Genesis Arms Gen-12 Dragon's Breath",
    category: "Shotguns",
    price: 6900,
    priceDisplay: "$6,900",
    caliber: "12-Gauge Incendiary",
    capacity: "10-Round Detachable Box Mag",
    barrelLength: "10.5 in Short Barrel",
    effectiveRange: "35 meters",
    image: "images/gen12_dragons_breath.jpg",
    description: "The devastating top-down breacher from the Paris apartment raid in Chapter 4. Fires incendiary Dragon's Breath magnesium rounds that ignite targets on impact with full semi-automatic AR-10 ergonomics.",
    specs: {
      action: "Short-Recoil Semi-Automatic AR-10 Architecture",
      sights: "EOTech EXPS3 Holographic Weapon Sight",
      finish: "Hardcoat Anodized Black",
      weight: "8.3 lbs"
    }
  },
  {
    id: "jw-09",
    name: "Remington 870 Tactical Breacher",
    category: "Shotguns",
    price: 3200,
    priceDisplay: "$3,200",
    caliber: "12-Gauge Standard",
    capacity: "6+1 Shells",
    barrelLength: "14.0 in Breaching Barrel",
    effectiveRange: "30 meters",
    image: "images/remington870.jpg",
    description: "Heavy-duty steel pump action shotgun fitted with a spiked door-breaching muzzle brake, Magpul SGA stock, and forward hand stop for tight room-clearing maneuvers.",
    specs: {
      action: "Pump Action with Twin Action Bars",
      sights: "XS Sights Front Bead",
      finish: "Parkerized Matte Dark Slate",
      weight: "7.2 lbs"
    }
  },
  {
    id: "jw-10",
    name: "Kel-Tec KSG Bullpup 12-Gauge",
    category: "Shotguns",
    price: 3600,
    priceDisplay: "$3,600",
    caliber: "12-Gauge Dual-Tube",
    capacity: "14+1 Shells",
    barrelLength: "18.5 in Bullpup",
    effectiveRange: "35 meters",
    image: "images/keltec_ksg.jpg",
    description: "Dual-magazine tube bullpup shotgun utilized in the church vault shootout. Allows instant switching between slugs and 00-buckshot with a total capacity of 15 shells.",
    specs: {
      action: "Downward-Ejecting Pump Action",
      sights: "Magpul MBUS Flip-Up Sights",
      finish: "High-Strength Polymer & Parkerized Steel",
      weight: "6.9 lbs"
    }
  },

  // ------------------ SUBMACHINE GUNS ------------------
  {
    id: "jw-11",
    name: "SIG MPX TTI Suppressed Spec",
    category: "Submachine Guns",
    price: 5800,
    priceDisplay: "$5,800",
    caliber: "9x19mm Subsonic",
    capacity: "35-Round Transparent Mag",
    barrelLength: "4.5 in Suppressed",
    effectiveRange: "80 meters",
    image: "images/sig_mpx.jpg",
    description: "The Sommelier's tactical submachine recommendation: 'Robust, precise, and delightfully light.' Fully suppressed closed-bolt short-stroke gas piston platform running subsonic 147gr loads.",
    specs: {
      action: "Gas-Piston Closed-Bolt Semi/Burst",
      sights: "Trijicon MRO Optic with Lower 1/3 Mount",
      finish: "FDE / Tungsten Cerakote with DLC Silencer",
      weight: "5.0 lbs"
    }
  },
  {
    id: "jw-12",
    name: "Heckler & Koch MP5K-PDW",
    category: "Submachine Guns",
    price: 6200,
    priceDisplay: "$6,200",
    caliber: "9x19mm NATO",
    capacity: "30-Round Curved Magazine",
    barrelLength: "5.8 in Threaded Tri-Lug",
    effectiveRange: "100 meters",
    image: "images/hk_mp5k.jpg",
    description: "Legendary roller-delayed blowback submachine gun in compact Personal Defense Weapon configuration. Features side-folding polymer stock, vertical foregrip, and Navy trigger group.",
    specs: {
      action: "Roller-Delayed Blowback",
      sights: "Rotary Drum Rear & Hooded Front Post",
      finish: "Hostile Environment Matte Black",
      weight: "5.6 lbs"
    }
  },
  {
    id: "jw-13",
    name: "B&T APC9 PRO-K Tactical",
    category: "Submachine Guns",
    price: 5100,
    priceDisplay: "$5,100",
    caliber: "9x19mm Parabellum",
    capacity: "30-Round B&T Mag",
    barrelLength: "4.3 in Cold Hammer-Forged",
    effectiveRange: "75 meters",
    image: "images/bt_apc9.jpg",
    description: "Swiss military and high-table security personal defense weapon equipped with a proprietary hydraulic buffer system that virtually eliminates recoil during rapid firing sequences.",
    specs: {
      action: "Hydraulic Buffered Blowback",
      sights: "Aimpoint Micro T-2 with Absolute Co-Witness",
      finish: "Type III Hard Anodized Alloy",
      weight: "5.2 lbs"
    }
  },
  {
    id: "jw-14",
    name: "CZ Scorpion EVO 3 S1 Tactical",
    category: "Submachine Guns",
    price: 4500,
    priceDisplay: "$4,500",
    caliber: "9x19mm Suppressed",
    capacity: "30-Round Windowed Mag",
    barrelLength: "7.7 in Threaded",
    effectiveRange: "90 meters",
    image: "images/cz_scorpion.jpg",
    description: "Lightweight fiber-reinforced polymer submachine gun featuring ambidextrous controls, non-reciprocating charging handle, and custom low-profile muzzle flash can.",
    specs: {
      action: "Blowback Semi-Automatic",
      sights: "Low-Profile Adjustable Aperture Sights",
      finish: "Tactical Matte Black Polymer",
      weight: "5.0 lbs"
    }
  },

  // ------------------ RIFLES & PRECISION PLATFORMS ------------------
  {
    id: "jw-15",
    name: "TTI TR-1 Ultralight AR-15",
    category: "Rifles",
    price: 8900,
    priceDisplay: "$8,900",
    caliber: "5.56x45mm NATO",
    capacity: "30-Round PMAG",
    barrelLength: "14.5 in Match with Pinned Compensator",
    effectiveRange: "400 meters",
    image: "images/tti_tr1.jpg",
    description: "John Wick's premier rifle in the Chapter 2 Rome catacombs assault. Taran Tactical custom build with BCM furniture, Hiperfire 24C match trigger, Trijicon AccuPoint 1-6x scope, and canted 45-degree Trijicon RMR.",
    specs: {
      action: "Direct Gas Impingement Match System",
      sights: "Trijicon AccuPoint 1-6x24 + Offset RMR",
      finish: "Matte Black Hardcoat Anodized",
      weight: "6.4 lbs"
    }
  },
  {
    id: "jw-16",
    name: "Desert Tech SRS-A1 Precision Sniper",
    category: "Rifles",
    price: 9500,
    priceDisplay: "$9,500",
    caliber: "7.62x51mm / .308 Win",
    capacity: "10-Round Steel Mag",
    barrelLength: "22.0 in Fluted Match",
    effectiveRange: "1,000 meters",
    image: "images/desert_tech_srs.jpg",
    description: "Compact bullpup bolt-action sniper rifle system engineered for high-value target neutralization. Match-grade trigger, monolithic receiver, and quick-change caliber conversion system.",
    specs: {
      action: "Bullpup Bolt Action",
      sights: "Schmidt & Bender 5-25x56 PM II Scope",
      finish: "Flat Dark Earth (FDE) & Hardcoat Black",
      weight: "10.5 lbs"
    }
  },
  {
    id: "jw-17",
    name: "SIG Sauer MCX Virtus Patrol",
    category: "Rifles",
    price: 7800,
    priceDisplay: "$7,800",
    caliber: "5.56x45mm NATO / .300 BLK",
    capacity: "30-Round Magpul PMAG",
    barrelLength: "16.0 in Cold Hammer Forged",
    effectiveRange: "500 meters",
    image: "images/sig_mcx.jpg",
    description: "Short-stroke gas piston rifle system proven in modern clandestine operations. Features interchangeable barrel system, folding skeleton stock, and Matchlite Duo two-stage trigger.",
    specs: {
      action: "Short-Stroke Gas Piston",
      sights: "SIG Romeo4T Red Dot + Juliet4 Magnifier",
      finish: "Stealth Grey Cerakote",
      weight: "7.9 lbs"
    }
  },
  {
    id: "jw-18",
    name: "CheyTac M200 Intervention .408",
    category: "Rifles",
    price: 14500,
    priceDisplay: "$14,500",
    caliber: ".408 CheyTac",
    capacity: "7-Round Detachable Mag",
    barrelLength: "29.0 in Free-Floating Fluted",
    effectiveRange: "2,200 meters",
    image: "images/cheytac_m200.jpg",
    description: "The ultimate long-range anti-materiel precision platform in the Continental inventory. Delivers sub-MOA precision at extreme distances beyond two kilometers with balanced high-ballistic-coefficient rounds.",
    specs: {
      action: "Heavy Bolt Action Precision",
      sights: "Nightforce ATACR 7-35x56 F1 ZeroStop",
      finish: "Armor Black Cerakote with Bipod & Carry Handle",
      weight: "31 lbs"
    }
  }
];

// High Table Realistic Events
const eventsData = [
  {
    id: "evt-01",
    title: "Continental Sommelier Unveiling",
    date: "October 14, 2026",
    location: "New York Continental Lounge",
    description: "Exclusive tasting and private presentation of custom match-grade sidearms and tactical carbon body armor linings.",
    image: "images/pit_viper.jpg"
  },
  {
    id: "evt-02",
    title: "Tactical Night Operations Briefing",
    date: "November 02, 2026",
    location: "Rome Armory Vaults",
    description: "Live night-vision combat simulation and thermal scope calibration workshops led by former High Table operatives.",
    image: "images/benelli_m4.jpg"
  },
  {
    id: "evt-03",
    title: "Subsonic Suppressor Masterclass",
    date: "December 10, 2026",
    location: "Osaka High Table Safehouse",
    description: "Advanced ballistics training focused on stealth engagements and custom subsonic cartridge handloading.",
    image: "images/sig_mpx.jpg"
  },
  {
    id: "evt-04",
    title: "Gold Ledger Coin Auction",
    date: "January 20, 2027",
    location: "Casablanca Continental Rooftop",
    description: "Bidding session for antique Continental mint coins, contracts, and rare prototype custom firearms.",
    image: "images/cheytac_m200.jpg"
  },
  {
    id: "evt-05",
    title: "Excommunicado Survival Tactics",
    date: "February 15, 2027",
    location: "Berlin Underground Range",
    description: "High-intensity close-quarters combat (CQC) drills and rapid reload maneuvers under active fire.",
    image: "images/gen12_dragons_breath.jpg"
  },
  {
    id: "evt-06",
    title: "Long-Range Ballistics Summit",
    date: "March 28, 2027",
    location: "Swiss Alps Firing Range",
    description: "Extreme long-range target engagement using anti-materiel precision rifles and telemetry optics.",
    image: "images/desert_tech_srs.jpg"
  }
];
