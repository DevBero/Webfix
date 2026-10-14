"""Build brand/index.html (Markenhandbuch) from template.html.

Run from brand/src:
    python3 wordmark.py InterTight-Variable.ttf 800 -0.03 wm800
    python3 build_logos.py ../logo InterTight-Variable.ttf
    python3 build.py
"""
import base64
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BRAND = HERE.parent

logo = json.load(open(HERE / "logo-data.json"))
wm = json.load(open(HERE / "wm800.json"))


# ---------- colour helpers ----------
def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(h):
    c = [x / 255 for x in rgb(h)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def cmyk(h):
    r, g, b = (x / 255 for x in rgb(h))
    k = 1 - max(r, g, b)
    if k >= 1:
        return (0, 0, 0, 100)
    return tuple(round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))


def de(n, digits=2):
    return f"{n:.{digits}f}".replace(".", ",")


def swatch(name, hexv, role, use, token):
    fg = "#FFFFFF" if lum(hexv) < 0.35 else "#1A1E23"
    r, g, b = rgb(hexv)
    c, m, y, k = cmyk(hexv)
    return f"""<div class="swatch">
  <div class="chip" style="background:{hexv};color:{fg}"><span class="name">{name}</span><span class="role">{role}</span></div>
  <dl class="data">
    <div><dt>Hex</dt><dd><button class="copy" type="button" data-value="{hexv}" aria-label="{name} {hexv} kopieren">{hexv}</button></dd></div>
    <div><dt>RGB</dt><dd>{r} {g} {b}</dd></div>
    <div><dt>CMYK*</dt><dd>{c} {m} {y} {k}</dd></div>
    <div><dt>Token</dt><dd>{token}</dd></div>
    <p class="use">{use}</p>
  </dl>
</div>"""


def status_swatch(name, text, bg, use, token):
    return f"""<div class="swatch">
  <div class="chip" style="background:{bg};color:{text};align-items:center"><span class="name">{name}</span><span class="badge" style="background:var(--white);color:{text}">{de(contrast(text, bg))} : 1</span></div>
  <dl class="data">
    <div><dt>Text</dt><dd><button class="copy" type="button" data-value="{text}" aria-label="{name} Text {text} kopieren">{text}</button></dd></div>
    <div><dt>Fläche</dt><dd><button class="copy" type="button" data-value="{bg}" aria-label="{name} Fläche {bg} kopieren">{bg}</button></dd></div>
    <div><dt>Token</dt><dd>{token}</dd></div>
    <p class="use">{use}</p>
  </dl>
</div>"""


primary = [
    ("Tinte", "#1A1E23", "Text & Logo", "Headlines, Fließtext, Wortmarke, Pill-Buttons. Nie reines Schwarz.", "primary"),
    ("Nebel", "#F2F7F7", "Seitengrund", "Grund hinter allen Blättern. Kühl, minimal grünlich.", "neutral"),
    ("Weiß", "#FFFFFF", "Flächen", "Sektionsblätter, Karten, Eingabefelder.", "surface"),
    ("Signalblau", "#2F68DB", "Aktion", "Primär-Button, Links, aktive Zustände, Fix-Punkt.", "tertiary"),
]
secondary = [
    ("Schiefer", "#515A63", "Sekundärtext", "Navigation, Leads, Beschreibungen.", "secondary"),
    ("Gedämpft", "#636E73", "Metadaten", "Platzhalter, Bildunterschriften, Labels.", "on-surface-subtle"),
    ("Stein", "#E9E9EB", "Neutrale Fläche", "Sekundär-Button, Score-Balken-Grund, Stat-Pills.", "surface-sunken"),
    ("Linie", "#E2E4E5", "Haarlinien", "1-px-Trennlinien und Rahmen. Nie für Text.", "outline"),
    ("Graphit", "#1F2429", "Dunkles Band", "Technik-Sektion, Footer, Visitenkarte.", "inverse-surface"),
    ("Creme", "#F8F8F3", "Wärme, einmal", "Eyebrow-Chips und ein Band pro Seite (Preise).", "surface-warm"),
    ("Blau tief", "#264EB4", "Hover", "Hover-Zustand des Primär-Buttons, Text auf Hellblau.", "tertiary-hover"),
    ("Blau hell", "#659FFD", "Blau auf Dunkel", "Fix-Punkt und Links auf Graphit.", "—"),
]
status = [
    ("Gut", "#1E7F4F", "#D9FDD3", "Score ab 80 („Gut“), Prüfzeile „Bestanden“, Formular gesendet.", "success"),
    ("Prüfen", "#9A5B00", "#FFF4D6", "Score 50–79 („Verbesserbar“), Prüfzeile „Prüfen“.", "warning"),
    ("Kritisch", "#C62445", "#FCEBEF", "Score unter 50 und Prüfzeile („Kritisch“), Formularfehler.", "error"),
]

