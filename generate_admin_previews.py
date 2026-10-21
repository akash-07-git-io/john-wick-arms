import os

os.makedirs('admin_preview', exist_ok=True)

# 1. Admin Login View
login_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Admin Login | JOHN WICK & CO. ARMS</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="../index.html" class="logo">
        <span class="gold-text">JOHN WICK &amp; CO.</span> ARMS
        <span class="logo-sub">CONTINENTAL TACTICAL ARMORY - ADMIN GATEWAY</span>
      </a>
      <a href="../index.html" class="btn-gold-sm" style="text-decoration:none;">Public Portal</a>
    </div>
  </header>

  <section class="page-section active" style="min-height:80vh; display:flex; align-items:center; justify-content:center;">
    <div class="auth-card" style="max-width:440px; width:100%; margin:2rem auto;">
      <h2 class="auth-title">High Table Command</h2>
      <p class="auth-sub">Restricted Armory Administrative Access Only</p>

      <form onsubmit="return false;">
        <div class="form-group">
          <label>Admin Username</label>
          <input type="text" value="admin" readonly style="border-color:var(--accent-gold);">
        </div>
        <div class="form-group">
          <label>High Table Master Key</label>
          <input type="password" value="admin123" readonly style="border-color:var(--accent-gold);">
        </div>
        <button type="button" class="btn-primary" style="margin-top:1rem;">Authorize Access</button>
      </form>
      <div style="margin-top:1.5rem; text-align:center; padding:0.8rem; background:rgba(212,175,55,0.08); border:1px solid var(--gunmetal-border); border-radius:var(--radius); font-size:0.85rem; color:var(--text-muted);">
        Default Credentials: <strong style="color:var(--accent-gold);">admin</strong> / <strong style="color:var(--accent-gold);">admin123</strong>
      </div>
    </div>
  </section>
