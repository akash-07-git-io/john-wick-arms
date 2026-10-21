// State Management
let currentUser = null;
let cart = [];
let registeredEvents = [];

document.addEventListener('DOMContentLoaded', () => {
  renderCatalogGrid(catalogData, 'home-featured-grid');
  renderCatalogGrid(catalogData, 'full-catalog-grid');
  renderEventsGrid(eventsData);
  updateCartUI();
});

// Single Page Navigation
function navigateTo(pageId) {
  document.querySelectorAll('.page-section').forEach(sec => sec.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));

  document.getElementById(`page-${pageId}`).classList.add('active');
  const activeNav = document.querySelector(`.nav-item[data-page="${pageId}"]`);
  if (activeNav) activeNav.classList.add('active');
  
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Render Products with Dynamic Add/Remove Cart Action
function renderCatalogGrid(data, containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = data.map(item => {
    const inCart = cart.some(cartItem => cartItem.id === item.id);
    return `
      <div class="product-card">
        <img src="${item.image}" alt="${item.name}" class="product-img">
        <div class="product-info">
          <div>
            <span class="product-tag">${item.category}</span>
            <h3 class="product-name">${item.name}</h3>
            <p class="product-desc">${item.description}</p>
          </div>
          <div>
            <div class="product-price">${item.priceDisplay}</div>
            ${inCart 
              ? `<button class="btn-danger" onclick="removeFromCart('${item.id}')">Remove from Cart</button>`
              : `<button class="btn-primary" onclick="addToCart('${item.id}')">Add to Cart</button>`
            }
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// Render High Table Events with Register Action
function renderEventsGrid(events) {
  const container = document.getElementById('events-grid');
  container.innerHTML = events.map(evt => {
    const isRegistered = registeredEvents.includes(evt.title);
    return `
      <div class="product-card">
        <img src="${evt.image}" alt="${evt.title}" class="product-img">
        <div class="product-info">
          <div>
            <span class="product-tag">📅 ${evt.date} | ${evt.location}</span>
            <h3 class="product-name">${evt.title}</h3>
            <p class="product-desc">${evt.description}</p>
          </div>
          <div>
            ${isRegistered
              ? `<button class="btn-secondary" style="color:var(--success-green); border-color:var(--success-green);" disabled>✓ Registered</button>`
              : `<button class="btn-primary" onclick="registerForEvent('${evt.title}')">Register for Event</button>`
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
  if (item && !cart.some(c => c.id === itemId)) {
    cart.push(item);
    updateCartUI();
  }
}

function removeFromCart(itemId) {
  cart = cart.filter(c => c.id !== itemId);
  updateCartUI();
}

function updateCartUI() {
  document.getElementById('cart-count').textContent = cart.length;
  renderCatalogGrid(catalogData, 'home-featured-grid');
  renderCatalogGrid(catalogData, 'full-catalog-grid');
  
  // Render Cart inside Payment Page
  const cartListContainer = document.getElementById('cart-items-list');
  const totalPriceElem = document.getElementById('cart-total-price');
  
  if (cart.length === 0) {
    cartListContainer.innerHTML = `<p style="color:var(--text-muted);">Your requisition cart is empty.</p>`;
    totalPriceElem.textContent = "$0";
  } else {
    let total = 0;
    cartListContainer.innerHTML = cart.map(item => {
      total += item.price;
      return `
        <div class="cart-item-row">
          <div>
            <div style="font-weight:600;">${item.name}</div>
            <div style="color:var(--accent-gold); font-size:0.85rem;">${item.priceDisplay}</div>
          </div>
          <button class="btn-danger" style="width:auto; padding:0.3rem 0.6rem; font-size:0.75rem;" onclick="removeFromCart('${item.id}')">Remove</button>
        </div>
      `;
    }).join('');
    totalPriceElem.textContent = `$${total.toLocaleString()}`;
  }
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