<?php
$page_title = 'Order Detail';
require_once 'admin_header.php';

$order_id = intval($_GET['id'] ?? 0);
if (!$order_id) {
    header('Location: orders.php');
    exit;
}

// Handle status update from this page
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['new_status'])) {
    $status = mysqli_real_escape_string($conn, $_POST['new_status']);
    mysqli_query($conn, "UPDATE orders SET order_status='$status' WHERE order_id=$order_id");
    header("Location: order_detail.php?id=$order_id&msg=updated");
    exit;
}

$order = mysqli_fetch_assoc(mysqli_query($conn, "SELECT o.*, c.full_name as customer_name, c.email as customer_email, c.phone as customer_phone FROM orders o JOIN customers c ON o.customer_id=c.customer_id WHERE o.order_id=$order_id"));

if (!$order) {
    header('Location: orders.php');
    exit;
}

$items = mysqli_query($conn, "SELECT oi.*, w.name as weapon_name, w.category, w.image FROM order_items oi JOIN weapons w ON oi.weapon_id=w.weapon_id WHERE oi.order_id=$order_id");

$status_colors = [
    'Pending'    => '#f39c12',
    'Processing' => '#3498db',
    'Dispatched' => '#9b59b6',
    'Delivered'  => '#2ecc71',
    'Cancelled'  => '#e74c3c',
];
$scolor = $status_colors[$order['order_status']] ?? '#9aa0b4';
?>

<section class="page-section active">
  <div class="catalog-container" style="max-width:900px;">
    <?php if (isset($_GET['msg']) && $_GET['msg'] === 'updated'): ?>
      <p style="color:var(--success-green); margin-bottom:1rem;">Order status updated successfully.</p>
    <?php endif; ?>

    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
      <h2 class="section-title" style="text-align:left; margin:0;">Order #<?php echo $order_id; ?></h2>
      <span style="background:<?php echo $scolor; ?>22; color:<?php echo $scolor; ?>; padding:0.5rem 1.2rem; border-radius:var(--radius); font-weight:700; border:1px solid <?php echo $scolor; ?>; font-size:1.1rem;">
        <?php echo $order['order_status']; ?>
      </span>
    </div>

    <!-- Customer & Delivery Info -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
      <div class="profile-card">
        <h3 style="color:var(--accent-gold); margin-bottom:0.8rem;">Customer Info</h3>
        <div class="profile-row"><span class="profile-label">Name:</span><span class="profile-val"><?php echo htmlspecialchars($order['customer_name']); ?></span></div>
        <div class="profile-row"><span class="profile-label">Email:</span><span class="profile-val"><?php echo htmlspecialchars($order['customer_email']); ?></span></div>
        <div class="profile-row"><span class="profile-label">Phone:</span><span class="profile-val"><?php echo htmlspecialchars($order['customer_phone'] ?? 'N/A'); ?></span></div>
      </div>
      <div class="profile-card">
        <h3 style="color:var(--accent-gold); margin-bottom:0.8rem;">Delivery Details</h3>
        <div class="profile-row"><span class="profile-label">Recipient:</span><span class="profile-val"><?php echo htmlspecialchars($order['delivery_name']); ?></span></div>
        <div class="profile-row"><span class="profile-label">Phone:</span><span class="profile-val"><?php echo htmlspecialchars($order['delivery_phone']); ?></span></div>
        <div class="profile-row"><span class="profile-label">Address:</span><span class="profile-val"><?php echo htmlspecialchars($order['delivery_address']); ?></span></div>
        <div class="profile-row"><span class="profile-label">City:</span><span class="profile-val"><?php echo htmlspecialchars($order['delivery_city']); ?></span></div>
        <div class="profile-row"><span class="profile-label">ZIP:</span><span class="profile-val"><?php echo htmlspecialchars($order['delivery_zip']); ?></span></div>
      </div>
    </div>

    <!-- Order Items -->
    <div class="cart-container" style="margin-bottom:1.5rem;">
      <h3 style="color:var(--accent-gold); margin-bottom:1rem;">Order Items</h3>
      <div class="cart-items-list" style="margin:0;">
        <?php while ($item = mysqli_fetch_assoc($items)): ?>
        <div class="cart-item-row">
          <div style="display:flex; gap:0.8rem; align-items:center;">
            <img src="<?php echo htmlspecialchars($item['image']); ?>" alt="" style="width:50px;height:35px;object-fit:cover;border-radius:4px;">
            <div>
              <div style="font-weight:600;"><?php echo htmlspecialchars($item['weapon_name']); ?></div>
              <div style="color:var(--text-muted); font-size:0.8rem;"><?php echo htmlspecialchars($item['category']); ?> | Qty: <?php echo $item['quantity']; ?></div>
            </div>
          </div>
          <span style="color:var(--accent-gold); font-weight:700;">$<?php echo number_format($item['unit_price'] * $item['quantity'], 2); ?></span>
        </div>
        <?php endwhile; ?>
      </div>
      <div class="cart-summary">
        <span>Order Total:</span>
        <span>$<?php echo number_format($order['total_amount'], 2); ?></span>
      </div>
    </div>

    <!-- Update Status -->
    <div class="form-container" style="max-width:400px;">
      <h3 class="section-title" style="font-size:1.2rem;">Update Order Status</h3>
      <form method="post">
        <div class="form-group">
          <select name="new_status">
            <?php foreach (['Pending','Processing','Dispatched','Delivered','Cancelled'] as $s): ?>
              <option value="<?php echo $s; ?>" <?php echo $order['order_status'] === $s ? 'selected' : ''; ?>><?php echo $s; ?></option>
            <?php endforeach; ?>
          </select>
        </div>
        <button type="submit" class="btn-primary">Update Status</button>
      </form>
    </div>

    <a href="orders.php" class="btn-secondary" style="display:block;text-align:center;text-decoration:none;margin-top:1.5rem;max-width:400px;">← Back to All Orders</a>
  </div>
</section>

<?php require_once 'admin_footer.php'; ?>
