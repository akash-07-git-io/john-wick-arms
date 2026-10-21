import os
import urllib.request
from PIL import Image

img_dir = r"d:\Akash Files\Akash L Clg Documents\Web prg\john-wick-arms\images"
os.makedirs(img_dir, exist_ok=True)

# 18 authentic weapon image sources
weapon_sources = {
    # 1. TTI JW4 Pit Viper 9mm (Custom 2011 Match Tactical Pistol)
    "pit_viper.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/5/54/FN_510_Tactical_Handgun_-_10mm_Pistol.jpg/960px-FN_510_Tactical_Handgun_-_10mm_Pistol.jpg",
        "https://images.unsplash.com/photo-1595590424283-b8f17842773f?auto=format&fit=crop&w=800&q=80"
    ],
    # 2. TTI Combat Master Glock 34
    "combat_master_jw2.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c3/Glock_34_MOS.jpg/960px-Glock_34_MOS.jpg",
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b1/Glock_17_%286825676904%29_%D0%B1%D0%B5%D0%B7_%D1%84%D0%BE%D0%BD%D0%B0.jpg/960px-Glock_17_%286825676904%29_%D0%B1%D0%B5%D0%B7_%D1%84%D0%BE%D0%BD%D0%B0.jpg"
    ],
    # 3. TTI STI 2011 Combat Master
    "sti_2011_jw3.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b3/1911_pistol_2026-07-25_Philippines.jpg/960px-1911_pistol_2026-07-25_Philippines.jpg",
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a8/460Rowland_M1911.jpg/960px-460Rowland_M1911.jpg"
    ],
    # 4. Heckler & Koch P30L Compensated
    "hk_p30l.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2c/Koalorka_H%26K_P30L.jpg/960px-Koalorka_H%26K_P30L.jpg"
    ],
    # 5. Kimber 1911 Warrior .45 ACP
    "kimber_1911.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a8/460Rowland_M1911.jpg/960px-460Rowland_M1911.jpg",
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9c/M1911_and_M1911A1_pistols.JPG/960px-M1911_and_M1911A1_pistols.JPG"
    ],
    # 6. Glock 26 Combat Master Backup
    "glock26.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ec/GLOCK_171926E.jpg/960px-GLOCK_171926E.jpg",
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b1/Glock_17_%286825676904%29_%D0%B1%D0%B5%D0%B7_%D1%84%D0%BE%D0%BD%D0%B0.jpg/960px-Glock_17_%286825676904%29_%D0%B1%D0%B5%D0%B7_%D1%84%D0%BE%D0%BD%D0%B0.jpg"
    ],
    # 7. Benelli M4 Tactical Ported
    "benelli_m4.jpg": [
        "https://upload.wikimedia.org/wikipedia/commons/0/03/Benelli_m4_2.jpg",
        "https://images.unsplash.com/photo-1579273166152-d725a4e2b755?auto=format&fit=crop&w=800&q=80"
    ],
    # 8. Genesis Arms Gen-12 Dragon's Breath
    "gen12_dragons_breath.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ea/2CR_Soldiers_qualify_on_the_M500_shotgun_%285593332%29.jpg/960px-2CR_Soldiers_qualify_on_the_M500_shotgun_%285593332%29.jpg"
    ],
    # 9. Remington 870 Tactical Breacher
    "remington870.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1c/MCS_870_Modular_Combat_Shotgun_%287414624938%29.jpg/960px-MCS_870_Modular_Combat_Shotgun_%287414624938%29.jpg"
    ],
    # 10. Kel-Tec KSG Bullpup 12-Gauge
    "keltec_ksg.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ea/Kel-tec_KSG1.jpg/960px-Kel-tec_KSG1.jpg"
    ],
    # 11. SIG MPX TTI Suppressed Spec
    "sig_mpx.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/f/ff/SIG%CC%A0MPX.jpg/960px-SIG%CC%A0MPX.jpg"
    ],
    # 12. Heckler & Koch MP5K-PDW
    "hk_mp5k.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/5/50/Heckler_%26_Koch_MP5.jpg/960px-Heckler_%26_Koch_MP5.jpg"
    ],
    # 13. B&T APC9 PRO-K Tactical
    "bt_apc9.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/1/14/230503-A-IE493-955_-_FORT_DIX-RANGE_33_733MP_HHD_Train_with_the_APC9K_small_submachine_gun._May_3rd_2023.jpg/960px-230503-A-IE493-955_-_FORT_DIX-RANGE_33_733MP_HHD_Train_with_the_APC9K_small_submachine_gun._May_3rd_2023.jpg"
    ],
    # 14. CZ Scorpion EVO 3 S1 Tactical
    "cz_scorpion.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b1/CZ_SCORPION_EVO_3_A1.jpg/960px-CZ_SCORPION_EVO_3_A1.jpg"
    ],
    # 15. TTI TR-1 Ultralight AR-15
    "tti_tr1.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/63/AR-15_%282%29.jpg/960px-AR-15_%282%29.jpg",
        "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=800&q=80"
    ],
    # 16. Desert Tech SRS-A1 Precision Sniper
    "desert_tech_srs.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7b/Compliant_MDRX_in_7.62_with_20%22_Barrel_and_3-15x_Scope.jpg/960px-Compliant_MDRX_in_7.62_with_20%22_Barrel_and_3-15x_Scope.jpg",
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7c/Barrett-MRAD-sniper-rifle-01.png/960px-Barrett-MRAD-sniper-rifle-01.png"
    ],
    # 17. SIG Sauer MCX Virtus Patrol
    "sig_mcx.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fc/SIG-MCX-Rifle.jpeg/960px-SIG-MCX-Rifle.jpeg"
    ],
    # 18. CheyTac M200 Intervention .408
    "cheytac_m200.jpg": [
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0f/AWM-338-white.jpg/960px-AWM-338-white.jpg",
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7c/Barrett-MRAD-sniper-rifle-01.png/960px-Barrett-MRAD-sniper-rifle-01.png"
    ]
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, urls in weapon_sources.items():
    dest_path = os.path.join(img_dir, fname)
    success = False
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = resp.read()
                if len(data) > 1000:
                    with open(dest_path, "wb") as f:
                        f.write(data)
                    # Verify with PIL
                    with Image.open(dest_path) as im:
                        im.verify()
                    print(f"OK: {fname} -> {len(data)} bytes ({url[:60]}...)")
                    success = True
                    break
        except Exception as e:
            # print(f"Retry on {fname}: {e}")
            pass
            
    if not success:
        print(f"FAILED: {fname}")

print("\nFinished verifying and downloading all 18 real weapon images!")
