"""Render the Webfix wordmark from Inter Tight as pure SVG paths.

Usage: python3 wordmark.py <font.ttf> <weight> <tracking_em> <out_prefix>
Writes <out_prefix>.json with path data for body + i-dot + metrics.
"""
import json
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

font_path, weight, tracking, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
font = instantiateVariableFont(TTFont(font_path), {"wght": weight})
upm = font["head"].unitsPerEm
gs = font.getGlyphSet()
cmap = font.getBestCmap()
hmtx = font["hmtx"]
os2 = font["OS/2"]

text = "Webfix"
# optical pair corrections (em): keep the f-hook clear of the blue i-dot
PAIR = {"f": 0.045}
x = 0.0
body, dot = [], []
prev = None
# kerning via GPOS is complex; Inter Tight is spaced well for this word, tracking handles the rest
for ch in text:
    gname = cmap[ord(ch)]
    rec = DecomposingRecordingPen(gs)
    gs[gname].draw(rec)
    # split into contours
    contours, cur = [], []
    for op, args in rec.value:
        cur.append((op, args))
        if op in ("closePath", "endPath"):
            contours.append(cur)
            cur = []
    for c in contours:
        pen = SVGPathPen(None)
        tp = TransformPen(pen, (1, 0, 0, -1, x, 0))  # flip y, baseline at 0
        bp = BoundsPen(None)
        for op, args in c:
            getattr(tp, op)(*args)
            getattr(bp, op)(*args)
        d = pen.getCommands()
        is_dot = ch == "i" and bp.bounds and bp.bounds[1] > os2.sxHeight * 0.9
        (dot if is_dot else body).append({"d": d, "bounds": bp.bounds, "x": x})
    x += hmtx[gname][0] + tracking * upm + (PAIR.get(ch, 0) * upm)
x -= tracking * upm

# overall bounds
allb = [c["bounds"] for c in body + dot if c["bounds"]]
xmin = min(b[0] + 0 for b in allb)
json.dump({
    "upm": upm, "advance": x, "capHeight": os2.sCapHeight, "xHeight": os2.sxHeight,
    "body": [c["d"] for c in body], "dot": [c["d"] for c in dot],
    "dotBounds": [ (c["bounds"][0] + c["x"], c["bounds"][1], c["bounds"][2] + c["x"], c["bounds"][3]) for c in dot],
    "inkLeft": min(c["bounds"][0] + c["x"] for c in body if c["bounds"]),
    "inkRight": max(c["bounds"][2] + c["x"] for c in body + dot if c["bounds"]),
    "inkBottom": min(c["bounds"][1] for c in body if c["bounds"]),
    "inkTop": max(c["bounds"][3] for c in body + dot if c["bounds"]),
}, open(out + ".json", "w"))
print("ok", out, x)
