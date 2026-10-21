# John Wick Arms – Weapon Management and Ordering System

The **John Wick Arms – Weapon Management and Ordering System** is a full-featured web-based application developed using **HTML, CSS, PHP, and MySQL**. Inspired by the high-precision world of the Continental and High Table Armory, it allows authorized customers (operatives) to browse different varieties of tactical weapons and gear, view detailed specifications and prices, add items to a shopping cart, and place orders by providing their delivery and contact information. 

The system provides a robust **Admin Module** allowing the armory manager to manage weapon inventories (adding, viewing, updating, and deleting weapon items) and oversee customer orders (viewing detailed orders and updating order fulfillment statuses in real-time). MySQL is utilized for structured relational data storage, while PHP powers backend business logic, session-based cart operations, authentication, and secure CRUD operations.

---

## 🛠️ Technology Stack
- **Frontend**: HTML5, CSS3 (Custom Dark & Gold Continental Luxury Theme), JavaScript
- **Backend**: PHP 7.4 / 8.x (Session management, prepared statements, CRUD)
- **Database**: MySQL / MariaDB (Relational schema with foreign keys)
- **Deployment Ready**: Docker, Docker Compose, Render Blueprint, Vercel

---

## 📁 System Architecture & File Structure
```text
john-wick-arms/
├── admin/                     # Admin Management Module
│   ├── add_weapon.php         # Admin: Create weapon product
│   ├── admin_footer.php       # Admin footer layout
│   ├── admin_header.php       # Admin navigation & session verification
│   ├── dashboard.php          # Admin dashboard with key metrics & recent orders
│   ├── edit_weapon.php        # Admin: Update weapon specs, price, status
│   ├── index.php              # Admin login page
│   ├── logout.php             # Admin session logout
│   ├── orders.php             # Admin: View all orders with status filtering
│   ├── order_detail.php       # Admin: Order line items & status updating
│   └── weapons.php            # Admin: Inventory table with CRUD actions
├── css/
│   └── styles.css             # Theme stylesheet
├── database/
│   └── john_wick_arms.sql     # Complete MySQL Database Schema & Seed Data
├── includes/
│   ├── header.php             # Customer navigation bar & session cart counter
│   └── footer.php             # Global footer
├── js/
│   ├── app.js                 # Interactive client scripts
│   ├── catalog-data.js        # Tactical inventory data
│   └── validation.js          # Client-side input validation
├── cart.php                   # Shopping Cart page
├── cart_action.php            # Cart session handler (Add/Update/Remove/Clear)
├── catalog.php                # Weapon Catalog page with category filtering
├── checkout.php               # Customer Checkout & Delivery Details form
├── db_connect.php             # MySQL Database connection configuration
├── index.html                 # Interactive Web UI (Single-Page static version)
├── index.php                  # Customer Home Page (Featured weapons)
├── login.php                  # Customer authentication
├── logout.php                 # Customer logout
├── my_orders.php              # Customer order history & real-time tracking
├── order_success.php          # Order confirmation screen
├── weapon_detail.php          # Weapon specifications & Add to Cart
├── Dockerfile                 # Containerized PHP 8.2 + Apache deployment
├── docker-compose.yml         # 1-click local Docker stack (App + MySQL)
├── render.yaml                # Render Cloud Blueprint deployment
├── vercel.json                # Vercel deployment configuration
└── README.md                  # Project documentation
```

---

## ⚙️ Local Setup Instructions (XAMPP / Wamp)

1. **Move files into web root**:
   Place the `john-wick-arms` directory inside your web root:
   - XAMPP: `C:/xampp/htdocs/john-wick-arms/`
   - WAMP: `C:/wamp64/www/john-wick-arms/`

2. **Start Services**:
   Launch your XAMPP/WAMP control panel and start **Apache** and **MySQL**.

3. **Import Database**:
   - Open browser and navigate to `http://localhost/phpmyadmin/`.
   - Click **New** and create a database named `john_wick_arms`.
   - Select the database, click the **Import** tab, choose `database/john_wick_arms.sql`, and click **Go**.

4. **Launch Application**:
   - **Customer Portal**: `http://localhost/john-wick-arms/index.php`
   - **Admin Portal**: `http://localhost/john-wick-arms/admin/index.php`
     - **Admin Username**: `admin`
     - **Admin Password**: `admin123`

---

## 🚀 Live Cloud Deployment

### Option A: Render (Docker Full Stack)
1. Push this repository to your GitHub account:
   ```bash
   git add .
   git commit -m "Initial commit of John Wick Arms"
   git remote add origin https://github.com/<your-username>/john-wick-arms.git
   git push -u origin main
   ```
2. Log into [Render.com](https://render.com) and click **New + > Web Service**.
3. Connect your GitHub repository.
4. Render will automatically detect the `Dockerfile` and configure port `80`.
5. Link a free MySQL database (e.g. from Aiven, Clever Cloud, or Render) and set environment variables `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`.

### Option B: Vercel (Interactive Static Showcase)
1. Run `vercel` or link repository in the Vercel Dashboard.
2. The `vercel.json` serves the interactive frontend with zero configuration.

---

## 📋 Academic Demonstration Scope
This project is an academic simulation designed for educational purposes in Web Programming (HTML, CSS, PHP, MySQL). No real-world armament transactions or procurement take place.
