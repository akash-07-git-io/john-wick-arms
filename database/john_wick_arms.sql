-- ============================================================
-- John Wick & Co. Arms - Weapon Management & Ordering System
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

-- Default admin credentials (username: admin | password: admin123)
INSERT INTO admin_users (username, password, full_name)
VALUES ('admin', 'admin123', 'The Continental Manager')
ON DUPLICATE KEY UPDATE full_name=VALUES(full_name);

-- -----------------------------------------------------------
-- 2. Customers (Operatives)
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id     INT AUTO_INCREMENT PRIMARY KEY,
    full_name       VARCHAR(100) NOT NULL,
    email           VARCHAR(100) NOT NULL UNIQUE,
    password        VARCHAR(255) NOT NULL,
    clearance_tier  VARCHAR(50)  DEFAULT 'Tier 2 — Sovereign Continental Diplomat',
    marker_code     VARCHAR(50)  DEFAULT 'BOM-7741-JW',
    duty_station    VARCHAR(100) DEFAULT 'New York Continental',
    phone           VARCHAR(30)  DEFAULT NULL,
    address         TEXT         DEFAULT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Default Demo Operative Customer (John Wick)
INSERT INTO customers (full_name, email, password, clearance_tier, marker_code, duty_station, phone, address)
VALUES ('John Wick', 'wick@continental.com', '$2y$10$w0f5u4nI3ZJbVz.V3uR8b.rT8f0v4Q5x6Y7Z8A9B0C1D2E3F4G5H6', 'Tier 3 — High Table Inner Circle', 'BOM-0001-WICK', 'New York Continental', '+1-555-0144', '1 Wall Street Court, Continental Safehouse Suite 812')
ON DUPLICATE KEY UPDATE full_name=VALUES(full_name);

