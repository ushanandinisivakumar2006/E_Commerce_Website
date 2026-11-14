/**
 * ZenithMart E-Commerce Application Logic
 * Implemented for Software Testing Portfolio Project
 */

// --- Sample Product Catalog (SVG Data URIs for offline independence) ---
function createProductSVG(bg, icon, text) {
  return `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><rect width="100%" height="100%" fill="${bg}"/><text x="50%" y="45%" font-size="64" text-anchor="middle" dominant-baseline="middle">${icon}</text><text x="50%" y="75%" font-family="sans-serif" font-size="16" font-weight="bold" fill="%231e293b" text-anchor="middle">${encodeURIComponent(text)}</text></svg>`;
}

const PRODUCTS_DATA = [
  {
    id: 1,
    title: "Quantum Pro Wireless Headphones",
    category: "Electronics",
    price: 199.99,
    rating: 4.8,
    reviews: 142,
    stock: 25,
    description: "Industry-leading noise canceling over-ear wireless headphones with 40-hour battery life, high-res audio drivers, and ultra-comfortable memory foam ear cushions.",
    image: "images/headphones.svg"
  },
  {
    id: 2,
    title: "UltraBook Pro 15.6-inch Laptop",
    category: "Electronics",
    price: 1099.99,
    rating: 4.9,
    reviews: 89,
    stock: 12,
    description: "Sleek aluminum chassis laptop powered by a 12-core processor, 16GB RAM, 512GB NVMe SSD, and a stunning 4K OLED display for professionals and creators.",
    image: "images/laptop.svg"
  },
  {
    id: 3,
    title: "SmartFit Fitness Smartwatch",
    category: "Electronics",
    price: 149.50,
    rating: 4.4,
    reviews: 215,
    stock: 30,
    description: "Waterproof smartwatch equipped with continuous heart-rate tracking, SpO2 sensor, sleep staging, built-in GPS, and 7-day battery life.",
    image: "images/smartwatch.svg"
  },
  {
    id: 4,
    title: "4K Action Sports Camera",
    category: "Electronics",
    price: 249.00,
    rating: 4.6,
    reviews: 78,
    stock: 18,
    description: "Ultra HD 4K/60fps waterproof action camera with HyperSmooth video stabilization, dual touchscreen displays, and voice command support.",
    image: "images/camera.svg"
  },
  {
    id: 5,
    title: "Classic Cotton Crewneck T-Shirt",
    category: "Apparel",
    price: 24.99,
    rating: 4.3,
    reviews: 310,
    stock: 80,
    description: "100% premium combed organic cotton crewneck tee. Pre-shrunk, breathable, ultra-soft hand feel, ideal for everyday casual wear.",
    image: "images/tshirt.svg"
  },
  {
    id: 6,
    title: "Slim-Fit Stretch Denim Jeans",
    category: "Apparel",
    price: 59.95,
    rating: 4.5,
    reviews: 164,
    stock: 45,
    description: "Tailored slim-fit denim jeans crafted with 2% elastane for maximum comfort and flexibility. Classic five-pocket styling and antique brass hardware.",
    image: "images/jeans.svg"
  },
  {
    id: 7,
    title: "All-Weather Polar Fleece Jacket",
    category: "Apparel",
    price: 89.99,
    rating: 4.7,
    reviews: 95,
    stock: 22,
    description: "Thermal insulated full-zip fleece jacket with wind-resistant collar, zippered chest pocket, and elasticized cuffs for cold weather outdoor adventures.",
    image: "images/jacket.svg"
  },
  {
    id: 8,
    title: "Clean Code & Software Architecture",
    category: "Books",
    price: 39.99,
    rating: 4.9,
    reviews: 520,
    stock: 50,
    description: "A handbook of agile software craftsmanship. Master design patterns, unit testing, refactoring, and clean architecture principles for modern development.",
    image: "images/clean_code.svg"
  },
  {
    id: 9,
    title: "Hands-On Test Automation with Selenium",
    category: "Books",
    price: 44.50,
    rating: 4.8,
    reviews: 180,
    stock: 35,
    description: "Practical guide covering Page Object Model, test reporting, continuous integration, and best practices for automated web application testing.",
    image: "images/selenium_book.svg"
  },
  {
    id: 10,
    title: "Precision Espresso Coffee Machine",
    category: "Home & Kitchen",
    price: 299.99,
    rating: 4.7,
    reviews: 112,
    stock: 14,
    description: "15-bar Italian pump stainless steel espresso maker with commercial steam wand for barista-style silky microfoam lattes and cappuccinos.",
    image: "images/coffee_maker.svg"
  },
  {
    id: 11,
    title: "Smart Air Purifier with HEPA Filter",
    category: "Home & Kitchen",
    price: 129.99,
    rating: 4.5,
    reviews: 84,
    stock: 20,
    description: "H13 True HEPA filter capturing 99.97% of airborne allergens, pollen, dust, and smoke. Whisper-quiet night mode and real-time PM2.5 display.",
    image: "images/air_purifier.svg"
  },
  {
    id: 12,
    title: "Cast Iron Dutch Oven 6-Quart",
    category: "Home & Kitchen",
    price: 69.95,
    rating: 4.8,
    reviews: 204,
    stock: 28,
    description: "Enameled cast iron Dutch oven with tight-fitting lid and heat-resistant stainless steel knob. Superior heat retention for baking, braising, and stews.",
    image: "images/dutch_oven.svg"
  }
];