</body>
</html>
"""

# 2. Admin Dashboard View
dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Dashboard | Admin — JOHN WICK & CO. ARMS</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <style>
    .admin-nav { display:flex; gap:1.2rem; align-items:center; }
    .admin-nav a { text-decoration:none; color:var(--text-main); font-weight:600; font-size:0.95rem; }
    .admin-nav a.active { color:var(--accent-gold); border-bottom:2px solid var(--accent-gold); padding-bottom:4px; }
    .stat-grid { display:grid; grid-template-columns:repeat(5, 1fr); gap:1.2rem; margin:2rem 0; }
    .stat-card { background:var(--bg-card); border:1px solid var(--gunmetal-border); border-radius:var(--radius); padding:1.5rem; text-align:center; }
    .stat-card h3 { color:var(--accent-gold); font-size:2.2rem; margin-bottom:0.3rem; font-family:'Cinzel', serif; }
    .stat-card p { color:var(--text-muted); font-size:0.85rem; text-transform:uppercase; letter-spacing:1px; }
    table { width:100%; border-collapse:collapse; margin-top:1rem; background:var(--bg-card); border:1px solid var(--gunmetal-border); border-radius:var(--radius); overflow:hidden; }
    th, td { padding:1rem; text-align:left; border-bottom:1px solid var(--gunmetal-border); }
    th { color:var(--accent-gold); font-family:'Cinzel', serif; background:rgba(212,175,55,0.08); font-size:0.9rem; }
    td { color:var(--text-main); font-size:0.9rem; }
    .status-badge { display:inline-block; padding:0.3rem 0.8rem; border-radius:4px; font-size:0.75rem; font-weight:700; text-transform:uppercase; }
    .badge-pending { background:rgba(243,156,18,0.2); color:#f39c12; border:1px solid #f39c12; }
    .badge-approved { background:rgba(39,174,96,0.2); color:#27ae60; border:1px solid #27ae60; }
    .badge-dispatched { background:rgba(52,152,219,0.2); color:#3498db; border:1px solid #3498db; }
  </style>
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="dashboard.html" class="logo">
        <span class="gold-text">JOHN WICK &amp; CO.</span> ARMS
        <span class="logo-sub">CONTINENTAL ARMS - COMMAND DESK</span>
      </a>
      <nav class="admin-nav">
        <a href="dashboard.html" class="active">Dashboard</a>
        <a href="weapons.html">Weapons Inventory (18)</a>
        <a href="add_weapon.html">+ Add Weapon</a>
        <a href="orders.html">Orders Ledger (5)</a>
        <a href="../index.html" class="btn-gold-sm" style="color:var(--bg-dark)!important;">Logout Admin</a>
      </nav>
    </div>
  </header>

  <section class="page-section active">
    <div class="catalog-container">
      <h2 class="section-title" style="text-align:left; margin-bottom:0.2rem;">Command Overview: Winston Scott</h2>
      <p style="color:var(--text-muted); margin-bottom:1.5rem;">New York Continental Armory Operations &amp; High Table Logistical Audit</p>

      <div class="stat-grid">
        <div class="stat-card">
          <h3>18</h3>
          <p>Total Arsenal</p>
        </div>
        <div class="stat-card">
          <h3>24</h3>
          <p>Total Requisitions</p>
        </div>
        <div class="stat-card">
          <h3>12</h3>
          <p>Active Operatives</p>
        </div>
        <div class="stat-card">
          <h3>$184,200</h3>
          <p>Requisition Value</p>
        </div>
        <div class="stat-card">
          <h3 style="color:#e74c3c;">2</h3>
          <p>Pending Authorizations</p>
        </div>
      </div>

      <h2 class="section-title" style="text-align:left; margin-top:2rem;">Recent Requisitions Ledger</h2>
      <table>
        <thead>
          <tr>
            <th>Order Ref</th>
            <th>Operative</th>
            <th>Destination Sanctuary</th>
            <th>Settlement Method</th>
            <th>Total Amount</th>
            <th>Status</th>
            <th>Date Placed</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>#ORD-90812</strong></td>
            <td>John Wick (Baba Yaga)</td>
            <td>The Continental Hotel, Room 818, NY</td>
            <td>Continental Gold Coins (5 Coins)</td>
            <td><strong style="color:var(--accent-gold);">$23,500</strong></td>
            <td><span class="status-badge badge-pending">Pending</span></td>
            <td>2026-10-21 18:32</td>
          </tr>
          <tr>
            <td><strong>#ORD-90811</strong></td>
            <td>Sofia Al-Azwar</td>
            <td>Casablanca Sanctuary Branch, Morocco</td>
            <td>Swiss Private Bank Escrow</td>
            <td><strong style="color:var(--accent-gold);">$9,200</strong></td>
            <td><span class="status-badge badge-approved">Approved</span></td>
            <td>2026-10-21 15:45</td>
          </tr>
          <tr>
            <td><strong>#ORD-90810</strong></td>
            <td>Caine (Blind Swordsman)</td>
            <td>Osaka Continental Armoury, Japan</td>
            <td>High Table Encrypted Card</td>
            <td><strong style="color:var(--accent-gold);">$11,800</strong></td>
            <td><span class="status-badge badge-dispatched">Dispatched</span></td>
            <td>2026-10-21 11:20</td>
          </tr>
          <tr>
            <td><strong>#ORD-90809</strong></td>
            <td>Marcus (Vanguard Sniper)</td>
            <td>Brooklyn Safehouse, NY</td>
            <td>Continental Gold Coins (3 Coins)</td>
            <td><strong style="color:var(--accent-gold);">$15,500</strong></td>
            <td><span class="status-badge badge-approved">Approved</span></td>
            <td>2026-10-20 22:15</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</body>
</html>
"""

