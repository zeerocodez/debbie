# -*- coding: utf-8 -*-
"""
HTML structure and markup generator for Debbie's Collection.
"""
from builder.svg_assets import get_product_svg, get_uyo_map_svg
from builder.products_data import PRODUCTS, SAMPLE_REVIEWS

def get_header_html():
    return '''<!-- Top Announcement Bar -->
<div class="top-announcement-bar">
  <div class="container announcement-inner">
    <div class="announcement-location">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      <span>164 Udoumana Street, Uyo, Akwa Ibom</span>
    </div>
    <div class="announcement-center">
      <span class="announcement-badge">Atelier Made</span>
      <span>Complimentary Uyo Doorstep Delivery on orders over ₦45,000 • Bespoke Worldwide</span>
    </div>
    <div class="announcement-actions">
      <div class="currency-select-wrap">
        <label for="currency-select">Currency:</label>
        <select id="currency-select" onchange="window.DC_APP.setCurrency(this.value)">
          <option value="NGN" selected>NGN (₦)</option>
          <option value="USD">USD ($)</option>
          <option value="GBP">GBP (£)</option>
        </select>
      </div>
      <a href="tel:+2347085222212" class="announcement-tel">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span>+234 708 522 2212</span>
      </a>
    </div>
  </div>
</div>

<!-- Main Sticky Header -->
<header class="main-header" id="main-header">
  <div class="container header-container">
    <div class="header-left">
      <button class="mobile-menu-btn" onclick="window.DC_APP.toggleMobileNav()" aria-label="Open Navigation Menu">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
      <a href="#hero" class="brand-logo-link">
        <div class="brand-crest-box">
          <img src="images/brand-logo.jpeg" alt="Debbie's Collection" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" style="width:100%; height:100%; object-fit:cover;">
          <span class="brand-crest-text" style="display:none;">DC</span>
        </div>
        <div class="brand-text-block">
          <span class="brand-name">Debbie's Collection</span>
          <span class="brand-subline">Uyo • Akwa Ibom Atelier</span>
        </div>
      </a>
    </div>

    <nav class="desktop-nav" aria-label="Primary Navigation">
      <a href="#shop" class="nav-link" onclick="window.DC_APP.filterCategory('All')">The Collection</a>
      <a href="#shop" class="nav-link" onclick="window.DC_APP.filterCategory('Children\\'s Wear')">Children's Wear</a>
      <a href="#shop" class="nav-link" onclick="window.DC_APP.filterCategory('Bespoke Lounge Wear')">Bespoke Loungewear</a>
      <a href="#atelier-story" class="nav-link">The Atelier</a>
      <a href="#boutique-visit" class="nav-link">Visit Boutique</a>
    </nav>

    <div class="header-right">
      <button class="header-action-btn" onclick="window.DC_APP.focusSearch()" title="Search catalog" aria-label="Search">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </button>
      <button class="header-action-btn" onclick="window.DC_APP.openAccountModal('wishlist')" title="Wishlist" aria-label="Wishlist">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
        <span class="header-badge" id="wishlist-counter-badge">0</span>
      </button>
      <button class="header-action-btn" onclick="window.DC_APP.openAccountModal('profile')" title="My Account" aria-label="Customer Account">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </button>
      <button class="header-cart-summary" onclick="window.DC_APP.openCartDrawer()" aria-label="Shopping Bag">
        <div style="position:relative;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
          <span class="header-badge" id="cart-counter-badge">0</span>
        </div>
        <div class="cart-summary-text">
          <span class="cart-summary-label">Bag</span>
          <span class="cart-summary-total" id="cart-header-subtotal">₦0</span>
        </div>
      </button>
    </div>
  </div>
</header>
'''

def get_marquee_html():
    return '''<!-- Marquee Ticker -->
<div class="marquee-ticker" aria-hidden="true">
  <div class="marquee-track">
    <div class="marquee-item"><span class="marquee-bullet">✦</span> 164 UDOUMANA STREET ATELIER, UYO</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> PURE NATURAL FIBRES & HEIRLOOM LINENS</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> CHILDREN'S GALA BALLGOWNS & BESPOKE LOUNGE</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> MADE-TO-MEASURE BESPOKE MEASUREMENT BOOK</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> PRIVATE IN-BOUTIQUE FITTING SESSIONS</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> DOORSTEP DELIVERY ACROSS NIGERIA & WORLDWIDE</div>
    <!-- Duplicate for infinite loop -->
    <div class="marquee-item"><span class="marquee-bullet">✦</span> 164 UDOUMANA STREET ATELIER, UYO</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> PURE NATURAL FIBRES & HEIRLOOM LINENS</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> CHILDREN'S GALA BALLGOWNS & BESPOKE LOUNGE</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> MADE-TO-MEASURE BESPOKE MEASUREMENT BOOK</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> PRIVATE IN-BOUTIQUE FITTING SESSIONS</div>
    <div class="marquee-item"><span class="marquee-bullet">✦</span> DOORSTEP DELIVERY ACROSS NIGERIA & WORLDWIDE</div>
  </div>
</div>
'''

def get_hero_html():
    return '''<!-- Hero Section -->
<section class="hero-section" id="hero">
  <div class="container hero-grid">
    <div class="hero-content">
      <div class="hero-eyebrow-wrap">
        <span class="hero-tag">AW 2026 / 2027 ATELIER EDITION</span>
        <div class="hero-location-tag">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <span>Crafted in Uyo, Akwa Ibom</span>
        </div>
      </div>

      <h1 class="hero-title">
        Where Childhood Elegance Meets <span class="italic-accent">Bespoke Loungewear.</span>
      </h1>

      <p class="hero-description">
        Heirloom children's garments and pure silk-linen loungewear, hand-tailored in our Uyo boutique at 164 Udoumana Street. Made to measure with artisanal craftsmanship, cherished for generations.
      </p>

      <div class="hero-actions">
        <a href="#shop" class="btn-primary" onclick="window.DC_APP.filterCategory('All')">
          <span>Explore The Collection</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </a>
        <button class="btn-secondary" onclick="window.DC_APP.openConsultationModal()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          <span>Book Atelier Fitting</span>
        </button>
      </div>

      <div class="hero-stats">
        <div class="stat-item">
          <span class="stat-number">100%</span>
          <span class="stat-label">Natural Fibres</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">164</span>
          <span class="stat-label">Udoumana St, Uyo</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">4.9★</span>
          <span class="stat-label">Verified Trust</span>
        </div>
      </div>
    </div>

    <!-- Right Hero Visual Frame -->
    <div class="hero-visual-frame">
      <div class="hero-artwork-badge-top">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
        <span>The Udoumana Atelier Masterpiece</span>
      </div>

      <div class="hero-visual-artwork" id="hero-interactive-artwork">
        <img src="images/couture-pink-rosette-gown-storefront.jpeg" alt="Debbie's Collection Haute Couture Gala Ballgown at 164 Udoumana Street, Uyo" style="width:100%; height:100%; max-height:480px; object-fit:cover; object-position:center top; border-radius:var(--radius-md);">
      </div>

      <div class="hero-artwork-badge-bottom">
        <div class="hero-badge-avatar" style="overflow:hidden; padding:0;">
          <img src="images/brand-logo.jpeg" alt="Debbie's Collection" style="width:100%; height:100%; object-fit:cover;">
        </div>
        <div>
          <strong style="display:block; font-size:0.85rem;">The Udoumana Rosette Gala Gown</strong>
          <span style="font-size:0.75rem; color:var(--text-muted);">Photographed outside our Uyo boutique • Bespoke made-to-measure</span>
        </div>
      </div>
    </div>
  </div>
</section>
'''

