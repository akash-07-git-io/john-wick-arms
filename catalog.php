<?php
$page_title = 'Armory Catalog';
require_once 'db_connect.php';
require_once 'includes/header.php';

// Filter by category
$category = isset($_GET['category']) ? mysqli_real_escape_string($conn, $_GET['category']) : '';

if ($category && $category !== 'all') {
    $query = "SELECT * FROM weapons WHERE status='available' AND category='$category' ORDER BY name";
} else {
    $query = "SELECT * FROM weapons WHERE status='available' ORDER BY name";
}
$result = mysqli_query($conn, $query);

// Get distinct categories for filter bar
$cat_result = mysqli_query($conn, "SELECT DISTINCT category FROM weapons WHERE status='available' ORDER BY category");
?>

<section class="page-section active">
  <div class="hero-banner catalog-hero">
    <span class="badge">Tactical Inventory</span>
    <h1 class="hero-title">ARMORY CATALOG</h1>
    <p class="hero-subtitle">Match-grade sidearms, tactical shotguns &amp; sniper platforms.</p>
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
        <p style="color:var(--text-muted);">No weapons found in this category.</p>
      <?php endif; ?>
      <?php while ($weapon = mysqli_fetch_assoc($result)): ?>
      <div class="product-card">
        <img src="<?php echo htmlspecialchars($weapon['image']); ?>" alt="<?php echo htmlspecialchars($weapon['name']); ?>" class="product-img">
        <div class="product-info">
          <div>
            <span class="product-tag"><?php echo htmlspecialchars($weapon['category']); ?></span>
            <h3 class="product-name"><?php echo htmlspecialchars($weapon['name']); ?></h3>
            <p class="product-desc"><?php echo htmlspecialchars($weapon['description']); ?></p>
          </div>
          <div>
            <div class="product-price">$<?php echo number_format($weapon['price'], 2); ?></div>
            <a href="weapon_detail.php?id=<?php echo $weapon['weapon_id']; ?>" class="btn-primary" style="display:block;text-align:center;text-decoration:none;margin-bottom:0.5rem;">View Details</a>
            <form method="post" action="cart_action.php">
              <input type="hidden" name="weapon_id" value="<?php echo $weapon['weapon_id']; ?>">
              <input type="hidden" name="action" value="add">
              <button type="submit" class="btn-secondary">Add to Cart</button>
            </form>
          </div>
        </div>
      </div>
      <?php endwhile; ?>
    </div>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