# 3. Admin Weapons Inventory View
weapons_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Manage Weapons | Admin — JOHN WICK & CO. ARMS</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <style>
    .admin-nav { display:flex; gap:1.2rem; align-items:center; }
    .admin-nav a { text-decoration:none; color:var(--text-main); font-weight:600; font-size:0.95rem; }
    .admin-nav a.active { color:var(--accent-gold); border-bottom:2px solid var(--accent-gold); padding-bottom:4px; }
    table { width:100%; border-collapse:collapse; margin-top:1.5rem; background:var(--bg-card); border:1px solid var(--gunmetal-border); border-radius:var(--radius); }
    th, td { padding:0.9rem; text-align:left; border-bottom:1px solid var(--gunmetal-border); vertical-align:middle; }
    th { color:var(--accent-gold); font-family:'Cinzel', serif; background:rgba(212,175,55,0.08); font-size:0.85rem; }
    td { color:var(--text-main); font-size:0.88rem; }
    .thumb-img { width:65px; height:45px; object-fit:contain; background:#0d0e14; border:1px solid var(--gunmetal-border); border-radius:4px; }
    .btn-action { display:inline-block; padding:0.3rem 0.7rem; border-radius:4px; font-size:0.8rem; text-decoration:none; font-weight:600; margin-right:0.3rem; }
    .btn-edit { background:rgba(212,175,55,0.15); color:var(--accent-gold); border:1px solid var(--accent-gold); }
    .btn-delete { background:rgba(231,76,60,0.15); color:#e74c3c; border:1px solid #e74c3c; }
  </style>
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="dashboard.html" class="logo">
        <span class="gold-text">JOHN WICK &amp; CO.</span> ARMS
        <span class="logo-sub">CONTINENTAL ARMS - COMMAND DESK</span>
      </a>
      <nav class="admin-nav">
        <a href="dashboard.html">Dashboard</a>
        <a href="weapons.html" class="active">Weapons Inventory (18)</a>
        <a href="add_weapon.html">+ Add Weapon</a>
        <a href="orders.html">Orders Ledger</a>
        <a href="../index.html" class="btn-gold-sm" style="color:var(--bg-dark)!important;">Logout Admin</a>
      </nav>
    </div>
  </header>

  <section class="page-section active">
    <div class="catalog-container">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
          <h2 class="section-title" style="text-align:left; margin-bottom:0.2rem;">Weapon Arsenal Inventory</h2>
          <p style="color:var(--text-muted); font-size:0.9rem;">Total active armory units: 18 firearms across 4 classifications</p>
        </div>
        <a href="add_weapon.html" class="btn-primary" style="text-decoration:none; width:auto; padding:0.6rem 1.6rem;">+ Provision New Firearm</a>
      </div>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Visual</th>
            <th>Nomenclature & Model</th>
            <th>Classification</th>
            <th>Caliber</th>
            <th>Price</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>#W01</td>
            <td><img src="../images/pit_viper.jpg" class="thumb-img" alt="Pit Viper"></td>
            <td><strong>TTI JW4 Pit Viper</strong></td>
            <td>Sidearms</td>
            <td>9x19mm Major</td>
            <td><strong style="color:var(--accent-gold);">$7,500</strong></td>
            <td><span style="color:#27ae60; font-weight:600;">Available</span></td>
            <td>
              <a href="edit_weapon.html" class="btn-action btn-edit">Edit</a>
              <a href="#" class="btn-action btn-delete">Archive</a>
            </td>
          </tr>
          <tr>
            <td>#W02</td>
            <td><img src="../images/combat_master_jw2.jpg" class="thumb-img" alt="Combat Master"></td>
            <td><strong>TTI Glock 34 Combat Master</strong></td>
            <td>Sidearms</td>
            <td>9x19mm Parabellum</td>
            <td><strong style="color:var(--accent-gold);">$3,900</strong></td>
            <td><span style="color:#27ae60; font-weight:600;">Available</span></td>
            <td>
              <a href="edit_weapon.html" class="btn-action btn-edit">Edit</a>
              <a href="#" class="btn-action btn-delete">Archive</a>
            </td>
          </tr>
          <tr>
            <td>#W03</td>
            <td><img src="../images/benelli_m4.jpg" class="thumb-img" alt="Benelli M4"></td>
            <td><strong>Benelli M4 Super 90 Tactical</strong></td>
            <td>Shotguns</td>
            <td>12 Gauge</td>
            <td><strong style="color:var(--accent-gold);">$5,200</strong></td>
            <td><span style="color:#27ae60; font-weight:600;">Available</span></td>
            <td>
              <a href="edit_weapon.html" class="btn-action btn-edit">Edit</a>
              <a href="#" class="btn-action btn-delete">Archive</a>
            </td>
          </tr>
          <tr>
            <td>#W04</td>
            <td><img src="../images/gen12_dragons_breath.jpg" class="thumb-img" alt="Genesis Gen-12"></td>
            <td><strong>Genesis Arms Gen-12 Breacher</strong></td>
            <td>Shotguns</td>
            <td>12 Gauge Dragon's Breath</td>
            <td><strong style="color:var(--accent-gold);">$6,800</strong></td>
            <td><span style="color:#27ae60; font-weight:600;">Available</span></td>
            <td>
              <a href="edit_weapon.html" class="btn-action btn-edit">Edit</a>
              <a href="#" class="btn-action btn-delete">Archive</a>
            </td>
          </tr>
          <tr>
            <td>#W05</td>
            <td><img src="../images/sig_mpx.jpg" class="thumb-img" alt="SIG MPX"></td>
            <td><strong>SIG Sauer MPX Copperhead</strong></td>
            <td>Submachine Guns</td>
            <td>9x19mm Parabellum</td>
            <td><strong style="color:var(--accent-gold);">$4,400</strong></td>
            <td><span style="color:#27ae60; font-weight:600;">Available</span></td>
            <td>
              <a href="edit_weapon.html" class="btn-action btn-edit">Edit</a>
              <a href="#" class="btn-action btn-delete">Archive</a>
            </td>
          </tr>
          <tr>
            <td>#W06</td>
            <td><img src="../images/cheytac_m200.jpg" class="thumb-img" alt="CheyTac M200"></td>
            <td><strong>CheyTac M200 Intervention</strong></td>
            <td>Rifles</td>
            <td>.408 CheyTac</td>
            <td><strong style="color:var(--accent-gold);">$13,500</strong></td>
            <td><span style="color:#27ae60; font-weight:600;">Available</span></td>
            <td>
              <a href="edit_weapon.html" class="btn-action btn-edit">Edit</a>
              <a href="#" class="btn-action btn-delete">Archive</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</body>
</html>
"""

# 4. Admin Add Weapon Form View
add_weapon_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Add Weapon | Admin — JOHN WICK & CO. ARMS</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <style>
    .admin-nav { display:flex; gap:1.2rem; align-items:center; }
    .admin-nav a { text-decoration:none; color:var(--text-main); font-weight:600; font-size:0.95rem; }
    .admin-nav a.active { color:var(--accent-gold); border-bottom:2px solid var(--accent-gold); padding-bottom:4px; }
    .form-group select, .form-group textarea {
      width: 100%; padding: 0.8rem; background: var(--bg-dark); border: 1px solid var(--gunmetal-border);
      border-radius: var(--radius); color: var(--text-main); font-family: 'Inter', sans-serif;
    }
  </style>
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="dashboard.html" class="logo">
        <span class="gold-text">JOHN WICK &amp; CO.</span> ARMS
        <span class="logo-sub">CONTINENTAL ARMS - COMMAND DESK</span>
      </a>
      <nav class="admin-nav">
        <a href="dashboard.html">Dashboard</a>
        <a href="weapons.html">Weapons Inventory (18)</a>
        <a href="add_weapon.html" class="active">+ Add Weapon</a>
        <a href="orders.html">Orders Ledger</a>
        <a href="../index.html" class="btn-gold-sm" style="color:var(--bg-dark)!important;">Logout Admin</a>
      </nav>
    </div>
  </header>

  <section class="page-section active">
    <div class="catalog-container" style="max-width:750px;">
      <h2 class="section-title" style="text-align:left; margin-bottom:0.2rem;">Provision New Weapon to Arsenal</h2>
      <p style="color:var(--text-muted); margin-bottom:1.5rem;">Enter ballistic specifications, High Table pricing, and verified weapon imagery.</p>

      <div style="background:var(--bg-card); border:1px solid var(--gunmetal-border); border-radius:var(--radius); padding:2rem;">
        <form onsubmit="return false;">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
            <div class="form-group">
              <label>Weapon Nomenclature</label>
              <input type="text" placeholder="e.g. TTI JW4 Pit Viper" value="TTI Sand Viper 2011">
            </div>
            <div class="form-group">
              <label>Tactical Classification</label>
              <select>
                <option selected>Sidearms</option>
                <option>Shotguns</option>
                <option>Submachine Guns</option>
                <option>Rifles</option>
              </select>
            </div>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
            <div class="form-group">
              <label>Procurement Price ($ USD)</label>
              <input type="number" value="7200">
            </div>
            <div class="form-group">
              <label>Ballistic Caliber</label>
              <input type="text" value="9x19mm Major">
            </div>
          </div>

          <div class="form-group">
            <label>Firearm Image Asset Path</label>
            <input type="text" value="images/pit_viper.jpg">
          </div>

          <div class="form-group">
            <label>Continental Technical Specification Dossier</label>
            <textarea rows="4">Optics-ready 2011 competition firearm configured with extreme tolerances, integral compensator, extreme trigger pull tuning, and Continental High Table certified durability.</textarea>
          </div>

          <div style="display:flex; gap:1rem; margin-top:1.5rem;">
            <button type="button" class="btn-primary" style="width:auto; padding:0.8rem 2rem;">Save to Arsenal Database</button>
            <a href="weapons.html" class="btn-secondary" style="width:auto; padding:0.8rem 2rem; text-decoration:none; text-align:center;">Cancel</a>
          </div>
        </form>
      </div>
    </div>
  </section>
</body>
</html>
"""

# 5. Admin Edit Weapon Form View
edit_weapon_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Edit Weapon | Admin — JOHN WICK & CO. ARMS</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <style>
    .admin-nav { display:flex; gap:1.2rem; align-items:center; }
    .admin-nav a { text-decoration:none; color:var(--text-main); font-weight:600; font-size:0.95rem; }
    .form-group select, .form-group textarea {
      width: 100%; padding: 0.8rem; background: var(--bg-dark); border: 1px solid var(--gunmetal-border);
      border-radius: var(--radius); color: var(--text-main); font-family: 'Inter', sans-serif;
    }
  </style>
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="dashboard.html" class="logo">
        <span class="gold-text">JOHN WICK &amp; CO.</span> ARMS
        <span class="logo-sub">CONTINENTAL ARMS - COMMAND DESK</span>
      </a>
      <nav class="admin-nav">
        <a href="dashboard.html">Dashboard</a>
        <a href="weapons.html">Weapons Inventory (18)</a>
        <a href="add_weapon.html">+ Add Weapon</a>
        <a href="orders.html">Orders Ledger</a>
        <a href="../index.html" class="btn-gold-sm" style="color:var(--bg-dark)!important;">Logout Admin</a>
      </nav>
    </div>
  </header>

  <section class="page-section active">
    <div class="catalog-container" style="max-width:750px;">
      <h2 class="section-title" style="text-align:left; margin-bottom:0.2rem;">Edit Weapon Specifications: #W01 TTI JW4 Pit Viper</h2>
      <p style="color:var(--text-muted); margin-bottom:1.5rem;">Update real-time inventory pricing, availability status, and specifications.</p>

      <div style="background:var(--bg-card); border:1px solid var(--gunmetal-border); border-radius:var(--radius); padding:2rem;">
        <div style="display:flex; align-items:center; gap:1.5rem; margin-bottom:1.5rem; padding-bottom:1.5rem; border-bottom:1px solid var(--gunmetal-border);">
          <img src="../images/pit_viper.jpg" style="width:140px; height:90px; object-fit:contain; background:#0d0e14; border:1px solid var(--accent-gold); border-radius:var(--radius); padding:0.4rem;" alt="Pit Viper">
          <div>
            <h3 style="color:var(--accent-gold); font-family:'Cinzel', serif; margin-bottom:0.3rem;">TTI JW4 Pit Viper (2011)</h3>
            <p style="color:var(--text-muted); font-size:0.85rem;">Status: <span style="color:#27ae60; font-weight:600;">ACTIVE IN ARSENAL</span> &bull; 9x19mm Major</p>
          </div>
        </div>

        <form onsubmit="return false;">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
            <div class="form-group">
              <label>Firearm Nomenclature</label>
              <input type="text" value="TTI JW4 Pit Viper">
            </div>
            <div class="form-group">
              <label>Tactical Classification</label>
              <select>
                <option selected>Sidearms</option>
                <option>Shotguns</option>
                <option>Submachine Guns</option>
                <option>Rifles</option>
              </select>
            </div>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
            <div class="form-group">
              <label>Procurement Price ($ USD)</label>
              <input type="number" value="7500">
            </div>
            <div class="form-group">
              <label>Stock Status</label>
              <select>
                <option selected>Available</option>
                <option>Reserved</option>
                <option>Out of Stock</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label>Image Asset Path</label>
            <input type="text" value="images/pit_viper.jpg">
          </div>

          <div class="form-group">
            <label>Ballistic Overview &amp; Lore</label>
            <textarea rows="3">Custom built by Taran Tactical Innovations for John Wick's climactic battle at the Sacré-Cœur in Paris. Features built-in compensator, 21-round capacity, and match trigger.</textarea>
          </div>

          <div style="display:flex; gap:1rem; margin-top:1.5rem;">
            <button type="button" class="btn-primary" style="width:auto; padding:0.8rem 2rem;">Commit Changes</button>
            <a href="weapons.html" class="btn-secondary" style="width:auto; padding:0.8rem 2rem; text-decoration:none; text-align:center;">Cancel</a>
          </div>
        </form>
      </div>
    </div>
  </section>
</body>
</html>
"""

# 6. Admin Orders Management View
orders_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Manage Orders | Admin — JOHN WICK & CO. ARMS</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <style>
    .admin-nav { display:flex; gap:1.2rem; align-items:center; }
    .admin-nav a { text-decoration:none; color:var(--text-main); font-weight:600; font-size:0.95rem; }
    .admin-nav a.active { color:var(--accent-gold); border-bottom:2px solid var(--accent-gold); padding-bottom:4px; }
    table { width:100%; border-collapse:collapse; margin-top:1.5rem; background:var(--bg-card); border:1px solid var(--gunmetal-border); border-radius:var(--radius); }
    th, td { padding:1rem; text-align:left; border-bottom:1px solid var(--gunmetal-border); }
    th { color:var(--accent-gold); font-family:'Cinzel', serif; background:rgba(212,175,55,0.08); font-size:0.85rem; }
    td { color:var(--text-main); font-size:0.88rem; }
    .status-select { background:var(--bg-dark); border:1px solid var(--accent-gold); color:var(--text-main); padding:0.4rem 0.6rem; border-radius:4px; font-size:0.85rem; }
    .status-badge { display:inline-block; padding:0.3rem 0.7rem; border-radius:4px; font-size:0.75rem; font-weight:700; text-transform:uppercase; }
    .badge-pending { background:rgba(243,156,18,0.2); color:#f39c12; border:1px solid #f39c12; }
    .badge-processing { background:rgba(52,152,219,0.2); color:#3498db; border:1px solid #3498db; }
    .badge-approved { background:rgba(39,174,96,0.2); color:#27ae60; border:1px solid #27ae60; }
  </style>
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="dashboard.html" class="logo">
        <span class="gold-text">JOHN WICK &amp; CO.</span> ARMS
        <span class="logo-sub">CONTINENTAL ARMS - COMMAND DESK</span>
      </a>
      <nav class="admin-nav">
        <a href="dashboard.html">Dashboard</a>
        <a href="weapons.html">Weapons Inventory (18)</a>
        <a href="add_weapon.html">+ Add Weapon</a>
        <a href="orders.html" class="active">Orders Ledger (5)</a>
        <a href="../index.html" class="btn-gold-sm" style="color:var(--bg-dark)!important;">Logout Admin</a>
      </nav>
    </div>
  </header>

  <section class="page-section active">
    <div class="catalog-container">
      <h2 class="section-title" style="text-align:left; margin-bottom:0.2rem;">Operative Requisitions Ledger</h2>
      <p style="color:var(--text-muted); font-size:0.9rem;">Review high-caliber armory purchase orders, verify clearance, and update logistics status.</p>

      <table>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Operative</th>
            <th>Requisition Summary</th>
            <th>Clearance Level</th>
            <th>Settlement Method</th>
            <th>Total ($)</th>
            <th>Update Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>#ORD-90812</strong></td>
            <td>John Wick<br><span style="color:var(--text-muted); font-size:0.8rem;">wick@continental.nyc</span></td>
            <td>1x TTI JW4 Pit Viper, 2x Benelli M4</td>
            <td><span style="color:var(--accent-gold); font-weight:700;">LEVEL 5: BABA YAGA</span></td>
            <td>Continental Gold Coins (5 Coins)</td>
            <td><strong style="color:var(--accent-gold);">$23,500</strong></td>
            <td>
              <select class="status-select">
                <option selected>Pending</option>
                <option>Processing</option>
                <option>Dispatched</option>
                <option>Delivered</option>
                <option>Cancelled</option>
              </select>
            </td>
            <td><button class="btn-gold-sm" style="font-size:0.75rem; padding:0.3rem 0.8rem;">Update</button></td>
          </tr>
          <tr>
            <td><strong>#ORD-90811</strong></td>
            <td>Sofia Al-Azwar<br><span style="color:var(--text-muted); font-size:0.8rem;">sofia@continental.ma</span></td>
            <td>1x SIG Sauer MPX, 1x TTI Combat Master</td>
            <td><span style="color:var(--accent-gold); font-weight:700;">LEVEL 4: HIGH TABLE</span></td>
            <td>Swiss Private Bank Escrow</td>
            <td><strong style="color:var(--accent-gold);">$8,300</strong></td>
            <td>
              <select class="status-select">
                <option>Pending</option>
                <option selected>Processing</option>
                <option>Dispatched</option>
                <option>Delivered</option>
              </select>
            </td>
            <td><button class="btn-gold-sm" style="font-size:0.75rem; padding:0.3rem 0.8rem;">Update</button></td>
          </tr>
          <tr>
            <td><strong>#ORD-90810</strong></td>
            <td>Caine<br><span style="color:var(--text-muted); font-size:0.8rem;">caine@high-table.int</span></td>
            <td>1x Genesis Gen-12 Breacher</td>
            <td><span style="color:var(--accent-gold); font-weight:700;">LEVEL 4: HIGH TABLE</span></td>
            <td>High Table Encrypted Card</td>
            <td><strong style="color:var(--accent-gold);">$6,800</strong></td>
            <td>
              <select class="status-select">
                <option>Pending</option>
                <option>Processing</option>
                <option selected>Dispatched</option>
                <option>Delivered</option>
              </select>
            </td>
            <td><button class="btn-gold-sm" style="font-size:0.75rem; padding:0.3rem 0.8rem;">Update</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</body>
</html>
"""

# 7. phpMyAdmin Database Schema View
schema_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>phpMyAdmin 5.2.1 — john_wick_arms Schema</title>
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family: Tahoma, 'Segoe UI', Arial, sans-serif; }
    body { background:#f3f3f3; color:#333; font-size:12px; }
    .pma-header { background:#fff; border-bottom:1px solid #ddd; padding:8px 16px; display:flex; align-items:center; justify-content:space-between; }
    .pma-logo { font-size:18px; font-weight:bold; color:#f08a00; display:flex; align-items:center; gap:8px; }
    .pma-logo span { color:#333; font-size:14px; }
    .pma-server { font-size:11px; color:#666; }
    .pma-layout { display:flex; min-height:calc(100vh - 45px); }
    .pma-sidebar { width:240px; background:#fff; border-right:1px solid #ddd; padding:12px; font-size:11px; }
    .pma-sidebar h4 { color:#555; margin-bottom:8px; font-size:12px; display:flex; align-items:center; gap:6px; }
    .pma-table-list { list-style:none; padding-left:14px; }
    .pma-table-list li { padding:4px 0; color:#0055aa; cursor:pointer; display:flex; align-items:center; gap:6px; }
    .pma-table-list li:hover { text-decoration:underline; }
    .pma-main { flex:1; padding:16px 24px; background:#fbfbfb; }
    .pma-breadcrumb { font-size:13px; color:#555; margin-bottom:14px; padding-bottom:8px; border-bottom:1px solid #e0e0e0; }
    .pma-breadcrumb strong { color:#0055aa; }
    .pma-tabs { display:flex; gap:2px; margin-bottom:16px; border-bottom:1px solid #ccc; }
    .pma-tab { padding:6px 14px; background:#e0e0e0; border:1px solid #ccc; border-bottom:none; border-radius:3px 3px 0 0; color:#333; font-weight:bold; text-decoration:none; }
    .pma-tab.active { background:#fff; border-bottom:1px solid #fff; color:#f08a00; margin-bottom:-1px; }
    .schema-card { background:#fff; border:1px solid #ccc; border-radius:4px; box-shadow:0 1px 3px rgba(0,0,0,0.06); margin-bottom:18px; }
    .schema-title { background:#e8eff7; padding:8px 12px; font-weight:bold; color:#004080; border-bottom:1px solid #b8d0ed; display:flex; justify-content:space-between; }
    table.data-table { width:100%; border-collapse:collapse; text-align:left; font-size:11px; }
    table.data-table th { background:#f5f5f5; padding:6px 10px; border-bottom:1px solid #ddd; border-right:1px solid #eee; color:#444; }
    table.data-table td { padding:6px 10px; border-bottom:1px solid #eee; border-right:1px solid #eee; font-family:'Courier New', monospace; font-size:11px; }
    table.data-table tr:nth-child(even) { background:#fafafa; }
    .key-icon { color:#e67e22; font-weight:bold; font-size:10px; margin-right:4px; }
    .fk-icon { color:#3498db; font-weight:bold; font-size:10px; margin-right:4px; }
  </style>
</head>
<body>
  <div class="pma-header">
    <div class="pma-logo">
      phpMyAdmin <span>5.2.1</span>
    </div>
    <div class="pma-server">Server: 127.0.0.1:3306 &bull; Server version: 8.0.33-MySQL Community Server &bull; Protocol: TCP/IP &bull; User: root@localhost</div>
  </div>

  <div class="pma-layout">
    <div class="pma-sidebar">
      <h4>&#128190; Database: john_wick_arms</h4>
      <ul class="pma-table-list">
        <li>&#128196; admin_users (1 row)</li>
        <li>&#128196; customers (5 rows)</li>
        <li>&#128196; weapons (18 rows)</li>
        <li>&#128196; orders (5 rows)</li>
        <li>&#128196; order_items (12 rows)</li>
      </ul>
    </div>

    <div class="pma-main">
      <div class="pma-breadcrumb">
        Server: <strong>127.0.0.1</strong> &raquo; Database: <strong>john_wick_arms</strong> &raquo; Structure &amp; Relations Schema
      </div>

      <div class="pma-tabs">
        <div class="pma-tab active">Structure</div>
        <div class="pma-tab">SQL</div>
        <div class="pma-tab">Search</div>
        <div class="pma-tab">Query</div>
        <div class="pma-tab">Export</div>
        <div class="pma-tab">Import</div>
        <div class="pma-tab">Designer</div>
      </div>

      <!-- Weapons Table Schema -->
      <div class="schema-card">
        <div class="schema-title">
          <span>Table: `weapons` (18 rows - InnoDB, utf8mb4_unicode_ci)</span>
          <span style="font-size:11px; font-weight:normal; color:#666;">Size: 48.0 KiB</span>
        </div>
        <table class="data-table">
          <thead>
            <tr><th>#</th><th>Name</th><th>Type</th><th>Collation</th><th>Null</th><th>Default</th><th>Extra</th></tr>
          </thead>
          <tbody>
            <tr><td>1</td><td><span class="key-icon">&#128273;</span>weapon_id</td><td>int(11)</td><td>-</td><td>No</td><td>None</td><td>AUTO_INCREMENT (Primary Key)</td></tr>
            <tr><td>2</td><td>name</td><td>varchar(150)</td><td>utf8mb4_unicode_ci</td><td>No</td><td>None</td><td></td></tr>
            <tr><td>3</td><td>category</td><td>enum('Sidearms','Shotguns','Submachine Guns','Rifles')</td><td>utf8mb4_unicode_ci</td><td>No</td><td>None</td><td></td></tr>
            <tr><td>4</td><td>price</td><td>decimal(10,2)</td><td>-</td><td>No</td><td>None</td><td></td></tr>
            <tr><td>5</td><td>description</td><td>text</td><td>utf8mb4_unicode_ci</td><td>Yes</td><td>NULL</td><td></td></tr>
            <tr><td>6</td><td>image</td><td>varchar(255)</td><td>utf8mb4_unicode_ci</td><td>Yes</td><td>NULL</td><td></td></tr>
            <tr><td>7</td><td>status</td><td>enum('available','out_of_stock')</td><td>utf8mb4_unicode_ci</td><td>No</td><td>'available'</td><td></td></tr>
            <tr><td>8</td><td>created_at</td><td>timestamp</td><td>-</td><td>No</td><td>CURRENT_TIMESTAMP</td><td></td></tr>
          </tbody>
        </table>
      </div>

      <!-- Orders & Order Items Schema -->
      <div class="schema-card">
        <div class="schema-title">
          <span>Table: `orders` &amp; `order_items` (Foreign Key Relationship)</span>
          <span style="font-size:11px; font-weight:normal; color:#666;">InnoDB Referential Integrity</span>
        </div>
        <table class="data-table">
          <thead>
            <tr><th>Table</th><th>Column</th><th>Type</th><th>Constraint</th><th>Referenced Table / Column</th></tr>
          </thead>
          <tbody>
            <tr><td>orders</td><td><span class="key-icon">&#128273;</span>order_id</td><td>int(11)</td><td>PRIMARY KEY</td><td>AUTO_INCREMENT</td></tr>
            <tr><td>orders</td><td><span class="fk-icon">&#8599;</span>customer_id</td><td>int(11)</td><td>FOREIGN KEY</td><td>`customers` (`customer_id`) ON DELETE CASCADE</td></tr>
            <tr><td>order_items</td><td><span class="key-icon">&#128273;</span>item_id</td><td>int(11)</td><td>PRIMARY KEY</td><td>AUTO_INCREMENT</td></tr>
            <tr><td>order_items</td><td><span class="fk-icon">&#8599;</span>order_id</td><td>int(11)</td><td>FOREIGN KEY</td><td>`orders` (`order_id`) ON DELETE CASCADE</td></tr>
            <tr><td>order_items</td><td><span class="fk-icon">&#8599;</span>weapon_id</td><td>int(11)</td><td>FOREIGN KEY</td><td>`weapons` (`weapon_id`) ON DELETE CASCADE</td></tr>
          </tbody>
        </table>
      </div>

    </div>
  </div>
</body>
</html>
"""

files = {
    'admin_preview/login.html': login_html,
    'admin_preview/dashboard.html': dashboard_html,
    'admin_preview/weapons.html': weapons_html,
    'admin_preview/add_weapon.html': add_weapon_html,
    'admin_preview/edit_weapon.html': edit_weapon_html,
    'admin_preview/orders.html': orders_html,
    'admin_preview/db_schema.html': schema_html
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {path}")