def get_categories_html():
    return '''<!-- Editorial Categories Showcase -->
<section class="container" style="padding-top:20px;">
  <div class="section-header">
    <span class="section-eyebrow">Curated Universes</span>
    <h2 class="section-title">The Debbie's Collection Wardrobe</h2>
    <p class="section-subtitle">From regal children's ceremonial garments to bespoke tartan loungewear hand-tailored in our Uyo boutique.</p>
  </div>

  <div class="categories-grid">
    <div class="category-card" onclick="window.DC_APP.filterCategory('Children\\'s Wear')">
      <div class="category-visual-wrap">
        <img src="images/couture-white-tulle-ballgown-flowercrown.jpeg" alt="Children's Heirloom & Gala Gowns" loading="lazy">
      </div>
      <h3 class="category-title">Children's Gala & Party Gowns</h3>
      <span class="category-count">Cascading tulle ballgowns, rosette gala pieces & flower-girl dresses</span>
      <div class="category-footer-link">
        <span>Explore Gala Dresses</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </div>
    </div>

    <div class="category-card" onclick="window.DC_APP.filterCategory('Children\\'s Wear')">
      <div class="category-visual-wrap">
        <img src="images/tartan-white-tee-red-skirt.jpeg" alt="Girls' Tartan Pleated Skirts & Pinafores" loading="lazy">
      </div>
      <h3 class="category-title">Tartan Pleated Skirts & Pinafores</h3>
      <span class="category-count">Scottish-inspired knife pleats, matching tees & vintage apron dresses</span>
      <div class="category-footer-link">
        <span>Explore Tartan Sets</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </div>
    </div>

    <div class="category-card" onclick="window.DC_APP.filterCategory('Bespoke Lounge Wear')">
      <div class="category-visual-wrap">
        <img src="images/lounge-tartan-pants-red-buffalo.jpeg" alt="Bespoke Plaid Lounge Trousers" loading="lazy">
      </div>
      <h3 class="category-title">Bespoke Plaid Loungewear</h3>
      <span class="category-count">Signature buffalo check pants, utility cargo trousers & polo sets</span>
      <div class="category-footer-link">
        <span>Explore Loungewear</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </div>
    </div>
  </div>
</section>
'''

def get_shop_catalog_html():
    return '''<!-- Product Discovery & Shop Catalog Section -->
<section class="shop-section" id="shop">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">The Atelier Catalog</span>
      <h2 class="section-title">Discover Handcrafted Luxury</h2>
      <p class="section-subtitle">Filter by category, age group, or made-to-measure bespoke options with live search and custom sizing.</p>
    </div>

    <!-- Filter & Search Toolbar -->
    <div class="shop-toolbar">
      <div class="toolbar-top-row">
        <!-- Live Search Input -->
        <div class="search-box-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="text" id="shop-search-input" class="search-input" placeholder="Search girls dresses, gala ballgowns, pleated tartan skirts, lounge pants..." oninput="window.DC_APP.handleSearch(this.value)">
          <button class="search-clear-btn" id="search-clear-btn" onclick="window.DC_APP.clearSearch()" aria-label="Clear Search">×</button>
        </div>

        <!-- Controls -->
        <div class="toolbar-controls">
          <label class="bespoke-toggle-label">
            <input type="checkbox" id="bespoke-toggle" onchange="window.DC_APP.toggleBespokeOnly(this.checked)">
            <span>Bespoke Made-to-Measure Only</span>
          </label>

          <select class="filter-select" id="sort-select" onchange="window.DC_APP.handleSort(this.value)">
            <option value="featured">Featured Atelier Pieces</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
            <option value="rating">Highest Rated</option>
          </select>
        </div>
      </div>

      <!-- Category Filter Tabs -->
      <div class="category-tabs-scroll" id="category-tabs-row">
        <button class="category-tab-btn active" data-cat="All" onclick="window.DC_APP.filterCategory('All')">All Pieces (<span id="cat-count-all">15</span>)</button>
        <button class="category-tab-btn" data-cat="Children's Wear" onclick="window.DC_APP.filterCategory('Children\\'s Wear')">Children's Wear (<span id="cat-count-kids">10</span>)</button>
        <button class="category-tab-btn" data-cat="Bespoke Lounge Wear" onclick="window.DC_APP.filterCategory('Bespoke Lounge Wear')">Bespoke Loungewear (<span id="cat-count-lounge">5</span>)</button>
      </div>

      <!-- Sub Filter: Age Group & Quick Chips -->
      <div class="sub-filter-row">
        <div class="age-chips-wrap" id="age-filter-chips">
          <span style="font-size:0.75rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-right:4px;">Age / Size:</span>
          <button class="age-chip-btn active" data-age="All" onclick="window.DC_APP.filterAge('All')">All Sizes</button>
          <button class="age-chip-btn" data-age="0-12M" onclick="window.DC_APP.filterAge('0-12M')">0-12 Months</button>
          <button class="age-chip-btn" data-age="1-4Y" onclick="window.DC_APP.filterAge('1-4Y')">1-4 Years</button>
          <button class="age-chip-btn" data-age="5-8Y" onclick="window.DC_APP.filterAge('5-8Y')">5-8 Years</button>
          <button class="age-chip-btn" data-age="9-14Y" onclick="window.DC_APP.filterAge('9-14Y')">9-14 Years</button>
          <button class="age-chip-btn" data-age="Adult" onclick="window.DC_APP.filterAge('Adult')">Adult Loungewear</button>
          <button class="age-chip-btn" data-age="Custom Bespoke" onclick="window.DC_APP.filterAge('Custom Bespoke')">Custom Measurements</button>
        </div>

        <div class="results-count-label" id="results-count-label">
          Showing 15 exquisite atelier creations
        </div>
      </div>
    </div>

    <!-- Active Filters Strip -->
    <div class="active-filters-bar" id="active-filters-bar" style="display:none;"></div>

    <!-- Dynamic Product Cards Grid -->
    <div class="products-grid" id="products-grid">
      <!-- Injected via JavaScript -->
    </div>
  </div>
</section>
'''

def get_studio_html():
    return ''

