<?php
$page_title = 'Manage Weapons';
require_once 'admin_header.php';

// Handle delete
if (isset($_GET['delete'])) {
    $del_id = intval($_GET['delete']);
    mysqli_query($conn, "DELETE FROM weapons WHERE weapon_id=$del_id");
    header('Location: weapons.php?msg=deleted');
    exit;
}

$weapons = mysqli_query($conn, "SELECT * FROM weapons ORDER BY created_at DESC");
?>

<section class="page-section active">
  <div class="catalog-container">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <h2 class="section-title" style="text-align:left;">Weapon Inventory</h2>
      <a href="add_weapon.php" class="btn-primary" style="width:auto; padding:0.5rem 1.5rem; text-decoration:none;">+ Add Weapon</a>
    </div>

    <?php if (isset($_GET['msg'])): ?>
      <p style="color:var(--success-green); margin:1rem 0;">
        <?php
          $msgs = ['added' => 'Weapon added successfully!', 'updated' => 'Weapon updated!', 'deleted' => 'Weapon deleted.'];
          echo $msgs[$_GET['msg']] ?? 'Action completed.';
        ?>
      </p>
    <?php endif; ?>

    <div style="overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Image</th>
            <th>Name</th>
            <th>Category</th>
            <th>Price</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <?php while ($w = mysqli_fetch_assoc($weapons)): ?>
          <tr>
            <td><?php echo $w['weapon_id']; ?></td>
            <td><img src="<?php echo htmlspecialchars($w['image']); ?>" alt="" style="width:60px;height:40px;object-fit:cover;border-radius:4px;"></td>
            <td><?php echo htmlspecialchars($w['name']); ?></td>
            <td><?php echo htmlspecialchars($w['category']); ?></td>
            <td style="color:var(--accent-gold);">$<?php echo number_format($w['price'], 2); ?></td>
            <td><?php echo $w['status']; ?></td>
            <td>
              <a href="edit_weapon.php?id=<?php echo $w['weapon_id']; ?>" style="color:var(--accent-gold); margin-right:0.8rem;">Edit</a>
              <a href="weapons.php?delete=<?php echo $w['weapon_id']; ?>" style="color:var(--error-red);" onclick="return confirm('Delete this weapon?');">Delete</a>
            </td>
          </tr>
          <?php endwhile; ?>
        </tbody>
      </table>
    </div>
  </div>
</section>

<?php require_once 'admin_footer.php'; ?>
