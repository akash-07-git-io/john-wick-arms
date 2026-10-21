<?php if (session_status() === PHP_SESSION_NONE) session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?php echo isset($page_title) ? $page_title . ' | ' : ''; ?>JOHN WICK &amp; CO. ARMS</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="index.php" class="brand-logo" style="text-decoration:none;">JOHN WICK <span>&amp; CO. ARMS</span></a>
      <nav class="nav-links">
        <a class="nav-item" href="index.php">Home</a>
        <a class="nav-item" href="catalog.php">Armory Catalog</a>
        <a class="nav-item" href="cart.php">Cart
          (<?php echo isset($_SESSION['cart']) ? array_sum($_SESSION['cart']) : 0; ?>)
        </a>
        <?php if (isset($_SESSION['customer_id'])): ?>
          <a class="nav-item" href="my_orders.php">My Orders</a>
          <a class="nav-item" href="logout.php">Logout</a>
        <?php else: ?>
          <a class="nav-item" href="register.php">Register</a>
          <a class="nav-item" href="login.php">Login</a>
        <?php endif; ?>
      </nav>
    </div>
  </header>
  <main id="app-root">
