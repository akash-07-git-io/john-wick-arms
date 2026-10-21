<?php
$page_title = 'Requisition Checkout';
require_once 'db_connect.php';

// Must be logged in
if (!isset($_SESSION['customer_id'])) {
    header('Location: login.php');
    exit;
}

// Must have items in cart
$cart = $_SESSION['cart'] ?? [];
if (empty($cart)) {
    header('Location: cart.php');
    exit;
}

$error = '';
$customer_id = $_SESSION['customer_id'];

// Fetch cart items from DB
$ids = implode(',', array_map('intval', array_keys($cart)));
$result = mysqli_query($conn, "SELECT * FROM weapons WHERE weapon_id IN ($ids)");
$cart_items = [];
$total = 0;
while ($row = mysqli_fetch_assoc($result)) {
    $qty = $cart[$row['weapon_id']];
    $row['quantity'] = $qty;
    $row['subtotal'] = $row['price'] * $qty;
    $total += $row['subtotal'];
    $cart_items[] = $row;
}

// Fetch customer details for pre-fill
$cust_result = mysqli_query($conn, "SELECT * FROM customers WHERE customer_id=$customer_id");
$customer = mysqli_fetch_assoc($cust_result);

// Process checkout
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $d_name    = trim($_POST['delivery_name'] ?? '');
    $d_phone   = trim($_POST['delivery_phone'] ?? '');
    $d_address = trim($_POST['delivery_address'] ?? '');
    $d_city    = trim($_POST['delivery_city'] ?? '');
    $d_zip     = trim($_POST['delivery_zip'] ?? '');
    $pay_method= trim($_POST['payment_method'] ?? 'Continental Gold Coins');

    if (!$d_name || !$d_phone || !$d_address || !$d_city || !$d_zip) {
        $error = 'All delivery details and coordinates are required.';
    } else {
        $d_name_e    = mysqli_real_escape_string($conn, $d_name);
        $d_phone_e   = mysqli_real_escape_string($conn, $d_phone);
        $d_address_e = mysqli_real_escape_string($conn, $d_address);
        $d_city_e    = mysqli_real_escape_string($conn, $d_city);
        $d_zip_e     = mysqli_real_escape_string($conn, $d_zip);
        $pay_e       = mysqli_real_escape_string($conn, $pay_method);

        $sql = "INSERT INTO orders (customer_id, total_amount, payment_method, delivery_name, delivery_phone, delivery_address, delivery_city, delivery_zip)
                VALUES ($customer_id, $total, '$pay_e', '$d_name_e', '$d_phone_e', '$d_address_e', '$d_city_e', '$d_zip_e')";

        if (mysqli_query($conn, $sql)) {
            $order_id = mysqli_insert_id($conn);

            foreach ($cart_items as $item) {
                $wid = $item['weapon_id'];
                $qty = $item['quantity'];
                $price = $item['price'];
                mysqli_query($conn, "INSERT INTO order_items (order_id, weapon_id, quantity, unit_price) VALUES ($order_id, $wid, $qty, $price)");
            }

            $_SESSION['cart'] = [];
            header("Location: order_success.php?order_id=$order_id&method=" . urlencode($pay_method));
            exit;
        } else {
            $error = 'Failed to place order: ' . mysqli_error($conn);
        }
    }
}

require_once 'includes/header.php';
$coins_needed = ceil($total / 1000);
?>

