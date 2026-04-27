"""Generate QR code PNGs for the FocusPal demo distribution links."""

from pathlib import Path

import qrcode

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

TARGETS = [
    ("qr-apk.png", "https://github.com/SacriTom/focuspal-demo/releases/latest"),
    ("qr-web.png", "https://sacritom.github.io/focuspal-demo/"),
    ("qr-repo.png", "https://github.com/SacriTom/focuspal-demo"),
]

for filename, url in TARGETS:
    img = qrcode.make(url, box_size=10, border=2)
    img.save(DOCS / filename)
    print(f"  {filename} -> {url}")
