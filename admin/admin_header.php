<?php
if (session_status() === PHP_SESSION_NONE) session_start();
require_once '../db_connect.php';

if (!isset($_SESSION['admin_id'])) {
    header('Location: index.php');
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?php echo isset($page_title) ? $page_title . ' | ' : ''; ?>Admin – JOHN WICK &amp; CO. ARMS</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <style>
    .admin-nav { display:flex; gap:1rem; flex-wrap:wrap; }
    .admin-nav a { text-decoration:none; }
    .stat-grid { display:grid; grid-template-columns:repeat(auto-fill, minmax(200px,1fr)); gap:1.5rem; margin:2rem 0; }
    .stat-card { background:var(--bg-card); border:1px solid var(--gunmetal-border); border-radius:var(--radius); padding:1.5rem; text-align:center; }
    .stat-card h3 { color:var(--accent-gold); font-size:2rem; margin-bottom:0.3rem; }
    .stat-card p { color:var(--text-muted); font-size:0.9rem; }
    table { width:100%; border-collapse:collapse; margin-top:1rem; }
    th, td { padding:0.8rem; text-align:left; border-bottom:1px solid var(--gunmetal-border); }
    th { color:var(--accent-gold); font-family:'Cinzel', serif; background:rgba(212,175,55,0.08); }
    td { color:var(--text-main); }
    .form-group select, .form-group textarea {
      width:100%; padding:0.8rem; background:var(--bg-dark); border:1px solid var(--gunmetal-border);
      border-radius:var(--radius); color:var(--text-main); font-family:'Inter', sans-serif;
    }
    .form-group select:focus, .form-group textarea:focus { outline:none; border-color:var(--accent-gold); }
  </style>
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="dashboard.php" class="brand-logo" style="text-decoration:none;">JOHN WICK <span>&amp; CO.</span> — ADMIN</a>
      <nav class="admin-nav">
        <a class="nav-item" href="dashboard.php">Dashboard</a>
        <a class="nav-item" href="weapons.php">Weapons</a>
        <a class="nav-item" href="add_weapon.php">Add Weapon</a>
        <a class="nav-item" href="orders.php">Orders</a>
        <a class="nav-item" href="logout.php">Logout</a>
      </nav>
    </div>
  </header>
  <main id="app-root">