// --- State Management ---
const AppState = {
  products: [...PRODUCTS_DATA],
  filteredProducts: [...PRODUCTS_DATA],
  cart: [],
  currentUser: null,
  activeFilter: {
    category: "all",
    maxPrice: 1500,
    searchQuery: "",
    sortBy: "featured"
  },
  // Registered mock users database
  users: [
    { name: "Test User", email: "testuser@example.com", password: "Password123!" }
  ]
};

// --- DOM Elements ---
const DOM = {
  productsGrid: document.getElementById("products-grid"),
  productsCountMsg: document.getElementById("products-count-msg"),
  noProductsMsg: document.getElementById("no-products-msg"),
  searchInput: document.getElementById("search-input"),
  searchBtn: document.getElementById("search-btn"),
  clearSearchBtn: document.getElementById("clear-search-btn"),
  clearSearchEmptyBtn: document.getElementById("clear-search-empty-btn"),
  priceRange: document.getElementById("price-range"),
  priceDisplay: document.getElementById("price-display"),
  resetFiltersBtn: document.getElementById("reset-filters-btn"),
  sortSelect: document.getElementById("sort-select"),
  categoryRadios: document.querySelectorAll('input[name="category"]'),
  
  // Auth Elements
  authGuest: document.getElementById("auth-guest"),
  authUser: document.getElementById("auth-user"),
  userGreeting: document.getElementById("user-greeting"),
  userAvatar: document.getElementById("user-avatar"),
  navLoginBtn: document.getElementById("nav-login-btn"),
  navRegisterBtn: document.getElementById("nav-register-btn"),
  navLogoutBtn: document.getElementById("nav-logout-btn"),
  
  // Login Modal
  loginModal: document.getElementById("login-modal"),
  closeLoginModalBtn: document.getElementById("close-login-modal-btn"),
  loginForm: document.getElementById("login-form"),
  loginEmail: document.getElementById("login-email"),
  loginPassword: document.getElementById("login-password"),
  loginEmailError: document.getElementById("login-email-error"),
  loginPasswordError: document.getElementById("login-password-error"),
  loginAlert: document.getElementById("login-alert"),
  switchToRegisterBtn: document.getElementById("switchToRegisterBtn") || document.getElementById("switch-to-register-btn"),
  
  // Register Modal
  registerModal: document.getElementById("register-modal"),
  closeRegisterModalBtn: document.getElementById("close-register-modal-btn"),
  registerForm: document.getElementById("register-form"),
  regName: document.getElementById("reg-name"),
  regEmail: document.getElementById("reg-email"),
  regPassword: document.getElementById("reg-password"),
  regConfirmPassword: document.getElementById("reg-confirm-password"),
  regNameError: document.getElementById("reg-name-error"),
  regEmailError: document.getElementById("reg-email-error"),
  regPasswordError: document.getElementById("reg-password-error"),
  regConfirmPasswordError: document.getElementById("reg-confirm-password-error"),
  registerAlert: document.getElementById("register-alert"),
  switchToLoginBtn: document.getElementById("switchToLoginBtn") || document.getElementById("switch-to-login-btn"),
  
  // Product Detail Modal
  productDetailModal: document.getElementById("product-detail-modal"),
  closeDetailModalBtn: document.getElementById("close-detail-modal-btn"),
  detailModalBody: document.getElementById("detail-modal-body"),
  
  // Cart Drawer
  cartToggleBtn: document.getElementById("cart-toggle-btn"),
  cartBadge: document.getElementById("cart-badge"),
  cartDrawer: document.getElementById("cart-drawer"),
  closeCartBtn: document.getElementById("close-cart-btn"),
  cartDrawerCount: document.getElementById("cart-drawer-count"),
  cartItemsContainer: document.getElementById("cart-items-container"),
  cartSubtotal: document.getElementById("cart-subtotal"),
  cartTax: document.getElementById("cart-tax"),
  cartTotal: document.getElementById("cart-total"),
  clearCartBtn: document.getElementById("clear-cart-btn"),
  proceedCheckoutBtn: document.getElementById("proceed-checkout-btn"),
  
  // Checkout Modal
  checkoutModal: document.getElementById("checkout-modal"),
  closeCheckoutModalBtn: document.getElementById("close-checkout-modal-btn"),
  checkoutForm: document.getElementById("checkout-form"),
  checkoutAlert: document.getElementById("checkout-alert"),
  chkName: document.getElementById("chk-name"),
  chkEmail: document.getElementById("chk-email"),
  chkAddress: document.getElementById("chk-address"),
  chkCity: document.getElementById("chk-city"),
  chkState: document.getElementById("chk-state"),
  chkZip: document.getElementById("chk-zip"),
  chkCardNumber: document.getElementById("chk-card-number"),
  chkCardExp: document.getElementById("chk-card-exp"),
  chkCardCvv: document.getElementById("chk-card-cvv"),
  chkTotalPayable: document.getElementById("chk-total-payable"),
  cardFieldsGroup: document.getElementById("card-fields-group"),
  paymentMethodRadios: document.querySelectorAll('input[name="payment-method"]'),
  
  // Order Confirmation Modal
  confirmationModal: document.getElementById("confirmation-modal"),
  confOrderId: document.getElementById("conf-order-id"),
  confName: document.getElementById("conf-name"),
  confEmail: document.getElementById("conf-email"),
  confAddress: document.getElementById("conf-address"),
  confPayment: document.getElementById("conf-payment"),
  confItemsList: document.getElementById("conf-items-list"),
  confTotal: document.getElementById("conf-total"),
  confContinueShoppingBtn: document.getElementById("conf-continue-shopping-btn"),
  
  // Toast
  toastContainer: document.getElementById("toast-container")
};