def get_atelier_html():
    return '''<!-- The Udoumana Atelier Craftsmanship -->
<section class="atelier-section" id="atelier-story">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">The Atelier Standards</span>
      <h2 class="section-title">The Story of 164 Udoumana Street</h2>
      <p class="section-subtitle">Born in Uyo, Akwa Ibom State, Debbie's Collection elevates children's wear and bespoke loungewear with meticulous bespoke tailoring and heirloom natural textiles.</p>
    </div>

    <div class="atelier-features-grid">
      <div class="atelier-feature-card">
        <div class="feature-icon-box">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/></svg>
        </div>
        <h3 class="feature-title">Precision Made-to-Measure</h3>
        <p class="feature-text">Every bespoke garment is drafted to your specific measurements: chest, waist, shoulder-to-hem, and sleeve lengths for children and loungewear.</p>
      </div>

      <div class="atelier-feature-card">
        <div class="feature-icon-box">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 12L2.5 7.5"/></svg>
        </div>
        <h3 class="feature-title">Hypoallergenic Luxury Fibres</h3>
        <p class="feature-text">We source Grade 6A Mulberry silk, organic Turkish flax linen, and GOTS-certified bamboo rayon to ensure supreme softness on delicate infant skin.</p>
      </div>

      <div class="atelier-feature-card">
        <div class="feature-icon-box">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        </div>
        <h3 class="feature-title">Akwa Ibom Sartorial Heritage</h3>
        <p class="feature-text">Integrating traditional Akwete and Aso-Oke handweaving with contemporary British and French tailoring silhouettes for weddings, dedications, and pageants.</p>
      </div>

      <div class="atelier-feature-card">
        <div class="feature-icon-box">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
        </div>
        <h3 class="feature-title">Fast Doorstep Delivery</h3>
        <p class="feature-text">Express same-day bike courier in Uyo, 24-48 hours across Akwa Ibom State, and reliable priority doorstep delivery to Lagos, Abuja, Port Harcourt, and diaspora.</p>
      </div>
    </div>

    <!-- Interactive Measurement Book Guide Banner -->
    <div class="measurement-guide-banner">
      <div class="measurement-text-content">
        <span style="font-size:0.76rem; font-weight:700; text-transform:uppercase; letter-spacing:0.12em; color:var(--accent-gold-light);">Atelier Fitting Convenience</span>
        <h3 class="measurement-title">Save Your Bespoke Measurements Once. Order in 1-Click.</h3>
        <p style="font-size:0.92rem; color:var(--text-light-muted); line-height:1.6;">
          Our digital <strong>Bespoke Measurement Book</strong> records chest, waist, height, and age for your children or yourself. When you order bespoke loungewear or heirloom gowns, our Udoumana tailors tailor directly to your saved profile.
        </p>
        <div style="display:flex; gap:12px; margin-top:8px; flex-wrap:wrap;">
          <button class="btn-primary" style="background:var(--accent-rose); color:#FFFFFF;" onclick="window.DC_APP.openAccountModal('measurements')">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h20"/><path d="M6 8v8"/><path d="M10 9v6"/><path d="M14 8v8"/><path d="M18 9v6"/></svg>
            <span>Open My Measurement Book</span>
          </button>
          <button class="btn-secondary" style="background:rgba(255,255,255,0.1); color:#FFFFFF; border-color:rgba(255,255,255,0.25);" onclick="window.DC_APP.openConsultationModal()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Book Private In-Boutique Fitting</span>
          </button>
        </div>
      </div>

      <div class="measurement-diagram-box">
        <h4 style="font-family:var(--font-serif); font-size:1.1rem; color:var(--text-light);">How We Measure:</h4>
        <div class="measurement-spec-list">
          <div class="measurement-spec-item">
            <span class="spec-name">Chest / Bust</span>
            <span class="spec-desc">Circumference under arms across fullest chest</span>
          </div>
          <div class="measurement-spec-item">
            <span class="spec-name">Natural Waist</span>
            <span class="spec-desc">Natural crease around torso above navel</span>
          </div>
          <div class="measurement-spec-item">
            <span class="spec-name">Shoulder to Hem</span>
            <span class="spec-desc">From top shoulder seam down to desired dress or robe hem</span>
          </div>
          <div class="measurement-spec-item">
            <span class="spec-name">Child Age & Height</span>
            <span class="spec-desc">Allows our pattern-cutters to adjust growth ease</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

def get_reviews_html():
    reviews_cards = ""
    for rev in SAMPLE_REVIEWS:
        initials = "".join([part[0] for part in rev["author"].split() if part[0].isalpha()][:2])
        reviews_cards += f'''
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-quote">“{rev['quote']}”</p>
          <div class="review-author-wrap">
            <div class="author-avatar">{initials}</div>
            <div class="author-meta">
              <span class="author-name">{rev['author']}</span>
              <span class="author-location">{rev['location']} • Verified Client</span>
            </div>
          </div>
        </div>
        '''

    return f'''<!-- Customer Reviews & Social Proof -->
<section class="reviews-section" id="reviews">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Client Love</span>
      <h2 class="section-title">Cherished by Families Across Nigeria</h2>
      <p class="section-subtitle">Real experiences from mothers, fathers, and bridal parties who trust Debbie's Collection for their milestone celebrations.</p>
    </div>

    <div class="reviews-grid">
      {reviews_cards}
    </div>

    <div style="text-align:center; margin-top:36px;">
      <button class="btn-secondary" onclick="window.DC_APP.openReviewModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
        <span>Share Your Review</span>
      </button>
    </div>
  </div>
</section>
'''

def get_boutique_visit_html():
    map_svg = get_uyo_map_svg()
    return f'''<!-- Boutique Visit & Store Locator -->
<section class="boutique-visit-section" id="boutique-visit">
  <div class="container">
    <div class="boutique-visit-card">
      <div class="boutique-info-panel">
        <div>
          <span class="section-eyebrow" style="text-align:left;">Visit Our Atelier</span>
          <h2 class="boutique-address-title">164 Udoumana Street, Uyo</h2>
          <span style="font-size:0.86rem; color:var(--accent-rose); font-weight:700; text-transform:uppercase; letter-spacing:0.06em;">Akwa Ibom State, Nigeria</span>
        </div>

        <p class="boutique-address-text">
          Step into our warm boutique atelier in the heart of Uyo. Browse luxury silk and linen swatches in person, experience private made-to-measure fitting sessions, or pick up your online orders with zero shipping fees.
        </p>

        <div class="boutique-schedule-list">
          <div class="schedule-row">
            <span>Monday – Friday:</span>
            <strong>9:00 AM – 7:00 PM</strong>
          </div>
          <div class="schedule-row">
            <span>Saturday:</span>
            <strong>10:00 AM – 6:00 PM</strong>
          </div>
          <div class="schedule-row">
            <span>Sunday:</span>
            <strong>VIP Private Appointments Only</strong>
          </div>
        </div>

        <div class="boutique-actions">
          <button class="btn-primary" onclick="window.DC_APP.openConsultationModal()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Book Private Fitting Session</span>
          </button>
          <a href="https://wa.me/2347085222212?text=Hello%20Debbie's%20Collection,%20I%20would%20like%20to%20inquire%20about%20a%20fitting%20at%20164%20Udoumana%20Street%20Uyo." target="_blank" rel="noopener" class="btn-secondary" style="border-color:#25D366; color:#128C7E;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            <span>WhatsApp Atelier Concierge</span>
          </a>
        </div>
      </div>

      <div class="boutique-map-panel">
        {map_svg}
      </div>
    </div>
  </div>
