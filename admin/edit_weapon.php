<?php
$page_title = 'Edit Weapon';
require_once 'admin_header.php';

$weapon_id = intval($_GET['id'] ?? 0);
if (!$weapon_id) {
    header('Location: weapons.php');
    exit;
}

$result = mysqli_query($conn, "SELECT * FROM weapons WHERE weapon_id=$weapon_id");
$weapon = mysqli_fetch_assoc($result);
if (!$weapon) {
    header('Location: weapons.php');
    exit;
}

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
        $img_e   = mysqli_real_escape_string($conn, $image ?: $weapon['image']);
        $status_e= mysqli_real_escape_string($conn, $status);

        $sql = "UPDATE weapons SET name='$name_e', category='$cat_e', price=$price, description='$desc_e', image='$img_e', status='$status_e' WHERE weapon_id=$weapon_id";
        if (mysqli_query($conn, $sql)) {
            header('Location: weapons.php?msg=updated');
            exit;
        } else {
            $error = 'Failed to update weapon. ' . mysqli_error($conn);
        }
    }
} else {
    // Pre-fill from DB
    $_POST = $weapon;
    $_POST['description'] = $weapon['description'];
}
?>

<section class="page-section active">
  <div class="form-container" style="max-width:650px;">
    <h2 class="section-title">Edit Weapon</h2>
    <p class="section-subtitle">Update tactical asset details.</p>

    <?php if ($error): ?>
      <p style="color:var(--error-red); text-align:center; margin-bottom:1rem;"><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>

    <form method="post" novalidate>
      <div class="form-group">
        <label for="name">Weapon Name *</label>
        <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($_POST['name'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="category">Category *</label>
        <select id="category" name="category">
          <?php
            $cats = ['Sidearms','Shotguns','Submachine Guns','Rifles'];
            foreach ($cats as $c) {
                $sel = ($_POST['category'] ?? '') === $c ? 'selected' : '';
                echo "<option value=\"$c\" $sel>$c</option>";
            }
          ?>
        </select>
      </div>
      <div class="form-group">
        <label for="price">Price ($) *</label>
        <input type="number" id="price" name="price" step="0.01" min="0" value="<?php echo htmlspecialchars($_POST['price'] ?? ''); ?>" required>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea id="description" name="description" rows="3"><?php echo htmlspecialchars($_POST['description'] ?? ''); ?></textarea>
      </div>
      <div class="form-group">
        <label for="image">Image URL</label>
        <input type="text" id="image" name="image" value="<?php echo htmlspecialchars($_POST['image'] ?? ''); ?>">
      </div>
      <div class="form-group">
        <label for="status">Status</label>
        <select id="status" name="status">
          <option value="available" <?php echo ($_POST['status'] ?? '') === 'available' ? 'selected' : ''; ?>>Available</option>
          <option value="out_of_stock" <?php echo ($_POST['status'] ?? '') === 'out_of_stock' ? 'selected' : ''; ?>>Out of Stock</option>
        </select>
      </div>
      <button type="submit" class="btn-primary">Update Weapon</button>
    </form>

    <a href="weapons.php" class="btn-secondary" style="display:block;text-align:center;text-decoration:none;margin-top:1rem;">← Back to Weapons List</a>
  </div>
</section>

<?php require_once 'admin_footer.php'; ?>