// --- Initialize Application ---
function initApp() {
  loadStoredData();
  renderProducts();
  updateCartBadge();
  setupEventListeners();
  checkSession();
}

// --- Persistence Helpers ---
function loadStoredData() {
  const storedUsers = localStorage.getItem("zenith_users");
  if (storedUsers) {
    try {
      AppState.users = JSON.parse(storedUsers);
    } catch (e) {
      console.warn("Could not parse stored users", e);
    }
  }

  const storedCart = localStorage.getItem("zenith_cart");
  if (storedCart) {
    try {
      AppState.cart = JSON.parse(storedCart);
      // Sync stored cart image paths with current product images
      AppState.cart.forEach(item => {
        const p = PRODUCTS_DATA.find(prod => prod.id === item.productId);
        if (p) item.image = p.image;
      });
    } catch (e) {
      console.warn("Could not parse stored cart", e);
    }
  }

  const storedSession = localStorage.getItem("zenith_session");
  if (storedSession) {
    try {
      AppState.currentUser = JSON.parse(storedSession);
    } catch (e) {
      console.warn("Could not parse stored session", e);
    }
  }
}

function saveCart() {
  localStorage.setItem("zenith_cart", JSON.stringify(AppState.cart));
}

function saveUsers() {
  localStorage.setItem("zenith_users", JSON.stringify(AppState.users));
}

// --- Toast Notifications ---
function showToast(message, type = "success") {
  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;
  toast.setAttribute("data-testid", "toast-notification");
  toast.innerHTML = `<span>${type === "success" ? "✓" : "⚠"}</span> <span>${message}</span>`;
  DOM.toastContainer.appendChild(toast);
  setTimeout(() => {
    toast.remove();
  }, 3200);
}

// --- Product Rendering & Filtering ---
function renderProducts() {
  const list = AppState.filteredProducts;
  DOM.productsGrid.innerHTML = "";

  if (list.length === 0) {
    DOM.noProductsMsg.style.display = "block";
    DOM.productsCountMsg.textContent = "Showing 0 products";
    return;
  }

  DOM.noProductsMsg.style.display = "none";
  DOM.productsCountMsg.textContent = `Showing ${list.length} of ${AppState.products.length} products`;

  list.forEach(product => {
    const card = document.createElement("div");
    card.className = "product-card";
    card.setAttribute("data-testid", `product-card-${product.id}`);

    card.innerHTML = `
      <div class="product-img-wrapper" data-testid="product-img-${product.id}">
        <span class="category-badge">${product.category}</span>
        <img src="${product.image}" alt="${product.title}">
      </div>
      <div class="product-body">
        <h3 class="product-title" data-testid="product-title-${product.id}">${product.title}</h3>
        <div class="product-rating">
          <span>★ ${product.rating.toFixed(1)}</span>
          <span class="rating-count">(${product.reviews})</span>
        </div>
        <div class="product-footer">
          <span class="product-price" data-testid="product-price-${product.id}">$${product.price.toFixed(2)}</span>
          <div class="card-actions">
            <button class="btn btn-outline btn-sm view-detail-btn" data-id="${product.id}" data-testid="view-detail-${product.id}">Details</button>
            <button class="btn btn-primary btn-sm add-cart-btn" data-id="${product.id}" data-testid="add-to-cart-${product.id}">Add to Cart</button>
          </div>
        </div>
      </div>
    `;

    DOM.productsGrid.appendChild(card);
  });
}