<section class="page-section active">
  <div class="hero-banner payment-hero">
    <span class="badge">Encrypted Checkout</span>
    <h1 class="hero-title">REQUISITION &amp; SETTLEMENT</h1>
  </div>

  <div class="payment-layout-container">
    <!-- Order Summary -->
    <div class="cart-container">
      <h2 class="section-title" style="text-align:left;">Order Summary</h2>
      <div class="cart-items-list">
        <?php foreach ($cart_items as $item): ?>
        <div class="cart-item-row">
          <div>
            <div style="font-weight:600;"><?php echo htmlspecialchars($item['name']); ?></div>
            <div style="color:var(--text-muted); font-size:0.85rem;">Qty: <?php echo $item['quantity']; ?> &times; $<?php echo number_format($item['price'], 2); ?></div>
          </div>
          <span style="color:var(--accent-gold); font-weight:700;">$<?php echo number_format($item['subtotal'], 2); ?></span>
        </div>
        <?php endforeach; ?>
      </div>
      <div class="cart-summary">
        <span>Total Ledger Amount:</span>
        <span>$<?php echo number_format($total, 2); ?></span>
      </div>
      <div style="margin-top:1rem; padding:0.8rem; background:rgba(212,175,55,0.08); border:1px solid var(--accent-gold); border-radius:var(--radius); text-align:center;">
        <span style="color:var(--accent-gold); font-size:0.9rem;">Continental Gold Coin Equivalent:</span>
        <div style="font-size:1.3rem; font-weight:bold; color:var(--accent-gold);"><?php echo $coins_needed; ?> Gold Coins</div>
      </div>
    </div>

    <!-- Settlement & Delivery Details Form -->
    <div class="form-container" style="margin:0; max-width:100%;">
      <h2 class="section-title">Delivery &amp; Payment Method</h2>
      <p class="section-subtitle">Select settlement channel and safehouse delivery coordinates.</p>

      <?php if ($error): ?>
        <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
      <?php endif; ?>

      <form method="post" novalidate>
        <div class="form-group">
          <label for="payment_method">Settlement Method *</label>
          <select id="payment_method" name="payment_method">
            <option value="Continental Gold Coins (Ledger Credit)">🪙 Continental Gold Coins (Ledger Credit — <?php echo $coins_needed; ?> Coins)</option>
            <option value="High Table Encrypted Card">💳 High Table Encrypted Card (Black Card)</option>
            <option value="Cold Vault Crypto Escrow (BTC/USDT/XMR)">🔒 Cold Vault Crypto Escrow (BTC / USDT / Monero)</option>
            <option value="Swiss Zurich Wire Transfer">🏦 Swiss Zurich Wire Transfer (Bank Leu Vault)</option>
            <option value="Safehouse Dead Drop Courier (Cash on Delivery)">📦 Safehouse Dead Drop Courier (Cash on Delivery)</option>
          </select>
        </div>

        <div class="form-group">
          <label for="delivery_name">Recipient Operative Name *</label>
          <input type="text" id="delivery_name" name="delivery_name"
                 value="<?php echo htmlspecialchars($_POST['delivery_name'] ?? $customer['full_name'] ?? ''); ?>"
                 placeholder="John Wick" required>
        </div>
        <div class="form-group">
          <label for="delivery_phone">Encrypted Contact Phone *</label>
          <input type="text" id="delivery_phone" name="delivery_phone"
                 value="<?php echo htmlspecialchars($_POST['delivery_phone'] ?? $customer['phone'] ?? '+1-555-0144'); ?>"
                 placeholder="+1-555-0144" required>
        </div>
        <div class="form-group">
          <label for="delivery_address">Safehouse Coordinates / Delivery Address *</label>
          <input type="text" id="delivery_address" name="delivery_address"
                 value="<?php echo htmlspecialchars($_POST['delivery_address'] ?? $customer['address'] ?? '1 Wall Street Court, Continental Safehouse Suite 812'); ?>"
                 placeholder="Continental Hotel, 123 Main St" required>
        </div>
        <div class="row-2">
          <div class="form-group">
            <label for="delivery_city">Base City *</label>
            <input type="text" id="delivery_city" name="delivery_city"
                   value="<?php echo htmlspecialchars($_POST['delivery_city'] ?? 'New York'); ?>"
                   placeholder="New York" required>
          </div>
          <div class="form-group">
            <label for="delivery_zip">Postal / Grid Code *</label>
            <input type="text" id="delivery_zip" name="delivery_zip"
                   value="<?php echo htmlspecialchars($_POST['delivery_zip'] ?? '10005'); ?>"
                   placeholder="10005" required>
          </div>
        </div>
        <button type="submit" class="btn-primary">Authorize &amp; Place Requisition Order</button>
      </form>
    </div>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
