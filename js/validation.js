// Registration Validation
function handleRegister(e) {
  e.preventDefault();
  let valid = true;
  
  const name = document.getElementById('reg-name').value.trim();
  const email = document.getElementById('reg-email').value.trim();
  const pass = document.getElementById('reg-password').value.trim();

  document.getElementById('err-reg-name').textContent = '';
  document.getElementById('err-reg-email').textContent = '';
  document.getElementById('err-reg-password').textContent = '';

  if (!name) {
    document.getElementById('err-reg-name').textContent = 'Operative name required.';
    valid = false;
  }
  if (!email || !/\S+@\S+\.\S+/.test(email)) {
    document.getElementById('err-reg-email').textContent = 'Valid email address required.';
    valid = false;
  }
  if (!pass || pass.length < 6) {
    document.getElementById('err-reg-password').textContent = 'Password must be at least 6 characters.';
    valid = false;
  }

  if (valid) {
    currentUser = { name, email, registeredEvents: registeredEvents };
    updateUserUI();
    navigateTo('profile');
  }
}

// Login Validation
function handleLogin(e) {
  e.preventDefault();
  let valid = true;

  const email = document.getElementById('login-email').value.trim();
  const pass = document.getElementById('login-password').value.trim();

  document.getElementById('err-login-email').textContent = '';
  document.getElementById('err-login-password').textContent = '';

  if (!email || !/\S+@\S+\.\S+/.test(email)) {
    document.getElementById('err-login-email').textContent = 'Enter a valid email.';
    valid = false;
  }
  if (!pass) {
    document.getElementById('err-login-password').textContent = 'Password required.';
    valid = false;
  }

  if (valid) {
    currentUser = { name: email.split('@')[0], email, registeredEvents: registeredEvents };
    updateUserUI();
    navigateTo('profile');
  }
}

// Credit Card Payment Validation
function handlePayment(e) {
  e.preventDefault();
  
  if (cart.length === 0) {
    alert("Your Requisition Cart is empty! Add items from the Armory Catalog first.");
    return;
  }

  let valid = true;
  const cardName = document.getElementById('card-name').value.trim();
  const cardNumber = document.getElementById('card-number').value.replace(/\s+/g, '');
  const cardExp = document.getElementById('card-exp').value.trim();
  const cardCvv = document.getElementById('card-cvv').value.trim();

  document.getElementById('err-card-name').textContent = '';
  document.getElementById('err-card-number').textContent = '';
  document.getElementById('err-card-exp').textContent = '';
  document.getElementById('err-card-cvv').textContent = '';

  if (!cardName) {
    document.getElementById('err-card-name').textContent = 'Cardholder name required.';
    valid = false;
  }
  if (!/^\d{16}$/.test(cardNumber)) {
    document.getElementById('err-card-number').textContent = 'Enter a valid 16-digit credit card number.';
    valid = false;
  }
  if (!/^(0[1-9]|1[0-2])\/\d{2}$/.test(cardExp)) {
    document.getElementById('err-card-exp').textContent = 'Expiry must match MM/YY format.';
    valid = false;
  }
  if (!/^\d{3,4}$/.test(cardCvv)) {
    document.getElementById('err-card-cvv').textContent = 'Valid 3 or 4 digit CVV required.';
    valid = false;
  }

  if (valid) {
    cart = [];
    updateCartUI();
    navigateTo('success');
  }
}