-- -----------------------------------------------------------
-- 3. Weapons (18 Authentic John Wick Tactical Arsenal)
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS weapons (
    weapon_id       INT AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(150) NOT NULL,
    category        VARCHAR(50)  NOT NULL,
    price           DECIMAL(10,2) NOT NULL,
    caliber         VARCHAR(50)  DEFAULT NULL,
    capacity        VARCHAR(50)  DEFAULT NULL,
    description     TEXT,
    image           VARCHAR(500) DEFAULT 'images/pit_viper.jpg',
    status          ENUM('available','out_of_stock') DEFAULT 'available',
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Clean existing seed data and re-insert 18 authentic weapons
TRUNCATE TABLE weapons;

INSERT INTO weapons (weapon_id, name, category, price, caliber, capacity, description, image, status) VALUES
(1,  'TTI JW4 Pit Viper 9mm',             'Sidearms',        7500.00, '9x19mm Major',         '21+1 Rounds',  'Single-port compensator, extreme-engineering lite-speed fire control, titanium-nitride fangs, and DLC finish.', 'images/pit_viper.jpg', 'available'),
(2,  'TTI Combat Master Glock 34',        'Sidearms',        6800.00, '9x19mm Parabellum',    '22+1 Rounds',  'Hand-stippled grip, flared competition magwell, lightened slide serrations, and bronze match barrel.',           'images/combat_master_jw2.jpg', 'available'),
(3,  'TTI STI 2011 Combat Master',        'Sidearms',        7200.00, '9mm Major',            '22+1 Rounds',  'STI double-stack 2011 frame, match bull barrel, oversized magazine release, and ambidextrous safety.',          'images/sti_2011_jw3.jpg', 'available'),
(4,  'Heckler & Koch P30L Compensated',   'Sidearms',        3800.00, '9x19mm NATO',          '15+1 Rounds',  'Custom aluminum counterweight compensator, ambidextrous controls, and cold hammer-forged polygonal rifling.',    'images/hk_p30l.jpg', 'available'),
(5,  'Kimber 1911 Warrior .45 ACP',       'Sidearms',        4200.00, '.45 ACP',              '7+1 Rounds',   'Desert tan KimPro finish, G10 tactical grips, Novak night sights, and 7-round single stack capacity.',           'images/kimber_1911.jpg', 'available'),
(6,  'Glock 26 Combat Master Backup',     'Sidearms',        2900.00, '9x19mm Parabellum',    '12+1 Rounds',  'Concealed ankle backup sidearm with tungsten guide rod, undercut trigger guard, and match trigger.',             'images/glock26.jpg', 'available'),

(7,  'Benelli M4 Tactical Ported',        'Shotguns',        5400.00, '12-Gauge Magnum',      '8+1 Shells',   'Auto-regulating gas-operated (ARGO) system with custom barrel porting, textured grip, and match loading port.',  'images/benelli_m4.jpg', 'available'),
(8,  'Genesis Arms Gen-12 Dragon\'s Breath','Shotguns',      6900.00, '12-Ga Incendiary',     '10-Round Mag', 'Short-barrel semi-auto AR-10 platform firing magnesium Dragon\'s Breath incendiary slugs.',                    'images/gen12_dragons_breath.jpg', 'available'),
(9,  'Remington 870 Tactical Breacher',   'Shotguns',        3200.00, '12-Gauge Tactical',    '6+1 Shells',   'Stand-off spiked door-breaching muzzle brake, twin action pump bars, and Magpul SGA tactical furniture.',       'images/remington870.jpg', 'available'),
(10, 'Kel-Tec KSG Bullpup 12-Gauge',      'Shotguns',        3600.00, '12-Ga Dual-Tube',      '14+1 Shells',  'Dual magazine tubes allowing instant switching between slugs and buckshot with a 15-round capacity.',            'images/keltec_ksg.jpg', 'available'),

(11, 'SIG MPX TTI Suppressed Spec',       'Submachine Guns', 5800.00, '9x19mm Subsonic',      '35-Round Mag', 'Closed-bolt short-stroke gas piston platform with integral suppressor optimized for subsonic CQB.',               'images/sig_mpx.jpg', 'available'),
(12, 'Heckler & Koch MP5K-PDW',           'Submachine Guns', 6200.00, '9x19mm NATO',          '30-Round Mag', 'Roller-delayed blowback system with side-folding stock, vertical foregrip, and threaded tri-lug muzzle.',      'images/hk_mp5k.jpg', 'available'),
(13, 'B&T APC9 PRO-K Tactical',           'Submachine Guns', 5100.00, '9x19mm Parabellum',    '30-Round Mag', 'Swiss hydraulic buffer system eliminating felt recoil with non-reciprocating ambidextrous charging handle.',     'images/bt_apc9.jpg', 'available'),
(14, 'CZ Scorpion EVO 3 S1 Tactical',     'Submachine Guns', 4500.00, '9x19mm Suppressed',    '30-Round Mag', 'Reinforced polymer submachine gun with low-profile aperture sights and custom tactical flash can.',             'images/cz_scorpion.jpg', 'available'),

(15, 'TTI TR-1 Ultralight AR-15',         'Rifles',          8900.00, '5.56x45mm NATO',       '30-Round PMAG','Trijicon AccuPoint 1-6x scope, canted 45-degree RMR, Hiperfire 24C match trigger, and BCM furniture.',         'images/tti_tr1.jpg', 'available'),
(16, 'Desert Tech SRS-A1 Precision',      'Rifles',          9500.00, '7.62x51mm / .308 Win', '10-Round Mag', 'Bullpup bolt-action precision rifle with monolithic receiver and quick caliber conversion system.',           'images/desert_tech_srs.jpg', 'available'),
(17, 'SIG Sauer MCX Virtus Patrol',       'Rifles',          7800.00, '5.56x45mm NATO',       '30-Round PMAG','Short-stroke gas piston system with Match Duo two-stage trigger and folding skeleton stock.',                    'images/sig_mcx.jpg', 'available'),
(18, 'CheyTac M200 Intervention .408',    'Rifles',         14500.00, '.408 CheyTac',         '7-Round Mag',  'Extreme long-range anti-materiel precision sniper platform delivering sub-MOA accuracy beyond 2,000 meters.',    'images/cheytac_m200.jpg', 'available');

-- -----------------------------------------------------------
-- 4. Orders
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS orders (
    order_id        INT AUTO_INCREMENT PRIMARY KEY,
    customer_id     INT NOT NULL,
    total_amount    DECIMAL(10,2) NOT NULL,
    payment_method  VARCHAR(100) DEFAULT 'Continental Gold Coins',
    delivery_name   VARCHAR(100) NOT NULL,
    delivery_phone  VARCHAR(30)  NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_city   VARCHAR(100) NOT NULL,
    delivery_zip    VARCHAR(30)  NOT NULL,
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