function applyFilters() {
  let result = [...AppState.products];

  // 1. Search Query Filter
  // DEFECT NOTE: If searchQuery contains leading/trailing whitespace without trim(), search may yield 0 matches.
  // We apply query directly from input as typed to preserve realistic QA test behavior.
  if (AppState.activeFilter.searchQuery) {
    const q = AppState.activeFilter.searchQuery.toLowerCase();
    result = result.filter(p => 
      p.title.toLowerCase().includes(q) || 
      p.category.toLowerCase().includes(q) ||
      p.description.toLowerCase().includes(q)
    );
  }

  // 2. Category Filter
  if (AppState.activeFilter.category !== "all") {
    result = result.filter(p => p.category === AppState.activeFilter.category);
  }

  // 3. Price Filter
  result = result.filter(p => p.price <= AppState.activeFilter.maxPrice);

  // 4. Sorting
  if (AppState.activeFilter.sortBy === "price-low") {
    result.sort((a, b) => a.price - b.price);
  } else if (AppState.activeFilter.sortBy === "price-high") {
    result.sort((a, b) => b.price - a.price);
  } else if (AppState.activeFilter.sortBy === "rating") {
    result.sort((a, b) => b.rating - a.rating);
  }

  AppState.filteredProducts = result;
  renderProducts();
}

function resetAllFilters() {
  AppState.activeFilter = {
    category: "all",
    maxPrice: 1500,
    searchQuery: "",
    sortBy: "featured"
  };

  DOM.searchInput.value = "";
  DOM.clearSearchBtn.style.display = "none";
  DOM.priceRange.value = 1500;
  DOM.priceDisplay.textContent = "$1500";
  DOM.sortSelect.value = "featured";

  const allCatRadio = document.querySelector('input[name="category"][value="all"]');
  if (allCatRadio) allCatRadio.checked = true;

  applyFilters();
}

// --- Product Detail Modal ---
function openProductDetail(productId) {
  const product = AppState.products.find(p => p.id === productId);
  if (!product) return;

  DOM.detailModalBody.innerHTML = `
    <div class="detail-img-box">
      <img src="${product.image}" alt="${product.title}">
    </div>
    <div class="detail-info">
      <span class="detail-category">${product.category}</span>
      <h2 data-testid="detail-title">${product.title}</h2>
      <div class="product-rating" style="margin-bottom:12px;">
        <span>★ ${product.rating.toFixed(1)} rating</span>
        <span class="rating-count">(${product.reviews} customer reviews)</span>
      </div>
      <div class="detail-price" data-testid="detail-price">$${product.price.toFixed(2)}</div>
      <p class="detail-desc" data-testid="detail-desc">${product.description}</p>
      <div class="detail-stock">✓ In Stock (${product.stock} units available)</div>
      <div class="detail-actions">
        <div class="quantity-control">
          <button id="modal-qty-minus" data-testid="modal-qty-minus">-</button>
          <input type="number" id="modal-qty-input" data-testid="modal-qty-input" value="1" min="1" max="${product.stock}">
          <button id="modal-qty-plus" data-testid="modal-qty-plus">+</button>
        </div>
        <button id="modal-add-cart-btn" data-testid="modal-add-cart-btn" class="btn btn-primary btn-lg" data-id="${product.id}">
          Add to Cart
        </button>
      </div>
    </div>
  `;

  // Qty button handlers inside modal
  const qtyInput = document.getElementById("modal-qty-input");
  document.getElementById("modal-qty-minus").addEventListener("click", () => {
    let val = parseInt(qtyInput.value) || 1;
    if (val > 1) qtyInput.value = val - 1;
  });
  document.getElementById("modal-qty-plus").addEventListener("click", () => {
    let val = parseInt(qtyInput.value) || 1;
    if (val < product.stock) qtyInput.value = val + 1;
  });
  document.getElementById("modal-add-cart-btn").addEventListener("click", () => {
    const qty = parseInt(qtyInput.value) || 1;
    addToCart(product.id, qty);
    DOM.productDetailModal.style.display = "none";
  });

  DOM.productDetailModal.style.display = "flex";
}

// --- Cart Operations ---
function addToCart(productId, quantity = 1) {
  const product = AppState.products.find(p => p.id === productId);
  if (!product) return;

  const existingItem = AppState.cart.find(item => item.productId === productId);
  if (existingItem) {
    existingItem.quantity += quantity;
  } else {
    AppState.cart.push({
      productId: product.id,
      title: product.title,
      price: product.price,
      image: product.image,
      quantity: quantity
    });
  }

  saveCart();
  updateCartBadge();
  renderCart();
  showToast(`Added "${product.title}" to cart!`);
}

function removeFromCart(productId) {
  AppState.cart = AppState.cart.filter(item => item.productId !== productId);
  saveCart();
  updateCartBadge();
  renderCart();
  showToast("Item removed from cart.", "danger");
}

function updateCartQuantity(productId, newQty) {
  const item = AppState.cart.find(i => i.productId === productId);
  if (!item) return;

  // NOTE: DEFECT / BUG-001 (Boundary Value Behavior):
  // When user uses +/- buttons, it ensures minimum 1.
  // BUT if user types directly into input and blur occurs with <= 0 or negative values without validation,
  // we record what happens in manual testing.
  item.quantity = newQty;

  saveCart();
  updateCartBadge();
  renderCart();
}

function clearCart() {
  if (AppState.cart.length === 0) return;
  AppState.cart = [];
  saveCart();
  updateCartBadge();
  renderCart();
  showToast("Shopping cart cleared.", "danger");
}

