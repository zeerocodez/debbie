# -*- coding: utf-8 -*-
"""
Client-side JavaScript Application Engine for Debbie's Collection.
Includes persistent client-side state,
product discovery, multi-step checkout, measurement book, and WhatsApp integration.
"""

def get_app_js():
    return '''// Debbie's Collection - Master Application Engine
(function() {
  'use strict';

  // --- Constants & Database Setup ---
  const STORAGE_KEY = 'debbie_collection_store_v5';
  const EXCHANGE_RATES = {
    NGN: 1,
    USD: 1 / 1550,
    GBP: 1 / 1980
  };

  // Default Seed Data
  const DEFAULT_DB = {
    currency: 'NGN',
    cart: [
      {
        cartId: 'item-init-1',
        productId: 'PROD-09',
        name: 'Bespoke Tartan Lounge Pants - Buffalo Red',
        price: 10000,
        size: 'Regular Flannel (All Sizes)',
        color: 'Red & Black Buffalo Plaid',
        quantity: 1,
        image: 'images/lounge-tartan-pants-red-buffalo.jpeg',
        svgId: 'svg-satin-pj'
      }
    ],
    wishlist: ['PROD-01', 'PROD-05'],
    appliedPromo: null,
    promoCodes: {
      'DEBBIEVIP': { type: 'percent', value: 15, desc: '15% VIP Atelier Discount' },
      'UYO10': { type: 'percent', value: 10, desc: '10% Uyo Welcome Discount' },
      'UDOUMANA': { type: 'flat', value: 5000, desc: '₦5,000 Atelier Savings' },
      'FREESHIP': { type: 'shipping', value: 100, desc: 'Free Shipping Across Nigeria' }
    },
    user: {
      name: 'Dr. Idara Akpan',
      email: 'idara.akpan@example.com',
      phone: '+234 803 456 7890',
      address: 'Plot 18, Ewet Housing Estate, Uyo, Akwa Ibom State',
      bespokeMeasurements: {
        child: {
          name: 'Princess Idara',
          relation: 'Child Profile (Girls Couture)',
          age: '4 Years',
          chest: '58cm',
          waist: '54cm',
          height: '104cm',
          shoulderToHem: '62cm'
        },
        adult: {
          name: 'Dr. Idara',
          relation: 'Adult Loungewear Profile',
          chest: '92cm',
          waist: '76cm',
          hips: '102cm',
          height: '168cm',
          shoulderToHem: '136cm'
        }
      }
    },
    orders: [
      {
        orderId: 'DC-2026-7814',
        date: 'October 24, 2026',
        items: [
          { name: 'The Udoumana Storefront Rosette Gala Gown', size: '7-8 Years', price: 35000, qty: 1 }
        ],
        subtotal: 35000,
        shipping: 0,
        total: 35000,
        deliveryMethod: 'Uyo Same-Day Bike Delivery',
        status: 'Delivered',
        customer: 'Dr. Idara Akpan • Ewet Housing Estate, Uyo',
        phone: '+234 803 456 7890'
      },
      {
        orderId: 'DC-2026-8941',
        date: 'November 6, 2026',
        items: [
          { name: 'Bespoke Tartan Lounge Pants - Buffalo Red', size: 'Regular Flannel (All Sizes)', price: 10000, qty: 1 }
        ],
        subtotal: 10000,
        shipping: 1500,
        total: 11500,
        deliveryMethod: 'Uyo Same-Day Bike Delivery',
        status: 'Tailoring in Atelier (Uyo)',
        customer: 'Lady Blessing Okon • Osongama, Uyo',
        phone: '+234 802 987 6543'
      }
    ]
  };

  // Initialize LocalStorage Database
  function getDb() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        return JSON.parse(stored);
      }
    } catch (e) {
      console.warn('LocalStorage unavailable, using memory DB', e);
    }
    return JSON.parse(JSON.stringify(DEFAULT_DB));
  }

  function saveDb(db) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(db));
    } catch (e) {
      console.warn('Failed to save to localStorage', e);
    }
  }

  let DB = getDb();
  if (!DB.products || !Array.isArray(DB.products) || DB.products.length === 0) {
    DB.products = JSON.parse(JSON.stringify(window.DC_PRODUCTS || []));
    saveDb(DB);
  }

  // --- Active Filter State ---
  let filterState = {
    category: 'All',
    age: 'All',
    bespokeOnly: false,
    search: '',
    sort: 'featured'
  };

  // --- Checkout State ---
  let checkoutState = {
    step: 1,
    shippingFee: 1500,
    deliveryMethodName: 'Uyo Same-Day Bike Delivery',
    measurementOption: 'saved',
    paymentMethod: 'card'
  };

  // --- Currency & Formatter Helpers ---
  function formatMoney(amountNgn) {
    const cur = DB.currency || 'NGN';
    const rate = EXCHANGE_RATES[cur] || 1;
    const converted = amountNgn * rate;

    if (cur === 'USD') {
      return '$' + converted.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    } else if (cur === 'GBP') {
      return '£' + converted.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    } else {
      return '₦' + Math.round(converted).toLocaleString('en-NG');
    }
  }

  function setCurrency(cur) {
    if (EXCHANGE_RATES[cur]) {
      DB.currency = cur;
      saveDb(DB);
      renderAll();
      showToast(`Currency updated to ${cur}`);
    }
  }

  // --- Toast System ---
  function showToast(message, icon = '✦') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast-pill';
    toast.innerHTML = `<span style="color:var(--accent-gold); font-size:1.1rem;">${icon}</span><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }

  // --- Cart Calculations ---
  function getCartSubtotal() {
    return DB.cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  }

  function getCartDiscount() {
    if (!DB.appliedPromo) return 0;
    const promo = DB.promoCodes[DB.appliedPromo];
    if (!promo) return 0;
    const subtotal = getCartSubtotal();
    if (promo.type === 'percent') {
      return Math.round(subtotal * (promo.value / 100));
    } else if (promo.type === 'flat') {
      return Math.min(promo.value, subtotal);
    }
    return 0;
  }

  function getCartShippingFee() {
    if (DB.appliedPromo && DB.promoCodes[DB.appliedPromo]?.type === 'shipping') {
      return 0;
    }
    if (checkoutState.deliveryMethodName.includes('Pickup')) {
      return 0;
    }
    const subtotal = getCartSubtotal();
    // Free delivery in Uyo over ₦45,000
    if (checkoutState.deliveryMethodName.includes('Uyo') && subtotal >= 45000) {
      return 0;
    }
    return checkoutState.shippingFee;
  }

  function getCartTotal() {
    const subtotal = getCartSubtotal();
    const discount = getCartDiscount();
    const shipping = getCartShippingFee();
    return Math.max(0, subtotal - discount + shipping);
  }

  // --- Render Header & Cart Counters ---
  function updateHeaderBadges() {
    const totalItems = DB.cart.reduce((sum, item) => sum + item.quantity, 0);
    const subtotal = getCartSubtotal();

    const cartBadge = document.getElementById('cart-counter-badge');
    const mobileCartBadge = document.getElementById('mobile-cart-badge');
    const subtotalLabel = document.getElementById('cart-header-subtotal');
    const wishlistBadge = document.getElementById('wishlist-counter-badge');
    const mobileWishBadge = document.getElementById('mobile-wishlist-badge');

    if (cartBadge) cartBadge.textContent = totalItems;
    if (mobileCartBadge) mobileCartBadge.textContent = totalItems;
    if (subtotalLabel) subtotalLabel.textContent = formatMoney(subtotal);
    if (wishlistBadge) wishlistBadge.textContent = DB.wishlist.length;
    if (mobileWishBadge) mobileWishBadge.textContent = DB.wishlist.length;
  }

  // --- Render Cart Drawer ---
  function renderCartDrawer() {
    const container = document.getElementById('cart-items-container');
    const drawerCount = document.getElementById('cart-drawer-count');
    const trackerText = document.getElementById('delivery-tracker-text');
    const trackerFill = document.getElementById('delivery-tracker-fill');
    const subtotalVal = document.getElementById('cart-subtotal-val');
    const discountLine = document.getElementById('discount-summary-line');
    const discountVal = document.getElementById('cart-discount-val');
    const shippingVal = document.getElementById('cart-shipping-val');
    const totalVal = document.getElementById('cart-total-val');

    const totalQty = DB.cart.reduce((sum, i) => sum + i.quantity, 0);
    const subtotal = getCartSubtotal();
    const discount = getCartDiscount();
    const shipping = getCartShippingFee();
    const total = getCartTotal();

    if (drawerCount) drawerCount.textContent = `${totalQty} item${totalQty === 1 ? '' : 's'}`;

    // Delivery Progress Tracker (₦45,000 threshold for free delivery in Uyo)
    const threshold = 45000;
    if (trackerFill && trackerText) {
      if (subtotal >= threshold) {
        trackerFill.style.width = '100%';
        trackerFill.style.background = 'var(--accent-sage)';
        trackerText.innerHTML = `<strong>Congratulations!</strong> You qualify for <strong>Free Doorstep Delivery in Uyo</strong>`;
      } else {
        const remaining = threshold - subtotal;
        const pct = Math.min(100, Math.round((subtotal / threshold) * 100));
        trackerFill.style.width = `${pct}%`;
        trackerFill.style.background = 'var(--accent-rose)';
        trackerText.innerHTML = `Add <strong>${formatMoney(remaining)}</strong> more for <strong>Free Delivery in Uyo</strong>`;
      }
    }

    // Cart Items
    if (container) {
      if (DB.cart.length === 0) {
        container.innerHTML = `
          <div style="text-align:center; padding:48px 16px; color:var(--text-muted);">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin:0 auto 16px; color:var(--accent-rose);"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            <h4 style="font-family:var(--font-serif); font-size:1.15rem; color:var(--text-primary); margin-bottom:6px;">Your Bag is Empty</h4>
            <p style="font-size:0.84rem; margin-bottom:18px;">Discover our bespoke loungewear and heirloom children's wear.</p>
            <button class="btn-primary" onclick="window.DC_APP.closeCartDrawer(); window.location.href='#shop';">Explore The Collection</button>
          </div>
        `;
      } else {
        container.innerHTML = DB.cart.map(item => {
          const itemThumb = item.image ?
            `<img src="${item.image}" alt="${item.name}" style="width:100%; height:100%; object-fit:cover; border-radius:var(--radius-sm);">` :
            (window.DC_SVGS?.[item.svgId] || `<div style="font-size:0.7rem; font-weight:700;">DC</div>`);
          return `
            <div class="cart-item-row" data-cart-id="${item.cartId}">
              <div class="cart-item-thumb">
                ${itemThumb}
              </div>
              <div class="cart-item-details">
                <h4 class="cart-item-title">${item.name}</h4>
                <div class="cart-item-spec">
                  <span>Size: <strong>${item.size}</strong></span>
                  ${item.color ? ` • <span>${item.color}</span>` : ''}
                </div>
                <div class="cart-item-qty-row">
                  <div class="qty-control-box">
                    <button class="qty-btn" onclick="window.DC_APP.updateCartQty('${item.cartId}', -1)" aria-label="Decrease quantity">−</button>
                    <span class="qty-val">${item.quantity}</span>
                    <button class="qty-btn" onclick="window.DC_APP.updateCartQty('${item.cartId}', 1)" aria-label="Increase quantity">+</button>
                  </div>
                  <strong class="cart-item-price">${formatMoney(item.price * item.quantity)}</strong>
                </div>
              </div>
              <button onclick="window.DC_APP.removeFromCart('${item.cartId}')" style="position:absolute; top:2px; right:0; color:var(--text-muted); font-size:1rem;" title="Remove">×</button>
            </div>
          `;
        }).join('');
      }
    }

    // Summary
    if (subtotalVal) subtotalVal.textContent = formatMoney(subtotal);
    if (discountLine && discountVal) {
      if (discount > 0) {
        discountLine.style.display = 'flex';
        discountVal.textContent = `-${formatMoney(discount)}`;
      } else {
        discountLine.style.display = 'none';
      }
    }
    if (shippingVal) {
      if (subtotal === 0) {
        shippingVal.textContent = formatMoney(0);
      } else if (shipping === 0) {
        shippingVal.innerHTML = `<span style="color:var(--accent-sage); font-weight:700;">FREE (Uyo Promotion)</span>`;
      } else {
        shippingVal.textContent = formatMoney(shipping);
      }
    }
    if (totalVal) totalVal.textContent = formatMoney(total);
  }

  // --- Cart Management Functions ---
  function addToCart(product, options = {}) {
    const size = options.size || (product.sizes && product.sizes[0]) || 'Standard';
    const color = options.color || (product.colors && product.colors[0]) || '';
    const customMeasurements = options.customMeasurements || null;

    // Check if duplicate item exists
    const existingIndex = DB.cart.findIndex(i =>
      i.productId === product.id &&
      i.size === size &&
      i.color === color
    );

    if (existingIndex > -1) {
      DB.cart[existingIndex].quantity += 1;
    } else {
      DB.cart.push({
        cartId: 'item-' + Date.now() + '-' + Math.random().toString(36).substr(2, 4),
        productId: product.id,
        name: product.name,
        price: product.price,
        size: size,
        color: color,
        customMeasurements: customMeasurements,
        quantity: 1,
        image: product.image || '',
        svgId: product.svgId
      });
    }

    saveDb(DB);
    updateHeaderBadges();
    renderCartDrawer();
    openCartDrawer();
    showToast(`Added ${product.name} to your bag`);
  }

  function removeFromCart(cartId) {
    const idx = DB.cart.findIndex(i => i.cartId === cartId);
    if (idx > -1) {
      const removed = DB.cart.splice(idx, 1)[0];
      saveDb(DB);
      updateHeaderBadges();
      renderCartDrawer();
      showToast(`Removed ${removed.name} from bag`);
    }
  }

  function updateCartQty(cartId, delta) {
    const item = DB.cart.find(i => i.cartId === cartId);
    if (!item) return;
    item.quantity += delta;
    if (item.quantity <= 0) {
      removeFromCart(cartId);
    } else {
      saveDb(DB);
      updateHeaderBadges();
      renderCartDrawer();
    }
  }

  function applyPromoCode() {
    const input = document.getElementById('cart-promo-input');
    const msg = document.getElementById('promo-feedback-msg');
    if (!input || !msg) return;

    const code = input.value.trim().toUpperCase();
    if (DB.promoCodes[code]) {
      DB.appliedPromo = code;
      saveDb(DB);
      renderCartDrawer();
      msg.style.display = 'block';
      msg.style.color = 'var(--accent-sage)';
      msg.textContent = `✓ ${DB.promoCodes[code].desc} applied!`;
      showToast(`Coupon ${code} applied successfully!`);
    } else {
      msg.style.display = 'block';
      msg.style.color = 'var(--accent-rose)';
      msg.textContent = 'Invalid promo code. Try DEBBIEVIP or UYO10.';
    }
  }

  function checkoutViaWhatsApp() {
    if (DB.cart.length === 0) {
      showToast('Your bag is empty.');
      return;
    }
    const lines = DB.cart.map((i, idx) =>
      `${idx + 1}. *${i.name}* (Qty: ${i.quantity}) - Size: ${i.size}${i.color ? `, Color: ${i.color}` : ''} - ${formatMoney(i.price * i.quantity)}`
    ).join('%0A');

    const total = formatMoney(getCartTotal());
    const message = `Hello Debbie's Collection Atelier Uyo! 👑%0AI would like to place an order:%0A%0A${lines}%0A%0A*Total: ${total}*%0A%0APlease confirm tailoring and delivery details to 164 Udoumana Street, Uyo. Thank you!`;
    window.open(`https://wa.me/2347085222212?text=${message}`, '_blank');
  }

  // --- Wishlist Management ---
  function toggleWishlist(productId) {
    const idx = DB.wishlist.indexOf(productId);
    if (idx > -1) {
      DB.wishlist.splice(idx, 1);
      showToast('Removed from your Wishlist');
    } else {
      DB.wishlist.push(productId);
      showToast('Saved to your Wishlist ♥');
    }
    saveDb(DB);
    updateHeaderBadges();
    renderProducts();
  }

  // --- Product Filter & Search Engine ---
  function filterCategory(cat) {
    filterState.category = cat;
    document.querySelectorAll('.category-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-cat') === cat);
    });
    renderProducts();
  }

  function filterAge(age) {
    filterState.age = age;
    document.querySelectorAll('.age-chip-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-age') === age);
    });
    renderProducts();
  }

  function toggleBespokeOnly(checked) {
    filterState.bespokeOnly = checked;
    renderProducts();
  }

  function handleSearch(query) {
    filterState.search = query.trim().toLowerCase();
    const clearBtn = document.getElementById('search-clear-btn');
    if (clearBtn) clearBtn.style.display = filterState.search ? 'block' : 'none';
    renderProducts();
  }

  function clearSearch() {
    const input = document.getElementById('shop-search-input');
    if (input) input.value = '';
    handleSearch('');
  }

  function focusSearch() {
    const input = document.getElementById('shop-search-input');
    if (input) {
      input.scrollIntoView({ behavior: 'smooth', block: 'center' });
      input.focus();
    }
  }

  function handleSort(sortVal) {
    filterState.sort = sortVal;
    renderProducts();
  }

  function renderProducts() {
    const grid = document.getElementById('products-grid');
    const countLabel = document.getElementById('results-count-label');
    const activeFiltersBar = document.getElementById('active-filters-bar');
    if (!grid) return;

    const allProducts = DB.products || window.DC_PRODUCTS || [];

    // Filter logic
    let filtered = allProducts.filter(p => {
      // Category filter
      if (filterState.category !== 'All' && p.category !== filterState.category) {
        return false;
      }
      // Bespoke only
      if (filterState.bespokeOnly && !p.isBespoke) {
        return false;
      }
      // Age filter
      if (filterState.age !== 'All') {
        const target = filterState.age.toLowerCase();
        const hasAge = (p.sizes || []).some(s => {
          const str = s.toLowerCase();
          if (target === '0-12m') return str.includes('0-12') || str.includes('baby') || str.includes('infant');
          if (target === '1-4y') return str.includes('1') || str.includes('2') || str.includes('3') || str.includes('4') || str.includes('3/4');
          if (target === '5-8y') return str.includes('5') || str.includes('6') || str.includes('7') || str.includes('8') || str.includes('6-7') || str.includes('7-8');
          if (target === '9-14y') return str.includes('9') || str.includes('10') || str.includes('11') || str.includes('12') || str.includes('14') || str.includes('9/10');
          if (target === 'adult') return str.includes('adult') || str.includes('flannel') || str.includes('all sizes') || str.includes('pants') || str.includes('polo') || str.includes('cargo') || ['xs','s','m','l','xl','xxl'].includes(str);
          return str.includes(target);
        });
        if (!hasAge) {
          return false;
        }
      }
      // Search query
      if (filterState.search) {
        const query = filterState.search;
        const matchesName = p.name.toLowerCase().includes(query);
        const matchesCat = p.category.toLowerCase().includes(query);
        const matchesFab = p.fabric.toLowerCase().includes(query);
        const matchesDesc = p.description.toLowerCase().includes(query);
        const matchesTag = p.tags && p.tags.some(t => t.toLowerCase().includes(query));
        if (!matchesName && !matchesCat && !matchesFab && !matchesDesc && !matchesTag) {
          return false;
        }
      }
      return true;
    });

    // Sorting logic
    if (filterState.sort === 'price-asc') {
      filtered.sort((a, b) => a.price - b.price);
    } else if (filterState.sort === 'price-desc') {
      filtered.sort((a, b) => b.price - a.price);
    } else if (filterState.sort === 'rating') {
      filtered.sort((a, b) => b.rating - a.rating);
    }

    if (countLabel) {
      countLabel.textContent = `Showing ${filtered.length} of ${allProducts.length} atelier creations`;
    }

    // Active Filter Pills
    if (activeFiltersBar) {
      const activePills = [];
      if (filterState.category !== 'All') {
        activePills.push(`Category: ${filterState.category} <button onclick="window.DC_APP.filterCategory('All')">×</button>`);
      }
      if (filterState.age !== 'All') {
        activePills.push(`Size: ${filterState.age} <button onclick="window.DC_APP.filterAge('All')">×</button>`);
      }
      if (filterState.bespokeOnly) {
        activePills.push(`Bespoke Only <button onclick="document.getElementById('bespoke-toggle').checked=false; window.DC_APP.toggleBespokeOnly(false)">×</button>`);
      }
      if (filterState.search) {
        activePills.push(`"${filterState.search}" <button onclick="window.DC_APP.clearSearch()">×</button>`);
      }

      if (activePills.length > 0) {
        activeFiltersBar.style.display = 'flex';
        activeFiltersBar.innerHTML = activePills.map(p => `<span class="filter-badge-pill">${p}</span>`).join('') +
          `<button class="clear-all-filters-btn" onclick="window.DC_APP.clearAllFilters()">Reset Filters</button>`;
      } else {
        activeFiltersBar.style.display = 'none';
      }
    }

    // Render Cards
    if (filtered.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align:center; padding:60px 20px; background:var(--bg-surface); border-radius:var(--radius-md); border:1px solid var(--border-light);">
          <h3 style="font-family:var(--font-serif); font-size:1.3rem; margin-bottom:8px;">No Garments Match Your Filters</h3>
          <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:20px;">Try adjusting your age selection, category, or search term.</p>
          <button class="btn-primary" onclick="window.DC_APP.clearAllFilters()">Reset All Filters</button>
        </div>
      `;
      return;
    }

    grid.innerHTML = filtered.map(p => {
      const isWish = DB.wishlist.includes(p.id);
      const svgCode = window.DC_SVGS?.[p.svgId] || '';
      const swatches = (p.colors || []).slice(0, 3).map((col, idx) => {
        let hex = '#F2D5CE';
        if (col.toLowerCase().includes('navy')) hex = '#182337';
        else if (col.toLowerCase().includes('white') || col.toLowerCase().includes('ivory')) hex = '#FFFDF9';
        else if (col.toLowerCase().includes('rose') || col.toLowerCase().includes('blush')) hex = '#E2B8AF';
        else if (col.toLowerCase().includes('gold') || col.toLowerCase().includes('champagne')) hex = '#D4AF37';
        else if (col.toLowerCase().includes('sage') || col.toLowerCase().includes('olive')) hex = '#9EB59B';
        else if (col.toLowerCase().includes('plum') || col.toLowerCase().includes('velvet')) hex = '#46132A';
        else if (col.toLowerCase().includes('terracotta')) hex = '#BA5F40';
        else if (col.toLowerCase().includes('espresso')) hex = '#241915';
        return `<span class="swatch-dot" style="background:${hex};" title="${col}"></span>`;
      }).join('');

      return `
        <article class="product-card" id="card-${p.id}">
          <div class="product-image-box" onclick="window.DC_APP.openQuickView('${p.id}')">
            ${p.badge ? `<span class="product-badge-tag ${p.badge === 'Bestseller' ? 'badge-rose' : ''}">${p.badge}</span>` : ''}
            <button class="wishlist-heart-btn ${isWish ? 'active' : ''}" onclick="event.stopPropagation(); window.DC_APP.toggleWishlist('${p.id}')" title="Wishlist">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="${isWish ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
            </button>
            ${p.image ? `
              <img src="${p.image}" alt="${p.name}" class="product-img" loading="lazy" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
              <div style="display:none; width:100%; height:100%; align-items:center; justify-content:center;">
                ${svgCode}
              </div>
            ` : `
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                ${svgCode}
              </div>
            `}
            <button class="quick-view-overlay-btn" onclick="event.stopPropagation(); window.DC_APP.openQuickView('${p.id}')">
              Quick View & Customize
            </button>
          </div>

          <div class="product-info-box">
            <div class="product-meta-row">
              <span class="product-category-label">${p.category}</span>
              <div class="product-rating-box">
                <span>★</span>
                <span>${p.rating} (${p.reviewsCount})</span>
              </div>
            </div>

            <h3 class="product-title" onclick="window.DC_APP.openQuickView('${p.id}')">${p.name}</h3>
            <p class="product-fabric-text">${p.description}</p>

            <div class="product-swatches-row">
              ${swatches}
              <span style="font-size:0.72rem; color:var(--text-muted); margin-left:4px;">${p.leadTime}</span>
            </div>

            <div class="product-bottom-row">
              <div class="product-price-box">
                <span class="price-current">${formatMoney(p.price)}</span>
                ${p.originalPrice ? `<span class="price-original">${formatMoney(p.originalPrice)}</span>` : ''}
              </div>
              <button class="card-action-btn" onclick="window.DC_APP.openQuickView('${p.id}')">
                <span>Tailor / Add</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              </button>
            </div>
          </div>
        </article>
      `;
    }).join('');
  }

  function clearAllFilters() {
    filterState.category = 'All';
    filterState.age = 'All';
    filterState.bespokeOnly = false;
    filterState.search = '';
    filterState.sort = 'featured';

    const bespokeToggle = document.getElementById('bespoke-toggle');
    if (bespokeToggle) bespokeToggle.checked = false;

    const searchInput = document.getElementById('shop-search-input');
    if (searchInput) searchInput.value = '';

    const sortSelect = document.getElementById('sort-select');
    if (sortSelect) sortSelect.value = 'featured';

    document.querySelectorAll('.category-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-cat') === 'All');
    });

    document.querySelectorAll('.age-chip-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-age') === 'All');
    });

    renderProducts();
    showToast('Filters reset to show all items');
  }

  // --- Quick View Modal ---
  function openQuickView(productId) {
    const product = (DB.products || window.DC_PRODUCTS || []).find(p => p.id === productId);
    if (!product) return;

    const modal = document.getElementById('quick-view-modal');
    const titleEl = document.getElementById('qv-title');
    const bodyEl = document.getElementById('qv-body-content');
    if (!modal || !bodyEl) return;

    if (titleEl) titleEl.textContent = product.name;

    const svgCode = window.DC_SVGS?.[product.svgId] || '';
    const sizes = product.sizes || ['Standard'];
    const colors = product.colors || ['Natural'];

    const gallery = (product.gallery && product.gallery.length > 0) ? product.gallery : (product.image ? [product.image] : []);
    const galleryStrip = gallery.length > 1 ? `
      <div style="display:flex; gap:8px; margin-top:10px; width:100%; justify-content:center; flex-wrap:wrap;">
        ${gallery.map((img, idx) => `
          <button type="button" onclick="document.getElementById('qv-hero-img').src='${img}'; this.parentElement.querySelectorAll('button').forEach(b=>b.style.borderColor='transparent'); this.style.borderColor='var(--accent-rose)';" style="border:2px solid ${idx===0 ? 'var(--accent-rose)' : 'transparent'}; border-radius:var(--radius-sm); overflow:hidden; width:54px; height:54px; padding:0; background:#fff; cursor:pointer;">
            <img src="${img}" alt="Preview" style="width:100%; height:100%; object-fit:cover;">
          </button>
        `).join('')}
      </div>
    ` : '';

    const visualHtml = product.image ? `
      <div style="width:100%; display:flex; flex-direction:column; align-items:center;">
        <div style="width:100%; height:320px; border-radius:var(--radius-sm); overflow:hidden; background:var(--bg-warm); display:flex; align-items:center; justify-content:center; border:1px solid var(--border-light);">
          <img id="qv-hero-img" src="${product.image}" alt="${product.name}" style="width:100%; height:100%; object-fit:contain; border-radius:var(--radius-sm);">
        </div>
        ${galleryStrip}
      </div>
    ` : `
      <div style="background:radial-gradient(circle, #FFFDF9 0%, #F5EDE7 100%); border-radius:var(--radius-md); padding:24px; display:flex; align-items:center; justify-content:center; border:1px solid var(--border-light); min-height:320px;">
        <div style="width:100%; max-width:280px;">
          ${svgCode}
        </div>
      </div>
    `;

    bodyEl.innerHTML = `
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:32px; align-items:start;">
        ${visualHtml}

        <div style="display:flex; flex-direction:column; gap:16px;">
          <div>
            <span style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--accent-rose); font-weight:700;">${product.category}</span>
            <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin:4px 0 8px;">${product.name}</h3>
            <div style="display:flex; align-items:center; gap:8px;">
              <span class="price-current" style="font-size:1.4rem;">${formatMoney(product.price)}</span>
              ${product.originalPrice ? `<span class="price-original" style="font-size:0.95rem;">${formatMoney(product.originalPrice)}</span>` : ''}
              <span style="font-size:0.75rem; background:var(--accent-rose-light); color:var(--accent-rose); padding:2px 8px; border-radius:var(--radius-full); font-weight:700;">${product.badge}</span>
            </div>
          </div>

          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">${product.description}</p>
          <div style="font-size:0.8rem; background:var(--bg-warm); padding:10px 14px; border-radius:var(--radius-sm); border:1px solid var(--border-light);">
            <strong>Fabric:</strong> ${product.fabric}<br>
            <strong>Atelier Timeline:</strong> ${product.leadTime}
          </div>

          <!-- Size Selector -->
          <div class="form-group">
            <label class="form-label">Select Size / Fit Option *</label>
            <select id="qv-size-select" class="form-select" onchange="window.DC_APP.handleQvSizeChange(this.value)">
              ${sizes.map(s => `<option value="${s}">${s}</option>`).join('')}
            </select>
          </div>

          <!-- Color Selector -->
          <div class="form-group">
            <label class="form-label">Atelier Fabric Color *</label>
            <select id="qv-color-select" class="form-select">
              ${colors.map(c => `<option value="${c}">${c}</option>`).join('')}
            </select>
          </div>

          <!-- Expandable Custom Measurements Panel -->
          <div id="qv-custom-meas-box" style="display:none; background:var(--bg-cream); padding:14px; border-radius:var(--radius-sm); border:1px solid var(--border-light);">
            <span style="font-size:0.78rem; font-weight:700; color:var(--accent-rose); display:block; margin-bottom:8px;">Custom Made-to-Measure Specifications:</span>
            <div class="form-grid-2">
              <input type="text" id="qv-meas-chest" class="form-input" placeholder="Chest (e.g. 60cm)">
              <input type="text" id="qv-meas-waist" class="form-input" placeholder="Waist (e.g. 54cm)">
            </div>
            <div class="form-grid-2" style="margin-top:8px;">
              <input type="text" id="qv-meas-len" class="form-input" placeholder="Shoulder to Hem">
              <input type="text" id="qv-meas-age" class="form-input" placeholder="Child Age / Height">
            </div>
          </div>

          <button class="btn-primary" style="width:100%; margin-top:6px;" onclick="window.DC_APP.submitQuickView('${product.id}')">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            <span>Add Garment to Bag</span>
          </button>
        </div>
      </div>
    `;

    modal.classList.add('open');
  }

  function handleQvSizeChange(sizeVal) {
    const box = document.getElementById('qv-custom-meas-box');
    if (box) {
      box.style.display = sizeVal.toLowerCase().includes('bespoke') || sizeVal.toLowerCase().includes('custom') ? 'block' : 'none';
    }
  }

  function submitQuickView(productId) {
    const product = (DB.products || window.DC_PRODUCTS || []).find(p => p.id === productId);
    if (!product) return;

    const sizeSelect = document.getElementById('qv-size-select');
    const colorSelect = document.getElementById('qv-color-select');

    const size = sizeSelect ? sizeSelect.value : 'Standard';
    const color = colorSelect ? colorSelect.value : '';

    let customMeasurements = null;
    if (size.toLowerCase().includes('bespoke') || size.toLowerCase().includes('custom')) {
      const chest = document.getElementById('qv-meas-chest')?.value || '';
      const waist = document.getElementById('qv-meas-waist')?.value || '';
      const len = document.getElementById('qv-meas-len')?.value || '';
      const age = document.getElementById('qv-meas-age')?.value || '';
      customMeasurements = { chest, waist, len, age };
    }

    addToCart(product, {
      size: size,
      color: color,
      customMeasurements: customMeasurements
    });

    closeQuickViewModal();
  }

  function closeQuickViewModal() {
    const modal = document.getElementById('quick-view-modal');
    if (modal) modal.classList.remove('open');
  }

  // --- Multi-Step Checkout Modal Operations ---
  function proceedToCheckout() {
    if (DB.cart.length === 0) {
      showToast('Your bag is empty.');
      return;
    }
    closeCartDrawer();
    goToCheckoutStep(1);
    const modal = document.getElementById('checkout-modal');
    if (modal) modal.classList.add('open');
  }

  function goToCheckoutStep(stepNum) {
    checkoutState.step = stepNum;

    // Update indicator bar
    for (let i = 1; i <= 4; i++) {
      const ind = document.getElementById(`chk-step-${i}-ind`);
      const stepDiv = document.getElementById(`checkout-step-${i}`);
      if (ind) {
        ind.classList.toggle('active', i === stepNum);
        ind.classList.toggle('completed', i < stepNum);
      }
      if (stepDiv) {
        stepDiv.style.display = i === stepNum ? 'flex' : 'none';
      }
    }

    if (stepNum === 3) {
      const payableEl = document.getElementById('chk-payable-amount');
      if (payableEl) payableEl.textContent = formatMoney(getCartTotal());
    }
  }

  function updateCheckoutShipping(method) {
    if (method === 'uyo-bike') {
      checkoutState.shippingFee = 1500;
      checkoutState.deliveryMethodName = 'Uyo Same-Day Bike Delivery';
    } else if (method === 'akwa-ibom') {
      checkoutState.shippingFee = 2500;
      checkoutState.deliveryMethodName = 'Akwa Ibom State Courier';
    } else if (method === 'nationwide') {
      checkoutState.shippingFee = 4500;
      checkoutState.deliveryMethodName = 'Nationwide Priority Doorstep';
    } else if (method === 'pickup') {
      checkoutState.shippingFee = 0;
      checkoutState.deliveryMethodName = 'In-Boutique Pickup at 164 Udoumana Street, Uyo';
    }
    renderCartDrawer();
    const payableEl = document.getElementById('chk-payable-amount');
    if (payableEl) payableEl.textContent = formatMoney(getCartTotal());
  }

  function selectMeasurementOption(opt) {
    checkoutState.measurementOption = opt;
    const customBox = document.getElementById('checkout-custom-meas-inputs');
    if (customBox) {
      customBox.style.display = opt === 'custom' ? 'block' : 'none';
    }
  }

  function selectPaymentMethod(method) {
    checkoutState.paymentMethod = method;
    const cardPanel = document.getElementById('payment-panel-card');
    const transferPanel = document.getElementById('payment-panel-transfer');
    const payBtnText = document.getElementById('btn-pay-now-text');

    if (cardPanel) cardPanel.style.display = method === 'card' ? 'flex' : 'none';
    if (transferPanel) transferPanel.style.display = method === 'transfer' ? 'flex' : 'none';

    if (payBtnText) {
      if (method === 'card') payBtnText.textContent = `Authorize & Pay ${formatMoney(getCartTotal())}`;
      else if (method === 'transfer') payBtnText.textContent = 'I Have Transferred • Verify Order';
      else payBtnText.textContent = 'Confirm Order for In-Boutique Pickup';
    }
  }

  function autofillTestCard() {
    const cardNum = document.getElementById('card-num');
    const cardExp = document.getElementById('card-exp');
    const cardCvv = document.getElementById('card-cvv');
    if (cardNum) cardNum.value = '5399 4210 8821 9812';
    if (cardExp) cardExp.value = '08/29';
    if (cardCvv) cardCvv.value = '418';
    showToast('Demo card credentials filled');
  }

  function copyAccountNumber() {
    const accNum = document.getElementById('uba-acc-num')?.textContent || '2127888264';
    navigator.clipboard?.writeText(accNum);
    showToast(`Copied UBA account: ${accNum}`);
  }

  function processOrderPayment() {
    const btn = document.getElementById('btn-pay-now');
    if (btn) btn.disabled = true;

    if (checkoutState.paymentMethod === 'card') {
      // Trigger 3D Secure OTP Simulation Modal
      const otpModal = document.getElementById('otp-modal');
      if (otpModal) otpModal.classList.add('open');
      if (btn) btn.disabled = false;
    } else {
      // Direct Bank Transfer or Pickup
      finalizeOrder('Verified Direct Payment');
      if (btn) btn.disabled = false;
    }
  }

  function confirmOtp() {
    closeOtpModal();
    finalizeOrder('Card Payment (3D Secure Authenticated)');
  }

  function closeOtpModal() {
    const otpModal = document.getElementById('otp-modal');
    if (otpModal) otpModal.classList.remove('open');
  }

  function finalizeOrder(paymentRef) {
    const customerName = document.getElementById('chk-name')?.value || DB.user.name;
    const customerEmail = document.getElementById('chk-email')?.value || DB.user.email;
    const customerPhone = document.getElementById('chk-phone')?.value || DB.user.phone;
    const customerAddress = document.getElementById('chk-address')?.value || DB.user.address;

    const orderId = 'DC-2026-' + Math.floor(1000 + Math.random() * 9000);
    const subtotal = getCartSubtotal();
    const discount = getCartDiscount();
    const shipping = getCartShippingFee();
    const total = getCartTotal();

    const newOrder = {
      orderId: orderId,
      date: new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }),
      items: JSON.parse(JSON.stringify(DB.cart)),
      subtotal: subtotal,
      discount: discount,
      shipping: shipping,
      total: total,
      deliveryMethod: checkoutState.deliveryMethodName,
      paymentMethod: paymentRef,
      customer: `${customerName} • ${customerAddress}`,
      phone: customerPhone,
      email: customerEmail,
      status: 'Pattern Drafting & Tailoring at 164 Udoumana Atelier'
    };

    DB.orders.unshift(newOrder);
    // Clear cart
    DB.cart = [];
    DB.appliedPromo = null;
    saveDb(DB);
    updateHeaderBadges();
    renderCartDrawer();

    // Populate Receipt Modal
    const rOrderId = document.getElementById('receipt-order-id');
    const rDate = document.getElementById('receipt-date');
    const rCust = document.getElementById('receipt-customer-info');
    const rList = document.getElementById('receipt-items-list');
    const rSub = document.getElementById('receipt-subtotal');
    const rShip = document.getElementById('receipt-shipping');
    const rTotal = document.getElementById('receipt-total');

    if (rOrderId) rOrderId.textContent = newOrder.orderId;
    if (rDate) rDate.textContent = newOrder.date;
    if (rCust) rCust.textContent = `${customerName} • ${customerPhone} • ${customerAddress}`;
    if (rSub) rSub.textContent = formatMoney(subtotal);
    if (rShip) rShip.textContent = shipping === 0 ? 'FREE' : formatMoney(shipping);
    if (rTotal) rTotal.textContent = formatMoney(total);

    if (rList) {
      rList.innerHTML = newOrder.items.map(i => `
        <div style="display:flex; justify-content:space-between; font-size:0.84rem;">
          <div>
            <strong>${i.name}</strong> (x${i.quantity})
            <span style="display:block; font-size:0.75rem; color:var(--text-muted);">${i.size}</span>
          </div>
          <strong>${formatMoney(i.price * i.quantity)}</strong>
        </div>
      `).join('');
    }

    goToCheckoutStep(4);
    showToast(`Order #${newOrder.orderId} Confirmed at Debbie's Collection!`);
  }

  function notifyWhatsAppOrder() {
    const order = DB.orders[0];
    if (!order) return;
    const text = `Hello Debbie's Collection Atelier! 👑%0AI just placed Order *#${order.orderId}* for ${formatMoney(order.total)}.%0ADelivery to: ${order.customer}.%0APlease confirm tailoring timeline at 164 Udoumana Street, Uyo. Thank you!`;
    window.open(`https://wa.me/2347085222212?text=${text}`, '_blank');
  }

  function closeCheckoutModal() {
    const modal = document.getElementById('checkout-modal');
    if (modal) modal.classList.remove('open');
  }

  // --- Customer Account Drawer & Measurement Book ---
  function openAccountModal(tab = 'profile') {
    const modal = document.getElementById('account-modal');
    if (modal) {
      modal.classList.add('open');
      switchAccountTab(tab);
    }
  }

  function closeAccountModal() {
    const modal = document.getElementById('account-modal');
    if (modal) modal.classList.remove('open');
  }

  function switchAccountTab(tab) {
    ['profile', 'measurements', 'orders', 'wishlist'].forEach(t => {
      const tabBtn = document.getElementById(`acc-tab-${t}`);
      if (tabBtn) tabBtn.classList.toggle('active', t === tab);
    });

    const body = document.getElementById('account-body-content');
    if (!body) return;

    if (tab === 'profile') {
      body.innerHTML = `
        <h4 style="font-family:var(--font-serif); font-size:1.15rem;">Customer Atelier Profile</h4>
        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">Full Name</label>
            <input type="text" id="acc-name" class="form-input" value="${DB.user.name}">
          </div>
          <div class="form-group">
            <label class="form-label">Email Address</label>
            <input type="email" id="acc-email" class="form-input" value="${DB.user.email}">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Phone (WhatsApp Connected)</label>
          <input type="tel" id="acc-phone" class="form-input" value="${DB.user.phone}">
        </div>
        <div class="form-group">
          <label class="form-label">Primary Delivery Address (Uyo & Across Nigeria)</label>
          <textarea id="acc-address" class="form-textarea" rows="2">${DB.user.address}</textarea>
        </div>
        <button class="btn-primary" onclick="window.DC_APP.saveProfile()">Save Profile Updates</button>
      `;
    } else if (tab === 'measurements') {
      const child = (DB.user.bespokeMeasurements || {}).child || {};
      const adult = (DB.user.bespokeMeasurements || {}).adult || {};
      body.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <div>
            <h4 style="font-family:var(--font-serif); font-size:1.15rem;">Bespoke Measurement Book</h4>
            <span style="font-size:0.78rem; color:var(--text-muted);">Saved specifications for made-to-measure tailoring</span>
          </div>
          <span style="font-size:0.75rem; background:var(--accent-gold-light); color:#59430E; padding:3px 10px; border-radius:var(--radius-full); font-weight:700;">Atelier Ready</span>
        </div>

        <!-- Child Profile -->
        <div style="background:var(--bg-warm); padding:16px; border-radius:var(--radius-sm); border:1px solid var(--border-light);">
          <strong style="color:var(--accent-rose); font-size:0.9rem; display:block; margin-bottom:10px;">Child Profile: ${child.name} (${child.age})</strong>
          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Chest Circumference</label>
              <input type="text" id="meas-child-chest" class="form-input" value="${child.chest}">
            </div>
            <div class="form-group">
              <label class="form-label">Waist Circumference</label>
              <input type="text" id="meas-child-waist" class="form-input" value="${child.waist}">
            </div>
          </div>
          <div class="form-grid-2" style="margin-top:8px;">
            <div class="form-group">
              <label class="form-label">Height / Length</label>
              <input type="text" id="meas-child-height" class="form-input" value="${child.height}">
            </div>
            <div class="form-group">
              <label class="form-label">Shoulder to Hem</label>
              <input type="text" id="meas-child-hem" class="form-input" value="${child.shoulderToHem}">
            </div>
          </div>
        </div>

        <!-- Adult Loungewear Profile -->
        <div style="background:var(--bg-warm); padding:16px; border-radius:var(--radius-sm); border:1px solid var(--border-light);">
          <strong style="color:var(--text-primary); font-size:0.9rem; display:block; margin-bottom:10px;">Adult Loungewear Profile: ${adult.name}</strong>
          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Bust / Chest</label>
              <input type="text" id="meas-adult-chest" class="form-input" value="${adult.chest}">
            </div>
            <div class="form-group">
              <label class="form-label">Waist</label>
              <input type="text" id="meas-adult-waist" class="form-input" value="${adult.waist}">
            </div>
          </div>
          <div class="form-grid-2" style="margin-top:8px;">
            <div class="form-group">
              <label class="form-label">Hips</label>
              <input type="text" id="meas-adult-hips" class="form-input" value="${adult.hips}">
            </div>
            <div class="form-group">
              <label class="form-label">Desired Robe Length</label>
              <input type="text" id="meas-adult-hem" class="form-input" value="${adult.shoulderToHem}">
            </div>
          </div>
        </div>

        <button class="btn-primary" onclick="window.DC_APP.saveMeasurements()">Update Measurement Book</button>
      `;
    } else if (tab === 'orders') {
      if (DB.orders.length === 0) {
        body.innerHTML = `<p style="text-align:center; padding:40px; color:var(--text-muted);">No orders found.</p>`;
      } else {
        body.innerHTML = `
          <h4 style="font-family:var(--font-serif); font-size:1.15rem;">Your Orders & Live Tracking</h4>
          <div style="display:flex; flex-direction:column; gap:16px;">
            ${DB.orders.map(o => `
              <div style="background:var(--bg-warm); border:1px solid var(--border-light); border-radius:var(--radius-sm); padding:16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <div>
                    <strong style="font-family:var(--font-serif); font-size:1.05rem;">Order #${o.orderId}</strong>
                    <span style="display:block; font-size:0.75rem; color:var(--text-muted);">${o.date}</span>
                  </div>
                  <span style="font-size:0.72rem; font-weight:700; background:var(--bg-surface); padding:3px 10px; border-radius:var(--radius-full); border:1px solid var(--border-light); color:var(--accent-rose);">
                    ${o.status}
                  </span>
                </div>
                <div style="font-size:0.84rem; color:var(--text-secondary); margin-bottom:10px;">
                  ${o.items.map(i => `• ${i.name} (${i.size || 'Standard'}) x${i.quantity || 1}`).join('<br>')}
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed var(--border-light); padding-top:10px;">
                  <strong>Total: ${formatMoney(o.total)}</strong>
                  <a href="https://wa.me/2347085222212?text=Hello%20Debbie's%20Collection,%20inquiry%20on%20Order%20%23${o.orderId}" target="_blank" rel="noopener" style="font-size:0.78rem; color:#25D366; font-weight:700;">
                    Track via WhatsApp →
                  </a>
                </div>
              </div>
            `).join('')}
          </div>
        `;
      }
    } else if (tab === 'wishlist') {
      const allProducts = DB.products || window.DC_PRODUCTS || [];
      const wishProducts = allProducts.filter(p => DB.wishlist.includes(p.id));

      if (wishProducts.length === 0) {
        body.innerHTML = `
          <div style="text-align:center; padding:48px 16px; color:var(--text-muted);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin:0 auto 12px; color:var(--accent-rose);"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
            <h4 style="font-family:var(--font-serif); font-size:1.1rem; color:var(--text-primary); margin-bottom:4px;">No Saved Favorites</h4>
            <p style="font-size:0.84rem;">Click the heart icon on any piece to save it for later.</p>
          </div>
        `;
      } else {
        body.innerHTML = `
          <h4 style="font-family:var(--font-serif); font-size:1.15rem;">Saved Atelier Pieces (${wishProducts.length})</h4>
          <div style="display:flex; flex-direction:column; gap:12px;">
            ${wishProducts.map(p => `
              <div style="display:flex; align-items:center; justify-content:space-between; background:var(--bg-warm); padding:10px 14px; border-radius:var(--radius-sm); border:1px solid var(--border-light);">
                <div style="display:flex; align-items:center; gap:12px;">
                  ${p.image ? `<img src="${p.image}" alt="${p.name}" style="width:48px; height:48px; object-fit:cover; border-radius:var(--radius-sm);">` : ''}
                  <div>
                    <strong style="font-family:var(--font-serif); font-size:0.95rem; display:block;">${p.name}</strong>
                    <span style="font-size:0.8rem; color:var(--text-muted);">${formatMoney(p.price)}</span>
                  </div>
                </div>
                <div style="display:flex; gap:8px;">
                  <button class="card-action-btn" onclick="window.DC_APP.openQuickView('${p.id}'); window.DC_APP.closeAccountModal();">View / Buy</button>
                  <button style="color:var(--accent-rose); font-size:0.8rem;" onclick="window.DC_APP.toggleWishlist('${p.id}'); window.DC_APP.switchAccountTab('wishlist');">Remove</button>
                </div>
              </div>
            `).join('')}
          </div>
        `;
      }
    }
  }

  function saveProfile() {
    const name = document.getElementById('acc-name')?.value;
    const email = document.getElementById('acc-email')?.value;
    const phone = document.getElementById('acc-phone')?.value;
    const address = document.getElementById('acc-address')?.value;

    if (name) DB.user.name = name;
    if (email) DB.user.email = email;
    if (phone) DB.user.phone = phone;
    if (address) DB.user.address = address;

    saveDb(DB);
    showToast('Customer profile updated');
  }

  function saveMeasurements() {
    const cc = document.getElementById('meas-child-chest')?.value;
    const cw = document.getElementById('meas-child-waist')?.value;
    const ch = document.getElementById('meas-child-height')?.value;
    const chem = document.getElementById('meas-child-hem')?.value;

    const ac = document.getElementById('meas-adult-chest')?.value;
    const aw = document.getElementById('meas-adult-waist')?.value;
    const ahip = document.getElementById('meas-adult-hips')?.value;
    const ahem = document.getElementById('meas-adult-hem')?.value;

    if (!DB.user.bespokeMeasurements) {
      DB.user.bespokeMeasurements = { child: {}, adult: {} };
    }
    if (cc) DB.user.bespokeMeasurements.child.chest = cc;
    if (cw) DB.user.bespokeMeasurements.child.waist = cw;
    if (ch) DB.user.bespokeMeasurements.child.height = ch;
    if (chem) DB.user.bespokeMeasurements.child.shoulderToHem = chem;

    if (ac) DB.user.bespokeMeasurements.adult.chest = ac;
    if (aw) DB.user.bespokeMeasurements.adult.waist = aw;
    if (ahip) DB.user.bespokeMeasurements.adult.hips = ahip;
    if (ahem) DB.user.bespokeMeasurements.adult.shoulderToHem = ahem;

    saveDb(DB);
    showToast('Bespoke Measurement Book saved for 1-click orders!');
  }

  // --- Private Fitting Consultation Booking Modal ---
  function openConsultationModal() {
    const modal = document.getElementById('consultation-modal');
    if (modal) modal.classList.add('open');
  }

  function closeConsultationModal() {
    const modal = document.getElementById('consultation-modal');
    if (modal) modal.classList.remove('open');
  }

  function submitConsultation(e) {
    e.preventDefault();
    const name = document.getElementById('fit-name')?.value;
    const phone = document.getElementById('fit-phone')?.value;
    const date = document.getElementById('fit-date')?.value;
    const time = document.getElementById('fit-time')?.value;
    const service = document.getElementById('fit-service')?.value;

    closeConsultationModal();
    showToast(`Fitting booked for ${date} (${time}) at 164 Udoumana St!`);

    const msg = `Hello Debbie's Collection! 👑%0AI have booked a Private Atelier Fitting:%0AName: ${name}%0APhone: ${phone}%0ADate: ${date} at ${time}%0AService: ${service}%0ALocation: 164 Udoumana Street, Uyo.`;
    window.open(`https://wa.me/2347085222212?text=${msg}`, '_blank');
  }

  // --- Review Submission Modal ---
  function openReviewModal() {
    const modal = document.getElementById('review-modal');
    if (modal) modal.classList.add('open');
  }

  function closeReviewModal() {
    const modal = document.getElementById('review-modal');
    if (modal) modal.classList.remove('open');
  }

  function submitReview(e) {
    e.preventDefault();
    const author = document.getElementById('rev-author')?.value;
    const loc = document.getElementById('rev-loc')?.value;
    const prod = document.getElementById('rev-prod')?.value;
    const quote = document.getElementById('rev-text')?.value;

    closeReviewModal();
    showToast('Thank you! Your verified review has been recorded.');
  }

  // --- Drawer & Modal Common Handlers ---
  function openCartDrawer() {
    const drawer = document.getElementById('cart-drawer');
    if (drawer) drawer.classList.add('open');
  }

  function closeCartDrawer() {
    const drawer = document.getElementById('cart-drawer');
    if (drawer) drawer.classList.remove('open');
  }

  function toggleMobileNav() {
    openAccountModal('profile');
  }

  function toggleFaq(itemEl) {
    const wasActive = itemEl.classList.contains('active');
    document.querySelectorAll('.faq-item').forEach(el => {
      el.classList.remove('active');
      const ans = el.querySelector('.faq-answer');
      if (ans) ans.style.maxHeight = null;
    });
    if (!wasActive) {
      itemEl.classList.add('active');
      const ans = itemEl.querySelector('.faq-answer');
      if (ans) ans.style.maxHeight = ans.scrollHeight + 'px';
    }
  }

  // --- Keyboard & Outside Click Listeners ---
  window.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      closeCartDrawer();
      closeCheckoutModal();
      closeAccountModal();
      closeQuickViewModal();
      closeConsultationModal();
      closeReviewModal();
      closeOtpModal();
    }
  });

  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', e => {
      if (e.target === overlay) {
        overlay.classList.remove('open');
      }
    });
  });

  // --- Render All Initial State ---
  function renderAll() {
    updateHeaderBadges();
    renderCartDrawer();
    renderProducts();

    if (window.location.hash === '#admin') {
      setTimeout(openAdminPortal, 300);
    }
  }

  window.addEventListener('hashchange', () => {
    if (window.location.hash === '#admin') {
      openAdminPortal();
    }
  });

  // --- Admin Dashboard & Inventory Suite Engine ---
  const ADMIN_PASSCODE = '1640';
  let adminActiveTab = 'overview';
  let adminEditingProductId = null;
  let adminShowNewProductForm = false;
  let adminShowWalkInSaleForm = false;

  function openAdminPortal() {
    if (sessionStorage.getItem('debbie_admin_auth') === 'true') {
      openAdminModal();
    } else {
      openAdminPinModal();
    }
  }

  function openAdminPinModal() {
    const modal = document.getElementById('admin-pin-modal');
    if (modal) {
      modal.classList.add('open');
      const input = document.getElementById('admin-pin-input');
      if (input) { input.value = ''; input.focus(); }
    }
  }

  function closeAdminPinModal() {
    const modal = document.getElementById('admin-pin-modal');
    if (modal) modal.classList.remove('open');
  }

  function verifyAdminPin(e) {
    if (e) e.preventDefault();
    const pin = document.getElementById('admin-pin-input')?.value.trim();
    if (pin === ADMIN_PASSCODE || pin === '164' || pin === 'admin') {
      sessionStorage.setItem('debbie_admin_auth', 'true');
      closeAdminPinModal();
      showToast('✦ Welcome, Debbie! Atelier Admin unlocked.');
      openAdminModal();
    } else {
      showToast('Incorrect passcode. Hint: 1640');
    }
  }

  function openAdminModal() {
    const modal = document.getElementById('admin-modal');
    if (modal) {
      modal.classList.add('open');
      switchAdminTab(adminActiveTab);
    }
  }

  function closeAdminModal() {
    const modal = document.getElementById('admin-modal');
    if (modal) modal.classList.remove('open');
  }

  function switchAdminTab(tabName) {
    adminActiveTab = tabName;
    document.querySelectorAll('.admin-tab-btn').forEach(b => b.classList.remove('active'));
    const btn = document.getElementById(`adm-tab-${tabName}`);
    if (btn) btn.classList.add('active');
    renderAdminTab(tabName);
  }

  function renderAdminTab(tabName) {
    const container = document.getElementById('admin-tab-body');
    if (!container) return;

    if (tabName === 'overview') {
      renderAdminOverview(container);
    } else if (tabName === 'products') {
      renderAdminProducts(container);
    } else if (tabName === 'inventory') {
      renderAdminInventory(container);
    } else if (tabName === 'orders') {
      renderAdminOrders(container);
    } else if (tabName === 'discounts') {
      renderAdminDiscounts(container);
    }
  }

  function renderAdminOverview(container) {
    const products = DB.products || [];
    const orders = DB.orders || [];
    const totalRev = orders.reduce((sum, o) => sum + (o.total || 0), 0);
    const totalUnits = products.reduce((sum, p) => sum + (p.stock || 0), 0);
    const lowStockItems = products.filter(p => (p.stock || 0) <= 4);

    container.innerHTML = `
      <!-- 4 Top KPI Cards -->
      <div class="admin-kpi-grid">
        <div class="admin-kpi-card">
          <span class="admin-kpi-label">Gross Revenue</span>
          <span class="admin-kpi-value">${formatMoney(totalRev)}</span>
          <span class="admin-kpi-sub">From ${orders.length} orders</span>
        </div>
        <div class="admin-kpi-card">
          <span class="admin-kpi-label">Active Catalog</span>
          <span class="admin-kpi-value">${products.length} Items</span>
          <span class="admin-kpi-sub">${products.filter(p => p.category === "Children's Wear").length} Kids • ${products.filter(p => p.category === "Bespoke Lounge Wear").length} Lounge</span>
        </div>
        <div class="admin-kpi-card">
          <span class="admin-kpi-label">Inventory On Hand</span>
          <span class="admin-kpi-value">${totalUnits} Units</span>
          <span class="admin-kpi-sub">Across ${products.filter(p => p.batch).length} batches</span>
        </div>
        <div class="admin-kpi-card">
          <span class="admin-kpi-label">Low Stock Alerts</span>
          <span class="admin-kpi-value" style="color:${lowStockItems.length > 0 ? 'var(--accent-rose)' : '#2E7D32'};">${lowStockItems.length} Items</span>
          <span class="admin-kpi-sub">${lowStockItems.length > 0 ? 'Restock recommended' : 'Stock healthy'}</span>
        </div>
      </div>

      <!-- Low Stock Alert Banner -->
      ${lowStockItems.length > 0 ? `
        <div class="admin-card" style="border-left:4px solid var(--accent-rose); background:#FFF5F3;">
          <div class="admin-card-header">
            <div>
              <strong style="color:var(--text-primary); font-size:0.95rem;">⚠️ Low Stock / Restock Needed</strong>
              <span style="display:block; font-size:0.76rem; color:var(--text-muted);">The following boutique garments have 4 or fewer pieces remaining:</span>
            </div>
          </div>
          <div style="display:flex; flex-wrap:wrap; gap:10px;">
            ${lowStockItems.map(p => `
              <div style="background:#FFFFFF; border:1px solid var(--border-light); border-radius:var(--radius-sm); padding:8px 12px; display:flex; align-items:center; gap:10px; font-size:0.8rem;">
                <img src="${p.image}" class="admin-thumb" style="width:32px; height:32px;">
                <div>
                  <strong>${p.name}</strong>
                  <span style="display:block; font-size:0.72rem; color:var(--text-muted);">${p.stock || 0} left • Batch: ${p.batch || 'A1'}</span>
                </div>
                <button class="admin-btn-action btn-success" onclick="window.DC_APP.adjustStock('${p.id}', 5)">+5 Restock</button>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}

      <!-- Recent Orders Section -->
      <div class="admin-card">
        <div class="admin-card-header">
          <h4 class="admin-card-title">Recent Boutique Sales & Tailoring Orders</h4>
          <button class="admin-btn-action" onclick="window.DC_APP.switchAdminTab('orders')">View All Orders →</button>
        </div>
        <div class="admin-table-wrap">
          <table class="admin-table">
            <thead>
              <tr>
                <th>Order #</th>
                <th>Customer</th>
                <th>Garment Ordered</th>
                <th>Total</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${orders.slice(0, 5).map(o => `
                <tr>
                  <td><strong>#${o.orderId}</strong><br><span style="font-size:0.7rem; color:var(--text-muted);">${o.date}</span></td>
                  <td>${o.customer || 'Client'}</td>
                  <td>${(o.items || []).map(i => `${i.name} (${i.size || 'Std'})`).join(', ')}</td>
                  <td><strong>${formatMoney(o.total)}</strong></td>
                  <td><span class="status-badge ${getStatusBadgeClass(o.status)}">${o.status}</span></td>
                  <td>
                    <button class="admin-btn-action" onclick="window.DC_APP.whatsappCustomerOrder('${o.orderId}')" title="Message via WhatsApp">
                      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <span>WhatsApp</span>
                    </button>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Quick Database Management -->
      <div class="admin-card" style="background:#FAF8F5;">
        <div class="admin-card-header">
          <div>
            <h4 class="admin-card-title">Store Data & Backup Management</h4>
            <span style="font-size:0.75rem; color:var(--text-muted);">Export or restore your boutique products, batches, and sales history.</span>
          </div>
          <div style="display:flex; gap:8px;">
            <button class="admin-btn-action" onclick="window.DC_APP.exportStoreData()">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span>Export Store JSON</span>
            </button>
            <button class="admin-btn-action btn-danger" onclick="window.DC_APP.resetStoreData()">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
              <span>Reset to Seed Defaults</span>
            </button>
          </div>
        </div>
      </div>
    `;
  }

  function getStatusBadgeClass(status) {
    if (!status) return 'in-stock';
    const s = status.toLowerCase();
    if (s.includes('deliver') || s.includes('complete')) return 'delivered';
    if (s.includes('tailor')) return 'tailoring';
    if (s.includes('pickup')) return 'pickup';
    if (s.includes('dispatch') || s.includes('courier')) return 'dispatched';
    return 'low-stock';
  }

  function renderAdminProducts(container) {
    const products = DB.products || [];
    const editItem = adminEditingProductId ? products.find(p => p.id === adminEditingProductId) : null;
    const showForm = adminShowNewProductForm || !!editItem;

    container.innerHTML = `
      <div class="admin-card-header">
        <div>
          <h4 class="admin-card-title">Manage Products, Prices & Available Ages</h4>
          <span style="font-size:0.75rem; color:var(--text-muted);">Adjust garment prices and ages inline, or upload new atelier creations.</span>
        </div>
        <button class="btn-primary" style="padding:8px 16px; font-size:0.78rem;" onclick="window.DC_APP.toggleProductForm()">
          ${showForm ? 'Close Form' : '+ Upload New Garment'}
        </button>
      </div>

      <!-- Upload / Edit Form -->
      ${showForm ? `
        <div class="admin-card" style="background:#FFFFFF; border:1px solid var(--accent-rose); margin-bottom:20px;">
          <h4 style="font-family:var(--font-serif); font-size:1.1rem; color:var(--text-primary); margin-bottom:14px;">
            ${editItem ? `Edit Garment: ${editItem.name}` : 'Upload New Product to Boutique'}
          </h4>
          <form onsubmit="window.DC_APP.saveAdminProduct(event)">
            <input type="hidden" id="adm-prod-id" value="${editItem ? editItem.id : ''}">
            
            <div class="form-grid-2">
              <div class="form-group">
                <label class="form-label">Garment Name *</label>
                <input type="text" id="adm-prod-name" class="form-input" required value="${editItem ? editItem.name : ''}" placeholder="e.g. Royal Emerald Tulle Ballgown">
              </div>
              <div class="form-group">
                <label class="form-label">Category *</label>
                <select id="adm-prod-cat" class="form-select">
                  <option value="Children's Wear" ${editItem && editItem.category === "Children's Wear" ? 'selected' : ''}>Children's Wear</option>
                  <option value="Bespoke Lounge Wear" ${editItem && editItem.category === "Bespoke Lounge Wear" ? 'selected' : ''}>Bespoke Lounge Wear</option>
                </select>
              </div>
            </div>

            <div class="form-grid-2">
              <div class="form-group">
                <label class="form-label">Selling Price (₦) *</label>
                <input type="number" id="adm-prod-price" class="form-input" required value="${editItem ? editItem.price : 10000}" placeholder="35000">
              </div>
              <div class="form-group">
                <label class="form-label">Original / Compare Price (₦)</label>
                <input type="number" id="adm-prod-orig-price" class="form-input" value="${editItem && editItem.originalPrice ? editItem.originalPrice : ''}" placeholder="42000">
              </div>
            </div>

            <div class="form-grid-2">
              <div class="form-group">
                <label class="form-label">Available Ages & Sizes (comma-separated) *</label>
                <input type="text" id="adm-prod-sizes" class="form-input" required value="${editItem ? (editItem.sizes || []).join(', ') : '3 Years, 4 Years, 6 Years, Custom Bespoke'}" placeholder="3 Years, 4 Years, 6 Years, Custom Bespoke">
                <span style="font-size:0.7rem; color:var(--text-muted);">e.g. 3 Years, 4 Years, 7-8 Years, Regular Flannel (All Sizes)</span>
              </div>
              <div class="form-group">
                <label class="form-label">Batch Code & Initial Stock *</label>
                <div style="display:flex; gap:8px;">
                  <input type="text" id="adm-prod-batch" class="form-input" value="${editItem ? (editItem.batch || 'BATCH-2026-A1') : 'BATCH-2026-A1'}" placeholder="Batch #" style="flex:1;">
                  <input type="number" id="adm-prod-stock" class="form-input" value="${editItem ? (editItem.stock || 5) : 5}" placeholder="Units" style="width:80px;">
                </div>
              </div>
            </div>

            <div class="form-grid-2">
              <div class="form-group">
                <label class="form-label">Lead Time</label>
                <input type="text" id="adm-prod-lead" class="form-input" value="${editItem ? (editItem.leadTime || '2-3 days tailoring') : '2-3 days tailoring'}" placeholder="2-3 days tailoring">
              </div>
              <div class="form-group">
                <label class="form-label">Boutique Badge / Tag</label>
                <input type="text" id="adm-prod-badge" class="form-input" value="${editItem ? (editItem.badge || '') : 'New Arrival'}" placeholder="e.g. Bestseller, Heirloom Edition">
              </div>
            </div>

            <!-- Image Uploader -->
            <div class="form-group">
              <label class="form-label">Product Image (Upload File or Enter Image Path) *</label>
              <div style="display:flex; gap:10px; align-items:center;">
                <input type="file" id="adm-file-input" class="form-input" accept="image/*" onchange="window.DC_APP.handleProductImageUpload(this)" style="padding:6px; flex:1;">
                <input type="text" id="adm-prod-image" class="form-input" value="${editItem ? editItem.image : 'images/couture-pink-rosette-gown-storefront.jpeg'}" placeholder="images/..." style="flex:1;">
              </div>
              <div style="margin-top:8px;">
                <img id="adm-img-preview" src="${editItem ? editItem.image : ''}" style="width:60px; height:60px; object-fit:cover; border-radius:var(--radius-sm); border:1px solid var(--border-light); display:${editItem ? 'block' : 'none'};">
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Garment Description</label>
              <textarea id="adm-prod-desc" class="form-textarea" rows="2" placeholder="Fabric details, handcrafted features, styling advice...">${editItem ? editItem.description : ''}</textarea>
            </div>

            <div style="display:flex; gap:10px; margin-top:14px;">
              <button type="submit" class="btn-primary" style="flex:1;">${editItem ? 'Save Updates' : 'Add to Catalog'}</button>
              <button type="button" class="btn-secondary" style="flex:1;" onclick="window.DC_APP.cancelProductEdit()">Cancel</button>
            </div>
          </form>
        </div>
      ` : ''}

      <!-- Products Catalog Table -->
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Garment</th>
              <th>Category</th>
              <th>Price (₦) [Quick Edit]</th>
              <th>Available Ages / Sizes [Quick Edit]</th>
              <th>Batch / Stock</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            ${products.map(p => `
              <tr>
                <td>
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="${p.image}" class="admin-thumb" onerror="this.src='images/brand-logo.jpeg'">
                    <div>
                      <strong style="display:block; font-size:0.86rem;">${p.name}</strong>
                      <span style="font-size:0.72rem; color:var(--text-muted);">${p.id} • ${p.badge || 'Standard'}</span>
                    </div>
                  </div>
                </td>
                <td><span style="font-size:0.78rem;">${p.category}</span></td>
                <td>
                  <div style="display:flex; align-items:center; gap:4px;">
                    <span style="font-weight:700;">₦</span>
                    <input type="number" class="admin-inline-input" value="${p.price}" onchange="window.DC_APP.updateProductPriceInline('${p.id}', this.value)" style="width:85px;">
                  </div>
                </td>
                <td>
                  <input type="text" class="admin-inline-input" value="${(p.sizes || []).join(', ')}" onchange="window.DC_APP.updateProductSizesInline('${p.id}', this.value)" style="width:200px; font-size:0.74rem;">
                </td>
                <td>
                  <span style="font-size:0.75rem; font-weight:700;">${p.batch || 'A1'}</span><br>
                  <span class="status-badge ${(p.stock || 0) <= 0 ? 'out-of-stock' : ((p.stock || 0) <= 4 ? 'low-stock' : 'in-stock')}">${p.stock || 0} units</span>
                </td>
                <td>
                  <div style="display:flex; gap:6px;">
                    <button class="admin-btn-action" onclick="window.DC_APP.editProductFull('${p.id}')" title="Edit Full Details">Edit</button>
                    <button class="admin-btn-action btn-danger" onclick="window.DC_APP.deleteAdminProduct('${p.id}')" title="Delete Product">Delete</button>
                  </div>
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  }

  function handleProductImageUpload(input) {
    if (input.files && input.files[0]) {
      const reader = new FileReader();
      reader.onload = function(e) {
        const pathInput = document.getElementById('adm-prod-image');
        if (pathInput) pathInput.value = e.target.result;
        const preview = document.getElementById('adm-img-preview');
        if (preview) {
          preview.src = e.target.result;
          preview.style.display = 'block';
        }
      };
      reader.readAsDataURL(input.files[0]);
    }
  }

  function toggleProductForm() {
    adminShowNewProductForm = !adminShowNewProductForm;
    adminEditingProductId = null;
    renderAdminTab('products');
  }

  function editProductFull(id) {
    adminEditingProductId = id;
    adminShowNewProductForm = true;
    renderAdminTab('products');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function cancelProductEdit() {
    adminEditingProductId = null;
    adminShowNewProductForm = false;
    renderAdminTab('products');
  }

  function saveAdminProduct(e) {
    if (e) e.preventDefault();
    const id = document.getElementById('adm-prod-id')?.value || ('PROD-' + Date.now().toString().slice(-4));
    const name = document.getElementById('adm-prod-name')?.value.trim();
    const category = document.getElementById('adm-prod-cat')?.value || "Children's Wear";
    const price = parseInt(document.getElementById('adm-prod-price')?.value, 10) || 10000;
    const origPrice = parseInt(document.getElementById('adm-prod-orig-price')?.value, 10) || (price + 5000);
    const sizesStr = document.getElementById('adm-prod-sizes')?.value || '3-4 Years, Custom Bespoke';
    const sizes = sizesStr.split(',').map(s => s.trim()).filter(Boolean);
    const batch = document.getElementById('adm-prod-batch')?.value.trim() || 'BATCH-2026-A1';
    const stock = parseInt(document.getElementById('adm-prod-stock')?.value, 10) || 5;
    const leadTime = document.getElementById('adm-prod-lead')?.value.trim() || '2-3 days tailoring';
    const badge = document.getElementById('adm-prod-badge')?.value.trim() || 'Atelier Piece';
    const image = document.getElementById('adm-prod-image')?.value.trim() || 'images/couture-pink-rosette-gown-storefront.jpeg';
    const desc = document.getElementById('adm-prod-desc')?.value.trim() || '';

    const existingIdx = DB.products.findIndex(p => p.id === id);
    const prodObj = {
      id,
      name,
      category,
      subcategory: category === "Children's Wear" ? "Dresses & Gowns" : "Lounge Trousers & Sets",
      price,
      originalPrice: origPrice,
      rating: 5.0,
      reviewsCount: 1,
      badge,
      isBespoke: true,
      sizes,
      stock,
      batch,
      colors: ["Bespoke Palette"],
      fabric: desc ? desc.slice(0, 60) : "Handcrafted Natural Fabric",
      leadTime,
      description: desc || name,
      editorialQuote: "Handcrafted luxury tailored in our 164 Udoumana Street atelier.",
      tags: [category.toLowerCase().includes('kids') ? 'kids' : 'lounge', 'bespoke'],
      careInstructions: "Machine wash delicate or dry clean.",
      image,
      gallery: [image],
      svgId: category === "Children's Wear" ? "svg-linen-dress" : "svg-satin-pj"
    };

    if (existingIdx > -1) {
      DB.products[existingIdx] = Object.assign({}, DB.products[existingIdx], prodObj);
      showToast(`Updated product: ${name}`);
    } else {
      DB.products.unshift(prodObj);
      showToast(`Added new product: ${name}`);
    }

    saveDb(DB);
    adminEditingProductId = null;
    adminShowNewProductForm = false;
    renderProducts();
    renderAdminTab('products');
  }

  function updateProductPriceInline(id, newPrice) {
    const p = DB.products.find(item => item.id === id);
    if (p) {
      p.price = parseInt(newPrice, 10) || p.price;
      saveDb(DB);
      renderProducts();
      showToast(`Updated price for ${p.name}: ₦${p.price.toLocaleString()}`);
    }
  }

  function updateProductSizesInline(id, newSizesStr) {
    const p = DB.products.find(item => item.id === id);
    if (p) {
      p.sizes = newSizesStr.split(',').map(s => s.trim()).filter(Boolean);
      saveDb(DB);
      renderProducts();
      showToast(`Updated available ages for ${p.name}`);
    }
  }

  function deleteAdminProduct(id) {
    if (!confirm('Are you sure you want to delete this garment from the boutique catalog?')) return;
    DB.products = DB.products.filter(p => p.id !== id);
    saveDb(DB);
    renderProducts();
    renderAdminTab('products');
    showToast('Garment deleted from catalog');
  }

  function renderAdminInventory(container) {
    const products = DB.products || [];

    container.innerHTML = `
      <div class="admin-card-header">
        <div>
          <h4 class="admin-card-title">Inventory & Batch Management</h4>
          <span style="font-size:0.75rem; color:var(--text-muted);">Monitor atelier stock counts, track fabric batch numbers, and restock units in 1-click.</span>
        </div>
      </div>

      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Garment & SKU</th>
              <th>Batch ID [Edit]</th>
              <th>Units On Hand</th>
              <th>Status</th>
              <th>Quick Stock Adjustment</th>
            </tr>
          </thead>
          <tbody>
            ${products.map(p => `
              <tr>
                <td>
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="${p.image}" class="admin-thumb" onerror="this.src='images/brand-logo.jpeg'">
                    <div>
                      <strong>${p.name}</strong>
                      <span style="display:block; font-size:0.72rem; color:var(--text-muted);">${p.id}</span>
                    </div>
                  </div>
                </td>
                <td>
                  <input type="text" class="admin-inline-input" value="${p.batch || 'BATCH-2026-A1'}" onchange="window.DC_APP.updateProductBatchInline('${p.id}', this.value)" style="width:140px;">
                </td>
                <td>
                  <span style="font-size:1.1rem; font-weight:700;">${p.stock || 0}</span>
                </td>
                <td>
                  <span class="status-badge ${(p.stock || 0) <= 0 ? 'out-of-stock' : ((p.stock || 0) <= 4 ? 'low-stock' : 'in-stock')}">
                    ${(p.stock || 0) <= 0 ? 'Out of Stock' : ((p.stock || 0) <= 4 ? 'Low Stock' : 'In Stock')}
                  </span>
                </td>
                <td>
                  <div style="display:flex; gap:4px; align-items:center;">
                    <button class="admin-btn-action" onclick="window.DC_APP.adjustStock('${p.id}', -1)" title="Minus 1">-1</button>
                    <button class="admin-btn-action btn-success" onclick="window.DC_APP.adjustStock('${p.id}', 1)" title="Add 1">+1</button>
                    <button class="admin-btn-action btn-success" onclick="window.DC_APP.adjustStock('${p.id}', 5)" title="Add 5">+5 Restock</button>
                  </div>
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  }

  function adjustStock(id, delta) {
    const p = DB.products.find(item => item.id === id);
    if (p) {
      p.stock = Math.max(0, (p.stock || 0) + delta);
      saveDb(DB);
      renderAdminTab(adminActiveTab);
      showToast(`${p.name} stock updated: ${p.stock} units`);
    }
  }

  function updateProductBatchInline(id, newBatch) {
    const p = DB.products.find(item => item.id === id);
    if (p) {
      p.batch = newBatch.trim();
      saveDb(DB);
      showToast(`Batch updated to: ${p.batch}`);
    }
  }

  function renderAdminOrders(container) {
    const orders = DB.orders || [];

    container.innerHTML = `
      <div class="admin-card-header">
        <div>
          <h4 class="admin-card-title">Customer Orders & Sales Dispatch</h4>
          <span style="font-size:0.75rem; color:var(--text-muted);">Manage tailoring workflow, update statuses, notify clients via WhatsApp, or record walk-in boutique sales.</span>
        </div>
        <button class="btn-primary" style="padding:8px 16px; font-size:0.78rem;" onclick="window.DC_APP.toggleWalkInSaleForm()">
          ${adminShowWalkInSaleForm ? 'Close Form' : '+ Record Boutique Walk-in Sale'}
        </button>
      </div>

      <!-- Walk-in Sale Form -->
      ${adminShowWalkInSaleForm ? `
        <div class="admin-card" style="background:#FFFFFF; border:1px solid var(--accent-gold); margin-bottom:20px;">
          <h4 style="font-family:var(--font-serif); font-size:1.1rem; color:var(--text-primary); margin-bottom:12px;">
            Record Walk-In Boutique Sale (164 Udoumana Street)
          </h4>
          <form onsubmit="window.DC_APP.recordWalkInSale(event)">
            <div class="form-grid-2">
              <div class="form-group">
                <label class="form-label">Client Name *</label>
                <input type="text" id="walkin-cust" class="form-input" required placeholder="e.g. Mrs. Aniekeme Bassey">
              </div>
              <div class="form-group">
                <label class="form-label">Client Phone (WhatsApp)</label>
                <input type="tel" id="walkin-phone" class="form-input" placeholder="+234 803 ...">
              </div>
            </div>
            <div class="form-grid-2">
              <div class="form-group">
                <label class="form-label">Select Garment *</label>
                <select id="walkin-prod" class="form-select">
                  ${(DB.products || []).map(p => `
                    <option value="${p.id}">${p.name} - ₦${p.price.toLocaleString()}</option>
                  `).join('')}
                </select>
              </div>
              <div class="form-group">
                <label class="form-label">Size / Age Selected</label>
                <input type="text" id="walkin-size" class="form-input" placeholder="e.g. 4 Years or Adult M" value="Standard">
              </div>
            </div>
            <div class="form-grid-2">
              <div class="form-group">
                <label class="form-label">Quantity</label>
                <input type="number" id="walkin-qty" class="form-input" value="1" min="1">
              </div>
              <div class="form-group">
                <label class="form-label">Payment Method</label>
                <select id="walkin-pay" class="form-select">
                  <option>Cash at Boutique</option>
                  <option>POS Card Swipe at Boutique</option>
                  <option>Direct UBA Bank Transfer (2127888264)</option>
                </select>
              </div>
            </div>
            <div style="display:flex; gap:10px; margin-top:10px;">
              <button type="submit" class="btn-primary" style="flex:1;">Confirm & Record Sale</button>
              <button type="button" class="btn-secondary" style="flex:1;" onclick="window.DC_APP.toggleWalkInSaleForm()">Cancel</button>
            </div>
          </form>
        </div>
      ` : ''}

      <!-- Orders List -->
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Order ID</th>
              <th>Customer & Contact</th>
              <th>Items & Sizing</th>
              <th>Total</th>
              <th>Tailoring / Delivery Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            ${orders.map(o => `
              <tr>
                <td>
                  <strong>#${o.orderId}</strong><br>
                  <span style="font-size:0.7rem; color:var(--text-muted);">${o.date}</span>
                </td>
                <td>
                  <strong>${o.customer || 'Customer'}</strong><br>
                  <span style="font-size:0.72rem; color:var(--text-muted);">${o.phone || '+234 708 522 2212'}</span><br>
                  <span style="font-size:0.7rem; color:var(--text-muted);">${o.deliveryMethod || 'Doorstep Delivery'}</span>
                </td>
                <td>
                  ${(o.items || []).map(i => `
                    <div style="font-size:0.78rem;">• ${i.name} [${i.size || 'Standard'}] x${i.quantity || 1}</div>
                  `).join('')}
                </td>
                <td><strong>${formatMoney(o.total)}</strong></td>
                <td>
                  <select class="form-select" style="padding:4px 8px; font-size:0.74rem;" onchange="window.DC_APP.updateOrderStatus('${o.orderId}', this.value)">
                    <option value="Pending Review" ${o.status === 'Pending Review' ? 'selected' : ''}>Pending Review</option>
                    <option value="Tailoring in Atelier (Uyo)" ${o.status === 'Tailoring in Atelier (Uyo)' || o.status.includes('Tailoring') ? 'selected' : ''}>Tailoring in Atelier (Uyo)</option>
                    <option value="Ready for Pickup (164 Udoumana)" ${o.status.includes('Pickup') ? 'selected' : ''}>Ready for Pickup (164 Udoumana)</option>
                    <option value="Dispatched with Courier" ${o.status.includes('Dispatch') ? 'selected' : ''}>Dispatched with Courier</option>
                    <option value="Delivered" ${o.status === 'Delivered' ? 'selected' : ''}>Delivered & Completed</option>
                  </select>
                </td>
                <td>
                  <button class="admin-btn-action" onclick="window.DC_APP.whatsappCustomerOrder('${o.orderId}')" title="Message Client via WhatsApp">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                    <span>Notify Client</span>
                  </button>
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  }

  function toggleWalkInSaleForm() {
    adminShowWalkInSaleForm = !adminShowWalkInSaleForm;
    renderAdminTab('orders');
  }

  function updateOrderStatus(orderId, newStatus) {
    const ord = DB.orders.find(o => o.orderId === orderId);
    if (ord) {
      ord.status = newStatus;
      saveDb(DB);
      showToast(`Order #${orderId} marked as: ${newStatus}`);
    }
  }

  function whatsappCustomerOrder(orderId) {
    const ord = DB.orders.find(o => o.orderId === orderId);
    if (!ord) return;
    const phone = ord.phone ? ord.phone.replace(/[^0-9]/g, '') : '2347085222212';
    const itemsList = (ord.items || []).map(i => i.name).join(', ');
    const msg = `Hello ${ord.customer || 'Valued Client'}! 👑%0AUpdate from Debbie's Collection (164 Udoumana Street, Uyo):%0AYour order *#${ord.orderId}* (${itemsList}) status is now: *${ord.status}*.%0AOrder Total: ₦${(ord.total || 0).toLocaleString()}.%0AThank you for shopping at Debbie's Collection!`;
    window.open(`https://wa.me/${phone}?text=${msg}`, '_blank');
  }

  function recordWalkInSale(e) {
    if (e) e.preventDefault();
    const custName = document.getElementById('walkin-cust')?.value || 'Walk-in Boutique Client';
    const custPhone = document.getElementById('walkin-phone')?.value || '+234 708 522 2212';
    const prodId = document.getElementById('walkin-prod')?.value;
    const qty = parseInt(document.getElementById('walkin-qty')?.value, 10) || 1;
    const size = document.getElementById('walkin-size')?.value || 'Standard';
    const payMethod = document.getElementById('walkin-pay')?.value || 'Cash at Boutique';
    const prod = DB.products.find(p => p.id === prodId) || DB.products[0];
    const total = prod.price * qty;

    const newOrder = {
      orderId: 'DC-UYO-' + Math.floor(1000 + Math.random() * 9000),
      date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
      items: [{ name: prod.name, size, price: prod.price, quantity: qty }],
      subtotal: total,
      shipping: 0,
      total: total,
      deliveryMethod: payMethod + ' (164 Udoumana Boutique)',
      status: 'Delivered',
      customer: custName,
      phone: custPhone
    };

    DB.orders.unshift(newOrder);
    if (prod.stock) prod.stock = Math.max(0, prod.stock - qty);
    saveDb(DB);
    adminShowWalkInSaleForm = false;
    showToast(`Recorded walk-in sale: ₦${total.toLocaleString()}`);
    renderAdminTab('orders');
  }

  function renderAdminDiscounts(container) {
    const promos = DB.promoCodes || {};
    const promoKeys = Object.keys(promos);

    container.innerHTML = `
      <div class="admin-card-header">
        <div>
          <h4 class="admin-card-title">Promotions & Discount Codes</h4>
          <span style="font-size:0.75rem; color:var(--text-muted);">Create boutique promo codes (% off, flat ₦ discount, or free delivery) to boost festive sales.</span>
        </div>
      </div>

      <!-- Add Promo Code Form -->
      <div class="admin-card" style="background:#FFFFFF; border:1px solid var(--border-light); margin-bottom:20px;">
        <h4 style="font-family:var(--font-serif); font-size:1.1rem; color:var(--text-primary); margin-bottom:12px;">
          Create New Promo Code
        </h4>
        <form onsubmit="window.DC_APP.createPromoCode(event)">
          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Promo Code *</label>
              <input type="text" id="new-promo-code" class="form-input" required placeholder="e.g. UYO2026" style="text-transform:uppercase;">
            </div>
            <div class="form-group">
              <label class="form-label">Discount Type *</label>
              <select id="new-promo-type" class="form-select">
                <option value="percent">Percentage (%) Off</option>
                <option value="flat">Flat Amount (₦) Off</option>
                <option value="shipping">Free Shipping</option>
              </select>
            </div>
          </div>
          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Discount Value (e.g. 15 for 15% or 5000 for ₦5,000) *</label>
              <input type="number" id="new-promo-val" class="form-input" required placeholder="15">
            </div>
            <div class="form-group">
              <label class="form-label">Description for Customer</label>
              <input type="text" id="new-promo-desc" class="form-input" placeholder="e.g. 15% Weekend Special">
            </div>
          </div>
          <button type="submit" class="btn-primary" style="margin-top:8px;">Activate Promo Code</button>
        </form>
      </div>

      <!-- Active Promo Codes Table -->
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead>
            <tr>
              <th>Code Name</th>
              <th>Discount Type</th>
              <th>Value</th>
              <th>Description</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            ${promoKeys.map(k => {
              const p = promos[k];
              return `
                <tr>
                  <td><strong style="color:var(--accent-rose); letter-spacing:0.05em;">${k}</strong></td>
                  <td>${p.type === 'percent' ? 'Percentage' : (p.type === 'flat' ? 'Flat Naira' : 'Free Shipping')}</td>
                  <td><strong>${p.type === 'percent' ? p.value + '%' : (p.type === 'flat' ? '₦' + p.value.toLocaleString() : '100% Free')}</strong></td>
                  <td>${p.desc || 'Special Promotion'}</td>
                  <td><span class="status-badge in-stock">Active</span></td>
                  <td>
                    <button class="admin-btn-action btn-danger" onclick="window.DC_APP.deletePromoCode('${k}')">Remove</button>
                  </td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
    `;
  }

  function createPromoCode(e) {
    if (e) e.preventDefault();
    const code = document.getElementById('new-promo-code')?.value.trim().toUpperCase();
    const type = document.getElementById('new-promo-type')?.value || 'percent';
    const val = parseInt(document.getElementById('new-promo-val')?.value, 10) || 10;
    const desc = document.getElementById('new-promo-desc')?.value.trim() || `${val}% Off Special`;

    if (!code) return;
    DB.promoCodes[code] = { type, value: val, desc, active: true };
    saveDb(DB);
    showToast(`Promo code ${code} activated!`);
    renderAdminTab('discounts');
  }

  function deletePromoCode(code) {
    if (!confirm(`Delete promo code ${code}?`)) return;
    delete DB.promoCodes[code];
    saveDb(DB);
    showToast(`Deleted promo code: ${code}`);
    renderAdminTab('discounts');
  }

  function exportStoreData() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(DB, null, 2));
    const dlAnchor = document.createElement('a');
    dlAnchor.setAttribute("href", dataStr);
    dlAnchor.setAttribute("download", `debbies_collection_backup_${Date.now()}.json`);
    dlAnchor.click();
    showToast('Store data downloaded as JSON backup');
  }

  function resetStoreData() {
    if (!confirm('Reset entire store catalog, batches, and orders to default factory seeds?')) return;
    localStorage.removeItem(STORAGE_KEY);
    DB = JSON.parse(JSON.stringify(DEFAULT_DB));
    DB.products = JSON.parse(JSON.stringify(window.DC_PRODUCTS || []));
    saveDb(DB);
    renderProducts();
    renderAdminTab('overview');
    showToast('Store reset to factory seed defaults');
  }

  // --- Expose Public API on window.DC_APP ---
  window.DC_APP = {
    setCurrency,
    focusSearch,
    handleSearch,
    clearSearch,
    handleSort,
    filterCategory,
    filterAge,
    toggleBespokeOnly,
    clearAllFilters,
    toggleWishlist,
    addToCart,
    removeFromCart,
    updateCartQty,
    applyPromoCode,
    checkoutViaWhatsApp,
    openCartDrawer,
    closeCartDrawer,
    toggleMobileNav,
    openQuickView,
    closeQuickViewModal,
    handleQvSizeChange,
    submitQuickView,
    proceedToCheckout,
    goToCheckoutStep,
    updateCheckoutShipping,
    selectMeasurementOption,
    selectPaymentMethod,
    autofillTestCard,
    copyAccountNumber,
    processOrderPayment,
    confirmOtp,
    closeOtpModal,
    notifyWhatsAppOrder,
    closeCheckoutModal,
    openAccountModal,
    closeAccountModal,
    switchAccountTab,
    saveProfile,
    saveMeasurements,
    openConsultationModal,
    closeConsultationModal,
    submitConsultation,
    openReviewModal,
    closeReviewModal,
    submitReview,
    toggleFaq,
    showToast,
    // Admin Suite API
    openAdminPortal,
    openAdminPinModal,
    closeAdminPinModal,
    verifyAdminPin,
    openAdminModal,
    closeAdminModal,
    switchAdminTab,
    toggleProductForm,
    editProductFull,
    cancelProductEdit,
    saveAdminProduct,
    handleProductImageUpload,
    updateProductPriceInline,
    updateProductSizesInline,
    updateProductBatchInline,
    adjustStock,
    deleteAdminProduct,
    toggleWalkInSaleForm,
    updateOrderStatus,
    whatsappCustomerOrder,
    recordWalkInSale,
    createPromoCode,
    deletePromoCode,
    exportStoreData,
    resetStoreData
  };

  // Run on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderAll);
  } else {
    renderAll();
  }

})();
'''

