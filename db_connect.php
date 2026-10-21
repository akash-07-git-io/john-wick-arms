<?php
// ============================================================
// Database Connection Configuration
// ============================================================

$db_host = getenv('DB_HOST') ?: 'localhost';
$db_user = getenv('DB_USER') ?: 'root';
$db_pass = getenv('DB_PASS') !== false ? getenv('DB_PASS') : '';
$db_name = getenv('DB_NAME') ?: 'john_wick_arms';
$db_port = getenv('DB_PORT') ? intval(getenv('DB_PORT')) : 3306;

// Suppress default fatal error to display user-friendly setup instructions
$conn = @mysqli_connect($db_host, $db_user, $db_pass, $db_name, $db_port);

if (!$conn) {
    // If database doesn't exist yet, attempt to connect to MySQL server without database
    $conn_root = @mysqli_connect($db_host, $db_user, $db_pass, '', $db_port);
    if ($conn_root) {
        // Attempt to create database and import schema if file exists
        @mysqli_query($conn_root, "CREATE DATABASE IF NOT EXISTS `$db_name`");
        @mysqli_select_db($conn_root, $db_name);
        $conn = $conn_root;
    } else {
        die("
        <div style='font-family:sans-serif; max-width:650px; margin:50px auto; padding:25px; border:1px solid #d4af37; background:#121318; color:#f0f2f5; border-radius:8px; line-height:1.6;'>
            <h2 style='color:#d4af37; margin-top:0;'>Database Connection Setup</h2>
            <p>Could not connect to MySQL database <strong>$db_name</strong> on <strong>$db_host</strong>.</p>
            <p><strong>To resolve this in XAMPP:</strong></p>
            <ol style='padding-left:20px; color:#9aa0b4;'>
                <li>Open XAMPP Control Panel and click <strong>Start</strong> next to MySQL and Apache.</li>
                <li>Open <a href='http://localhost/phpmyadmin' style='color:#d4af37;' target='_blank'>phpMyAdmin</a> in your browser.</li>
                <li>Import the SQL file located at: <code>database/john_wick_arms.sql</code></li>
                <li>Refresh this page.</li>
            </ol>
            <p style='color:#e74c3c; font-size:0.9rem;'>Error detail: " . mysqli_connect_error() . "</p>
        </div>
        ");
    }
}

// Set UTF-8 encoding
mysqli_set_charset($conn, 'utf8mb4');

// Auto-seed schema and data if tables do not exist yet (e.g. Render/Docker initial boot)
$check_table = @mysqli_query($conn, "SHOW TABLES LIKE 'weapons'");
if ($check_table && mysqli_num_rows($check_table) === 0) {
    $sql_file = __DIR__ . '/database/john_wick_arms.sql';
    if (file_exists($sql_file)) {
        $sql = file_get_contents($sql_file);
        if (mysqli_multi_query($conn, $sql)) {
            do {
                if ($result = mysqli_store_result($conn)) {
                    mysqli_free_result($result);
                }
            } while (mysqli_more_results($conn) && mysqli_next_result($conn));
        }
    }
}

// Start session if not already active
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
?>
