<?php
$page_title = 'Checkout';
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

    if (!$d_name || !$d_phone || !$d_address || !$d_city || !$d_zip) {
        $error = 'All delivery fields are required.';
    } else {
        // Insert order
        $d_name_e    = mysqli_real_escape_string($conn, $d_name);
        $d_phone_e   = mysqli_real_escape_string($conn, $d_phone);
        $d_address_e = mysqli_real_escape_string($conn, $d_address);
        $d_city_e    = mysqli_real_escape_string($conn, $d_city);
        $d_zip_e     = mysqli_real_escape_string($conn, $d_zip);

        $sql = "INSERT INTO orders (customer_id, total_amount, delivery_name, delivery_phone, delivery_address, delivery_city, delivery_zip)
                VALUES ($customer_id, $total, '$d_name_e', '$d_phone_e', '$d_address_e', '$d_city_e', '$d_zip_e')";

        if (mysqli_query($conn, $sql)) {
            $order_id = mysqli_insert_id($conn);

            // Insert order items
            foreach ($cart_items as $item) {
                $wid = $item['weapon_id'];
                $qty = $item['quantity'];
                $price = $item['price'];
                mysqli_query($conn, "INSERT INTO order_items (order_id, weapon_id, quantity, unit_price) VALUES ($order_id, $wid, $qty, $price)");
            }

            // Clear cart
            $_SESSION['cart'] = [];

            // Redirect to success
            header("Location: order_success.php?order_id=$order_id");
            exit;
        } else {
            $error = 'Failed to place order. Please try again.';
        }
    }
}

require_once 'includes/header.php';
?>

<section class="page-section active">
  <div class="hero-banner payment-hero">
    <span class="badge">Encrypted Checkout</span>
    <h1 class="hero-title">REQUISITION &amp; DELIVERY</h1>
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
            <div style="color:var(--text-muted); font-size:0.85rem;">Qty: <?php echo $item['quantity']; ?> × $<?php echo number_format($item['price'], 2); ?></div>
          </div>
          <span style="color:var(--accent-gold); font-weight:700;">$<?php echo number_format($item['subtotal'], 2); ?></span>
        </div>
        <?php endforeach; ?>
      </div>
      <div class="cart-summary">
        <span>Total Amount:</span>
        <span>$<?php echo number_format($total, 2); ?></span>
      </div>
    </div>

    <!-- Delivery Details Form -->
    <div class="form-container" style="margin:0; max-width:100%;">
      <h2 class="section-title">Delivery Details</h2>
      <p class="section-subtitle">Provide your delivery information to complete the requisition.</p>

      <?php if ($error): ?>
        <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
      <?php endif; ?>

      <form method="post" novalidate>
        <div class="form-group">
          <label for="delivery_name">Recipient Full Name *</label>
          <input type="text" id="delivery_name" name="delivery_name"
                 value="<?php echo htmlspecialchars($_POST['delivery_name'] ?? $customer['full_name'] ?? ''); ?>"
                 placeholder="John Wick" required>
        </div>
        <div class="form-group">
          <label for="delivery_phone">Contact Phone *</label>
          <input type="text" id="delivery_phone" name="delivery_phone"
                 value="<?php echo htmlspecialchars($_POST['delivery_phone'] ?? $customer['phone'] ?? ''); ?>"
                 placeholder="+1-555-0123" required>
        </div>
        <div class="form-group">
          <label for="delivery_address">Delivery Address *</label>
          <input type="text" id="delivery_address" name="delivery_address"
                 value="<?php echo htmlspecialchars($_POST['delivery_address'] ?? $customer['address'] ?? ''); ?>"
                 placeholder="Continental Hotel, 123 Main St" required>
        </div>
        <div class="row-2">
          <div class="form-group">
            <label for="delivery_city">City *</label>
            <input type="text" id="delivery_city" name="delivery_city"
                   value="<?php echo htmlspecialchars($_POST['delivery_city'] ?? ''); ?>"
                   placeholder="New York" required>
          </div>
          <div class="form-group">
            <label for="delivery_zip">ZIP Code *</label>
            <input type="text" id="delivery_zip" name="delivery_zip"
                   value="<?php echo htmlspecialchars($_POST['delivery_zip'] ?? ''); ?>"
                   placeholder="10001" required>
          </div>
        </div>
        <button type="submit" class="btn-primary">Place Order</button>
      </form>
    </div>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
