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
  </div>

  <div class="catalog-container">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem; margin-top:1rem;">
      <!-- Weapon Image -->
      <div>
        <img src="<?php echo htmlspecialchars($weapon['image']); ?>" alt="<?php echo htmlspecialchars($weapon['name']); ?>"
             style="width:100%; border-radius:var(--radius); border:1px solid var(--gunmetal-border);">
      </div>
      <!-- Weapon Details -->
      <div class="form-container" style="margin:0; max-width:100%;">
        <h2 class="section-title" style="text-align:left;"><?php echo htmlspecialchars($weapon['name']); ?></h2>
        <p style="color:var(--text-muted); margin-bottom:1rem;"><?php echo htmlspecialchars($weapon['description']); ?></p>

        <div class="profile-card">
          <div class="profile-row">
            <span class="profile-label">Category:</span>
            <span class="profile-val"><?php echo htmlspecialchars($weapon['category']); ?></span>
          </div>
          <div class="profile-row">
            <span class="profile-label">Price:</span>
            <span class="profile-val">$<?php echo number_format($weapon['price'], 2); ?></span>
          </div>
          <div class="profile-row">
            <span class="profile-label">Status:</span>
            <span class="profile-val" style="color:var(--success-green);">
              <?php echo $weapon['status'] === 'available' ? '✓ Available' : '✗ Out of Stock'; ?>
            </span>
          </div>
        </div>

        <?php if ($weapon['status'] === 'available'): ?>
        <form method="post" action="cart_action.php">
          <input type="hidden" name="weapon_id" value="<?php echo $weapon['weapon_id']; ?>">
          <input type="hidden" name="action" value="add">
          <div class="form-group">
            <label for="qty">Quantity</label>
            <input type="number" id="qty" name="quantity" value="1" min="1" max="10" style="width:100px;">
          </div>
          <button type="submit" class="btn-primary">Add to Requisition Cart</button>
        </form>
        <?php endif; ?>

        <a href="catalog.php" class="btn-secondary" style="display:block;text-align:center;text-decoration:none;margin-top:1rem;">← Back to Catalog</a>
      </div>
    </div>
  </div>
</section>

<?php require_once 'includes/footer.php'; ?>
