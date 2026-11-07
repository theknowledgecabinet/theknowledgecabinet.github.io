"""The Knowledge Cabinet logo: a card-catalogue cabinet, one drawer per site.

    python3 sites/home/brand/make-logo.py     -> brand/logo-1000.png (GitHub avatar), logo-512.png, logo-192.png

Drawn inside the central circle, because GitHub shows user avatars as circles.
Drawer label colours: Daily Idea (rose), Hastings Daily (teal), The Long View (lavender).
"""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).parent
INK, CREAM, WOOD, SHADE = (31, 58, 95), (247, 244, 236), (233, 226, 210), (207, 197, 176)
IDEA, NEWS, VIEW, GOLD = (163, 68, 111), (27, 94, 126), (122, 95, 192), (214, 160, 73)

def draw(size):
    s = size * 4
    img = Image.new("RGB", (s, s), INK)
    d = ImageDraw.Draw(img)
    u = s / 100                                   # 1 unit = 1% of the side
    R = lambda *v: tuple(round(x * u) for x in v)
    # soft halo so it reads on GitHub's light and dark themes
    d.ellipse(R(9, 9, 91, 91), fill=(40, 70, 110))
    # legs, body, cornice
    d.rectangle(R(31, 74, 35, 80), fill=WOOD); d.rectangle(R(65, 74, 69, 80), fill=WOOD)
    d.rounded_rectangle(R(27, 26, 73, 76), radius=round(2.2 * u), fill=CREAM)
    d.rounded_rectangle(R(24, 21, 76, 28), radius=round(1.6 * u), fill=WOOD)
    # 2 x 3 drawers; three carry a site colour on the label
    labels = {(0, 0): IDEA, (1, 1): NEWS, (2, 0): VIEW}
    for row in range(3):
        for col in range(2):
            x0, y0 = 31 + col * 20, 32 + row * 14.3
            open_ = (row, col) == (1, 1)
            dx, dy = (0, 1.4) if open_ else (0, 0)
            if open_:   # pulled out a little: a shadow and a card peeking up
                d.rectangle(R(x0, y0, x0 + 18, y0 + 12), fill=SHADE)
                d.rectangle(R(x0 + 4, y0 - 2.6 + dy, x0 + 14, y0 + 3), fill=(255, 253, 248))
                d.line(R(x0 + 5.5, y0 - 1 + dy, x0 + 12.5, y0 - 1 + dy), fill=GOLD, width=round(0.8 * u))
            d.rounded_rectangle(R(x0 + dx, y0 + dy, x0 + 18 + dx, y0 + 12 + dy), radius=round(1.2 * u),
                                fill=WOOD, outline=SHADE, width=round(0.5 * u))
            lab = labels.get((row, col), SHADE)
            d.rounded_rectangle(R(x0 + 5 + dx, y0 + 2.6 + dy, x0 + 13 + dx, y0 + 6.2 + dy), radius=round(0.6 * u), fill=lab)
            d.ellipse(R(x0 + 7.8 + dx, y0 + 7.6 + dy, x0 + 10.2 + dx, y0 + 10 + dy), fill=INK)
    # a small star above the cabinet: ideas worth keeping
    cx, cy, r = 50 * u, 14.5 * u, 3.2 * u
    d.polygon([(cx, cy - r), (cx + r * .28, cy - r * .28), (cx + r, cy), (cx + r * .28, cy + r * .28),
               (cx, cy + r), (cx - r * .28, cy + r * .28), (cx - r, cy), (cx - r * .28, cy - r * .28)], fill=GOLD)
    return img.resize((size, size), Image.LANCZOS)

for n in (1000, 512, 192):
    draw(n).save(OUT / f"logo-{n}.png", optimize=True)
print("ok")