function updateCartBadge() {
  const totalItems = AppState.cart.reduce((sum, item) => sum + (parseInt(item.quantity) || 0), 0);
  DOM.cartBadge.textContent = totalItems;
  DOM.cartDrawerCount.textContent = totalItems;
}

function getCartCalculations() {
  const subtotal = AppState.cart.reduce((sum, item) => {
    const q = parseInt(item.quantity) || 0;
    return sum + (item.price * q);
  }, 0);
  const tax = subtotal * 0.08;
  const total = subtotal + tax;
  return {
    subtotal: subtotal.toFixed(2),
    tax: tax.toFixed(2),
    total: total.toFixed(2)
  };
}

function renderCart() {
  DOM.cartItemsContainer.innerHTML = "";
  const calcs = getCartCalculations();

  DOM.cartSubtotal.textContent = `$${calcs.subtotal}`;
  DOM.cartTax.textContent = `$${calcs.tax}`;
  DOM.cartTotal.textContent = `$${calcs.total}`;
  DOM.chkTotalPayable.textContent = `$${calcs.total}`;

  if (AppState.cart.length === 0) {
    DOM.cartItemsContainer.innerHTML = `
      <div class="cart-empty-state" data-testid="cart-empty-state">
        <div class="icon">🛒</div>
        <p>Your shopping cart is empty.</p>
        <span style="font-size:0.8rem; color:#94a3b8;">Add products from catalog to start checkout.</span>
      </div>
    `;
    DOM.proceedCheckoutBtn.disabled = true;
    DOM.clearCartBtn.disabled = true;
    return;
  }

  DOM.proceedCheckoutBtn.disabled = false;
  DOM.clearCartBtn.disabled = false;

  AppState.cart.forEach(item => {
    const itemEl = document.createElement("div");
    itemEl.className = "cart-item";
    itemEl.setAttribute("data-testid", `cart-item-${item.productId}`);

    const itemSubtotal = (item.price * item.quantity).toFixed(2);

    itemEl.innerHTML = `
      <div class="cart-item-img">
        <img src="${item.image}" alt="${item.title}">
      </div>
      <div class="cart-item-info">
        <div class="cart-item-title" data-testid="cart-item-title-${item.productId}">${item.title}</div>
        <div class="cart-item-price">$${item.price.toFixed(2)} each</div>
        <div class="cart-item-qty">
          <button class="qty-btn qty-minus" data-id="${item.productId}" data-testid="cart-qty-minus-${item.productId}">-</button>
          <input type="number" class="qty-input" data-id="${item.productId}" data-testid="cart-qty-input-${item.productId}" value="${item.quantity}">
          <button class="qty-btn qty-plus" data-id="${item.productId}" data-testid="cart-qty-plus-${item.productId}">+</button>
        </div>
      </div>
      <div class="cart-item-total">
        <span class="cart-item-subtotal" data-testid="cart-item-subtotal-${item.productId}">$${itemSubtotal}</span>
        <button class="remove-item-btn" data-id="${item.productId}" data-testid="cart-remove-btn-${item.productId}">Remove</button>
      </div>
    `;

    DOM.cartItemsContainer.appendChild(itemEl);
  });

  // Attach dynamic cart item events
  DOM.cartItemsContainer.querySelectorAll(".qty-minus").forEach(btn => {
    btn.addEventListener("click", () => {
      const pid = parseInt(btn.dataset.id);
      const item = AppState.cart.find(i => i.productId === pid);
      if (item && item.quantity > 1) {
        updateCartQuantity(pid, item.quantity - 1);
      } else if (item && item.quantity <= 1) {
        removeFromCart(pid);
      }
    });
  });

  DOM.cartItemsContainer.querySelectorAll(".qty-plus").forEach(btn => {
    btn.addEventListener("click", () => {
      const pid = parseInt(btn.dataset.id);
      const item = AppState.cart.find(i => i.productId === pid);
      if (item) {
        updateCartQuantity(pid, item.quantity + 1);
      }
    });
  });

  DOM.cartItemsContainer.querySelectorAll(".qty-input").forEach(input => {
    input.addEventListener("change", (e) => {
      const pid = parseInt(input.dataset.id);
      const val = parseInt(e.target.value);
      // QA Defect BUG-001 reproduction point:
      // If user enters 0 or negative value manually, raw assignment updates without validation floor!
      updateCartQuantity(pid, val);
    });
  });

  DOM.cartItemsContainer.querySelectorAll(".remove-item-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      removeFromCart(parseInt(btn.dataset.id));
    });
  });
}

// --- Authentication Operations ---
function checkSession() {
  if (AppState.currentUser) {
    DOM.authGuest.style.display = "none";
    DOM.authUser.style.display = "flex";
    DOM.userGreeting.textContent = `Hi, ${AppState.currentUser.name}`;
    DOM.userAvatar.textContent = AppState.currentUser.name.substring(0, 2).toUpperCase();
  } else {
    DOM.authGuest.style.display = "flex";
    DOM.authUser.style.display = "none";
  }
}

