<?php
$page_title = 'Register';
require_once 'db_connect.php';

$error = '';
$success = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name     = trim($_POST['full_name'] ?? '');
    $email    = trim($_POST['email'] ?? '');
    $password = trim($_POST['password'] ?? '');
    $phone    = trim($_POST['phone'] ?? '');
    $address  = trim($_POST['address'] ?? '');

    if (!$name || !$email || !$password) {
        $error = 'Full name, email, and password are required.';
    } elseif (strlen($password) < 6) {
        $error = 'Password must be at least 6 characters.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = 'Please enter a valid email address.';
    } else {
        // Check if email exists
        $check = mysqli_query($conn, "SELECT customer_id FROM customers WHERE email='" . mysqli_real_escape_string($conn, $email) . "'");
        if (mysqli_num_rows($check) > 0) {
            $error = 'An account with this email already exists.';
        } else {
            $name_e  = mysqli_real_escape_string($conn, $name);
            $email_e = mysqli_real_escape_string($conn, $email);
            $pass_e  = mysqli_real_escape_string($conn, $password);
            $phone_e = mysqli_real_escape_string($conn, $phone);
            $addr_e  = mysqli_real_escape_string($conn, $address);

            $sql = "INSERT INTO customers (full_name, email, password, phone, address) VALUES ('$name_e', '$email_e', '$pass_e', '$phone_e', '$addr_e')";
            if (mysqli_query($conn, $sql)) {
                $success = 'Registration successful! You can now login.';
            } else {
                $error = 'Registration failed. Please try again.';
            }
        }
    }
}

require_once 'includes/header.php';
?>

<section class="page-section active">
  <div class="hero-banner register-hero">
    <span class="badge">Continental Credentialing</span>
    <h1 class="hero-title">OPERATIVE REGISTRATION</h1>
  </div>

  <div class="form-container">
    <h2 class="section-title">New Credentials</h2>
    <p class="section-subtitle">Create your High Table clearance profile.</p>

    <?php if ($error): ?>
      <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>
    <?php if ($success): ?>
      <p style="color:var(--success-green); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($success); ?></p>
      <a href="login.php" class="btn-primary" style="display:block;text-align:center;text-decoration:none;">Proceed to Login</a>
    <?php else: ?>

    <form method="post" novalidate>
      <div class="form-group">
        <label for="full_name">Full Operative Name *</label>
        <input type="text" id="full_name" name="full_name" placeholder="John Wick" value="<?php echo htmlspecialchars($_POST['full_name'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="email">Secure Email Address *</label>
        <input type="email" id="email" name="email" placeholder="wick@continental.com" value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="password">Security Password * (min 6 characters)</label>
        <input type="password" id="password" name="password" placeholder="At least 6 characters" required>
      </div>
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="text" id="phone" name="phone" placeholder="+1-555-0123" value="<?php echo htmlspecialchars($_POST['phone'] ?? ''); ?>">
      </div>
      <div class="form-group">
        <label for="address">Delivery Address</label>
        <input type="text" id="address" name="address" placeholder="Continental Hotel, NYC" value="<?php echo htmlspecialchars($_POST['address'] ?? ''); ?>">
      </div>
      <button type="submit" class="btn-primary">Register Account</button>
    </form>

    <p style="text-align:center; margin-top:1rem; color:var(--text-muted);">Already registered? <a href="login.php" style="color:var(--accent-gold);">Login here</a></p>
    <?php endif; ?>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
