<?php
$page_title = 'Operative Registration';
require_once 'db_connect.php';

$error = '';
$success = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name     = trim($_POST['full_name'] ?? '');
    $email    = trim($_POST['email'] ?? '');
    $password = trim($_POST['password'] ?? '');
    $tier     = trim($_POST['clearance_tier'] ?? 'Tier 2 — Sovereign Continental Diplomat');
    $marker   = trim($_POST['marker_code'] ?? 'BOM-7741-JW');
    $duty     = trim($_POST['duty_station'] ?? 'New York Continental');
    $phone    = trim($_POST['phone'] ?? '');
    $address  = trim($_POST['address'] ?? '');

    if (!$name || !$email || !$password) {
        $error = 'Full name, email, and security password are required.';
    } elseif (strlen($password) < 6) {
        $error = 'Password must be at least 6 characters.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = 'Please enter a valid Continental email address.';
    } else {
        $email_e = mysqli_real_escape_string($conn, $email);
        $check = mysqli_query($conn, "SELECT customer_id FROM customers WHERE email='$email_e'");
        if (mysqli_num_rows($check) > 0) {
            $error = 'An operative profile with this email already exists.';
        } else {
            $name_e   = mysqli_real_escape_string($conn, $name);
            $pass_e   = password_hash($password, PASSWORD_DEFAULT);
            $tier_e   = mysqli_real_escape_string($conn, $tier);
            $marker_e = mysqli_real_escape_string($conn, $marker);
            $duty_e   = mysqli_real_escape_string($conn, $duty);
            $phone_e  = mysqli_real_escape_string($conn, $phone);
            $addr_e   = mysqli_real_escape_string($conn, $address);

            $sql = "INSERT INTO customers (full_name, email, password, clearance_tier, marker_code, duty_station, phone, address) 
                    VALUES ('$name_e', '$email_e', '$pass_e', '$tier_e', '$marker_e', '$duty_e', '$phone_e', '$addr_e')";
            if (mysqli_query($conn, $sql)) {
                $success = 'High Table Weapon Clearance Approved! You may now authenticate.';
            } else {
                $error = 'Registration failed: ' . mysqli_error($conn);
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

  <div class="form-container" style="max-width:680px;">
    <h2 class="section-title">New Credentials &amp; Weapon Clearance</h2>
    <p class="section-subtitle">Complete your high-table biometric and tactical clearance profile.</p>

    <?php if ($error): ?>
      <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>
    <?php if ($success): ?>
      <p style="color:var(--success-green); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($success); ?></p>
      <a href="login.php" class="btn-primary" style="display:block;text-align:center;text-decoration:none;">Proceed to Operative Login</a>
    <?php else: ?>

    <form method="post" novalidate>
      <div class="row-2">
        <div class="form-group">
          <label for="full_name">Full Operative Legal / Alias Name *</label>
          <input type="text" id="full_name" name="full_name" placeholder="John Wick" value="<?php echo htmlspecialchars($_POST['full_name'] ?? ''); ?>" required>
        </div>
        <div class="form-group">
          <label for="email">Secure Continental Email *</label>
          <input type="email" id="email" name="email" placeholder="wick@continental.com" value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>" required>
        </div>
      </div>

      <div class="row-2">
        <div class="form-group">
          <label for="clearance_tier">High Table Clearance Tier *</label>
          <select id="clearance_tier" name="clearance_tier">
            <option value="Tier 1 — Standard Operative">Tier 1 &mdash; Standard Operative</option>
            <option value="Tier 2 — Sovereign Continental Diplomat" selected>Tier 2 &mdash; Sovereign Continental Diplomat</option>
            <option value="Tier 3 — High Table Inner Circle">Tier 3 &mdash; High Table Inner Circle</option>
          </select>
        </div>
        <div class="form-group">
          <label for="marker_code">Blood Oath Marker / Operative Code *</label>
          <input type="text" id="marker_code" name="marker_code" placeholder="BOM-7741-JW" value="<?php echo htmlspecialchars($_POST['marker_code'] ?? 'BOM-7741-JW'); ?>">
        </div>
      </div>

      <div class="row-2">
        <div class="form-group">
          <label for="duty_station">Assigned Duty Continental Safehouse *</label>
          <select id="duty_station" name="duty_station">
            <option value="New York Continental">New York Continental</option>
            <option value="Rome Continental">Rome Continental</option>
            <option value="Osaka Continental">Osaka Continental</option>
            <option value="Casablanca Continental">Casablanca Continental</option>
            <option value="Berlin Underground">Berlin Underground Safehouse</option>
          </select>
        </div>
        <div class="form-group">
          <label for="phone">Encrypted Comms Phone Number</label>
          <input type="text" id="phone" name="phone" placeholder="+1-555-0144" value="<?php echo htmlspecialchars($_POST['phone'] ?? ''); ?>">
        </div>
      </div>

      <div class="form-group">
        <label for="address">Delivery Safehouse Coordinates / Street Address *</label>
        <input type="text" id="address" name="address" placeholder="1 Wall Street Court, Continental Hotel NYC" value="<?php echo htmlspecialchars($_POST['address'] ?? ''); ?>" required>
      </div>

      <div class="form-group">
        <label for="password">Security Clearance Password * (min 6 characters)</label>
        <input type="password" id="password" name="password" placeholder="••••••••••••" required>
      </div>

      <div class="form-group" style="display:flex; align-items:center; gap:0.6rem; margin:1rem 0;">
        <input type="checkbox" id="rules" checked required style="accent-color:var(--accent-gold); width:18px; height:18px;">
        <label for="rules" style="font-size:0.85rem; color:var(--text-muted);">
          I swear allegiance to Continental rules. No business shall be conducted on Continental grounds.
        </label>
      </div>

      <button type="submit" class="btn-primary">Register Continental Clearance</button>
    </form>

    <p style="text-align:center; margin-top:1.2rem; color:var(--text-muted);">
      Already authenticated? <a href="login.php" style="color:var(--accent-gold);">Login here</a>
    </p>
    <?php endif; ?>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