function handleLogin(email, password) {
  // Clear previous errors
  DOM.loginEmailError.textContent = "";
  DOM.loginPasswordError.textContent = "";
  DOM.loginAlert.style.display = "none";
  DOM.loginEmail.classList.remove("is-invalid");
  DOM.loginPassword.classList.remove("is-invalid");

  let isValid = true;

  if (!email.trim()) {
    DOM.loginEmailError.textContent = "Email address is required";
    DOM.loginEmail.classList.add("is-invalid");
    isValid = false;
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    DOM.loginEmailError.textContent = "Please enter a valid email format";
    DOM.loginEmail.classList.add("is-invalid");
    isValid = false;
  }

  if (!password) {
    DOM.loginPasswordError.textContent = "Password is required";
    DOM.loginPassword.classList.add("is-invalid");
    isValid = false;
  }

  if (!isValid) return false;

  const foundUser = AppState.users.find(u => u.email.toLowerCase() === email.toLowerCase());

  if (!foundUser) {
    DOM.loginAlert.textContent = "Invalid credentials: User does not exist.";
    DOM.loginAlert.style.display = "block";
    return false;
  }

  if (foundUser.password !== password) {
    DOM.loginAlert.textContent = "Invalid credentials: Incorrect password.";
    DOM.loginAlert.style.display = "block";
    return false;
  }

  // Success
  AppState.currentUser = { name: foundUser.name, email: foundUser.email };
  localStorage.setItem("zenith_session", JSON.stringify(AppState.currentUser));
  checkSession();
  DOM.loginModal.style.display = "none";
  DOM.loginForm.reset();
  showToast(`Welcome back, ${foundUser.name}!`);
  return true;
}

function handleRegister(name, email, password, confirmPassword) {
  // Clear previous errors
  DOM.regNameError.textContent = "";
  DOM.regEmailError.textContent = "";
  DOM.regPasswordError.textContent = "";
  DOM.regConfirmPasswordError.textContent = "";
  DOM.registerAlert.style.display = "none";
  [DOM.regName, DOM.regEmail, DOM.regPassword, DOM.regConfirmPassword].forEach(el => el.classList.remove("is-invalid"));

  let isValid = true;

  if (!name.trim()) {
    DOM.regNameError.textContent = "Full name is required";
    DOM.regName.classList.add("is-invalid");
    isValid = false;
  }

  if (!email.trim()) {
    DOM.regEmailError.textContent = "Email address is required";
    DOM.regEmail.classList.add("is-invalid");
    isValid = false;
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    DOM.regEmailError.textContent = "Please enter a valid email format";
    DOM.regEmail.classList.add("is-invalid");
    isValid = false;
  }

  if (!password) {
    DOM.regPasswordError.textContent = "Password is required";
    DOM.regPassword.classList.add("is-invalid");
    isValid = false;
  } else if (password.length < 6) {
    DOM.regPasswordError.textContent = "Password must be at least 6 characters";
    DOM.regPassword.classList.add("is-invalid");
    isValid = false;
  }

  if (!confirmPassword) {
    DOM.regConfirmPasswordError.textContent = "Please confirm your password";
    DOM.regConfirmPassword.classList.add("is-invalid");
    isValid = false;
  } else if (password !== confirmPassword) {
    DOM.regConfirmPasswordError.textContent = "Passwords do not match";
    DOM.regConfirmPassword.classList.add("is-invalid");
    isValid = false;
  }

  if (!isValid) return false;

  // Check duplicate
  const exists = AppState.users.some(u => u.email.toLowerCase() === email.toLowerCase());
  if (exists) {
    DOM.registerAlert.textContent = "An account with this email already exists.";
    DOM.registerAlert.style.display = "block";
    return false;
  }

  // Register new user
  const newUser = { name: name.trim(), email: email.trim(), password: password };
  AppState.users.push(newUser);
  saveUsers();

  AppState.currentUser = { name: newUser.name, email: newUser.email };
  localStorage.setItem("zenith_session", JSON.stringify(AppState.currentUser));
  checkSession();

  DOM.registerModal.style.display = "none";
  DOM.registerForm.reset();
  showToast(`Account created successfully! Welcome, ${newUser.name}.`);
  return true;
}

function handleLogout() {
  AppState.currentUser = null;
  localStorage.removeItem("zenith_session");
  checkSession();
  showToast("Logged out successfully.");
}

