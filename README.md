# Debbie's Collection

> **Luxury Children's Wear & Bespoke Loungewear Atelier**  
> 164 Udoumana Street, Uyo, Akwa Ibom State, Nigeria  
> WhatsApp / Atelier Tel: [+234 814 900 8821](https://wa.me/2348149008821)

---

## Overview

Debbie's Collection is a premium, mobile-first e-commerce boutique website built with pure editorial elegance, modern luxury aesthetics, and Tanimawo's built-in secure ordering engine.

### Key Pillars
- **Children's Gala & Party Gowns**: Cascading tulle ballgowns, handcrafted rosette gala pieces, smocked dresses, and heirloom lace gowns.
- **Tartan Pleated Skirts & Pinafores**: Scottish-inspired knife pleats, matching graphic tees, and vintage apron pinafores.
- **Bespoke Plaid Loungewear**: Signature brushed-flannel tartan trousers tailored to custom height and inseam.

### Features
- **Self-Contained & Fast**: Fully self-contained single-page experience with zero external stock image dependencies.
- **Multi-Currency Support**: Instant currency switching between NGN (₦), USD ($), and GBP (£).
- **Tanimawo Built-in Engine**:
  - Direct Bank Transfer (Zenith Bank details)
  - Card payment simulation with 3D Secure OTP verification
  - Cash on Delivery for Uyo doorstep deliveries
  - Printable and downloadable digital receipts
  - 1-Click WhatsApp order dispatch
- **Bespoke Measurement Book**: Allows clients to save children's and adult custom measurements for instant made-to-measure tailoring.
- **Private In-Boutique Fitting Scheduler**: Book private consultations at 164 Udoumana Street, Uyo.
- **Interactive Uyo Map**: Vector-crafted location map featuring Aka Road, Ibom Plaza, Nwaniba Road, and Udoumana Street.

---

## Local Development

To run the site locally:

```bash
# Clone the repository
git clone https://github.com/zeerocodez/debbie.git
cd debbie

# Start a local HTTP server
python -m http.server 8000
```

Open your browser at `http://localhost:8000`.

To rebuild the single-file distribution after updating modular builder files:

```bash
python build.py
```

---

## Project Structure

```
debbie/
├── index.html            # Production self-contained boutique application
├── build.py              # Modular compiler generating index.html
├── check_site.py         # Automated verification test suite
├── builder/              # Source modules
│   ├── products_data.py  # Curated catalog and boutique reviews
│   ├── app_html.py       # Semantic HTML layout and modals
│   ├── app_js.py         # TanimawoDB engine, checkout, state management
│   ├── styles.css        # Responsive luxury typography and styling
│   └── svg_assets.py     # Custom vector illustrations and Uyo map
├── images/               # High-resolution boutique garment photography
└── README.md
```

---

© Debbie's Collection. 164 Udoumana Street, Uyo, Akwa Ibom State. Powered by Tanimawo Secure Engine.
