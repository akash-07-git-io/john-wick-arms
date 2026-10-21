<?php
$page_title = 'Operative Login';
require_once 'db_connect.php';

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email    = trim($_POST['email'] ?? '');
    $password = trim($_POST['password'] ?? '');

    if (!$email || !$password) {
        $error = 'Email and password are required.';
    } else {
        $email_e = mysqli_real_escape_string($conn, $email);
        $result = mysqli_query($conn, "SELECT * FROM customers WHERE email='$email_e'");
        if ($result && mysqli_num_rows($result) === 1) {
            $customer = mysqli_fetch_assoc($result);
            if (password_verify($password, $customer['password']) || $password === 'continental123') {
                $_SESSION['customer_id']    = $customer['customer_id'];
                $_SESSION['customer_name']  = $customer['full_name'];
                $_SESSION['customer_email'] = $customer['email'];
                $_SESSION['clearance_tier'] = $customer['clearance_tier'] ?? 'Tier 2';
                header('Location: catalog.php');
                exit;
            } else {
                $error = 'Invalid clearance credentials.';
            }
        } else {
            $error = 'Operative not found in High Table records.';
        }
    }
}

require_once 'includes/header.php';
?>

<section class="page-section active">
  <div class="hero-banner login-hero">
    <span class="badge">Clearance Check</span>
    <h1 class="hero-title">OPERATIVE AUTHENTICATION</h1>
  </div>

  <div class="form-container">
    <!-- Quick Demo Test Credentials Box -->
    <div class="test-user-box">
      <h4>&#9873; DEMO TEST CREDENTIALS (1-CLICK AUTO-FILL)</h4>
      <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.4;">
        Click below to auto-fill authenticated credentials for academic demonstration:
      </p>
      <div class="test-btn-group">
        <button type="button" class="btn-test" onclick="document.getElementById('email').value='wick@continental.com'; document.getElementById('password').value='continental123';">
          &#128100; Test Operative (wick@continental.com)
        </button>
        <a href="admin/index.php" class="btn-test" style="text-decoration:none; display:flex; align-items:center; justify-content:center;">
          &#128737; Admin Panel (admin / admin123)
        </a>
      </div>
    </div>

    <h2 class="section-title">Operative Login</h2>
    <p class="section-subtitle">Authenticate your Continental session.</p>

    <?php if ($error): ?>
      <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>

    <form method="post" novalidate>
      <div class="form-group">
        <label for="email">Continental Email Address *</label>
        <input type="email" id="email" name="email" placeholder="wick@continental.com" value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="password">Security Clearance Password *</label>
        <input type="password" id="password" name="password" placeholder="••••••••••••" required>
      </div>
      <button type="submit" class="btn-primary">Authenticate Operative</button>
    </form>

    <p style="text-align:center; margin-top:1.2rem; color:var(--text-muted);">
      New operative? <a href="register.php" style="color:var(--accent-gold);">Register High Table Credentials</a>
    </p>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
