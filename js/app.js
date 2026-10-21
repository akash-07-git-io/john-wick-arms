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
  let weapon = catalogData.find(w => w.id === weaponId);
  if (!weapon) {
    weapon = catalogData.find(w => w.id.includes(weaponId) || w.name.toLowerCase().includes(String(weaponId).toLowerCase())) || catalogData[0];
  }
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
  
  // Render Cart inside Payment Page & Dedicated Cart Page
  const cartListContainer = document.getElementById('cart-items-list');
  const totalPriceElem = document.getElementById('cart-total-price');
  const dedicatedCartList = document.getElementById('dedicated-cart-items-list');
  const dedicatedTotalPrice = document.getElementById('dedicated-cart-total-price');
  
  let total = 0;
  cart.forEach(item => total += item.price);

  if (cart.length === 0) {
    if (cartListContainer) {
      cartListContainer.innerHTML = `<p style="color:var(--text-muted);">Your requisition cart is empty. Add tactical hardware from the Armory Catalog.</p>`;
    }
    if (totalPriceElem) totalPriceElem.textContent = "$0";
    if (dedicatedCartList) {
      dedicatedCartList.innerHTML = `<p style="color:var(--text-muted); padding:2rem 0; text-align:center;">Your requisition cart is empty. Visit the <a href="javascript:void(0)" onclick="navigateTo('catalog')" style="color:var(--accent-gold); text-decoration:none;">Armory Catalog</a> to add weapons.</p>`;
    }
    if (dedicatedTotalPrice) dedicatedTotalPrice.textContent = "$0";
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

    const itemsHtml = uniqueItems.map(item => {
      return `
        <div class="cart-item-row" style="display:flex; justify-content:space-between; align-items:center; padding:1rem 0; border-bottom:1px solid var(--gunmetal-border);">
          <div style="display:flex; align-items:center; gap:1.2rem;">
            <img src="${item.image}" alt="${item.name}" style="width:70px; height:50px; object-fit:contain; background:#0d0e14; border:1px solid var(--gunmetal-border); border-radius:4px; padding:2px;">
            <div>
              <div style="font-weight:600; font-size:1rem;">${item.name}</div>
              <div style="color:var(--text-muted); font-size:0.8rem;">${item.category} &bull; ${item.caliber || ''}</div>
              <div style="color:var(--accent-gold); font-size:0.9rem; margin-top:2px;">Qty: ${item.count} &times; ${item.priceDisplay} = <strong>$${item.subtotal.toLocaleString()}</strong></div>
            </div>
          </div>
          <button class="btn-danger" style="width:auto; padding:0.4rem 0.8rem; font-size:0.8rem;" onclick="removeFromCart('${item.id}')">Remove</button>
        </div>
      `;
    }).join('');

    if (cartListContainer) cartListContainer.innerHTML = itemsHtml;
    if (totalPriceElem) totalPriceElem.textContent = `$${total.toLocaleString()}`;
    if (dedicatedCartList) dedicatedCartList.innerHTML = itemsHtml;
    if (dedicatedTotalPrice) dedicatedTotalPrice.textContent = `$${total.toLocaleString()}`;
  }

  // Update Continental Gold Coins requirement (1 coin = $1,000)
  const coinsNeeded = Math.ceil(total / 1000);
  const coinsElem = document.getElementById('gold-coins-needed');
  if (coinsElem) {
    coinsElem.textContent = total === 0 ? "0 Coins" : `${coinsNeeded} Gold Coin${coinsNeeded > 1 ? 's' : ''} ($${total.toLocaleString()})`;
  }
}

function clearCart() {
  cart = [];
  updateCartUI();
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

// Deep linking & URL Hash Support for Academic Demo & Direct Navigation
function handleUrlHash() {
  const raw = window.location.hash.replace(/^#\/?/, '').replace('page-', '');
  if (!raw) return;

  const parts = raw.split('?');
  const pageId = parts[0];
  const queryParams = new URLSearchParams(parts[1] || '');

  if (pageId === 'weapon-detail') {
    const weaponId = queryParams.get('id') || 'jw-01';
    viewWeaponDetail(weaponId);
  } else if (pageId === 'cart') {
    if (cart.length === 0) {
      addToCart('jw-01');
      addToCart('jw-07');
      addToCart('jw-11');
    }
    navigateTo('cart');
  } else if (pageId === 'payment') {
    if (cart.length === 0) {
      addToCart('jw-01');
      addToCart('jw-02');
    }
    navigateTo('payment');
  } else if (pageId === 'login') {
    fillTestUser('wick');
    navigateTo('login');
  } else if (pageId === 'profile') {
    currentUser = {
      name: 'John Wick',
      email: 'wick@continental.nyc',
      tier: 'Level 5 — Baba Yaga Sovereign Diplomat',
      marker: 'BOM-7741-JW'
    };
    updateUserUI();
    navigateTo('profile');
  } else if (pageId === 'register') {
    navigateTo('register');
  } else if (pageId === 'catalog') {
    navigateTo('catalog');
  } else if (pageId === 'success') {
    navigateTo('success');
  } else if (pageId === 'home') {
    navigateTo('home');
  } else {
    navigateTo(pageId);
  }
}

window.addEventListener('hashchange', handleUrlHash);
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(handleUrlHash, 100);
});
