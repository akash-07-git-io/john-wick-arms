<?php
// ============================================================
// Database Connection Configuration
// ============================================================

$db_host = getenv('DB_HOST') ?: 'localhost';
$db_user = getenv('DB_USER') ?: 'root';
$db_pass = getenv('DB_PASS') !== false ? getenv('DB_PASS') : '';
$db_name = getenv('DB_NAME') ?: 'john_wick_arms';
$db_port = getenv('DB_PORT') ? intval(getenv('DB_PORT')) : 3306;

// Turn off automatic exception throwing so failed connections can be handled gracefully
if (function_exists('mysqli_report')) {
    @mysqli_report(MYSQLI_REPORT_OFF);
}

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
        $conn = false;
    }
}

if ($conn) {
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
}

// Start session if not already active
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
?>
