<?php
$page_title = 'Login';
require_once 'db_connect.php';

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email    = trim($_POST['email'] ?? '');
    $password = trim($_POST['password'] ?? '');

    if (!$email || !$password) {
        $error = 'Email and password are required.';
    } else {
        $email_e = mysqli_real_escape_string($conn, $email);
        $pass_e  = mysqli_real_escape_string($conn, $password);

        $result = mysqli_query($conn, "SELECT * FROM customers WHERE email='$email_e' AND password='$pass_e'");
        if ($result && mysqli_num_rows($result) === 1) {
            $customer = mysqli_fetch_assoc($result);
            $_SESSION['customer_id']   = $customer['customer_id'];
            $_SESSION['customer_name'] = $customer['full_name'];
            $_SESSION['customer_email']= $customer['email'];
            header('Location: index.php');
            exit;
        } else {
            $error = 'Invalid email or password.';
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
    <h2 class="section-title">Operative Login</h2>
    <p class="section-subtitle">Authenticate your Continental session.</p>

    <?php if ($error): ?>
      <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>

    <form method="post" novalidate>
      <div class="form-group">
        <label for="email">Email Address *</label>
        <input type="email" id="email" name="email" placeholder="wick@continental.com" value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="password">Password *</label>
        <input type="password" id="password" name="password" placeholder="••••••••" required>
      </div>
      <button type="submit" class="btn-primary">Authenticate Operative</button>
    </form>

    <p style="text-align:center; margin-top:1rem; color:var(--text-muted);">New operative? <a href="register.php" style="color:var(--accent-gold);">Register here</a></p>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
