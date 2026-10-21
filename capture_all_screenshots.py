import os
import shutil
import subprocess
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
dest_dir = r"d:\Akash Files\Akash L Clg Documents\Web prg\john-wick-arms\screenshots"
os.makedirs(dest_dir, exist_ok=True)

targets = [
    ("screenshot_01_home.png", "http://localhost:3000/index.html#home"),
    ("screenshot_02_catalog.png", "http://localhost:3000/index.html#catalog"),
    ("screenshot_03_weapon_detail.png", "http://localhost:3000/index.html#weapon-detail?id=jw-01"),
    ("screenshot_04_register.png", "http://localhost:3000/index.html#register"),
    ("screenshot_05_login.png", "http://localhost:3000/index.html#login"),
    ("screenshot_06_cart.png", "http://localhost:3000/index.html#cart"),
    ("screenshot_07_checkout_payment.png", "http://localhost:3000/index.html#payment"),
    ("screenshot_08_order_success.png", "http://localhost:3000/index.html#success"),
    ("screenshot_09_my_orders.png", "http://localhost:3000/index.html#profile"),
    ("screenshot_10_admin_login.png", "http://localhost:3000/admin_preview/login.html"),
    ("screenshot_11_admin_dashboard.png", "http://localhost:3000/admin_preview/dashboard.html"),
    ("screenshot_12_admin_weapons.png", "http://localhost:3000/admin_preview/weapons.html"),
    ("screenshot_13_admin_add_weapon.png", "http://localhost:3000/admin_preview/add_weapon.html"),
    ("screenshot_14_admin_edit_weapon.png", "http://localhost:3000/admin_preview/edit_weapon.html"),
    ("screenshot_15_admin_orders.png", "http://localhost:3000/admin_preview/orders.html"),
    ("screenshot_16_db_schema.png", "http://localhost:3000/admin_preview/db_schema.html"),
]

print(f"Starting capture of {len(targets)} screenshots...")
temp_dir = os.environ['TEMP']

for filename, url in targets:
    tmp_path = os.path.join(temp_dir, f"tmp_{filename}")
    final_path = os.path.join(dest_dir, filename)
    
    if os.path.exists(tmp_path):
        os.remove(tmp_path)
        
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1280,800",
        "--hide-scrollbars",
        "--virtual-time-budget=2000",
        f"--screenshot={tmp_path}",
        url
    ]
    
    subprocess.run(cmd, capture_output=True)
    
    if os.path.exists(tmp_path) and os.path.getsize(tmp_path) > 1000:
        shutil.copy2(tmp_path, final_path)
        im = Image.open(final_path)
        size_kb = os.path.getsize(final_path) // 1024
        print(f"[OK] {filename} -> {im.size}, {size_kb} KB (from {url})")
    else:
        print(f"[ERROR] Failed to capture {filename} from {url}")

print("\nScreenshot capture process finished!")
