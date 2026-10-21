// ============================================================
// Input Validation & Client Security Form Handlers
// ============================================================

// Registration Validation with Weapon Clearance Details
function handleRegister(e) {
  e.preventDefault();
  let valid = true;
  
  const nameInput = document.getElementById('reg-name');
  const emailInput = document.getElementById('reg-email');
  const passInput = document.getElementById('reg-pass') || document.getElementById('reg-password');
  const tierInput = document.getElementById('reg-tier');
  const markerInput = document.getElementById('reg-marker');
  const dutyInput = document.getElementById('reg-duty');
  const phoneInput = document.getElementById('reg-phone');
  const addressInput = document.getElementById('reg-address');

  const name = nameInput ? nameInput.value.trim() : '';
  const email = emailInput ? emailInput.value.trim() : '';
  const pass = passInput ? passInput.value.trim() : '';
  const tier = tierInput ? tierInput.value : 'Tier 2 — Sovereign Continental Diplomat';
  const marker = markerInput ? markerInput.value.trim() : 'BOM-7741-JW';
  const duty = dutyInput ? dutyInput.value : 'New York Continental';
  const phone = phoneInput ? phoneInput.value.trim() : '';
  const address = addressInput ? addressInput.value.trim() : '';

  // Clear previous errors
  const errName = document.getElementById('err-reg-name');
  const errEmail = document.getElementById('err-reg-email');
  const errPass = document.getElementById('err-reg-pass') || document.getElementById('err-reg-password');

  if (errName) errName.textContent = '';
  if (errEmail) errEmail.textContent = '';
  if (errPass) errPass.textContent = '';

  if (!name) {
    if (errName) errName.textContent = 'Operative full name & alias required.';
    valid = false;
  }
  if (!email || !/\S+@\S+\.\S+/.test(email)) {
    if (errEmail) errEmail.textContent = 'Valid Continental email required.';
    valid = false;
  }
  if (!pass || pass.length < 6) {
    if (errPass) errPass.textContent = 'Password must be at least 6 characters.';
    valid = false;
  }

  if (valid) {
    currentUser = {
      name: name,
      email: email,
      tier: tier,
      marker: marker,
      duty: duty,
      phone: phone,
      address: address,
      registeredEvents: registeredEvents
    };
    updateUserUI();
    alert(`High Table Weapon Clearance Approved!\nWelcome, Operative ${name} (${tier}).`);
    navigateTo('profile');
  }
}

// Operative Login Validation
function handleLogin(e) {
  e.preventDefault();
  let valid = true;

  const emailInput = document.getElementById('login-email');
  const passInput  = document.getElementById('login-pass') || document.getElementById('login-password');

  const email = emailInput ? emailInput.value.trim() : '';
  const pass  = passInput ? passInput.value.trim() : '';

  const errEmail = document.getElementById('err-login-email');
  const errPass  = document.getElementById('err-login-pass') || document.getElementById('err-login-password');

  if (errEmail) errEmail.textContent = '';
  if (errPass) errPass.textContent = '';

  if (!email || !/\S+@\S+\.\S+/.test(email)) {
    if (errEmail) errEmail.textContent = 'Enter a valid secure email.';
    valid = false;
  }
  if (!pass) {
    if (errPass) errPass.textContent = 'Security clearance password required.';
    valid = false;
  }

  if (valid) {
    const isWick = email.toLowerCase().includes('wick');
    currentUser = {
      name: isWick ? 'John Wick (Baba Yaga)' : (email.split('@')[0].toUpperCase()),
      email: email,
      tier: isWick ? 'Tier 3 — High Table Inner Circle' : 'Tier 2 — Sovereign Continental Diplomat',
      marker: isWick ? 'BOM-0001-WICK' : 'BOM-8832-OP',
      registeredEvents: registeredEvents
    };
    updateUserUI();
    navigateTo('profile');
  }
}

// Card Form Handler
function handlePayment(e) {
  handlePaymentSubmit(e, 'High Table Encrypted Card');
}
