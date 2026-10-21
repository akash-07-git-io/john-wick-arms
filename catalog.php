<?php
$page_title = 'Armory Catalog';
require_once 'db_connect.php';
require_once 'includes/header.php';

// Filter by category
$category = isset($_GET['category']) ? mysqli_real_escape_string($conn, $_GET['category']) : '';

if ($category && $category !== 'all') {
    $query = "SELECT * FROM weapons WHERE status='available' AND category='$category' ORDER BY price DESC";
} else {
    $query = "SELECT * FROM weapons WHERE status='available' ORDER BY category, price DESC";
}
$result = mysqli_query($conn, $query);

// Get distinct categories
$cat_result = mysqli_query($conn, "SELECT DISTINCT category FROM weapons WHERE status='available' ORDER BY category");
?>

<section class="page-section active">
  <div class="hero-banner catalog-hero">
    <span class="badge">Tactical Inventory</span>
    <h1 class="hero-title">ARMORY CATALOG</h1>
    <p class="hero-subtitle">Match-grade sidearms, tactical shotguns, suppressed SMGs &amp; precision platforms.</p>
  </div>

  <div class="catalog-container">
    <div class="filter-bar">
      <a href="catalog.php" class="filter-btn <?php echo !$category || $category==='all' ? 'active' : ''; ?>" style="text-decoration:none;">All Items</a>
      <?php while ($cat = mysqli_fetch_assoc($cat_result)): ?>
        <a href="catalog.php?category=<?php echo urlencode($cat['category']); ?>"
           class="filter-btn <?php echo $category === $cat['category'] ? 'active' : ''; ?>"
           style="text-decoration:none;">
          <?php echo htmlspecialchars($cat['category']); ?>
        </a>
      <?php endwhile; ?>
    </div>

    <div class="product-grid">
      <?php if (mysqli_num_rows($result) === 0): ?>
        <p style="color:var(--text-muted); text-align:center; grid-column:1/-1;">No tactical assets found in this category.</p>
      <?php endif; ?>
      <?php while ($weapon = mysqli_fetch_assoc($result)): ?>
      <div class="product-card">
        <a href="weapon_detail.php?id=<?php echo $weapon['weapon_id']; ?>">
          <img src="<?php echo htmlspecialchars($weapon['image']); ?>" alt="<?php echo htmlspecialchars($weapon['name']); ?>" class="product-img" style="cursor:pointer;">
        </a>
        <div class="product-info">
          <div>
            <span class="product-tag"><?php echo htmlspecialchars($weapon['category']); ?> <?php echo isset($weapon['caliber']) ? '| ' . htmlspecialchars($weapon['caliber']) : ''; ?></span>
            <h3 class="product-name">
              <a href="weapon_detail.php?id=<?php echo $weapon['weapon_id']; ?>" style="color:inherit; text-decoration:none;">
                <?php echo htmlspecialchars($weapon['name']); ?>
              </a>
            </h3>
            <p class="product-desc"><?php echo htmlspecialchars(substr($weapon['description'], 0, 110)); ?>...</p>
          </div>
          <div>
            <div class="product-price">$<?php echo number_format($weapon['price'], 2); ?></div>
            <div style="display:flex; gap:0.5rem; margin-top:0.5rem;">
              <a href="weapon_detail.php?id=<?php echo $weapon['weapon_id']; ?>" class="btn-secondary" style="flex:1; text-align:center; text-decoration:none; padding:0.55rem 0.5rem; font-size:0.8rem;">View Details</a>
              <form method="post" action="cart_action.php" style="flex:1;">
                <input type="hidden" name="weapon_id" value="<?php echo $weapon['weapon_id']; ?>">
                <input type="hidden" name="action" value="add">
                <button type="submit" class="btn-primary" style="padding:0.55rem 0.5rem; font-size:0.8rem;">Add to Cart</button>
              </form>
            </div>
          </div>
        </div>
      </div>
      <?php endwhile; ?>
    </div>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
