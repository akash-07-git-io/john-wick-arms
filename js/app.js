// ============================================================
// State Management & Core Application Logic
// ============================================================

let currentUser = null;
let cart = [];
let registeredEvents = [];
let activeCategory = 'all';
let currentlyViewedWeaponId = null;

document.addEventListener('DOMContentLoaded', () => {
  renderCatalogGrid(catalogData.slice(0, 4), 'home-featured-grid');
  renderCatalogGrid(catalogData, 'full-catalog-grid');
  renderEventsGrid(eventsData);
  updateCartUI();
});

// Single Page Navigation
function navigateTo(pageId) {
  document.querySelectorAll('.page-section').forEach(sec => sec.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));

  const targetSection = document.getElementById(`page-${pageId}`);
  if (targetSection) {
    targetSection.classList.add('active');
  }

  const activeNav = document.querySelector(`.nav-item[data-page="${pageId}"]`);
  if (activeNav) {
    activeNav.classList.add('active');
  }
  
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Filter Catalog by Category
function filterCatalog(category) {
  activeCategory = category;
  
  // Update button active styles
  document.querySelectorAll('.filter-bar .filter-btn').forEach(btn => btn.classList.remove('active'));
  if (category === 'all') {
    document.getElementById('filter-all')?.classList.add('active');
  } else if (category === 'Sidearms') {
    document.getElementById('filter-sidearms')?.classList.add('active');
  } else if (category === 'Shotguns') {
    document.getElementById('filter-shotguns')?.classList.add('active');
  } else if (category === 'Submachine Guns') {
    document.getElementById('filter-smg')?.classList.add('active');
  } else if (category === 'Rifles') {
    document.getElementById('filter-rifles')?.classList.add('active');
  }

  // Filter and re-render
  const filtered = category === 'all' 
    ? catalogData 
    : catalogData.filter(item => item.category === category);

  renderCatalogGrid(filtered, 'full-catalog-grid');
}

