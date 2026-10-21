<?php
// Cart Action Handler – Add / Remove / Update cart items via session
require_once 'db_connect.php';

$action    = $_POST['action'] ?? '';
$weapon_id = intval($_POST['weapon_id'] ?? 0);
$quantity  = intval($_POST['quantity'] ?? 1);
if ($quantity < 1) $quantity = 1;

if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

switch ($action) {
    case 'add':
        if ($weapon_id > 0) {
            if (isset($_SESSION['cart'][$weapon_id])) {
                $_SESSION['cart'][$weapon_id] += $quantity;
            } else {
                $_SESSION['cart'][$weapon_id] = $quantity;
            }
        }
        break;

    case 'remove':
        unset($_SESSION['cart'][$weapon_id]);
        break;

    case 'update':
        if ($weapon_id > 0 && $quantity > 0) {
            $_SESSION['cart'][$weapon_id] = $quantity;
        } elseif ($quantity <= 0) {
            unset($_SESSION['cart'][$weapon_id]);
        }
        break;

    case 'clear':
        $_SESSION['cart'] = [];
        break;
}

// Redirect back to the referring page, or cart
$redirect = $_POST['redirect'] ?? $_SERVER['HTTP_REFERER'] ?? 'cart.php';
header("Location: $redirect");
exit;
?>
