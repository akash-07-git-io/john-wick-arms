<?php
require_once 'db_connect.php';

if (!isset($_GET['id'])) {
    header('Location: catalog.php');
    exit;
}

$weapon_id = intval($_GET['id']);
$result = mysqli_query($conn, "SELECT * FROM weapons WHERE weapon_id=$weapon_id");
$weapon = mysqli_fetch_assoc($result);

if (!$weapon) {
    header('Location: catalog.php');
    exit;
}

$page_title = $weapon['name'];
require_once 'includes/header.php';
?>

<section class="page-section active">
  <div class="hero-banner catalog-hero">
    <span class="badge"><?php echo htmlspecialchars($weapon['category']); ?></span>
    <h1 class="hero-title"><?php echo strtoupper(htmlspecialchars($weapon['name'])); ?></h1>
    <p class="hero-subtitle">Continental Sommelier Ballistic Evaluation</p>
  </div>

  <div class="catalog-container">
    <div class="weapon-detail-container">
      <!-- Weapon Image Box -->
      <div class="weapon-detail-img-box">
        <img src="<?php echo htmlspecialchars($weapon['image']); ?>" alt="<?php echo htmlspecialchars($weapon['name']); ?>">
      </div>

      <!-- Specs & Details -->
      <div>
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="product-tag"><?php echo htmlspecialchars($weapon['category']); ?></span>
          <span style="color:var(--success-green); font-weight:600; font-size:0.85rem;">
            <?php echo $weapon['status'] === 'available' ? '&#10003; High Table Allocation Available' : '&#10007; Out of Stock'; ?>
          </span>
        </div>

        <h2 style="color:var(--accent-gold); margin:0.8rem 0 0.4rem; font-size:1.8rem;"><?php echo htmlspecialchars($weapon['name']); ?></h2>
        <div class="product-price" style="font-size:1.6rem; margin-bottom:1rem;">$<?php echo number_format($weapon['price'], 2); ?></div>

        <p style="color:var(--text-muted); line-height:1.6; margin-bottom:1.5rem;"><?php echo htmlspecialchars($weapon['description']); ?></p>

        <!-- Technical Specs -->
        <h3 style="font-size:1rem; color:var(--text-main); text-transform:uppercase; letter-spacing:1px; margin-bottom:0.5rem;">Technical Specifications</h3>
        <div class="specs-grid">
          <div class="spec-item">
            <span class="spec-label">Caliber</span>
            <span class="spec-val"><?php echo htmlspecialchars($weapon['caliber'] ?? '9x19mm'); ?></span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Capacity</span>
            <span class="spec-val"><?php echo htmlspecialchars($weapon['capacity'] ?? 'Standard'); ?></span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Category</span>
            <span class="spec-val"><?php echo htmlspecialchars($weapon['category']); ?></span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Status</span>
            <span class="spec-val"><?php echo ucfirst($weapon['status']); ?></span>
          </div>
        </div>

        <?php if ($weapon['status'] === 'available'): ?>
        <form method="post" action="cart_action.php" style="display:flex; gap:1rem; align-items:center; margin-top:1.5rem;">
          <input type="hidden" name="weapon_id" value="<?php echo $weapon['weapon_id']; ?>">
          <input type="hidden" name="action" value="add">
          <div style="flex:1;">
            <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:0.3rem;">Allocation Quantity</label>
            <input type="number" id="qty" name="quantity" value="1" min="1" max="10" style="width:100%; padding:0.75rem; background:var(--bg-dark); border:1px solid var(--gunmetal-border); color:var(--text-main); border-radius:var(--radius); text-align:center;">
          </div>
          <div style="flex:2; margin-top:1.2rem;">
            <button type="submit" class="btn-primary">Add to Requisition Cart</button>
          </div>
        </form>
        <?php endif; ?>

        <div style="margin-top:1.2rem;">
          <a href="catalog.php" class="btn-secondary" style="display:inline-block; text-decoration:none; padding:0.5rem 1.2rem;">&larr; Return to Armory Catalog</a>
        </div>
      </div>
    </div>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