// Render Products with Both "View Details" & "Add to Cart" Actions
function renderCatalogGrid(data, containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = data.map(item => {
    const inCart = cart.some(cartItem => cartItem.id === item.id);
    return `
      <div class="product-card">
        <img src="${item.image}" alt="${item.name}" class="product-img" onclick="viewWeaponDetail('${item.id}')" style="cursor:pointer;" title="Click to view specifications">
        <div class="product-info">
          <div>
            <span class="product-tag">${item.category} | ${item.caliber || ''}</span>
            <h3 class="product-name" onclick="viewWeaponDetail('${item.id}')" style="cursor:pointer;">${item.name}</h3>
            <p class="product-desc">${item.description.substring(0, 110)}...</p>
          </div>
          <div>
            <div class="product-price">${item.priceDisplay}</div>
            <div style="display:flex; gap:0.5rem; margin-top:0.5rem;">
              <button class="btn-secondary" style="flex:1; padding:0.55rem 0.5rem; font-size:0.8rem;" onclick="viewWeaponDetail('${item.id}')">View Details</button>
              ${inCart 
                ? `<button class="btn-danger" style="flex:1; padding:0.55rem 0.5rem; font-size:0.8rem;" onclick="removeFromCart('${item.id}')">Remove</button>`
                : `<button class="btn-primary" style="flex:1; padding:0.55rem 0.5rem; font-size:0.8rem;" onclick="addToCart('${item.id}')">Add to Cart</button>`
              }
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// Weapon Specification & Detail View
function viewWeaponDetail(weaponId) {
  const weapon = catalogData.find(w => w.id === weaponId);
  if (!weapon) return;

  currentlyViewedWeaponId = weapon.id;

  // Populate view fields
  document.getElementById('detail-title').textContent = weapon.name.toUpperCase();
  document.getElementById('detail-subtitle').textContent = `Continental Sommelier Specification — ${weapon.category}`;
  document.getElementById('detail-img').src = weapon.image;
  document.getElementById('detail-tag').textContent = `${weapon.category} | ${weapon.caliber}`;
  document.getElementById('detail-name').textContent = weapon.name;
  document.getElementById('detail-price').textContent = weapon.priceDisplay;
  document.getElementById('detail-desc').textContent = weapon.description;

  // Specs
  document.getElementById('spec-caliber').textContent = weapon.caliber || 'N/A';
  document.getElementById('spec-capacity').textContent = weapon.capacity || 'N/A';
  document.getElementById('spec-barrel').textContent = weapon.barrelLength || 'N/A';
  document.getElementById('spec-range').textContent = weapon.effectiveRange || 'N/A';
  document.getElementById('spec-action').textContent = weapon.specs?.action || 'Semi-Automatic';
  document.getElementById('spec-sights').textContent = weapon.specs?.sights || 'Tactical Combat Optics';
  document.getElementById('spec-finish').textContent = weapon.specs?.finish || 'DLC Diamond-Like Carbon';
  document.getElementById('spec-weight').textContent = weapon.specs?.weight || '32 oz';

  document.getElementById('detail-qty').value = 1;

  navigateTo('weapon-detail');
}

// Add currently viewed weapon to cart with quantity
function addCurrentWeaponToCart() {
  if (!currentlyViewedWeaponId) return;
  const qty = parseInt(document.getElementById('detail-qty').value) || 1;
  const weapon = catalogData.find(w => w.id === currentlyViewedWeaponId);
  
  if (weapon) {
    for (let i = 0; i < qty; i++) {
      cart.push({ ...weapon, cartInstanceId: Math.random() });
    }
    updateCartUI();
    alert(`Added ${qty}x ${weapon.name} to your Requisition Cart!`);
    navigateTo('payment');
  }
}

// Render High Table Events
function renderEventsGrid(events) {
  const container = document.getElementById('events-grid');
  if (!container) return;

  container.innerHTML = events.map(evt => {
    const isRegistered = registeredEvents.includes(evt.title);
    return `
      <div class="product-card">
        <img src="${evt.image}" alt="${evt.title}" class="product-img">
        <div class="product-info">
          <div>
            <span class="product-tag">${evt.date} | ${evt.location}</span>
            <h3 class="product-name">${evt.title}</h3>
            <p class="product-desc">${evt.description}</p>
          </div>
          <div>
            ${isRegistered
              ? `<button class="btn-secondary" style="color:var(--success-green); border-color:var(--success-green);" disabled>&#10003; Reserved</button>`
              : `<button class="btn-primary" onclick="registerForEvent('${evt.title}')">Reserve Allocation</button>`
            }
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// Cart State Management
function addToCart(itemId) {
  const item = catalogData.find(prod => prod.id === itemId);
  if (item) {
    cart.push({ ...item, cartInstanceId: Math.random() });
    updateCartUI();
  }
}

function removeFromCart(itemId) {
  const idx = cart.findIndex(c => c.id === itemId);
  if (idx !== -1) {
    cart.splice(idx, 1);
  }
  updateCartUI();
}

function updateCartUI() {
  document.getElementById('cart-count').textContent = cart.length;
  
  // Re-render catalog grids
  renderCatalogGrid(catalogData.slice(0, 4), 'home-featured-grid');
  const filtered = activeCategory === 'all' 
    ? catalogData 
    : catalogData.filter(item => item.category === activeCategory);
  renderCatalogGrid(filtered, 'full-catalog-grid');
  
  // Render Cart inside Payment Page
  const cartListContainer = document.getElementById('cart-items-list');
  const totalPriceElem = document.getElementById('cart-total-price');
  
  let total = 0;
  cart.forEach(item => total += item.price);

  if (cart.length === 0) {
    cartListContainer.innerHTML = `<p style="color:var(--text-muted);">Your requisition cart is empty. Add tactical hardware from the Armory Catalog.</p>`;
    totalPriceElem.textContent = "$0";
  } else {
    // Group items by id
    const counts = {};
    cart.forEach(item => {
      counts[item.id] = (counts[item.id] || 0) + 1;
    });

    const uniqueItems = Array.from(new Set(cart.map(c => c.id))).map(id => {
      const item = catalogData.find(c => c.id === id);
      return { ...item, count: counts[id], subtotal: item.price * counts[id] };
    });

    cartListContainer.innerHTML = uniqueItems.map(item => {
      return `
        <div class="cart-item-row">
          <div>
            <div style="font-weight:600;">${item.name}</div>
            <div style="color:var(--accent-gold); font-size:0.85rem;">Qty: ${item.count} &times; ${item.priceDisplay} = $${item.subtotal.toLocaleString()}</div>
          </div>
          <button class="btn-danger" style="width:auto; padding:0.3rem 0.6rem; font-size:0.75rem;" onclick="removeFromCart('${item.id}')">Remove</button>
        </div>
      `;
    }).join('');
    totalPriceElem.textContent = `$${total.toLocaleString()}`;
  }

  // Update Continental Gold Coins requirement (1 coin = $1,000)
  const coinsNeeded = Math.ceil(total / 1000);
  const coinsElem = document.getElementById('gold-coins-needed');
  if (coinsElem) {
    coinsElem.textContent = total === 0 ? "0 Coins" : `${coinsNeeded} Gold Coin${coinsNeeded > 1 ? 's' : ''} ($${total.toLocaleString()})`;
  }
}

// 1-Click Test User Credentials Auto-Fill
function fillTestUser(role) {
  const emailInput = document.getElementById('login-email');
  const passInput  = document.getElementById('login-pass');

  if (role === 'wick') {
    emailInput.value = 'wick@continental.com';
    passInput.value  = 'continental123';
  } else if (role === 'admin') {
    emailInput.value = 'admin@continental.com';
    passInput.value  = 'admin123';
  }
}

// Multiple Payment Methods Tab Switching
function switchPaymentMethod(methodKey) {
  // Update tabs
  document.querySelectorAll('.payment-tab-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.payment-tab-pane').forEach(pane => pane.classList.remove('active'));

  document.getElementById(`tab-${methodKey}`)?.classList.add('active');
  document.getElementById(`pane-${methodKey}`)?.classList.add('active');
}

// Process Multi-channel Payment Requisition
function handlePaymentSubmit(event, methodName) {
  event.preventDefault();
  if (cart.length === 0) {
    alert('Your requisition cart is empty. Please select weapons from the Armory Catalog.');
    navigateTo('catalog');
    return;
  }

  const total = cart.reduce((sum, item) => sum + item.price, 0);
  const msgElem = document.getElementById('success-method-msg');
  if (msgElem) {
    msgElem.innerHTML = `Settlement authorized via <strong>${methodName}</strong> for a total ledger amount of <strong>$${total.toLocaleString()}</strong>. Your tactical hardware allocation is armed and sealed for safehouse delivery.`;
  }

  // Clear cart
  cart = [];
  updateCartUI();
  navigateTo('success');
}

function copyCryptoAddress() {
  navigator.clipboard.writeText('bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh').then(() => {
    alert('Multisig Escrow Wallet Address copied to clipboard!');
  });
}

// Register for Events Action
function registerForEvent(eventTitle) {
  if (!registeredEvents.includes(eventTitle)) {
    registeredEvents.push(eventTitle);
    renderEventsGrid(eventsData);
    if (currentUser) {
      currentUser.registeredEvents = registeredEvents;
    }
    updateUserUI();
    alert(`Successfully registered for: ${eventTitle}`);
  }
}

// User UI Updates
function updateUserUI() {
  if (currentUser) {
    document.getElementById('profile-display-name').textContent = currentUser.name;
    document.getElementById('profile-display-email').textContent = currentUser.email;
    if (document.getElementById('profile-display-tier')) {
      document.getElementById('profile-display-tier').textContent = currentUser.tier || 'Tier 2 — Sovereign Continental Diplomat';
    }
    if (document.getElementById('profile-display-marker')) {
      document.getElementById('profile-display-marker').textContent = currentUser.marker || 'BOM-7741-JW';
    }
    document.getElementById('profile-display-events').textContent = 
      registeredEvents.length > 0 ? registeredEvents.join(', ') : 'None';
      
    document.getElementById('nav-register').style.display = 'none';
    document.getElementById('nav-login').style.display = 'none';
    document.getElementById('nav-profile').style.display = 'inline-block';
  }
}

function handleLogout() {
  currentUser = null;
  registeredEvents = [];
  renderEventsGrid(eventsData);
  document.getElementById('nav-register').style.display = 'inline-block';
  document.getElementById('nav-login').style.display = 'inline-block';
  document.getElementById('nav-profile').style.display = 'none';
  navigateTo('home');
}