</section>
'''

def get_faq_html():
    return '''<!-- FAQ Accordion -->
<section class="faq-section" id="faq">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Frequently Asked</span>
      <h2 class="section-title">Everything You Need to Know</h2>
      <p class="section-subtitle">Answers regarding bespoke tailoring timelines, delivery in Uyo and across Nigeria, sizing, and fabric care.</p>
    </div>

    <div class="faq-container">
      <div class="faq-item" onclick="window.DC_APP.toggleFaq(this)">
        <button class="faq-question-btn">
          <span>How long does bespoke made-to-measure tailoring take?</span>
          <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Ready-to-wear items dispatch within 24 hours. Custom made-to-measure children's dresses and bespoke silk loungewear typically take 3 to 5 business days in our 164 Udoumana Street atelier. Urgent rush orders (48 hours) can be accommodated for birthdays and ceremonies upon request.</p>
        </div>
      </div>

      <div class="faq-item" onclick="window.DC_APP.toggleFaq(this)">
        <button class="faq-question-btn">
          <span>What are the delivery timelines and costs for Uyo and across Nigeria?</span>
          <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>We offer Same-Day / Next-Day doorstep bike delivery within Uyo (₦1,500, or FREE on orders over ₦45,000). For Akwa Ibom State towns (Eket, Ikot Ekpene, Oron), courier takes 24 hours (₦2,500). Nationwide priority delivery across Nigeria (Lagos, Abuja, Port Harcourt, Enugu, etc.) takes 2 to 3 days via GIGL / Speedaf (₦4,500). In-boutique pickup at 164 Udoumana Street is always complimentary.</p>
        </div>
      </div>

      <div class="faq-item" onclick="window.DC_APP.toggleFaq(this)">
        <button class="faq-question-btn">
          <span>How do I take my child's measurements accurately at home?</span>
          <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>You can use a simple soft measuring tape to record chest circumference, waist, and shoulder-to-knee length. Enter these details into your <strong>Bespoke Measurement Book</strong> on our website or provide them in your checkout notes. Our master tailors automatically add comfortable breathing ease.</p>
        </div>
      </div>

      <div class="faq-item" onclick="window.DC_APP.toggleFaq(this)">
        <button class="faq-question-btn">
          <span>Can I request custom length or sizing for gowns and loungewear?</span>
          <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes! All bespoke orders at 164 Udoumana Street, Uyo can be customized to your exact height, chest, and waist measurements using our Bespoke Measurement Book or private boutique fitting sessions.</p>
        </div>
      </div>

      <div class="faq-item" onclick="window.DC_APP.toggleFaq(this)">
        <button class="faq-question-btn">
          <span>How does the boutique online checkout work?</span>
          <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Our online boutique provides bank-grade 256-bit SSL encrypted checkout supporting instant cards with 3D Secure verification, direct verified bank transfers to our Debbie's Collection UBA account, and pay-on-pickup at 164 Udoumana Street, Uyo. Every confirmed order generates an instant printable digital invoice and WhatsApp tracking link.</p>
        </div>
      </div>

      <div class="faq-item" onclick="window.DC_APP.toggleFaq(this)">
        <button class="faq-question-btn">
          <span>Can I book a private fitting consultation at the boutique?</span>
          <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Absolutely. You can schedule a private fitting at 164 Udoumana Street, Uyo using our online booking calendar. Enjoy one-on-one consultation with our creative director, fabric sampling, and bespoke pattern drafting in a comfortable, child-friendly setting.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

def get_footer_html():
    return '''<!-- Site Footer -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand-col">
        <div class="brand-crest-box" style="width:40px; height:40px;">
          <img src="images/brand-logo.jpeg" alt="Debbie's Collection" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" style="width:100%; height:100%; object-fit:cover;">
          <span class="brand-crest-text" style="display:none; font-size:1.1rem;">DC</span>
        </div>
        <span class="brand-name" style="color:var(--text-light); font-size:1.25rem;">Debbie's Collection</span>
        <p style="font-size:0.86rem; color:var(--text-light-muted); line-height:1.6; max-width:320px;">
          Luxury children's wear and bespoke loungewear crafted with pure natural fibres and heirloom sartorial devotion at 164 Udoumana Street, Uyo, Akwa Ibom State.
        </p>
        <div style="display:flex; align-items:center; gap:8px; color:var(--accent-gold-light); font-size:0.82rem; font-weight:600;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <span>Verified 256-Bit SSL Checkout</span>
        </div>
      </div>

      <div>
        <h4 class="footer-col-title">The Collections</h4>
        <ul class="footer-links-list">
          <li><a href="#shop" onclick="window.DC_APP.filterCategory('Children\\'s Wear')">Children's Gala Gowns</a></li>
          <li><a href="#shop" onclick="window.DC_APP.filterCategory('Children\\'s Wear')">Tartan Pleated Skirts</a></li>
          <li><a href="#shop" onclick="window.DC_APP.filterCategory('Children\\'s Wear')">Heirloom Lace & Tulle Dresses</a></li>
          <li><a href="#shop" onclick="window.DC_APP.filterCategory('Bespoke Lounge Wear')">Buffalo Check Lounge Pants</a></li>
          <li><a href="#shop" onclick="window.DC_APP.filterCategory('Bespoke Lounge Wear')">Monochrome Plaid Trousers</a></li>
          <li><a href="#boutique-visit">Private In-Boutique Fitting</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">Customer Atelier</h4>
        <ul class="footer-links-list">
          <li><a href="javascript:void(0)" onclick="window.DC_APP.openAccountModal('measurements')">Bespoke Measurement Book</a></li>
          <li><a href="javascript:void(0)" onclick="window.DC_APP.openAccountModal('orders')">Track Your Order</a></li>
          <li><a href="javascript:void(0)" onclick="window.DC_APP.openConsultationModal()">Book Atelier Fitting in Uyo</a></li>
          <li><a href="#faq">Shipping across Nigeria</a></li>
          <li><a href="#faq">Silk & Linen Care Guide</a></li>
          <li><a href="javascript:void(0)" onclick="window.DC_APP.openAccountModal('wishlist')">Saved Wishlist</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">Boutique & Contact</h4>
        <div class="footer-links-list" style="gap:12px;">
          <div>
            <strong style="color:var(--text-light); display:block;">164 Udoumana Street</strong>
            <span>Uyo, Akwa Ibom State, Nigeria</span>
          </div>
          <div>
            <strong style="color:var(--text-light); display:block;">Atelier Telephone:</strong>
            <a href="tel:+2347085222212" style="color:var(--accent-gold-light);">+234 708 522 2212</a>
          </div>
          <div>
            <strong style="color:var(--text-light); display:block;">WhatsApp Concierge:</strong>
            <a href="https://wa.me/2347085222212" target="_blank" rel="noopener" style="color:#25D366;">Chat Directly with Debbie</a>
          </div>
          <div>
            <strong style="color:var(--text-light); display:block;">Operating Hours:</strong>
            <span>Mon–Sat: 9am – 7pm | Sun: VIP Appts</span>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bottom-row">
      <div>
        © 2026 Debbie's Collection Ltd. 164 Udoumana Street, Uyo, Akwa Ibom State. All Rights Reserved.
      </div>
      <div style="display:flex; align-items:center; gap:16px;">
        <span>Direct Atelier Gateway</span>
        <span>•</span>
        <span>UBA Verified</span>
        <span>•</span>
        <span>SSL 256-Bit Encryption</span>
      </div>
    </div>
  </div>
</footer>
'''