// --- Checkout & Validation ---
function validateCheckoutForm() {
  let isValid = true;
  DOM.checkoutAlert.style.display = "none";

  const fields = [
    { input: DOM.chkName, error: document.getElementById("chk-name-error"), name: "Full name" },
    { input: DOM.chkEmail, error: document.getElementById("chk-email-error"), name: "Email address", isEmail: true },
    { input: DOM.chkAddress, error: document.getElementById("chk-address-error"), name: "Street address" },
    { input: DOM.chkCity, error: document.getElementById("chk-city-error"), name: "City" },
    { input: DOM.chkState, error: document.getElementById("chk-state-error"), name: "State" },
    // QA Defect BUG-002: ZIP code only checks required, allowing letters e.g. "ABCDE" without postal code regex validation!
    { input: DOM.chkZip, error: document.getElementById("chk-zip-error"), name: "ZIP code" }
  ];

  fields.forEach(f => {
    f.error.textContent = "";
    f.input.classList.remove("is-invalid");

    if (!f.input.value.trim()) {
      f.error.textContent = `${f.name} is required`;
      f.input.classList.add("is-invalid");
      isValid = false;
    } else if (f.isEmail && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.input.value.trim())) {
      f.error.textContent = "Enter a valid email address";
      f.input.classList.add("is-invalid");
      isValid = false;
    }
  });

  // If credit card selected, validate mock card details
  const selectedPay = document.querySelector('input[name="payment-method"]:checked').value;
  if (selectedPay === "credit") {
    const cardFields = [
      { input: DOM.chkCardNumber, error: document.getElementById("chk-card-number-error"), name: "Card number", minLen: 12 },
      { input: DOM.chkCardExp, error: document.getElementById("chk-card-exp-error"), name: "Expiry date" },
      { input: DOM.chkCardCvv, error: document.getElementById("chk-card-cvv-error"), name: "CVV", minLen: 3 }
    ];

    cardFields.forEach(f => {
      f.error.textContent = "";
      f.input.classList.remove("is-invalid");

      if (!f.input.value.trim()) {
        f.error.textContent = `${f.name} is required`;
        f.input.classList.add("is-invalid");
        isValid = false;
      } else if (f.minLen && f.input.value.trim().length < f.minLen) {
        f.error.textContent = `${f.name} format is incomplete`;
        f.input.classList.add("is-invalid");
        isValid = false;
      }
    });
  }

  return isValid;
}

function processOrder() {
  if (AppState.cart.length === 0) {
    DOM.checkoutAlert.textContent = "Your cart is empty. Please add items before checking out.";
    DOM.checkoutAlert.style.display = "block";
    return;
  }

  const calcs = getCartCalculations();
  const orderId = "ORD-" + Math.floor(100000 + Math.random() * 900000);
  const selectedPayment = document.querySelector('input[name="payment-method"]:checked').value === "credit" 
    ? "Credit Card (Mock)" 
    : "Cash on Delivery";

  // Fill Confirmation Modal
  DOM.confOrderId.textContent = orderId;
  DOM.confName.textContent = DOM.chkName.value.trim();
  DOM.confEmail.textContent = DOM.chkEmail.value.trim();
  DOM.confAddress.textContent = `${DOM.chkAddress.value.trim()}, ${DOM.chkCity.value.trim()}, ${DOM.chkState.value.trim()} ${DOM.chkZip.value.trim()}`;
  DOM.confPayment.textContent = selectedPayment;
  DOM.confTotal.textContent = `$${calcs.total}`;

  // Fill Confirmed Items
  DOM.confItemsList.innerHTML = "";
  AppState.cart.forEach(item => {
    const row = document.createElement("div");
    row.className = "conf-item-row";
    row.innerHTML = `
      <span>${item.title} (x${item.quantity})</span>
      <strong>$${(item.price * item.quantity).toFixed(2)}</strong>
    `;
    DOM.confItemsList.appendChild(row);
  });

  // Clear Cart & Form
  AppState.cart = [];
  saveCart();
  updateCartBadge();
  renderCart();

  DOM.checkoutModal.style.display = "none";
  DOM.checkoutForm.reset();
  DOM.confirmationModal.style.display = "flex";
  showToast("Order placed successfully!", "success");
}