contrast_pairs = [
    ("Tinte auf Weiß", "#1A1E23", "#FFFFFF", "Headlines, Fließtext"),
    ("Tinte auf Nebel", "#1A1E23", "#F2F7F7", "Text in Pausen-Sektionen"),
    ("Schiefer auf Weiß", "#515A63", "#FFFFFF", "Sekundärtext, Navigation"),
    ("Schiefer auf Nebel", "#515A63", "#F2F7F7", "Sekundärtext auf Grund"),
    ("Gedämpft auf Weiß", "#636E73", "#FFFFFF", "Platzhalter, Metadaten"),
    ("Gedämpft auf Nebel", "#636E73", "#F2F7F7", "Bildunterschriften"),
    ("Weiß auf Signalblau", "#FFFFFF", "#2F68DB", "Primär-Button"),
    ("Weiß auf Blau tief", "#FFFFFF", "#264EB4", "Primär-Button Hover"),
    ("Signalblau auf Weiß", "#2F68DB", "#FFFFFF", "Links"),
    ("Weiß auf Graphit", "#FFFFFF", "#1F2429", "Text im dunklen Band"),
    ("Grau auf Graphit", "#A6ADB3", "#1F2429", "Sekundärtext dunkel"),
    ("Blau hell auf Graphit", "#659FFD", "#1F2429", "Links auf Dunkel"),
    ("Gut", "#1E7F4F", "#D9FDD3", "Badge"),
    ("Prüfen", "#9A5B00", "#FFF4D6", "Badge"),
    ("Kritisch", "#C62445", "#FCEBEF", "Badge"),
    ("Weiß auf Referenz-Blau", "#FFFFFF", "#397DFF", "Verworfen"),
    ("Linie auf Weiß", "#E2E4E5", "#FFFFFF", "Nur Dekoration"),
]


def rating(cr):
    if cr >= 7:
        return '<span class="badge b-ok">AAA</span>'
    if cr >= 4.5:
        return '<span class="badge b-ok">AA</span>'
    if cr >= 3:
        return '<span class="badge b-warn">nur groß / UI</span>'
    return '<span class="badge b-err">nicht für Text</span>'


rows = []
for label, fg, bg, use in contrast_pairs:
    cr = contrast(fg, bg)
    rows.append(
        f'<tr><td><span class="sample" style="color:{fg};background:{bg};box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)">{label}</span></td>'
        f'<td class="num">{fg}</td><td class="num">{bg}</td><td class="num">{de(cr)} : 1</td><td>{rating(cr)}</td><td>{use}</td></tr>'
    )

