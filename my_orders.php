<?php
$page_title = 'My Orders';
require_once 'db_connect.php';

if (!isset($_SESSION['customer_id'])) {
    header('Location: login.php');
    exit;
}

$customer_id = $_SESSION['customer_id'];
$orders = mysqli_query($conn, "SELECT * FROM orders WHERE customer_id=$customer_id ORDER BY order_date DESC");

require_once 'includes/header.php';
?>

<section class="page-section active">
  <div class="hero-banner profile-hero">
    <span class="badge">Order Tracking</span>
    <h1 class="hero-title">MY REQUISITIONS</h1>
  </div>

  <div class="catalog-container" style="max-width:900px;">
    <?php if (mysqli_num_rows($orders) === 0): ?>
      <div class="form-container" style="max-width:600px;">
        <h2 class="section-title">No Orders Yet</h2>
        <p class="section-subtitle">You haven't placed any requisitions. Browse the armory to get started.</p>
        <a href="catalog.php" class="btn-primary" style="display:block;text-align:center;text-decoration:none;">Browse Armory</a>
      </div>
    <?php else: ?>
      <?php while ($order = mysqli_fetch_assoc($orders)):
        // Fetch order items
        $items = mysqli_query($conn, "SELECT oi.*, w.name, w.image FROM order_items oi JOIN weapons w ON oi.weapon_id=w.weapon_id WHERE oi.order_id=" . $order['order_id']);

        // Status color
        $status_colors = [
            'Pending'    => '#f39c12',
            'Processing' => '#3498db',
            'Dispatched' => '#9b59b6',
            'Delivered'  => '#2ecc71',
            'Cancelled'  => '#e74c3c',
        ];
        $scolor = $status_colors[$order['order_status']] ?? '#9aa0b4';
      ?>
      <div class="cart-container" style="margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
          <div>
            <h3 style="color:var(--accent-gold); margin:0;">Order #<?php echo $order['order_id']; ?></h3>
            <p style="color:var(--text-muted); font-size:0.85rem; margin:0;"><?php echo date('M d, Y h:i A', strtotime($order['order_date'])); ?></p>
          </div>
          <span style="background:<?php echo $scolor; ?>22; color:<?php echo $scolor; ?>; padding:0.3rem 1rem; border-radius:var(--radius); font-weight:600; border:1px solid <?php echo $scolor; ?>;">
            <?php echo $order['order_status']; ?>
          </span>
        </div>

        <div class="cart-items-list" style="margin:0.5rem 0;">
          <?php while ($item = mysqli_fetch_assoc($items)): ?>
          <div class="cart-item-row">
            <div style="display:flex; gap:0.8rem; align-items:center;">
              <img src="<?php echo htmlspecialchars($item['image']); ?>" alt="" style="width:45px;height:35px;object-fit:cover;border-radius:4px;">
              <span><?php echo htmlspecialchars($item['name']); ?> × <?php echo $item['quantity']; ?></span>
            </div>
            <span style="color:var(--accent-gold);">$<?php echo number_format($item['unit_price'] * $item['quantity'], 2); ?></span>
          </div>
          <?php endwhile; ?>
        </div>

        <div class="cart-summary">
          <span>Total:</span>
          <span>$<?php echo number_format($order['total_amount'], 2); ?></span>
        </div>

        <div style="margin-top:0.8rem; color:var(--text-muted); font-size:0.85rem;">
          <strong>Deliver to:</strong> <?php echo htmlspecialchars($order['delivery_name']); ?>,
          <?php echo htmlspecialchars($order['delivery_address']); ?>,
          <?php echo htmlspecialchars($order['delivery_city']); ?> – <?php echo htmlspecialchars($order['delivery_zip']); ?>
        </div>
      </div>
      <?php endwhile; ?>
    <?php endif; ?>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