// --- Setup All Event Listeners ---
function setupEventListeners() {
  // Search
  DOM.searchBtn.addEventListener("click", () => {
    AppState.activeFilter.searchQuery = DOM.searchInput.value;
    DOM.clearSearchBtn.style.display = DOM.searchInput.value ? "block" : "none";
    applyFilters();
  });

  DOM.searchInput.addEventListener("keyup", (e) => {
    AppState.activeFilter.searchQuery = DOM.searchInput.value;
    DOM.clearSearchBtn.style.display = DOM.searchInput.value ? "block" : "none";
    if (e.key === "Enter") {
      applyFilters();
    } else {
      applyFilters();
    }
  });

  DOM.clearSearchBtn.addEventListener("click", () => {
    DOM.searchInput.value = "";
    AppState.activeFilter.searchQuery = "";
    DOM.clearSearchBtn.style.display = "none";
    applyFilters();
  });

  if (DOM.clearSearchEmptyBtn) {
    DOM.clearSearchEmptyBtn.addEventListener("click", resetAllFilters);
  }

  // Categories
  DOM.categoryRadios.forEach(radio => {
    radio.addEventListener("change", (e) => {
      AppState.activeFilter.category = e.target.value;
      applyFilters();
    });
  });

  // Price Slider
  DOM.priceRange.addEventListener("input", (e) => {
    const val = e.target.value;
    DOM.priceDisplay.textContent = `$${val}`;
    AppState.activeFilter.maxPrice = parseFloat(val);
    applyFilters();
  });

  // Sort
  DOM.sortSelect.addEventListener("change", (e) => {
    AppState.activeFilter.sortBy = e.target.value;
    applyFilters();
  });

  // Reset Filters
  DOM.resetFiltersBtn.addEventListener("click", resetAllFilters);

  // Delegate Product Card clicks (Details & Add to Cart)
  DOM.productsGrid.addEventListener("click", (e) => {
    const detailBtn = e.target.closest(".view-detail-btn");
    if (detailBtn) {
      const pid = parseInt(detailBtn.dataset.id);
      openProductDetail(pid);
      return;
    }

    const imgWrapper = e.target.closest(".product-img-wrapper");
    if (imgWrapper) {
      const card = imgWrapper.closest(".product-card");
      const pid = parseInt(card.querySelector(".view-detail-btn").dataset.id);
      openProductDetail(pid);
      return;
    }

    const titleEl = e.target.closest(".product-title");
    if (titleEl) {
      const card = titleEl.closest(".product-card");
      const pid = parseInt(card.querySelector(".view-detail-btn").dataset.id);
      openProductDetail(pid);
      return;
    }

    const addBtn = e.target.closest(".add-cart-btn");
    if (addBtn) {
      const pid = parseInt(addBtn.dataset.id);
      addToCart(pid, 1);
      return;
    }
  });

  // Product Detail Modal Close
  DOM.closeDetailModalBtn.addEventListener("click", () => {
    DOM.productDetailModal.style.display = "none";
  });

  // Cart Drawer Open / Close
  DOM.cartToggleBtn.addEventListener("click", () => {
    renderCart();
    DOM.cartDrawer.style.display = "block";
  });

  DOM.closeCartBtn.addEventListener("click", () => {
    DOM.cartDrawer.style.display = "none";
  });

  DOM.clearCartBtn.addEventListener("click", clearCart);

  DOM.proceedCheckoutBtn.addEventListener("click", () => {
    if (AppState.cart.length === 0) {
      showToast("Cannot checkout an empty cart!", "danger");
      return;
    }
    DOM.cartDrawer.style.display = "none";
    const calcs = getCartCalculations();
    DOM.chkTotalPayable.textContent = `$${calcs.total}`;

    // Pre-fill user data if logged in
    if (AppState.currentUser) {
      DOM.chkName.value = AppState.currentUser.name;
      DOM.chkEmail.value = AppState.currentUser.email;
    }

    DOM.checkoutModal.style.display = "flex";
  });

  // Auth Modals Open / Close
  DOM.navLoginBtn.addEventListener("click", () => {
    DOM.loginModal.style.display = "flex";
  });

  DOM.closeLoginModalBtn.addEventListener("click", () => {
    DOM.loginModal.style.display = "none";
  });

  DOM.navRegisterBtn.addEventListener("click", () => {
    DOM.registerModal.style.display = "flex";
  });

  DOM.closeRegisterModalBtn.addEventListener("click", () => {
    DOM.registerModal.style.display = "none";
  });

  DOM.navLogoutBtn.addEventListener("click", handleLogout);

  DOM.switchToRegisterBtn.addEventListener("click", () => {
    DOM.loginModal.style.display = "none";
    DOM.registerModal.style.display = "flex";
  });

  DOM.switchToLoginBtn.addEventListener("click", () => {
    DOM.registerModal.style.display = "none";
    DOM.loginModal.style.display = "flex";
  });

  // Form Submissions
  DOM.loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleLogin(DOM.loginEmail.value, DOM.loginPassword.value);
  });

  DOM.registerForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleRegister(
      DOM.regName.value,
      DOM.regEmail.value,
      DOM.regPassword.value,
      DOM.regConfirmPassword.value
    );
  });

  // Checkout Payment Toggle
  DOM.paymentMethodRadios.forEach(radio => {
    radio.addEventListener("change", (e) => {
      if (e.target.value === "cod") {
        DOM.cardFieldsGroup.style.display = "none";
      } else {
        DOM.cardFieldsGroup.style.display = "block";
      }
    });
  });

  DOM.closeCheckoutModalBtn.addEventListener("click", () => {
    DOM.checkoutModal.style.display = "none";
  });

  DOM.checkoutForm.addEventListener("submit", (e) => {
    e.preventDefault();
    if (validateCheckoutForm()) {
      processOrder();
    }
  });

  // Order Confirmation Continue Shopping
  DOM.confContinueShoppingBtn.addEventListener("click", () => {
    DOM.confirmationModal.style.display = "none";
    resetAllFilters();
  });

  // Close modals on clicking outside
  window.addEventListener("click", (e) => {
    if (e.target === DOM.loginModal) DOM.loginModal.style.display = "none";
    if (e.target === DOM.registerModal) DOM.registerModal.style.display = "none";
    if (e.target === DOM.productDetailModal) DOM.productDetailModal.style.display = "none";
    if (e.target === DOM.cartDrawer) DOM.cartDrawer.style.display = "none";
    if (e.target === DOM.checkoutModal) DOM.checkoutModal.style.display = "none";
    if (e.target === DOM.confirmationModal) DOM.confirmationModal.style.display = "none";
  });
}

// Start application when DOM is ready
document.addEventListener("DOMContentLoaded", initApp);

