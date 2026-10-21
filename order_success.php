<?php
$page_title = 'Order Confirmed';
require_once 'db_connect.php';
require_once 'includes/header.php';

$order_id = intval($_GET['order_id'] ?? 0);
$method   = htmlspecialchars($_GET['method'] ?? 'Continental Gold Coins');
?>

<section class="page-section active">
  <div class="status-card">
    <h2 style="color: var(--accent-gold); font-size: 2rem;">&#10003; Requisition Approved</h2>
    <p style="margin: 1rem 0; color: var(--text-muted);">
      Your order <strong style="color:var(--accent-gold);">#<?php echo $order_id; ?></strong> has been placed and authorized via <strong style="color:var(--accent-gold);"><?php echo $method; ?></strong>.
      The Continental Sommelier has sealed your tactical hardware allocation.
    </p>
    <div style="background:#0e1017; border:1px solid var(--accent-gold); padding:1.2rem; border-radius:var(--radius); max-width:400px; margin:1.5rem auto; text-align:left;">
      <p><strong style="color:var(--accent-gold);">Allocation Order:</strong> #<?php echo $order_id; ?></p>
      <p><strong style="color:var(--accent-gold);">Settlement:</strong> <?php echo $method; ?></p>
      <p><strong style="color:var(--accent-gold);">Status:</strong> Pre-Dispatched to Safehouse</p>
    </div>
    <p style="margin: 0.5rem 0; color: var(--text-muted);">You can track real-time fulfillment in <a href="my_orders.php" style="color:var(--accent-gold);">My Orders</a>.</p>
    <a href="catalog.php" class="btn-secondary" style="display:inline-block; margin-top:1.5rem; text-decoration:none;">Explore More Arsenal</a>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