# ---------- clear-space diagram (font units) ----------
l, t, W, H = logo["wm_viewBox"][0], -logo["wm_viewBox"][1], logo["wm_viewBox"][2], logo["wm_viewBox"][3]
xh = wm["xHeight"]
pad = 60
vb = f"{l - xh - pad:.0f} {-t - xh - pad:.0f} {W + 2 * xh + 2 * pad:.0f} {H + 2 * xh + 2 * pad:.0f}"
ox, oy, ow, oh = l - xh, -t - xh, W + 2 * xh, H + 2 * xh
corners = [(ox, oy), (ox + ow - xh, oy), (ox, oy + oh - xh), (ox + ow - xh, oy + oh - xh)]
corner_svg = "".join(
    f'<rect x="{cx:.0f}" y="{cy:.0f}" width="{xh}" height="{xh}" rx="40" fill="#E7F5FD"/>'
    f'<text x="{cx + xh / 2:.0f}" y="{cy + xh / 2:.0f}" text-anchor="middle" dominant-baseline="central" '
    f'font-family="Inter Tight, sans-serif" font-size="520" fill="#2F68DB">x</text>'
    for cx, cy in corners
)
clear_svg = (
    f'<svg viewBox="{vb}" role="img" aria-label="Schutzzone der Wortmarke: rundum eine x-Höhe">'
    f'{corner_svg}'
    f'<rect x="{ox:.0f}" y="{oy:.0f}" width="{ow:.0f}" height="{oh:.0f}" fill="none" stroke="#2F68DB" stroke-width="14" stroke-dasharray="70 50"/>'
    f'<rect x="{l:.0f}" y="{-t:.0f}" width="{W:.0f}" height="{H:.0f}" fill="none" stroke="#D4D7D7" stroke-width="10"/>'
    f'<use href="#wm" class="wm-std" x="{l:.0f}" y="{-t:.0f}" width="{W:.0f}" height="{H:.0f}"/>'
    f'</svg>'
)

icon_grid = "".join(f'<line x1="{i}" y1="0" x2="{i}" y2="24"/><line x1="0" y1="{i}" x2="24" y2="{i}"/>' for i in range(25))

# ---------- fonts as data URIs (no external font host) ----------
fonts = [
    ("Newsreader", "newsreader-variable.woff2", "200 800"),
    ("Inter Tight", "inter-tight-variable.woff2", "100 900"),
    ("JetBrains Mono", "jetbrains-mono-variable.woff2", "100 800"),
]
fontface = "\n".join(
    "@font-face { font-family: \"%s\"; src: url(data:font/woff2;base64,%s) format(\"woff2\"); font-weight: %s; font-style: normal; font-display: swap; }"
    % (fam, base64.b64encode((BRAND / "fonts" / f).read_bytes()).decode(), w)
    for fam, f, w in fonts
)

repl = {
    "{{FONTFACE}}": fontface,
    "{{WM_VB_SYM}}": " ".join(f"{v:.1f}" for v in logo["wm_viewBox"]),
    "{{WM_VB}}": f"0 0 {W:.1f} {H:.1f}",
    "{{WM_BODY}}": logo["body"],
    "{{WM_DOT}}": logo["dot"],
    "{{WM_RATIO}}": de(W / H, 1),
    "{{WM_AR}}": f"{W:.1f} / {H:.1f}",
    "{{ICON_W}}": logo["w_path"],
    "{{ICON_CX}}": f'{logo["cx"]:.1f}',
    "{{ICON_CY}}": f'{logo["cy"]:.1f}',
    "{{ICON_DOT}}": f'{logo["r"]:.1f}',
    "{{ICON_R}}": str(logo["R"]),
    "{{CLEAR_SVG}}": clear_svg,
    "{{ICON_GRID}}": icon_grid,
    "{{PALETTE_PRIMARY}}": "".join(swatch(*p) for p in primary),
    "{{PALETTE_SECONDARY}}": "".join(swatch(*p) for p in secondary),
    "{{PALETTE_STATUS}}": "".join(status_swatch(*p) for p in status),
    "{{CONTRAST_ROWS}}": "".join(rows),
}
html = (HERE / "template.html").read_text()
for k, v in repl.items():
    html = html.replace(k, v)
assert "{{" not in html, [ln for ln in html.splitlines() if "{{" in ln][:3]
(BRAND / "index.html").write_text(html)
print("wrote", BRAND / "index.html", f"{len(html) / 1024:.0f} KB")
