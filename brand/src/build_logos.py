"""Build the Webfix logo SVG set into <outdir> from wm800.json + Inter Tight 'W'."""
import json
import os
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
wm = json.load(open("wm800.json"))

INK, WHITE, BLUE, BLUE_ON_DARK = "#1A1E23", "#FFFFFF", "#2F68DB", "#659FFD"

l, r, t, b = wm["inkLeft"], wm["inkRight"], wm["inkTop"], wm["inkBottom"]
W, H = r - l, t - b
body = " ".join(wm["body"])
dot = " ".join(wm["dot"])


def wordmark(fg, dotc, title="Webfix"):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{l:.1f} {-t:.1f} {W:.1f} {H:.1f}" '
        f'width="{W/20:.0f}" height="{H/20:.0f}" role="img" aria-label="{title}">'
        f'<title>{title}</title><path fill="{fg}" d="{body}"/><path fill="{dotc}" d="{dot}"/></svg>\n'
    )


variants = {
    "webfix-wordmark.svg": (INK, BLUE),
    "webfix-wordmark-on-dark.svg": (WHITE, BLUE_ON_DARK),
    "webfix-wordmark-mono-ink.svg": (INK, INK),
    "webfix-wordmark-mono-white.svg": (WHITE, WHITE),
}
for name, (fg, dc) in variants.items():
    open(os.path.join(out, name), "w").write(wordmark(fg, dc))

# --- Monogram: W + Fix-Punkt in a rounded square --------------------------
font = instantiateVariableFont(TTFont(sys.argv[2]), {"wght": 800})
gs = font.getGlyphSet()
g = font.getBestCmap()[ord("W")]
bp = BoundsPen(gs)
gs[g].draw(bp)
gx0, gy0, gx1, gy1 = bp.bounds
gw, gh = gx1 - gx0, gy1 - gy0

S = 512
R = 116  # ~22.6 % corner radius, matches app-icon conventions
dot_b = wm["dotBounds"][0]
dot_d = dot_b[2] - dot_b[0]  # dot diameter in font units
# W + gap + dot should sit optically centred
target_w = S * 0.66
gap = dot_d * 0.18
scale = target_w / (gw + gap + dot_d)
total_h = gh * scale
ox = (S - target_w) / 2 - gx0 * scale
oy = (S + total_h) / 2 - gy0 * scale - total_h * 0.0  # baseline position
oy = (S - total_h) / 2 + gy1 * scale  # top of W at centred position

pen = SVGPathPen(None)
gs[g].draw(TransformPen(pen, (scale, 0, 0, -scale, ox, oy)))
w_path = pen.getCommands()
cx = ox + (gx1 + gap + dot_d / 2) * scale
# dot sits at cap height like the i-dot sits above the x-height
cy = oy - (gy1 - dot_d / 2) * scale
rad = dot_d / 2 * scale


def icon(bg, fg, dotc):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" width="{S}" height="{S}" role="img" aria-label="Webfix">'
        f'<title>Webfix</title><rect width="{S}" height="{S}" rx="{R}" fill="{bg}"/>'
        f'<path fill="{fg}" d="{w_path}"/><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{rad:.1f}" fill="{dotc}"/></svg>\n'
    )


open(os.path.join(out, "webfix-icon.svg"), "w").write(icon(INK, WHITE, BLUE_ON_DARK))
open(os.path.join(out, "webfix-icon-light.svg"), "w").write(icon(WHITE, INK, BLUE))
open(os.path.join(out, "webfix-icon-blue.svg"), "w").write(icon(BLUE, WHITE, WHITE))
# favicon: same as dark icon (crisp at 16/32px)
open(os.path.join(out, "favicon.svg"), "w").write(icon(INK, WHITE, BLUE_ON_DARK))
json.dump({"w_path": w_path, "cx": cx, "cy": cy, "r": rad, "S": S, "R": R,
           "wm_viewBox": [l, -t, W, H], "body": body, "dot": dot},
          open("logo-data.json", "w"))
print("built", sorted(os.listdir(out)))
