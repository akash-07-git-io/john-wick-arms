<?php
$page_title = 'Dashboard';
require_once 'admin_header.php';

// Stats
$weapon_count   = mysqli_fetch_assoc(mysqli_query($conn, "SELECT COUNT(*) as c FROM weapons"))['c'];
$order_count    = mysqli_fetch_assoc(mysqli_query($conn, "SELECT COUNT(*) as c FROM orders"))['c'];
$customer_count = mysqli_fetch_assoc(mysqli_query($conn, "SELECT COUNT(*) as c FROM customers"))['c'];
$revenue        = mysqli_fetch_assoc(mysqli_query($conn, "SELECT COALESCE(SUM(total_amount),0) as r FROM orders WHERE order_status != 'Cancelled'"))['r'];
$pending_orders = mysqli_fetch_assoc(mysqli_query($conn, "SELECT COUNT(*) as c FROM orders WHERE order_status='Pending'"))['c'];

// Recent orders
$recent_orders = mysqli_query($conn, "SELECT o.*, c.full_name as customer_name FROM orders o JOIN customers c ON o.customer_id=c.customer_id ORDER BY o.order_date DESC LIMIT 5");
?>

<section class="page-section active">
  <div class="catalog-container">
    <h2 class="section-title" style="text-align:left;">Welcome, <?php echo htmlspecialchars($_SESSION['admin_name']); ?></h2>
    <p style="color:var(--text-muted); margin-bottom:1rem;">Continental Command Center – System Overview</p>

    <!-- Stats -->
    <div class="stat-grid">
      <div class="stat-card">
        <h3><?php echo $weapon_count; ?></h3>
        <p>Total Weapons</p>
      </div>
      <div class="stat-card">
        <h3><?php echo $order_count; ?></h3>
        <p>Total Orders</p>
      </div>
      <div class="stat-card">
        <h3><?php echo $customer_count; ?></h3>
        <p>Registered Customers</p>
      </div>
      <div class="stat-card">
        <h3>$<?php echo number_format($revenue, 0); ?></h3>
        <p>Total Revenue</p>
      </div>
      <div class="stat-card">
        <h3 style="color:var(--error-red);"><?php echo $pending_orders; ?></h3>
        <p>Pending Orders</p>
      </div>
    </div>

    <!-- Recent Orders -->
    <h2 class="section-title" style="text-align:left; margin-top:2rem;">Recent Orders</h2>
    <div style="overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Order #</th>
            <th>Customer</th>
            <th>Total</th>
            <th>Status</th>
            <th>Date</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <?php if (mysqli_num_rows($recent_orders) === 0): ?>
            <tr><td colspan="6" style="text-align:center;color:var(--text-muted);">No orders yet.</td></tr>
          <?php endif; ?>
          <?php while ($order = mysqli_fetch_assoc($recent_orders)): ?>
          <tr>
            <td>#<?php echo $order['order_id']; ?></td>
            <td><?php echo htmlspecialchars($order['customer_name']); ?></td>
            <td style="color:var(--accent-gold);">$<?php echo number_format($order['total_amount'], 2); ?></td>
            <td><?php echo $order['order_status']; ?></td>
            <td><?php echo date('M d, Y', strtotime($order['order_date'])); ?></td>
            <td><a href="order_detail.php?id=<?php echo $order['order_id']; ?>" style="color:var(--accent-gold);">View</a></td>
          </tr>
          <?php endwhile; ?>
        </tbody>
      </table>
    </div>
  </div>
</section>

<?php require_once 'admin_footer.php'; ?>
