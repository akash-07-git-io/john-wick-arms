<?php
$page_title = 'Requisition Cart';
require_once 'db_connect.php';
require_once 'includes/header.php';

$cart = $_SESSION['cart'] ?? [];
$cart_items = [];
$total = 0;

if (!empty($cart)) {
    $ids = implode(',', array_map('intval', array_keys($cart)));
    $result = mysqli_query($conn, "SELECT * FROM weapons WHERE weapon_id IN ($ids)");
    while ($row = mysqli_fetch_assoc($result)) {
        $qty = $cart[$row['weapon_id']];
        $row['quantity'] = $qty;
        $row['subtotal'] = $row['price'] * $qty;
        $total += $row['subtotal'];
        $cart_items[] = $row;
    }
}
?>

<section class="page-section active">
  <div class="hero-banner payment-hero">
    <span class="badge">Requisition Summary</span>
    <h1 class="hero-title">YOUR REQUISITION CART</h1>
  </div>

  <div class="catalog-container" style="max-width:900px;">
    <?php if (empty($cart_items)): ?>
      <div class="form-container" style="max-width:600px;">
        <h2 class="section-title">Cart is Empty</h2>
        <p class="section-subtitle">Your requisition cart has no items. Browse the armory catalog to add weapons.</p>
        <a href="catalog.php" class="btn-primary" style="display:block;text-align:center;text-decoration:none;">Browse Armory Catalog</a>
      </div>
    <?php else: ?>
      <div class="cart-container" style="margin-bottom:2rem;">
        <h2 class="section-title" style="text-align:left; margin-bottom:1rem;">Cart Items</h2>
        <div class="cart-items-list">
          <?php foreach ($cart_items as $item): ?>
          <div class="cart-item-row">
            <div style="display:flex; gap:1rem; align-items:center;">
              <img src="<?php echo htmlspecialchars($item['image']); ?>" alt="" style="width:60px;height:45px;object-fit:cover;border-radius:4px;">
              <div>
                <div style="font-weight:600;"><?php echo htmlspecialchars($item['name']); ?></div>
                <div style="color:var(--text-muted); font-size:0.85rem;"><?php echo htmlspecialchars($item['category']); ?></div>
              </div>
            </div>
            <div style="display:flex; gap:1rem; align-items:center;">
              <form method="post" action="cart_action.php" style="display:flex; gap:0.5rem; align-items:center;">
                <input type="hidden" name="weapon_id" value="<?php echo $item['weapon_id']; ?>">
                <input type="hidden" name="action" value="update">
                <input type="hidden" name="redirect" value="cart.php">
                <input type="number" name="quantity" value="<?php echo $item['quantity']; ?>" min="1" max="10" style="width:60px; padding:0.3rem; background:var(--bg-dark); border:1px solid var(--gunmetal-border); color:var(--text-main); border-radius:4px; text-align:center;">
                <button type="submit" class="btn-secondary" style="width:auto; padding:0.3rem 0.6rem; font-size:0.75rem;">Update</button>
              </form>
              <span style="color:var(--accent-gold); font-weight:700; min-width:80px; text-align:right;">$<?php echo number_format($item['subtotal'], 2); ?></span>
              <form method="post" action="cart_action.php">
                <input type="hidden" name="weapon_id" value="<?php echo $item['weapon_id']; ?>">
                <input type="hidden" name="action" value="remove">
                <input type="hidden" name="redirect" value="cart.php">
                <button type="submit" class="btn-danger" style="width:auto; padding:0.3rem 0.6rem; font-size:0.75rem;">Remove</button>
              </form>
            </div>
          </div>
          <?php endforeach; ?>
        </div>
        <div class="cart-summary">
          <span>Total Ledger Amount:</span>
          <span>$<?php echo number_format($total, 2); ?></span>
        </div>
      </div>

      <div style="display:flex; gap:1rem;">
        <a href="checkout.php" class="btn-primary" style="text-align:center;text-decoration:none;">Proceed to Checkout</a>
        <form method="post" action="cart_action.php" style="flex:1;">
          <input type="hidden" name="action" value="clear">
          <input type="hidden" name="redirect" value="cart.php">
          <button type="submit" class="btn-danger">Clear Entire Cart</button>
        </form>
      </div>
    <?php endif; ?>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