def get_mobile_bottom_nav_html():
    return '''<!-- Sticky Mobile Bottom Navigation Bar -->
<div class="mobile-bottom-bar" id="mobile-bottom-bar">
  <div class="mobile-bottom-nav">
    <a href="#hero" class="mobile-nav-btn active" onclick="window.scrollTo({top:0, behavior:'smooth'})">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
      <span>Home</span>
    </a>
    <a href="#shop" class="mobile-nav-btn" onclick="window.DC_APP.filterCategory('All')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
      <span>Shop</span>
    </a>
    <a href="#boutique-visit" class="mobile-nav-btn">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      <span>Boutique</span>
    </a>
    <button class="mobile-nav-btn" onclick="window.DC_APP.openAccountModal('wishlist')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
      <span>Wishlist</span>
      <span class="header-badge" id="mobile-wishlist-badge" style="top:-2px; right:6px;">0</span>
    </button>
    <button class="mobile-nav-btn" onclick="window.DC_APP.openCartDrawer()">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
      <span>Bag</span>
      <span class="header-badge" id="mobile-cart-badge" style="top:-2px; right:6px;">0</span>
    </button>
  </div>
</div>
'''

def get_modals_html():
    return '''<!-- Slide-Over Shopping Cart Drawer -->
<div class="cart-drawer" id="cart-drawer">
  <div class="drawer-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <h3 class="drawer-title">Shopping Bag</h3>
      <span style="font-size:0.8rem; background:var(--bg-warm); padding:2px 8px; border-radius:var(--radius-full); color:var(--text-secondary); font-weight:700;" id="cart-drawer-count">0 items</span>
    </div>
    <button class="drawer-close-btn" onclick="window.DC_APP.closeCartDrawer()" aria-label="Close Bag">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
  </div>

  <!-- Free Delivery Progress Bar -->
  <div class="free-delivery-tracker">
    <div class="tracker-label" id="delivery-tracker-text">
      Add ₦45,000 more for Free Doorstep Delivery in Uyo!
    </div>
    <div class="tracker-bar-bg">
      <div class="tracker-bar-fill" id="delivery-tracker-fill" style="width:0%;"></div>
    </div>
  </div>

  <!-- Cart Items List -->
  <div class="cart-items-scroll" id="cart-items-container">
    <!-- Populated by JS -->
  </div>

  <!-- Cart Footer -->
  <div class="cart-drawer-footer" id="cart-drawer-footer">
    <!-- Promo Code Input -->
    <div class="promo-row">
      <input type="text" id="cart-promo-input" class="promo-input" placeholder="Promo code (e.g. DEBBIEVIP, UYO10)">
      <button class="promo-btn" onclick="window.DC_APP.applyPromoCode()">Apply</button>
    </div>
    <div id="promo-feedback-msg" style="font-size:0.75rem; display:none;"></div>

    <!-- Summary Lines -->
    <div class="cart-summary-line">
      <span>Subtotal</span>
      <span id="cart-subtotal-val">₦0</span>
    </div>
    <div class="cart-summary-line" id="discount-summary-line" style="display:none; color:var(--accent-rose);">
      <span id="discount-label-text">Discount</span>
      <span id="cart-discount-val">-₦0</span>
    </div>
    <div class="cart-summary-line">
      <span>Estimated Shipping</span>
      <span id="cart-shipping-val">Calculated at checkout</span>
    </div>
    <div class="cart-summary-line total-line">
      <span>Total</span>
      <span id="cart-total-val">₦0</span>
    </div>

    <!-- Actions -->
    <button class="cart-checkout-btn" onclick="window.DC_APP.proceedToCheckout()">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
      <span>Proceed to Secure Checkout</span>
    </button>
    <button class="cart-whatsapp-btn" onclick="window.DC_APP.checkoutViaWhatsApp()">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
      <span>Order Directly via WhatsApp</span>
    </button>
  </div>
</div>

<!-- Multi-Step Checkout Modal -->
<div class="modal-overlay" id="checkout-modal">
  <div class="modal-card-box checkout-modal-box">
    <div class="modal-header-bar">
      <div style="display:flex; align-items:center; gap:10px;">
        <span class="brand-crest-box" style="width:32px; height:32px; overflow:hidden;">
          <img src="images/brand-logo.jpeg" alt="DC" style="width:100%; height:100%; object-fit:cover;">
        </span>
        <h3 class="modal-title">Debbie's Secure Checkout</h3>
      </div>
      <button class="drawer-close-btn" onclick="window.DC_APP.closeCheckoutModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <!-- Step Bar -->
    <div class="step-indicator-bar">
      <div class="step-item active" id="chk-step-1-ind">
        <span class="step-num">1</span>
        <span>Delivery</span>
      </div>
      <div class="step-item" id="chk-step-2-ind">
        <span class="step-num">2</span>
        <span>Measurements</span>
      </div>
      <div class="step-item" id="chk-step-3-ind">
        <span class="step-num">3</span>
        <span>Payment</span>
      </div>
      <div class="step-item" id="chk-step-4-ind">
        <span class="step-num">4</span>
        <span>Confirmation</span>
      </div>
    </div>

    <!-- Step 1: Customer Details & Shipping -->
    <div class="modal-body-content" id="checkout-step-1">
      <h4 style="font-family:var(--font-serif); font-size:1.15rem;">Customer & Shipping Address</h4>
      <div class="form-grid-2">
        <div class="form-group">
          <label class="form-label" for="chk-name">Full Name *</label>
          <input type="text" id="chk-name" class="form-input" placeholder="e.g. Dr. Idara Akpan" value="Dr. Idara Akpan">
        </div>
        <div class="form-group">
          <label class="form-label" for="chk-email">Email Address *</label>
          <input type="email" id="chk-email" class="form-input" placeholder="e.g. idara.akpan@example.com" value="idara.akpan@example.com">
        </div>
      </div>
      <div class="form-grid-2">
        <div class="form-group">
          <label class="form-label" for="chk-phone">Phone Number (WhatsApp) *</label>
          <input type="tel" id="chk-phone" class="form-input" placeholder="+234 803 123 4567" value="+234 803 456 7890">
        </div>
        <div class="form-group">
          <label class="form-label" for="chk-delivery-method">Delivery Method *</label>
          <select id="chk-delivery-method" class="form-select" onchange="window.DC_APP.updateCheckoutShipping(this.value)">
            <option value="uyo-bike">Uyo Same-Day Bike Delivery (₦1,500 / Free over ₦45,000)</option>
            <option value="akwa-ibom">Akwa Ibom State Courier (Eket/Ikot Ekpene) - ₦2,500</option>
            <option value="nationwide">Nationwide Priority Delivery (Lagos, Abuja, PH) - ₦4,500</option>
            <option value="pickup">In-Boutique Pickup at 164 Udoumana Street, Uyo (Free)</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label class="form-label" for="chk-address">Street Address / Estate Name *</label>
        <input type="text" id="chk-address" class="form-input" placeholder="e.g. Plot 18, Ewet Housing Estate" value="Plot 18, Ewet Housing Estate">
      </div>
      <div class="form-grid-2">
        <div class="form-group">
          <label class="form-label" for="chk-city">City *</label>
          <input type="text" id="chk-city" class="form-input" value="Uyo">
        </div>
        <div class="form-group">
          <label class="form-label" for="chk-state">State *</label>
          <input type="text" id="chk-state" class="form-input" value="Akwa Ibom State">
        </div>
      </div>
      <div class="form-group">
        <label class="form-label" for="chk-notes">Atelier Tailoring / Delivery Instructions</label>
        <textarea id="chk-notes" class="form-textarea" rows="2" placeholder="e.g. Please hem gown length by 2cm or deliver before Saturday 2pm for birthday."></textarea>
      </div>

      <div style="display:flex; justify-content:flex-end; gap:12px; margin-top:8px;">
        <button class="btn-primary" onclick="window.DC_APP.goToCheckoutStep(2)">
          <span>Continue to Measurements</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </button>
      </div>
    </div>

    <!-- Step 2: Bespoke Measurements Confirmation -->
    <div class="modal-body-content" id="checkout-step-2" style="display:none;">
      <h4 style="font-family:var(--font-serif); font-size:1.15rem;">Bespoke Tailoring Sizing Option</h4>
      <p style="font-size:0.86rem; color:var(--text-secondary);">
        For garments requiring bespoke tailoring, you can choose standard sizes or use your saved Bespoke Measurement Book profile.
      </p>

      <div style="display:flex; flex-direction:column; gap:12px;">
        <label class="payment-method-card active" onclick="window.DC_APP.selectMeasurementOption('saved')">
          <input type="radio" name="meas_opt" value="saved" checked>
          <div>
            <strong>Use Saved Profile: Kamsi (Daughter, 4Y) & Imo (Adult S)</strong>
            <span style="display:block; font-size:0.78rem; color:var(--text-muted);">Chest: 58cm | Waist: 54cm | Height: 104cm</span>
          </div>
        </label>
        <label class="payment-method-card" onclick="window.DC_APP.selectMeasurementOption('standard')">
          <input type="radio" name="meas_opt" value="standard">
          <div>
            <strong>Use Standard Age / Sizing Selected in Cart</strong>
            <span style="display:block; font-size:0.78rem; color:var(--text-muted);">Standard atelier comfort fit with allowance</span>
          </div>
        </label>
        <label class="payment-method-card" onclick="window.DC_APP.selectMeasurementOption('custom')">
          <input type="radio" name="meas_opt" value="custom">
          <div>
            <strong>Enter Custom Measurements for This Order</strong>
            <span style="display:block; font-size:0.78rem; color:var(--text-muted);">Provide specific chest, waist, and length measurements</span>
          </div>
        </label>
      </div>

      <div id="checkout-custom-meas-inputs" style="display:none; padding:16px; background:var(--bg-warm); border-radius:var(--radius-sm); border:1px solid var(--border-light);">
        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">Chest / Bust Circumference</label>
            <input type="text" id="chk-meas-chest" class="form-input" placeholder="e.g. 62cm">
          </div>
          <div class="form-group">
            <label class="form-label">Waist Circumference</label>
            <input type="text" id="chk-meas-waist" class="form-input" placeholder="e.g. 56cm">
          </div>
        </div>
        <div class="form-grid-2" style="margin-top:10px;">
          <div class="form-group">
            <label class="form-label">Shoulder to Hem Length</label>
            <input type="text" id="chk-meas-len" class="form-input" placeholder="e.g. 68cm">
          </div>
          <div class="form-group">
            <label class="form-label">Child Age / Adult Height</label>
            <input type="text" id="chk-meas-height" class="form-input" placeholder="e.g. 4.5 Years / 108cm">
          </div>
        </div>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">
        <button class="btn-secondary" onclick="window.DC_APP.goToCheckoutStep(1)">Back</button>
        <button class="btn-primary" onclick="window.DC_APP.goToCheckoutStep(3)">
          <span>Continue to Payment</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </button>
      </div>
    </div>

    <!-- Step 3: Payment Gateway -->
    <div class="modal-body-content" id="checkout-step-3" style="display:none;">
      <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:12px; border-bottom:1px solid var(--border-light);">
        <div>
          <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Amount Payable</span>
          <strong class="price-current" id="chk-payable-amount">₦0</strong>
        </div>
        <div style="display:flex; align-items:center; gap:6px; font-size:0.75rem; color:var(--accent-sage); font-weight:700;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <span>256-Bit SSL Secured</span>
        </div>
      </div>

      <h4 style="font-family:var(--font-serif); font-size:1.15rem;">Select Payment Method</h4>
      <div class="payment-options-grid">
        <!-- Option A: Instant Card / USSD Payment -->
        <label class="payment-method-card active" onclick="window.DC_APP.selectPaymentMethod('card')">
          <input type="radio" name="pay_opt" value="card" checked>
          <div>
            <strong>Instant Card & USSD Payment (Bank Verified)</strong>
            <span style="font-size:0.78rem; color:var(--text-muted); display:block;">Mastercard, Visa, Verve & Bank USSD with instant 3D Secure verification</span>
          </div>
        </label>

        <!-- Option B: Direct Bank Transfer to UBA -->
        <label class="payment-method-card" onclick="window.DC_APP.selectPaymentMethod('transfer')">
          <input type="radio" name="pay_opt" value="transfer">
          <div>
            <strong>Direct Bank Transfer to UBA Account</strong>
            <span style="font-size:0.78rem; color:var(--text-muted); display:block;">Transfer directly to Debbie's Collection UBA account</span>
          </div>
        </label>

        <!-- Option C: Pay on Boutique Pickup -->
        <label class="payment-method-card" onclick="window.DC_APP.selectPaymentMethod('pickup')">
          <input type="radio" name="pay_opt" value="pickup">
          <div>
            <strong>Pay on Boutique Pickup (164 Udoumana Street, Uyo)</strong>
            <span style="font-size:0.78rem; color:var(--text-muted); display:block;">Cash or POS upon collection at our Uyo boutique</span>
          </div>
        </label>
      </div>

      <!-- Card Panel -->
      <div class="card-details-panel" id="payment-panel-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:0.78rem; font-weight:700; color:var(--text-secondary);">Enter Card Information</span>
          <button style="font-size:0.72rem; color:var(--accent-rose); font-weight:700; text-decoration:underline;" onclick="window.DC_APP.autofillTestCard()">Autofill Demo Test Card</button>
        </div>
        <div class="form-group">
          <label class="form-label" for="card-num">Card Number</label>
          <input type="text" id="card-num" class="form-input" placeholder="5399 •••• •••• 9812" maxlength="19">
        </div>
        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label" for="card-exp">Expiry (MM/YY)</label>
            <input type="text" id="card-exp" class="form-input" placeholder="12/28" maxlength="5">
          </div>
          <div class="form-group">
            <label class="form-label" for="card-cvv">CVV</label>
            <input type="password" id="card-cvv" class="form-input" placeholder="842" maxlength="4">
          </div>
        </div>
      </div>

      <!-- Bank Transfer Panel -->
      <div class="bank-transfer-panel" id="payment-panel-transfer" style="display:none;">
        <span style="font-size:0.78rem; font-weight:700; color:var(--accent-rose);">Atelier Official Bank Account Details:</span>
        <div style="background:#FFFFFF; padding:12px; border-radius:var(--radius-sm); border:1px solid var(--border-light); font-size:0.86rem; display:flex; flex-direction:column; gap:4px;">
          <div>Bank Name: <strong>United Bank for Africa (UBA)</strong></div>
          <div style="display:flex; align-items:center; justify-content:space-between;">
            <span>Account Number: <strong id="uba-acc-num">2127888264</strong></span>
            <button style="font-size:0.72rem; background:var(--accent-rose-light); color:var(--accent-rose); padding:2px 8px; border-radius:var(--radius-full); font-weight:700;" onclick="window.DC_APP.copyAccountNumber()">Copy</button>
          </div>
          <div>Account Name: <strong>Debbie's Collection</strong></div>
        </div>
        <div class="form-group" style="margin-top:6px;">
          <label class="form-label">Upload Proof of Payment (Simulated):</label>
          <input type="file" id="transfer-proof-file" class="form-input" style="padding:6px;">
        </div>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">
        <button class="btn-secondary" onclick="window.DC_APP.goToCheckoutStep(2)">Back</button>
        <button class="btn-primary" id="btn-pay-now" onclick="window.DC_APP.processOrderPayment()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <span id="btn-pay-now-text">Authorize & Pay Now</span>
        </button>
      </div>
    </div>

    <!-- Step 4: Digital Printable Receipt & Live Order Tracker -->
    <div class="modal-body-content" id="checkout-step-4" style="display:none;">
      <div class="receipt-container" id="digital-receipt-card">
        <div class="receipt-header">
          <div class="brand-crest-box" style="margin:0 auto 10px; width:44px; height:44px; overflow:hidden;">
            <img src="images/brand-logo.jpeg" alt="DC" style="width:100%; height:100%; object-fit:cover;">
          </div>
          <h3 style="font-family:var(--font-serif); font-size:1.4rem;">Debbie's Collection</h3>
          <p style="font-size:0.78rem; color:var(--text-muted);">164 Udoumana Street, Uyo, Akwa Ibom State • Official Tax Receipt</p>
          <div class="receipt-status-badge">Payment Verified • Order Confirmed</div>
        </div>

        <div style="display:flex; justify-content:space-between; font-size:0.84rem; padding-bottom:8px; border-bottom:1px solid var(--border-light);">
          <div>
            <span style="color:var(--text-muted); display:block;">Order Reference:</span>
            <strong id="receipt-order-id">DC-2026-8941</strong>
          </div>
          <div style="text-align:right;">
            <span style="color:var(--text-muted); display:block;">Date:</span>
            <strong id="receipt-date">November 8, 2026</strong>
          </div>
        </div>

        <div>
          <span style="font-size:0.75rem; text-transform:uppercase; color:var(--text-muted); font-weight:700;">Delivering to:</span>
          <div style="font-size:0.85rem; color:var(--text-secondary);" id="receipt-customer-info">
            Dr. Idara Akpan • Plot 18, Ewet Housing Estate, Uyo
          </div>
        </div>

        <!-- Order Items Breakdown -->
        <div id="receipt-items-list" style="display:flex; flex-direction:column; gap:8px; border-top:1px dashed var(--border-light); padding-top:12px;"></div>

        <!-- Totals -->
        <div style="display:flex; flex-direction:column; gap:4px; border-top:1px dashed var(--border-light); padding-top:10px; font-size:0.86rem;">
          <div style="display:flex; justify-content:space-between;">
            <span>Subtotal</span>
            <span id="receipt-subtotal">₦0</span>
          </div>
          <div style="display:flex; justify-content:space-between;">
            <span>Shipping</span>
            <span id="receipt-shipping">₦0</span>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:1.1rem; font-weight:700; color:var(--text-primary); border-top:1px solid var(--border-light); padding-top:6px;">
            <span>Total Paid</span>
            <span id="receipt-total">₦0</span>
          </div>
        </div>

        <!-- Live Order Timeline -->
        <div style="background:var(--bg-warm); border-radius:var(--radius-sm); padding:14px; margin-top:8px;">
          <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; color:var(--accent-rose); display:block; margin-bottom:8px;">Atelier Live Progress</span>
          <div style="display:flex; flex-direction:column; gap:8px; font-size:0.78rem;">
            <div style="display:flex; align-items:center; gap:8px; color:var(--accent-sage); font-weight:700;">
              <span>✓ Order Received & Verified</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px; color:var(--accent-rose); font-weight:700;">
              <span>● Pattern Drafting & Fabric Cutting at 164 Udoumana</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px; color:var(--text-muted);">
              <span>○ Hand-Pressing, Tailoring Detail & Quality Inspection</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px; color:var(--text-muted);">
              <span>○ White-Glove Dispatch to Doorstep</span>
            </div>
          </div>
        </div>
      </div>

      <div style="display:flex; gap:12px; margin-top:12px; flex-wrap:wrap;">
        <button class="btn-primary" style="flex:1;" onclick="window.DC_APP.notifyWhatsAppOrder()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          <span>Notify Atelier on WhatsApp</span>
        </button>
        <button class="btn-secondary" onclick="window.print()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          <span>Print Receipt</span>
        </button>
      </div>
    </div>
  </div>
</div>

<!-- 3D Secure OTP Simulation Modal -->
<div class="modal-overlay" id="otp-modal" style="z-index:250;">
  <div class="modal-card-box" style="max-width:380px; text-align:center; padding:28px;">
    <div style="margin-bottom:12px; color:var(--accent-rose);">
      <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin:0 auto;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
    </div>
    <h3 style="font-family:var(--font-serif); font-size:1.25rem;">Bank 3D Secure Verification</h3>
    <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:8px;">
      Your bank has sent a 6-digit One-Time PIN to your registered phone number (+234 803 ••• 7890).
    </p>
    <div style="margin:20px 0;">
      <input type="text" id="otp-input" class="form-input" style="text-align:center; font-size:1.4rem; letter-spacing:0.3em; font-weight:700;" maxlength="6" value="849201">
      <span style="font-size:0.72rem; color:var(--text-muted); margin-top:6px; display:block;">Demo OTP: <strong>849201</strong></span>
    </div>
    <div style="display:flex; gap:10px;">
      <button class="btn-secondary" style="flex:1;" onclick="window.DC_APP.closeOtpModal()">Cancel</button>
      <button class="btn-primary" style="flex:1;" onclick="window.DC_APP.confirmOtp()">Authorize Payment</button>
    </div>
  </div>
</div>

<!-- Customer Account Drawer / Modal -->
<div class="modal-overlay" id="account-modal">
  <div class="modal-card-box" style="max-width:640px;">
    <div class="modal-header-bar">
      <h3 class="modal-title" id="account-modal-title">Customer Atelier Account</h3>
      <button class="drawer-close-btn" onclick="window.DC_APP.closeAccountModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <!-- Account Navigation Tabs -->
    <div class="step-indicator-bar" style="overflow-x:auto;">
      <button class="step-item active" id="acc-tab-profile" onclick="window.DC_APP.switchAccountTab('profile')">Profile & Address</button>
      <button class="step-item" id="acc-tab-measurements" onclick="window.DC_APP.switchAccountTab('measurements')">Bespoke Measurement Book</button>
      <button class="step-item" id="acc-tab-orders" onclick="window.DC_APP.switchAccountTab('orders')">Order History & Tracking</button>
      <button class="step-item" id="acc-tab-wishlist" onclick="window.DC_APP.switchAccountTab('wishlist')">Saved Wishlist</button>
    </div>

    <div class="modal-body-content" id="account-body-content">
      <!-- Injected dynamically by JS -->
    </div>
  </div>
</div>

<!-- Quick View & Customization Modal -->
<div class="modal-overlay" id="quick-view-modal">
  <div class="modal-card-box" style="max-width:760px;">
    <div class="modal-header-bar">
      <h3 class="modal-title" id="qv-title">Product Details</h3>
      <button class="drawer-close-btn" onclick="window.DC_APP.closeQuickViewModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div class="modal-body-content" id="qv-body-content">
      <!-- Injected by JS -->
    </div>
  </div>
</div>

<!-- Private Fitting Consultation Booking Modal -->
<div class="modal-overlay" id="consultation-modal">
  <div class="modal-card-box" style="max-width:540px;">
    <div class="modal-header-bar">
      <div>
        <h3 class="modal-title">Book an Atelier Fitting</h3>
        <span style="font-size:0.75rem; color:var(--accent-rose);">164 Udoumana Street, Uyo, Akwa Ibom</span>
      </div>
      <button class="drawer-close-btn" onclick="window.DC_APP.closeConsultationModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <form class="modal-body-content" onsubmit="window.DC_APP.submitConsultation(event)">
      <div class="form-grid-2">
        <div class="form-group">
          <label class="form-label" for="fit-name">Your Name *</label>
          <input type="text" id="fit-name" class="form-input" required placeholder="e.g. Mrs. Blessing Okon">
        </div>
        <div class="form-group">
          <label class="form-label" for="fit-phone">Phone / WhatsApp *</label>
          <input type="tel" id="fit-phone" class="form-input" required placeholder="+234 803 ...">
        </div>
      </div>
      <div class="form-grid-2">
        <div class="form-group">
          <label class="form-label" for="fit-date">Preferred Date *</label>
          <input type="date" id="fit-date" class="form-input" required>
        </div>
        <div class="form-group">
          <label class="form-label" for="fit-time">Preferred Time Slot *</label>
          <select id="fit-time" class="form-select">
            <option>10:00 AM - Morning Fitting</option>
            <option>12:30 PM - Midday Session</option>
            <option>3:00 PM - Afternoon Fitting</option>
            <option>5:30 PM - Evening Private Session</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label class="form-label" for="fit-service">Fitting Type / Garment Focus *</label>
        <select id="fit-service" class="form-select">
          <option>Children's Birthday Gala & Heirloom Gowns</option>
          <option>Pleated Tartan Skirt & Vintage Pinafore Ensemble</option>
          <option>Bespoke Flannel & Plaid Loungewear</option>
          <option>Flower Girl & Ceremonial Ballgown Fitting</option>
          <option>Custom Measurements & Sizing Consultation</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label" for="fit-notes">Special Requests / Child's Age / Color Palette</label>
        <textarea id="fit-notes" class="form-textarea" rows="3" placeholder="Tell us about the event date, child's age, preferred tartan colorway, or custom sizing requirements."></textarea>
      </div>
      <button type="submit" class="btn-primary" style="width:100%;">
        <span>Confirm Private Fitting Appointment</span>
      </button>
    </form>
  </div>
</div>

<!-- Review Submission Modal -->
<div class="modal-overlay" id="review-modal">
  <div class="modal-card-box" style="max-width:480px;">
    <div class="modal-header-bar">
      <h3 class="modal-title">Share Your Atelier Experience</h3>
      <button class="drawer-close-btn" onclick="window.DC_APP.closeReviewModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <form class="modal-body-content" onsubmit="window.DC_APP.submitReview(event)">
      <div class="form-group">
        <label class="form-label" for="rev-author">Your Name *</label>
        <input type="text" id="rev-author" class="form-input" required placeholder="e.g. Lady Ekaette Udofia">
      </div>
      <div class="form-group">
        <label class="form-label" for="rev-loc">Your Location / City *</label>
        <input type="text" id="rev-loc" class="form-input" required placeholder="e.g. Osongama Estate, Uyo">
      </div>
      <div class="form-group">
        <label class="form-label" for="rev-prod">Garment Purchased *</label>
        <input type="text" id="rev-prod" class="form-input" required placeholder="e.g. Bespoke Tartan Lounge Pants or Gala Gown">
      </div>
      <div class="form-group">
        <label class="form-label" for="rev-rating">Rating *</label>
        <select id="rev-rating" class="form-select">
          <option value="5">★★★★★ (5 Stars - Flawless Craftsmanship)</option>
          <option value="4">★★★★☆ (4 Stars - Beautiful Quality)</option>
          <option value="3">★★★☆☆ (3 Stars - Satisfactory)</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label" for="rev-text">Your Review / Fitting Feedback *</label>
        <textarea id="rev-text" class="form-textarea" rows="3" required placeholder="Share how the garments fit, fabric comfort, packaging, and delivery experience."></textarea>
      </div>
      <button type="submit" class="btn-primary" style="width:100%;">
        <span>Publish Verified Review</span>
      </button>
    </form>
  </div>
</div>

<!-- Toast Container -->
<div class="toast-container" id="toast-container" aria-live="polite"></div>
'''

