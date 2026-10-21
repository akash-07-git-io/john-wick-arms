<?php
$page_title = 'Order Confirmed';
require_once 'db_connect.php';
require_once 'includes/header.php';

$order_id = intval($_GET['order_id'] ?? 0);
?>

<section class="page-section active">
  <div class="status-card">
    <h2 style="color: var(--accent-gold); font-size: 2rem;">✓ Requisition Approved</h2>
    <p style="margin: 1rem 0; color: var(--text-muted);">
      Your order <strong style="color:var(--accent-gold);">#<?php echo $order_id; ?></strong> has been placed successfully.
      The Sommelier will process your tactical hardware allocation shortly.
    </p>
    <p style="margin: 0.5rem 0; color: var(--text-muted);">You can track your order status from <a href="my_orders.php" style="color:var(--accent-gold);">My Orders</a>.</p>
    <a href="index.php" class="btn-secondary" style="display:inline-block; margin-top:1.5rem; text-decoration:none;">Return to Home</a>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
