<?php
$page_title = 'Add Weapon';
require_once 'admin_header.php';

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name     = trim($_POST['name'] ?? '');
    $category = trim($_POST['category'] ?? '');
    $price    = floatval($_POST['price'] ?? 0);
    $desc     = trim($_POST['description'] ?? '');
    $image    = trim($_POST['image'] ?? '');
    $status   = $_POST['status'] ?? 'available';

    if (!$name || !$category || $price <= 0) {
        $error = 'Name, category, and a valid price are required.';
    } else {
        $name_e  = mysqli_real_escape_string($conn, $name);
        $cat_e   = mysqli_real_escape_string($conn, $category);
        $desc_e  = mysqli_real_escape_string($conn, $desc);
        $img_e   = mysqli_real_escape_string($conn, $image ?: 'https://images.stockcake.com/public/2/e/4/2e4919a9-1519-444b-84e7-4d67c789f123/neo-noir-assault-rifle-stockcake.jpg');
        $status_e= mysqli_real_escape_string($conn, $status);

        $sql = "INSERT INTO weapons (name, category, price, description, image, status) VALUES ('$name_e', '$cat_e', $price, '$desc_e', '$img_e', '$status_e')";
        if (mysqli_query($conn, $sql)) {
            header('Location: weapons.php?msg=added');
            exit;
        } else {
            $error = 'Failed to add weapon. ' . mysqli_error($conn);
        }
    }
}
?>

<section class="page-section active">
  <div class="form-container" style="max-width:650px;">
    <h2 class="section-title">Add New Weapon</h2>
    <p class="section-subtitle">Register a new tactical asset to the armory inventory.</p>

    <?php if ($error): ?>
      <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>

    <form method="post" novalidate>
      <div class="form-group">
        <label for="name">Weapon Name *</label>
        <input type="text" id="name" name="name" placeholder="e.g. Custom Pit Viper 9mm" value="<?php echo htmlspecialchars($_POST['name'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="category">Category *</label>
        <select id="category" name="category">
          <option value="Sidearms" <?php echo ($_POST['category'] ?? '') === 'Sidearms' ? 'selected' : ''; ?>>Sidearms</option>
          <option value="Shotguns" <?php echo ($_POST['category'] ?? '') === 'Shotguns' ? 'selected' : ''; ?>>Shotguns</option>
          <option value="Submachine Guns" <?php echo ($_POST['category'] ?? '') === 'Submachine Guns' ? 'selected' : ''; ?>>Submachine Guns</option>
          <option value="Rifles" <?php echo ($_POST['category'] ?? '') === 'Rifles' ? 'selected' : ''; ?>>Rifles</option>
        </select>
      </div>
      <div class="form-group">
        <label for="price">Price ($) *</label>
        <input type="number" id="price" name="price" placeholder="7500" step="0.01" min="0" value="<?php echo htmlspecialchars($_POST['price'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea id="description" name="description" rows="3" placeholder="Weapon description..."><?php echo htmlspecialchars($_POST['description'] ?? ''); ?></textarea>
      </div>
      <div class="form-group">
        <label for="image">Image URL</label>
        <input type="text" id="image" name="image" placeholder="https://example.com/weapon.jpg" value="<?php echo htmlspecialchars($_POST['image'] ?? ''); ?>">
      </div>
      <div class="form-group">
        <label for="status">Status</label>
        <select id="status" name="status">
          <option value="available">Available</option>
          <option value="out_of_stock">Out of Stock</option>
        </select>
      </div>
      <button type="submit" class="btn-primary">Add Weapon to Armory</button>
    </form>
  </div>
</section>

<?php require_once 'admin_footer.php'; ?>
