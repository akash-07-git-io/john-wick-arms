<?php
$page_title = 'Admin Login';
session_start();

require_once '../db_connect.php';

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = trim($_POST['password'] ?? '');

    if (!$username || !$password) {
        $error = 'Username and password are required.';
    } else {
        $username_e = mysqli_real_escape_string($conn, $username);
        $password_e = mysqli_real_escape_string($conn, $password);
        $result = mysqli_query($conn, "SELECT * FROM admin_users WHERE username='$username_e' AND password='$password_e'");

        if ($result && mysqli_num_rows($result) === 1) {
            $admin = mysqli_fetch_assoc($result);
            $_SESSION['admin_id']   = $admin['admin_id'];
            $_SESSION['admin_name'] = $admin['full_name'];
            header('Location: dashboard.php');
            exit;
        } else {
            $error = 'Invalid admin credentials.';
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Login | JOHN WICK &amp; CO. ARMS</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <div class="brand-logo">JOHN WICK <span>&amp; CO. ARMS</span> — ADMIN</div>
    </div>
  </header>
  <main id="app-root">
    <section class="page-section active">
      <div class="hero-banner login-hero">
        <span class="badge">Administrative Access</span>
        <h1 class="hero-title">CONTINENTAL COMMAND CENTER</h1>
      </div>

      <div class="form-container">
        <h2 class="section-title">Admin Login</h2>
        <p class="section-subtitle">Authenticate as Continental Manager.</p>

        <?php if ($error): ?>
          <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
        <?php endif; ?>

        <form method="post" novalidate>
          <div class="form-group">
            <label for="username">Username *</label>
            <input type="text" id="username" name="username" placeholder="admin" required>
          </div>
          <div class="form-group">
            <label for="password">Password *</label>
            <input type="password" id="password" name="password" placeholder="••••••••" required>
          </div>
          <button type="submit" class="btn-primary">Login to Admin Panel</button>
        </form>

        <p style="text-align:center; margin-top:1rem;"><a href="../index.php" style="color:var(--text-muted);">← Back to Store</a></p>
      </div>
    </section>
  </main>
  <footer class="footer"><p>&copy; 2026 JOHN WICK &amp; CO. ARMS – Admin Panel</p></footer>
</body>
</html>
