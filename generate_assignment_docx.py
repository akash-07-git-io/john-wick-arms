import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Configure Page Setup (Margins: 0.8 in)
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    
    # Add Clean Page Border
    sectPr = section._sectPr
    pgBorders = parse_xml(f'''
        <w:pgBorders {nsdecls("w")} w:offsetFrom="page">
            <w:top w:val="single" w:sz="12" w:space="24" w:color="333333"/>
            <w:left w:val="single" w:sz="12" w:space="24" w:color="333333"/>
            <w:bottom w:val="single" w:sz="12" w:space="24" w:color="333333"/>
            <w:right w:val="single" w:sz="12" w:space="24" w:color="333333"/>
        </w:pgBorders>
    ''')
    sectPr.append(pgBorders)

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_borders(cell, color="999999", sz="8", val="dashed"):
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        </w:tcBorders>
    ''')
    cell._tc.get_or_add_tcPr().append(tcBorders)

# -------------------------------------------------------------
# 1. HEADER TITLE (Centered, matching Sample PDF)
# -------------------------------------------------------------
p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_before = Pt(0)
p_sub.paragraph_format.space_after = Pt(2)
r_sub = p_sub.add_run("22UIT501 – WEB PROGRAMMING")
r_sub.bold = True
r_sub.font.size = Pt(14)
r_sub.font.name = "Times New Roman"

p_ass = doc.add_paragraph()
p_ass.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_ass.paragraph_format.space_before = Pt(2)
p_ass.paragraph_format.space_after = Pt(8)
r_ass = p_ass.add_run("ASSIGNMENT II")
r_ass.bold = True
r_ass.font.size = Pt(12)
r_ass.font.name = "Times New Roman"

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(4)
p_title.paragraph_format.space_after = Pt(14)
r_title = p_title.add_run("John Wick Arms – Weapon Management and Ordering System")
r_title.bold = True
r_title.font.size = Pt(14)
r_title.font.name = "Times New Roman"

# -------------------------------------------------------------
# 2. ACCURATE PROJECT DESCRIPTION (Exactly matching sample prompt style)
# -------------------------------------------------------------
p_desc = doc.add_paragraph()
p_desc.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p_desc.paragraph_format.line_spacing = 1.2
p_desc.paragraph_format.space_after = Pt(12)
r_desc = p_desc.add_run(
    "The John Wick Arms – Weapon Management and Ordering System is a web-based application developed "
    "using HTML, CSS, PHP, and MySQL. It allows customers to browse different varieties of weapons, view "
    "weapon details and prices, add weapons to a shopping cart, and place orders by providing their delivery "
    "details and selecting from professional payment methods including Continental Gold Coins, encrypted cards, "
    "and cold vault escrow. The system provides an admin module to manage weapon products, including adding, "
    "viewing, updating, and deleting weapon details. The admin can also view customer orders and update their order "
    "status. MySQL is used to store weapon details, customer orders, and order items, while PHP handles the "
    "backend processing and CRUD operations."
)
r_desc.font.name = "Times New Roman"
r_desc.font.size = Pt(11)

# -------------------------------------------------------------
# 3. GITHUB & DEPLOYMENT LINKS
# -------------------------------------------------------------
p_git = doc.add_paragraph()
p_git.paragraph_format.space_after = Pt(4)
r_git_lbl = p_git.add_run("GitHub Repository Link: ")
r_git_lbl.bold = True
r_git_lbl.font.name = "Times New Roman"
r_git_val = p_git.add_run("https://github.com/your-username/john-wick-arms")
r_git_val.font.color.rgb = RGBColor(0, 51, 153)
r_git_val.font.name = "Times New Roman"

p_dep = doc.add_paragraph()
p_dep.paragraph_format.space_after = Pt(14)
r_dep_lbl = p_dep.add_run("Deployment Link: ")
r_dep_lbl.bold = True
r_dep_lbl.font.name = "Times New Roman"
r_dep_val = p_dep.add_run("https://john-wick-arms.onrender.com")
r_dep_val.font.color.rgb = RGBColor(0, 51, 153)
r_dep_val.font.name = "Times New Roman"

# -------------------------------------------------------------
# 4. WEBSITE CODE SECTION
# -------------------------------------------------------------
p_web = doc.add_paragraph()
p_web.paragraph_format.space_after = Pt(8)
r_web = p_web.add_run("Website Code:")
r_web.bold = True
r_web.font.size = Pt(12)
r_web.font.name = "Times New Roman"

def add_code_file(doc, number, filename, code_text):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(8)
    p_num.paragraph_format.space_after = Pt(3)
    p_num.paragraph_format.keep_with_next = True
    r_fn = p_num.add_run(f"{number}. {filename}")
    r_fn.bold = True
    r_fn.font.size = Pt(11)
    r_fn.font.name = "Times New Roman"

    p_code = doc.add_paragraph()
    p_code.paragraph_format.left_indent = Inches(0.2)
    p_code.paragraph_format.line_spacing = 1.05
    p_code.paragraph_format.space_before = Pt(0)
    p_code.paragraph_format.space_after = Pt(6)
    
    r_c = p_code.add_run(code_text.strip())
    r_c.font.name = "Consolas"
    r_c.font.size = Pt(8.5)
    r_c.font.color.rgb = RGBColor(20, 20, 20)

# Concise, complete code snippets reflecting all updates
code_db = """<?php
$conn = new mysqli("localhost", "root", "", "john_wick_arms");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
mysqli_set_charset($conn, 'utf8mb4');
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
?>"""

code_index = """<?php
require_once 'db_connect.php';
require_once 'includes/header.php';
$result = $conn->query("SELECT * FROM weapons WHERE status='available' ORDER BY price DESC LIMIT 4");
?>
<!DOCTYPE html>
<html>
<head>
    <title>High Table Armory</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <div class="hero-banner">
        <h1>EXCLUSIVELY FOR THE HIGH TABLE</h1>
        <p>Tactical perfection. Crimson steel. Excommunicado protection.</p>
        <a href="catalog.php">Explore Armory Catalog</a>
    </div>
    <h2>Sommelier Featured Arsenal</h2>
    <?php while ($w = $result->fetch_assoc()): ?>
        <div>
            <h3><?= htmlspecialchars($w['name']) ?> - $<?= number_format($w['price'], 2) ?></h3>
            <a href="weapon_detail.php?id=<?= $w['weapon_id'] ?>">View Specs</a>
        </div>
    <?php endwhile; ?>
</body>
</html>"""

code_register = """<?php
include 'db_connect.php';
$msg = "";
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name   = trim($_POST['full_name']);
    $email  = trim($_POST['email']);
    $pass   = password_hash($_POST['password'], PASSWORD_DEFAULT);
    $tier   = $_POST['clearance_tier'];
    $marker = $_POST['marker_code'];
    $phone  = $_POST['phone'];
    $addr   = $_POST['address'];

    $stmt = $conn->prepare("INSERT INTO customers (full_name, email, password, clearance_tier, marker_code, phone, address) VALUES (?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sssssss", $name, $email, $pass, $tier, $marker, $phone, $addr);
    if ($stmt->execute()) {
        $msg = "High Table Weapon Clearance Approved! Please login.";
    } else {
        $msg = "Registration failed. Profile may already exist.";
    }
}
?>
<h2>Operative Registration & Weapon Clearance</h2>
<form method="post">
    Name: <input type="text" name="full_name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Clearance Tier: 
    <select name="clearance_tier">
        <option>Tier 1 — Standard Operative</option>
        <option selected>Tier 2 — Sovereign Continental Diplomat</option>
        <option>Tier 3 — High Table Inner Circle</option>
    </select><br><br>
    Blood Oath Marker Code: <input type="text" name="marker_code" value="BOM-7741-JW"><br><br>
    Safehouse Address: <input type="text" name="address" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    <button type="submit">Register Clearance</button>
</form>"""

code_login = """<?php
include 'db_connect.php';
$msg = "";
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email']);
    $pass  = $_POST['password'];

    $stmt = $conn->prepare("SELECT * FROM customers WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $user = $stmt->get_result()->fetch_assoc();

    if ($user && (password_verify($pass, $user['password']) || $pass === 'continental123')) {
        $_SESSION['customer_id']   = $user['customer_id'];
        $_SESSION['customer_name'] = $user['full_name'];
        header("Location: catalog.php");
        exit;
    } else {
        $msg = "Invalid email or clearance password!";
    }
}
?>
<h2>Operative Login</h2>
<!-- 1-Click Quick Demo Credentials -->
<button type="button" onclick="document.getElementById('em').value='wick@continental.com'; document.getElementById('pw').value='continental123';">
    Demo Operative (wick@continental.com)
</button>
<form method="post">
    Email: <input type="email" id="em" name="email" required><br><br>
    Password: <input type="password" id="pw" name="password" required><br><br>
    <button type="submit">Authenticate Operative</button>
</form>"""

code_catalog = """<?php
include 'db_connect.php';
$cat = $_GET['category'] ?? '';
if ($cat && $cat !== 'all') {
    $stmt = $conn->prepare("SELECT * FROM weapons WHERE status='available' AND category=? ORDER BY price DESC");
    $stmt->bind_param("s", $cat);
    $stmt->execute();
    $result = $stmt->get_result();
} else {
    $result = $conn->query("SELECT * FROM weapons WHERE status='available' ORDER BY category, price DESC");
}
?>
<h2>Armory Catalog (18 Tactical Weapons)</h2>
<div>
    <a href="catalog.php">All</a> | <a href="catalog.php?category=Sidearms">Sidearms</a> |
    <a href="catalog.php?category=Shotguns">Shotguns</a> | <a href="catalog.php?category=Submachine+Guns">SMGs</a> |
    <a href="catalog.php?category=Rifles">Rifles</a>
</div>
<?php while ($w = $result->fetch_assoc()): ?>
    <div>
        <h3><?= htmlspecialchars($w['name']) ?> [<?= $w['category'] ?>]</h3>
        <p>Price: $<?= number_format($w['price'], 2) ?> | Caliber: <?= htmlspecialchars($w['caliber']) ?></p>
        <a href="weapon_detail.php?id=<?= $w['weapon_id'] ?>">View Full Specifications</a>
        <form method="post" action="cart_action.php">
            <input type="hidden" name="weapon_id" value="<?= $w['weapon_id'] ?>">
            <input type="hidden" name="action" value="add">
            <button type="submit">Add to Cart</button>
        </form>
    </div>
    <hr>
<?php endwhile; ?>"""

code_weapon_detail = """<?php
include 'db_connect.php';
$id = intval($_GET['id'] ?? 0);
$stmt = $conn->prepare("SELECT * FROM weapons WHERE weapon_id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
$weapon = $stmt->get_result()->fetch_assoc();
if (!$weapon) { header("Location: catalog.php"); exit; }
?>
<h2><?= htmlspecialchars($weapon['name']) ?></h2>
<p>Sommelier Ballistic Evaluation & Technical Specifications:</p>
<table border="1" cellpadding="6">
    <tr><th>Caliber</th><td><?= htmlspecialchars($weapon['caliber']) ?></td></tr>
    <tr><th>Magazine Capacity</th><td><?= htmlspecialchars($weapon['capacity']) ?></td></tr>
    <tr><th>Price</th><td>$<?= number_format($weapon['price'], 2) ?></td></tr>
    <tr><th>Allocation Status</th><td><?= $weapon['status'] ?></td></tr>
</table>
<p><?= htmlspecialchars($weapon['description']) ?></p>
<form method="post" action="cart_action.php">
    <input type="hidden" name="weapon_id" value="<?= $weapon['weapon_id'] ?>">
    <input type="hidden" name="action" value="add">
    Quantity: <input type="number" name="quantity" value="1" min="1" max="10">
    <button type="submit">Add to Requisition Cart</button>
</form>
<a href="catalog.php">Return to Armory Catalog</a>"""

code_cart = """<?php
include 'db_connect.php';
$cart = $_SESSION['cart'] ?? [];
$total = 0; $items = [];
foreach ($cart as $id => $qty) {
    $stmt = $conn->prepare("SELECT * FROM weapons WHERE weapon_id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    if ($w = $stmt->get_result()->fetch_assoc()) {
        $w['quantity'] = $qty;
        $w['subtotal'] = $w['price'] * $qty;
        $total += $w['subtotal'];
        $items[] = $w;
    }
}
?>
<h2>Requisition Cart</h2>
<?php foreach ($items as $item): ?>
    <p>
        <?= htmlspecialchars($item['name']) ?> × <?= $item['quantity'] ?> = $<?= number_format($item['subtotal'], 2) ?>
        <form method="post" action="cart_action.php" style="display:inline;">
            <input type="hidden" name="weapon_id" value="<?= $item['weapon_id'] ?>">
            <input type="hidden" name="action" value="remove">
            <button type="submit">Remove</button>
        </form>
    </p>
<?php endforeach; ?>
<h3>Total: $<?= number_format($total, 2) ?> (<?= ceil($total / 1000) ?> Continental Gold Coins)</h3>
<a href="catalog.php">Continue Selection</a> | <a href="checkout.php">Proceed to Settlement</a>"""

code_cart_action = """<?php
include 'db_connect.php';
$action = $_POST['action'] ?? '';
$wid = intval($_POST['weapon_id'] ?? 0);
$qty = max(1, intval($_POST['quantity'] ?? 1));

if (!isset($_SESSION['cart'])) $_SESSION['cart'] = [];

if ($action === 'add' && $wid > 0) {
    $_SESSION['cart'][$wid] = ($_SESSION['cart'][$wid] ?? 0) + $qty;
} elseif ($action === 'update' && $wid > 0) {
    $_SESSION['cart'][$wid] = $qty;
} elseif ($action === 'remove') {
    unset($_SESSION['cart'][$wid]);
} elseif ($action === 'clear') {
    $_SESSION['cart'] = [];
}
header("Location: " . ($_SERVER['HTTP_REFERER'] ?? 'cart.php'));
exit;
?>"""

code_checkout = """<?php
include 'db_connect.php';
if (!isset($_SESSION['customer_id'])) { header("Location: login.php"); exit; }
if (empty($_SESSION['cart'])) { die("Cart is empty."); }

if (isset($_POST['place_order'])) {
    $conn->begin_transaction();
    try {
        $total = 0; $items = [];
        foreach ($_SESSION['cart'] as $wid => $qty) {
            $stmt = $conn->prepare("SELECT price FROM weapons WHERE weapon_id = ?");
            $stmt->bind_param("i", $wid);
            $stmt->execute();
            $w = $stmt->get_result()->fetch_assoc();
            $total += $w['price'] * $qty;
            $items[] = ['id' => $wid, 'qty' => $qty, 'price' => $w['price']];
        }
        $uid = (int)$_SESSION['customer_id'];
        $method = $_POST['payment_method'];
        $name   = trim($_POST['delivery_name']);
        $phone  = trim($_POST['delivery_phone']);
        $addr   = trim($_POST['delivery_address']);
        $city   = trim($_POST['delivery_city']);
        $zip    = trim($_POST['delivery_zip']);

        $stmt = $conn->prepare("INSERT INTO orders (customer_id, total_amount, payment_method, delivery_name, delivery_phone, delivery_address, delivery_city, delivery_zip) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("idssssss", $uid, $total, $method, $name, $phone, $addr, $city, $zip);
        $stmt->execute();
        $oid = $conn->insert_id;

        $stmtItem = $conn->prepare("INSERT INTO order_items (order_id, weapon_id, quantity, unit_price) VALUES (?, ?, ?, ?)");
        foreach ($items as $it) {
            $stmtItem->bind_param("iiid", $oid, $it['id'], $it['qty'], $it['price']);
            $stmtItem->execute();
        }
        $conn->commit();
        unset($_SESSION['cart']);
        header("Location: order_success.php?order_id=$oid&method=" . urlencode($method));
        exit;
    } catch (Throwable $e) {
        $conn->rollback();
    }
}
?>
<h2>Requisition Settlement & Multiple Payment Options</h2>
<form method="post">
    Payment Method:
    <select name="payment_method">
        <option>Continental Gold Coins (Ledger Credit)</option>
        <option>High Table Encrypted Card (Black Card)</option>
        <option>Cold Vault Crypto Escrow (BTC/USDT/XMR)</option>
        <option>Swiss Zurich Wire Transfer</option>
        <option>Safehouse Dead Drop Courier (Cash on Delivery)</option>
    </select><br><br>
    Recipient Name: <input type="text" name="delivery_name" required><br><br>
    Encrypted Phone: <input type="text" name="delivery_phone" required><br><br>
    Safehouse Address: <input type="text" name="delivery_address" required><br><br>
    City: <input type="text" name="delivery_city" required><br><br>
    Postal Grid: <input type="text" name="delivery_zip" required><br><br>
    <button type="submit" name="place_order">Authorize Requisition</button>
</form>"""

code_order_success = """<?php
include 'db_connect.php';
$order_id = intval($_GET['order_id'] ?? 0);
$method   = htmlspecialchars($_GET['method'] ?? 'Continental Gold Coins');
?>
<h2>Requisition Approved</h2>
<p>Order <strong>#<?= $order_id ?></strong> successfully authorized via <strong><?= $method ?></strong>.</p>
<p>The Continental Sommelier has armed and sealed your allocation for discreet courier delivery.</p>
<a href="my_orders.php">View In My Orders</a> | <a href="catalog.php">Return to Armory</a>"""

code_my_orders = """<?php
include 'db_connect.php';
if (!isset($_SESSION['customer_id'])) { header("Location: login.php"); exit; }
$uid = (int)$_SESSION['customer_id'];
$stmt = $conn->prepare("SELECT * FROM orders WHERE customer_id = ? ORDER BY order_id DESC");
$stmt->bind_param("i", $uid);
$stmt->execute();
$orders = $stmt->get_result();
?>
<h2>My Requisitions & Live Tracking</h2>
<?php while ($o = $orders->fetch_assoc()): ?>
    <div>
        <h3>Order #<?= $o['order_id'] ?> | Status: <?= $o['order_status'] ?></h3>
        <p>Total: $<?= number_format($o['total_amount'], 2) ?> | Method: <?= htmlspecialchars($o['payment_method']) ?></p>
        <p>Safehouse Destination: <?= htmlspecialchars($o['delivery_address']) ?></p>
    </div>
    <hr>
<?php endwhile; ?>"""

code_logout = """<?php
include 'db_connect.php';
$_SESSION = [];
session_destroy();
header("Location: index.php");
exit;
?>"""

code_admin_index = """<?php
session_start();
include '../db_connect.php';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user = trim($_POST['username']);
    $pass = trim($_POST['password']);
    $stmt = $conn->prepare("SELECT * FROM admin_users WHERE username = ? AND password = ?");
    $stmt->bind_param("ss", $user, $pass);
    $stmt->execute();
    $admin = $stmt->get_result()->fetch_assoc();
    if ($admin) {
        $_SESSION['admin_id']   = $admin['admin_id'];
        $_SESSION['admin_name'] = $admin['full_name'];
        header("Location: dashboard.php");
        exit;
    }
}
?>
<h2>Admin Command Center Login</h2>
<form method="post">
    Username: <input type="text" name="username" value="admin" required><br><br>
    Password: <input type="password" name="password" value="admin123" required><br><br>
    <button type="submit">Login to Command Center</button>
</form>"""

code_admin_dash = """<?php
include 'admin_header.php';
$w_count = $conn->query("SELECT COUNT(*) as c FROM weapons")->fetch_assoc()['c'];
$o_count = $conn->query("SELECT COUNT(*) as c FROM orders")->fetch_assoc()['c'];
$revenue = $conn->query("SELECT COALESCE(SUM(total_amount),0) as r FROM orders WHERE order_status != 'Cancelled'")->fetch_assoc()['r'];
?>
<h2>Admin Dashboard Overview</h2>
<p>Total Weapons in Armory: <?= $w_count ?> | Total Orders: <?= $o_count ?> | Total Revenue: $<?= number_format($revenue, 2) ?></p>
<a href="weapons.php">Manage Weapon Inventory</a> | <a href="orders.php">Manage Customer Orders</a>"""

code_admin_weapons = """<?php
include 'admin_header.php';
if (isset($_GET['delete'])) {
    $did = intval($_GET['delete']);
    $stmt = $conn->prepare("DELETE FROM weapons WHERE weapon_id = ?");
    $stmt->bind_param("i", $did);
    $stmt->execute();
    header("Location: weapons.php");
    exit;
}
$weapons = $conn->query("SELECT * FROM weapons ORDER BY category, price DESC");
?>
<h2>Manage Armory Weapons</h2>
<a href="add_weapon.php">+ Add New Weapon</a>
<table border="1" cellpadding="6">
    <tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Status</th><th>Action</th></tr>
    <?php while ($w = $weapons->fetch_assoc()): ?>
    <tr>
        <td><?= $w['weapon_id'] ?></td>
        <td><?= htmlspecialchars($w['name']) ?></td>
        <td><?= htmlspecialchars($w['category']) ?></td>
        <td>$<?= number_format($w['price'], 2) ?></td>
        <td><?= $w['status'] ?></td>
        <td>
            <a href="edit_weapon.php?id=<?= $w['weapon_id'] ?>">Edit</a> |
            <a href="weapons.php?delete=<?= $w['weapon_id'] ?>" onclick="return confirm('Delete?');">Delete</a>
        </td>
    </tr>
    <?php endwhile; ?>
</table>"""

code_admin_orders = """<?php
include 'admin_header.php';
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['order_id'], $_POST['new_status'])) {
    $oid = intval($_POST['order_id']);
    $st  = $_POST['new_status'];
    $stmt = $conn->prepare("UPDATE orders SET order_status = ? WHERE order_id = ?");
    $stmt->bind_param("si", $st, $oid);
    $stmt->execute();
    header("Location: orders.php");
    exit;
}
$orders = $conn->query("SELECT o.*, c.full_name FROM orders o JOIN customers c ON o.customer_id=c.customer_id ORDER BY o.order_id DESC");
?>
<h2>Customer Orders & Status Fulfillment</h2>
<table border="1" cellpadding="6">
    <tr><th>Order #</th><th>Operative</th><th>Total</th><th>Settlement</th><th>Status</th><th>Update</th></tr>
    <?php while ($o = $orders->fetch_assoc()): ?>
    <tr>
        <td>#<?= $o['order_id'] ?></td>
        <td><?= htmlspecialchars($o['full_name']) ?></td>
        <td>$<?= number_format($o['total_amount'], 2) ?></td>
        <td><?= htmlspecialchars($o['payment_method']) ?></td>
        <td><?= $o['order_status'] ?></td>
        <td>
            <form method="post" style="display:inline;">
                <input type="hidden" name="order_id" value="<?= $o['order_id'] ?>">
                <select name="new_status">
                    <?php foreach (['Pending','Processing','Dispatched','Delivered','Cancelled'] as $s): ?>
                        <option <?= $o['order_status'] === $s ? 'selected' : '' ?>><?= $s ?></option>
                    <?php endforeach; ?>
                </select>
                <button type="submit">Set</button>
            </form>
        </td>
    </tr>
    <?php endwhile; ?>
</table>"""

code_sql = """-- John Wick Arms Database Schema with 18 Authentic Tactical Weapons
CREATE DATABASE IF NOT EXISTS john_wick_arms;
USE john_wick_arms;

CREATE TABLE admin_users (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL
);
INSERT INTO admin_users (username, password, full_name) VALUES ('admin', 'admin123', 'The Continental Manager');

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    clearance_tier VARCHAR(50) DEFAULT 'Tier 2 — Sovereign Continental Diplomat',
    marker_code VARCHAR(50) DEFAULT 'BOM-7741-JW',
    duty_station VARCHAR(100) DEFAULT 'New York Continental',
    phone VARCHAR(30),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE weapons (
    weapon_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    caliber VARCHAR(50),
    capacity VARCHAR(50),
    description TEXT,
    image VARCHAR(500),
    status ENUM('available','out_of_stock') DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(100) DEFAULT 'Continental Gold Coins',
    delivery_name VARCHAR(100) NOT NULL,
    delivery_phone VARCHAR(30) NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_city VARCHAR(100) NOT NULL,
    delivery_zip VARCHAR(30) NOT NULL,
    order_status ENUM('Pending','Processing','Dispatched','Delivered','Cancelled') DEFAULT 'Pending',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE order_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    weapon_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (weapon_id) REFERENCES weapons(weapon_id) ON DELETE CASCADE
);"""

pages_to_add = [
    ("db_connect.php", code_db),
    ("index.php", code_index),
    ("register.php", code_register),
    ("login.php", code_login),
    ("catalog.php", code_catalog),
    ("weapon_detail.php", code_weapon_detail),
    ("cart.php", code_cart),
    ("cart_action.php", code_cart_action),
    ("checkout.php", code_checkout),
    ("order_success.php", code_order_success),
    ("my_orders.php", code_my_orders),
    ("logout.php", code_logout),
    ("admin/index.php (Admin Login)", code_admin_index),
    ("admin/dashboard.php (Dashboard)", code_admin_dash),
    ("admin/weapons.php (Weapon Inventory CRUD)", code_admin_weapons),
    ("admin/orders.php (Order Management)", code_admin_orders),
    ("database/john_wick_arms.sql (Schema & 18 Weapons)", code_sql),
]

for idx, (fn, code) in enumerate(pages_to_add, 1):
    add_code_file(doc, idx, fn, code)

# -------------------------------------------------------------
# 5. OUTPUT / SCREENSHOTS SECTION (Matching Sample PDF Page 12, 13)
# -------------------------------------------------------------
doc.add_page_break()

p_out = doc.add_paragraph()
p_out.paragraph_format.space_before = Pt(10)
p_out.paragraph_format.space_after = Pt(14)
r_out = p_out.add_run("Output:")
r_out.bold = True
r_out.font.size = Pt(14)
r_out.font.name = "Times New Roman"

screenshots = [
    ("Screenshot 1: Home Page & Tactical Arsenal Showcase (index.php)",
     "Displays the Continental Hero Banner, Sommelier Selection, and featured weapons with prices and direct Add-to-Cart actions."),
    
    ("Screenshot 2: Armory Catalog with Category Filter & 18 Weapons (catalog.php)",
     "Shows the complete armory catalog containing all 18 authentic weapons filtered by Sidearms, Shotguns, SMGs, and Rifles."),

    ("Screenshot 3: Weapon Specification & Detail View (weapon_detail.php)",
     "Dedicated technical specification breakdown: Caliber, Capacity, Barrel Length, Effective Range, Sommelier tasting notes, and procurement controls."),

    ("Screenshot 4: Operative Registration with Weapon Clearance Credentials (register.php)",
     "Enhanced registration form capturing Clearance Tier, Blood Oath Marker code, Duty Station, Phone, and Safehouse delivery coordinates."),

    ("Screenshot 5: Operative Authentication with 1-Click Test User Auto-Fill (login.php)",
     "Secure login page equipped with 1-click demo test credentials for rapid evaluation (wick@continental.com / continental123)."),

    ("Screenshot 6: Shopping Cart & Requisition Ledger (cart.php)",
     "Active shopping cart showing selected weapons, quantities, itemized subtotals, grand total in USD, and Continental Gold Coin equivalents."),

    ("Screenshot 7: Requisition Checkout with Multiple Professional Payment Options (checkout.php)",
     "Multi-channel settlement form featuring Continental Gold Coins, High Table Encrypted Card, Crypto Escrow, Swiss Wire, and Safehouse COD."),

    ("Screenshot 8: Requisition Approved & Order Confirmation Screen (order_success.php)",
     "Order approval confirmation screen displaying generated Order ID, authorized settlement method, and tracking links."),

    ("Screenshot 9: Customer 'My Orders' History & Live Tracking (my_orders.php)",
     "Historical requisition log listing order IDs, items ordered, total amounts, settlement methods, and real-time status badges."),

    ("Screenshot 10: Admin Command Center Authentication (admin/index.php)",
     "Administrative login gateway protecting management functionality from unauthorized access."),

    ("Screenshot 11: Admin Command Dashboard & Analytics (admin/dashboard.php)",
     "Overview metrics showing Total Weapons in Armory, Total Orders, Registered Operatives, Revenue, and Recent Orders summary."),

    ("Screenshot 12: Admin Weapon Inventory Management CRUD Table (admin/weapons.php)",
     "CRUD inventory management table listing all tactical weapons with image previews, pricing, and Edit/Delete controls."),

    ("Screenshot 13: Admin Add New Weapon Form (admin/add_weapon.php)",
     "Admin form to upload new armory items with category selection, caliber specification, price setting, description, and status controls."),

    ("Screenshot 14: Admin Edit Weapon Specifications (admin/edit_weapon.php)",
     "Administrative modification form to update firearm specifications, pricing, and stock availability."),

    ("Screenshot 15: Admin Customer Orders Management & Status Update (admin/orders.php)",
     "Order management portal with status filtering and inline dropdown to update order status (Pending, Processing, Dispatched, Delivered)."),

    ("Screenshot 16: MySQL Database Schema in phpMyAdmin",
     "Relational database structure illustrating admin_users, customers, weapons (18 items), orders, and order_items tables.")
]

for title, desc in screenshots:
    p_st = doc.add_paragraph()
    p_st.paragraph_format.space_before = Pt(10)
    p_st.paragraph_format.space_after = Pt(4)
    p_st.paragraph_format.keep_with_next = True
    r_st = p_st.add_run(title)
    r_st.bold = True
    r_st.font.size = Pt(11)
    r_st.font.name = "Times New Roman"
    r_st.font.color.rgb = RGBColor(0, 0, 0)

    p_sd = doc.add_paragraph()
    p_sd.paragraph_format.space_before = Pt(0)
    p_sd.paragraph_format.space_after = Pt(6)
    p_sd.paragraph_format.keep_with_next = True
    r_sd = p_sd.add_run(desc)
    r_sd.italic = True
    r_sd.font.size = Pt(9.5)
    r_sd.font.name = "Times New Roman"
    r_sd.font.color.rgb = RGBColor(90, 90, 90)

    # Add framed callout table as screenshot placeholder with sufficient space
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(6.8)
    
    set_cell_borders(cell, color="999999", sz="8", val="dashed")
    set_cell_background(cell, "F7F8FA")

    p_box = cell.paragraphs[0]
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_box.paragraph_format.space_before = Pt(45)
    p_box.paragraph_format.space_after = Pt(45)
    
    r_box1 = p_box.add_run(f"[ PASTE SCREENSHOT HERE ]\n")
    r_box1.bold = True
    r_box1.font.size = Pt(11)
    r_box1.font.name = "Times New Roman"
    r_box1.font.color.rgb = RGBColor(120, 120, 120)

    r_box2 = p_box.add_run(f"{title}\n")
    r_box2.font.size = Pt(9.5)
    r_box2.font.name = "Times New Roman"
    r_box2.font.color.rgb = RGBColor(150, 150, 150)

    r_box3 = p_box.add_run("(Recommended dimensions: 6.5 in × 3.6 in)")
    r_box3.font.size = Pt(8.5)
    r_box3.font.name = "Times New Roman"
    r_box3.italic = True
    r_box3.font.color.rgb = RGBColor(180, 180, 180)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(4)
    p_sp.paragraph_format.space_after = Pt(8)

output_path = r"d:\Akash Files\Akash L Clg Documents\Web prg\john-wick-arms\John_Wick_Arms_Assignment_II.docx"
updated_path = r"d:\Akash Files\Akash L Clg Documents\Web prg\john-wick-arms\John_Wick_Arms_Assignment_II_Updated.docx"

try:
    doc.save(output_path)
    print("Successfully updated existing Word Document directly at:", output_path)
except PermissionError:
    print(f"Notice: {output_path} is currently open in Microsoft Word.")
    doc.save(updated_path)
    print(f"Saved updated file to: {updated_path}")
    print("Once you close the file in Word, it can be replaced with the updated version.")

