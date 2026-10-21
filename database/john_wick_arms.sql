-- ============================================================
-- John Wick & Co. Arms – Weapon Management & Ordering System
-- Database Schema for MySQL
-- ============================================================

CREATE DATABASE IF NOT EXISTS john_wick_arms;
USE john_wick_arms;

-- -----------------------------------------------------------
-- 1. Admin Users
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS admin_users (
    admin_id    INT AUTO_INCREMENT PRIMARY KEY,
    username    VARCHAR(50)  NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,
    full_name   VARCHAR(100) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Default admin  (username: admin  |  password: admin123)
INSERT INTO admin_users (username, password, full_name)
VALUES ('admin', 'admin123', 'The Continental Manager');

-- -----------------------------------------------------------
-- 2. Customers
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name   VARCHAR(100) NOT NULL,
    email       VARCHAR(100) NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,
    phone       VARCHAR(20)  DEFAULT NULL,
    address     TEXT         DEFAULT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- -----------------------------------------------------------
-- 3. Weapons (Products)
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS weapons (
    weapon_id   INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(150) NOT NULL,
    category    VARCHAR(50)  NOT NULL,
    price       DECIMAL(10,2) NOT NULL,
    description TEXT,
    image       VARCHAR(500) DEFAULT 'images/default.jpg',
    status      ENUM('available','out_of_stock') DEFAULT 'available',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Sample weapons
INSERT INTO weapons (name, category, price, description, image) VALUES
('Custom Pit Viper 9mm',        'Sidearms',        7500.00, 'Match-grade barrel, titanium nitrided finish, and ultra-smooth cycling.',                      'https://images.stockcake.com/public/2/e/4/2e4919a9-1519-444b-84e7-4d67c789f123/neo-noir-assault-rifle-stockcake.jpg'),
('Benelli M4 Tactical Ported',  'Shotguns',        4200.00, 'Auto-regulating gas-operated system with custom textured grip.',                               'https://img.magnific.com/premium-psd/shotgun-profile-view-overlay-black-background_886588-2563.jpg?semt=ais_hybrid&w=740&q=80'),
('SIG MPX Suppressed Spec',     'Submachine Guns', 5800.00, 'Subsonic precision optimized for close-quarters indoor operations.',                           'https://png.pngtree.com/png-clipart/20250427/original/pngtree-golden-rifle-bullets-in-3d-with-tactical-aesthetic-png-image_20853094.png'),
('Desert Tech SRS-A1 Precision','Rifles',          9500.00, 'Bullpup bolt-action sniper system for high-value target neutralization.',                      'https://images.stockcake.com/public/1/6/8/1680fe30-65bf-4e5a-927e-a0bff144e54f/golden-coins-stacked-stockcake.jpg'),
('Glock 34 Combat Master',      'Sidearms',        6800.00, 'Taran Tactical Innovations custom build with flared magwell and fiber optic sights.',          'https://images.stockcake.com/public/2/e/4/2e4919a9-1519-444b-84e7-4d67c789f123/neo-noir-assault-rifle-stockcake.jpg'),
('Remington 870 Breacher',      'Shotguns',        3500.00, 'Short-barrel breaching shotgun with door-breaching muzzle brake and pistol grip.',             'https://img.magnific.com/premium-psd/shotgun-profile-view-overlay-black-background_886588-2563.jpg?semt=ais_hybrid&w=740&q=80');

-- -----------------------------------------------------------
-- 4. Orders
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS orders (
    order_id        INT AUTO_INCREMENT PRIMARY KEY,
    customer_id     INT NOT NULL,
    total_amount    DECIMAL(10,2) NOT NULL,
    delivery_name   VARCHAR(100) NOT NULL,
    delivery_phone  VARCHAR(20)  NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_city   VARCHAR(100) NOT NULL,
    delivery_zip    VARCHAR(20)  NOT NULL,
    order_status    ENUM('Pending','Processing','Dispatched','Delivered','Cancelled') DEFAULT 'Pending',
    order_date      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- -----------------------------------------------------------
-- 5. Order Items
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS order_items (
    item_id     INT AUTO_INCREMENT PRIMARY KEY,
    order_id    INT NOT NULL,
    weapon_id   INT NOT NULL,
    quantity    INT NOT NULL DEFAULT 1,
    unit_price  DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id)  REFERENCES orders(order_id)  ON DELETE CASCADE,
    FOREIGN KEY (weapon_id) REFERENCES weapons(weapon_id) ON DELETE CASCADE
) ENGINE=InnoDB;
