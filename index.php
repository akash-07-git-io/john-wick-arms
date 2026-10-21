<?php
$page_title = 'High Table Armory';
require_once 'db_connect.php';
require_once 'includes/header.php';

// Fetch featured weapons (latest 4)
$result = mysqli_query($conn, "SELECT * FROM weapons WHERE status='available' ORDER BY created_at DESC LIMIT 4");
?>

<!-- Hero Banner -->
<section class="page-section active">
  <div class="hero-banner home-hero">
    <span class="badge">Continental Sommelier Selection</span>
    <h1 class="hero-title">EXCLUSIVELY FOR THE HIGH TABLE</h1>
    <p class="hero-subtitle">Tactical perfection. Crimson steel. Excommunicado protection.</p>
    <a href="catalog.php" class="btn-primary" style="max-width:250px;margin:1.5rem auto 0;display:block;text-align:center;text-decoration:none;">Explore Armory Catalog</a>
  </div>

  <div class="catalog-container">
    <h2 class="section-title" style="margin-bottom:1.5rem;">Sommelier Featured Arsenal</h2>
    <div class="product-grid">
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
