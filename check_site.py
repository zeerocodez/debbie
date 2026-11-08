import re
import os
import urllib.request

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text, re.I)
print('Found <img> tags:', len(imgs))

# All images must be local files that exist on disk
static_imgs = [img for img in imgs if not img.startswith('${')]
missing_images = [img for img in set(static_imgs) if not os.path.exists(img)]
print('Missing static <img> files on disk:', missing_images)

urls = re.findall(r'url\(["\']?(https?://[^)"\']+\.(?:png|jpg|jpeg|webp|gif|svg))["\']?\)', text, re.I)
print('Found external image URLs in CSS (must be 0):', len(urls))

# Check unwanted elements
unwanted = ["Monogram Studio", "Personalized Monograms", "Family & Duo", "Boys’ Sartorial", "Boys Sartorial"]
present_unwanted = [u for u in unwanted if u in text]
print('Unwanted elements present (must be empty):', present_unwanted)

# Check all button onclick handlers and IDs
onclicks = re.findall(r'onclick="([^"]+)"', text)
print(f'Total onclick handlers: {len(onclicks)}')

# Check key requirements
requirements = {
    "164 Udoumana Street, Uyo": "164 Udoumana Street" in text and "Uyo" in text,
    "Children's Wear Category": "Children's Wear" in text,
    "Bespoke Lounge Wear Category": "Bespoke Lounge Wear" in text,
    "Tanimawo Backend / Gateway": "Tanimawo" in text,
    "Customer Accounts": "account-modal" in text,
    "Shopping Bag / Cart": "cart-drawer" in text,
    "Checkout Flow": "checkout-modal" in text,
    "Bespoke Measurement Book": "Bespoke Measurement Book" in text,
    "Uyo Map": "UDOUMANA STREET" in text,
    "WhatsApp Integrations": "https://wa.me/2347085222212" in text,
    "Currency Switcher (NGN, USD, GBP)": "currency-select" in text,
    "Zenith Bank Transfer details": "Zenith Bank" in text and "1018492041" in text,
    "Printable Digital Receipt": "digital-receipt-card" in text,
    "3D Secure OTP Simulation": "otp-modal" in text,
    "Zero External Stock Images": len(urls) == 0,
    "All Local Images Valid": len(missing_images) == 0,
    "Monograms & Family Sets Removed": len(present_unwanted) == 0,
}

print("\n--- Requirements Verification ---")
all_passed = True
for req, passed in requirements.items():
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {req}")
    if not passed:
        all_passed = False

print(f"\nAll Requirements Met: {all_passed}")

# HTTP check
try:
    resp = urllib.request.urlopen("http://localhost:8000/")
    print(f"Localhost HTTP status: {resp.status} OK")
except Exception as e:
    print(f"Localhost HTTP check failed: {e}")


