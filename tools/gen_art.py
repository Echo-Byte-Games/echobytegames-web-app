"""Generates the pixel-art SVG assets used by the Echo Byte Games site.

Run from anywhere:  python tools/gen_art.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "images"
OUT.mkdir(parents=True, exist_ok=True)


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parts = []

    def px(self, x, y, w=1, h=1, color="#fff"):
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>'
        )

    def sprite(self, rows, palette, ox, oy, scale=1):
        for r, row in enumerate(rows):
            for c, ch in enumerate(row):
                if ch in palette and ch != ".":
                    self.px(ox + c * scale, oy + r * scale, scale, scale, palette[ch])

    def disc(self, cx, cy, radius, color):
        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):
                if x * x + y * y <= radius * radius:
                    self.px(cx + x, cy + y, 1, 1, color)

    def save(self, name):
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'shape-rendering="crispEdges">\n'
            + "\n".join(self.parts)
            + "\n</svg>\n"
        )
        (OUT / name).write_text(svg, encoding="utf-8")
        print("wrote", name)


# ---------------------------------------------------------------------------
# Brand + decorative sprites
# ---------------------------------------------------------------------------

GAMEPAD = [
    "................",
    "................",
    "....########....",
    "..############..",
    ".##############.",
    ".##HH######HH##.",
    ".##D######A#B##.",
    ".#DDD#####AB###.",
    ".##D######B#A##.",
    ".##############.",
    "..############..",
    "...##########...",
]
GAMEPAD_COLORS = {
    "#": "#29f0d5",
    "H": "#bffff4",
    "D": "#0b0e1a",
    "A": "#ff2e97",
    "B": "#ffd93d",
}

INVADER = [
    "..1.....1..",
    "...1...1...",
    "..1111111..",
    ".11.111.11.",
    "11111111111",
    "1.1111111.1",
    "1.1.....1.1",
    "...11.11...",
]

INVADER_SMALL = [
    ".1....1.",
    "..1..1..",
    ".111111.",
    "11.11.11",
    "11111111",
    "1.1111.1",
    "1.1..1.1",
    "..11.11.",
]

HEART = [
    ".##...##.",
    "####.####",
    "##++#####",
    "##++++###",
    ".##++###.",
    "..#####..",
    "...###...",
    "....#....",
]

STAR = [
    "...#...",
    "...#...",
    "#######",
    ".#####.",
    "..###..",
    ".##.##.",
    "##...##",
]


def build_icons():
    cv = Canvas(16, 12)
    cv.sprite(GAMEPAD, GAMEPAD_COLORS, 0, 0)
    cv.save("logo-gamepad.svg")

    cv = Canvas(11, 8)
    cv.sprite(INVADER, {"1": "#6bff6b"}, 0, 0)
    cv.save("invader.svg")

    cv = Canvas(8, 8)
    cv.sprite(INVADER_SMALL, {"1": "#29f0d5"}, 0, 0)
    cv.save("favicon.svg")

    cv = Canvas(9, 8)
    cv.sprite(HEART, {"#": "#ff2e97", "+": "#ff8cc6"}, 0, 0)
    cv.save("heart.svg")

    cv = Canvas(7, 7)
    cv.sprite(STAR, {"#": "#ffd93d"}, 0, 0)
    cv.save("star.svg")


# ---------------------------------------------------------------------------
# Game thumbnail scenes
# ---------------------------------------------------------------------------

def thumb_neon_drift():
    cv = Canvas(24, 14)
    cv.px(0, 0, 24, 4, "#160a2e")
    cv.px(0, 4, 24, 4, "#2b1046")
    for x, y in [(2, 1), (6, 2), (10, 1), (15, 2), (20, 1), (22, 3), (4, 3), (18, 0)]:
        cv.px(x, y, 1, 1, "#7df9ff")
    cv.disc(12, 5, 3, "#ff3cac")
    for y in (6, 7):
        cv.px(9, y, 6, 1, "#2b1046")
    cv.px(0, 8, 24, 1, "#ff2e97")
    for x in range(0, 8):
        h = max(0, 3 - abs(x - 3))
        for yy in range(8 - h, 8):
            cv.px(x, yy, 1, 1, "#0d0620")
    for x in range(17, 24):
        h = max(0, 3 - abs(x - 20))
        for yy in range(8 - h, 8):
            cv.px(x, yy, 1, 1, "#0d0620")
    for y in range(8, 14):
        half = 2 + (y - 8)
        cv.px(12 - half, y, half * 2, 1, "#120a24")
        cv.px(12 - half, y, 1, 1, "#29f0d5")
        cv.px(12 + half - 1, y, 1, 1, "#29f0d5")
    for y in (10, 12):
        half = 2 + (y - 8)
        cv.px(0, y, 12 - half, 1, "#3a1352")
        cv.px(12 + half, y, 24 - (12 + half), 1, "#3a1352")
    for y in (9, 11):
        cv.px(12, y, 1, 1, "#ffd93d")
    car = ["..A..", ".AAA.", "AAAAA"]
    cv.sprite(car, {"A": "#7df9ff"}, 10, 11)
    cv.save("thumb-neon-drift.svg")


def thumb_dungeon_bits():
    cv = Canvas(24, 14)
    cv.px(0, 0, 24, 14, "#0d0a1a")
    for y in range(0, 10):
        band = (y // 2) % 2
        cv.px(0, y, 24, 1, "#241f3a" if band == 0 else "#2b2444")
        for x in range(0, 24, 4):
            cv.px(x if band == 0 else x + 2, y, 1, 1, "#15112a")
    cv.px(0, 10, 24, 4, "#1b1630")
    for y in (11, 13):
        cv.px(0, y, 24, 1, "#2b2444")
    for x in range(0, 24, 3):
        cv.px(x, 12, 1, 1, "#2b2444")
    cv.px(4, 5, 1, 4, "#6b4423")
    cv.px(3, 2, 1, 1, "#ffd93d")
    cv.px(4, 2, 1, 2, "#ff8c00")
    cv.px(5, 3, 1, 1, "#ffd93d")
    cv.px(4, 4, 1, 1, "#ff3c00")
    cv.px(3, 4, 1, 1, "#ff8c00")
    cv.px(13, 8, 6, 4, "#7a4a22")
    cv.px(13, 8, 6, 1, "#ffd93d")
    cv.px(13, 11, 6, 1, "#3a2410")
    cv.px(15, 9, 2, 2, "#ffd93d")
    cv.px(16, 9, 1, 1, "#3a2410")
    hero = ["..H..", ".HHH.", ".SSS.", ".HHH.", "H.H.H", ".B.B."]
    cv.sprite(hero, {"H": "#9fb3ff", "S": "#c9d6ff", "B": "#3a3a5a"}, 8, 6)
    bat = ["B.B", ".B."]
    cv.sprite(bat, {"B": "#0a0814"}, 19, 2)
    cv.save("thumb-dungeon-bits.svg")


def thumb_starfall():
    cv = Canvas(24, 14)
    cv.px(0, 0, 24, 14, "#05081a")
    for x, y in [(2, 1), (5, 3), (8, 0), (13, 1), (15, 4), (22, 1), (1, 6), (23, 8), (7, 9)]:
        cv.px(x, y, 1, 1, "#7df9ff")
    cv.disc(19, 4, 3, "#3a7bd5")
    cv.px(18, 3, 1, 1, "#6fa8ff")
    cv.px(20, 5, 1, 1, "#2a5fa8")
    cv.px(15, 7, 8, 1, "#00d2ff")
    foe = ["..1..", "11111", "1.1.1"]
    cv.sprite(foe, {"1": "#6bff6b"}, 3, 1)
    cv.sprite(foe, {"1": "#ff2e97"}, 10, 2)
    cv.px(11, 8, 1, 2, "#ffd93d")
    cv.px(13, 7, 1, 3, "#ff2e97")
    cv.px(6, 5, 1, 1, "#ff8c00")
    cv.px(5, 6, 1, 1, "#ffd93d")
    cv.px(7, 6, 1, 1, "#ff3c00")
    cv.px(6, 7, 1, 1, "#ff8c00")
    ship = ["...A...", "..AAA..", ".AAAAA.", "AA.A.AA"]
    cv.sprite(ship, {"A": "#7df9ff"}, 10, 10)
    cv.save("thumb-starfall.svg")


def thumb_pixel_puzzle():
    cv = Canvas(24, 14)
    cv.px(0, 0, 24, 14, "#0b1024")
    frame = "#29f0d5"
    cv.px(5, 1, 14, 1, frame)
    cv.px(5, 13, 14, 1, frame)
    cv.px(5, 1, 1, 13, frame)
    cv.px(18, 1, 1, 13, frame)
    colors = {"C": "#29f0d5", "M": "#ff2e97", "Y": "#ffd93d", "G": "#6bff6b"}
    cols = [6, 8, 10, 12, 14, 16]
    layout = {
        11: ["C", "C", ".", "M", "M", "."],
        9: [".", "C", "C", "M", ".", "."],
        7: ["Y", "Y", ".", "G", "G", "."],
        5: [".", ".", "Y", ".", "G", "."],
        3: [".", ".", "M", "M", ".", "."],
    }
    for y, row in layout.items():
        for x, ch in zip(cols, row):
            if ch in colors:
                cv.px(x, y, 2, 2, colors[ch])
    cv.px(20, 3, 2, 2, colors["Y"])
    cv.px(22, 3, 2, 2, colors["Y"])
    cv.px(21, 5, 2, 2, colors["Y"])
    cv.save("thumb-pixel-puzzle.svg")


def build_thumbs():
    thumb_neon_drift()
    thumb_dungeon_bits()
    thumb_starfall()
    thumb_pixel_puzzle()


if __name__ == "__main__":
    build_icons()
    build_thumbs()
