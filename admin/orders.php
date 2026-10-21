<?php
$page_title = 'Manage Orders';
require_once 'admin_header.php';

// Handle status update
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['order_id']) && isset($_POST['new_status'])) {
    $oid    = intval($_POST['order_id']);
    $status = mysqli_real_escape_string($conn, $_POST['new_status']);
    mysqli_query($conn, "UPDATE orders SET order_status='$status' WHERE order_id=$oid");
    header('Location: orders.php?msg=updated');
    exit;
}

// Filter
$status_filter = $_GET['status'] ?? '';
$where = '';
if ($status_filter && $status_filter !== 'all') {
    $sf = mysqli_real_escape_string($conn, $status_filter);
    $where = "WHERE o.order_status='$sf'";
}

$orders = mysqli_query($conn, "SELECT o.*, c.full_name as customer_name, c.email as customer_email FROM orders o JOIN customers c ON o.customer_id=c.customer_id $where ORDER BY o.order_date DESC");
?>

<section class="page-section active">
  <div class="catalog-container">
    <h2 class="section-title" style="text-align:left;">Customer Orders</h2>

    <?php if (isset($_GET['msg']) && $_GET['msg'] === 'updated'): ?>
      <p style="color:var(--success-green); margin:0.5rem 0;">Order status updated successfully.</p>
    <?php endif; ?>

    <!-- Filter bar -->
    <div class="filter-bar" style="margin:1rem 0;">
      <a href="orders.php" class="filter-btn <?php echo !$status_filter || $status_filter==='all' ? 'active' : ''; ?>" style="text-decoration:none;">All</a>
      <?php foreach (['Pending','Processing','Dispatched','Delivered','Cancelled'] as $s): ?>
        <a href="orders.php?status=<?php echo $s; ?>" class="filter-btn <?php echo $status_filter === $s ? 'active' : ''; ?>" style="text-decoration:none;"><?php echo $s; ?></a>
      <?php endforeach; ?>
    </div>

    <div style="overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Order #</th>
            <th>Customer</th>
            <th>Email</th>
            <th>Total</th>
            <th>Status</th>
            <th>Date</th>
            <th>Update Status</th>
            <th>Details</th>
          </tr>
        </thead>
        <tbody>
          <?php if (mysqli_num_rows($orders) === 0): ?>
            <tr><td colspan="8" style="text-align:center;color:var(--text-muted);">No orders found.</td></tr>
          <?php endif; ?>
          <?php while ($order = mysqli_fetch_assoc($orders)): ?>
          <tr>
            <td>#<?php echo $order['order_id']; ?></td>
            <td><?php echo htmlspecialchars($order['customer_name']); ?></td>
            <td style="color:var(--text-muted); font-size:0.85rem;"><?php echo htmlspecialchars($order['customer_email']); ?></td>
            <td style="color:var(--accent-gold);">$<?php echo number_format($order['total_amount'], 2); ?></td>
            <td><?php echo $order['order_status']; ?></td>
            <td><?php echo date('M d, Y', strtotime($order['order_date'])); ?></td>
            <td>
              <form method="post" style="display:flex; gap:0.3rem;">
                <input type="hidden" name="order_id" value="<?php echo $order['order_id']; ?>">
                <select name="new_status" style="padding:0.3rem; background:var(--bg-dark); border:1px solid var(--gunmetal-border); color:var(--text-main); border-radius:4px; font-size:0.8rem;">
                  <?php foreach (['Pending','Processing','Dispatched','Delivered','Cancelled'] as $s): ?>
                    <option value="<?php echo $s; ?>" <?php echo $order['order_status'] === $s ? 'selected' : ''; ?>><?php echo $s; ?></option>
                  <?php endforeach; ?>
                </select>
                <button type="submit" class="btn-primary" style="width:auto; padding:0.3rem 0.5rem; font-size:0.75rem;">Set</button>
              </form>
            </td>
            <td><a href="order_detail.php?id=<?php echo $order['order_id']; ?>" style="color:var(--accent-gold);">View</a></td>
          </tr>
          <?php endwhile; ?>
        </tbody>
      </table>
    </div>
  </div>
</section>

<?php require_once 'admin_footer.php'; ?>
