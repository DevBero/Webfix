---
version: alpha
name: Webfix Quiet Premium
description: Ruhiges, redaktionelles SaaS-Design. Serif-Display in Light auf kühlem Nebelgrund, kleine präzise Grotesk, eine einzige Akzentfarbe, abwechselnd helle und dunkle Bänder in eingerückten, stark gerundeten Flächen. Abgeleitet aus voiceflow.com (Typo, Farbe, Rhythmus) und optivio.framer.website (Flächen, Pills, Formensprache).
colors:
  primary: "#1A1E23"
  on-primary: "#FFFFFF"
  secondary: "#515A63"
  tertiary: "#2F68DB"
  on-tertiary: "#FFFFFF"
  tertiary-hover: "#264EB4"
  tertiary-soft: "#E7F5FD"
  neutral: "#F2F7F7"
  background: "#F2F7F7"
  on-background: "#1A1E23"
  surface: "#FFFFFF"
  on-surface: "#1A1E23"
  surface-muted: "#F1F2F2"
  surface-sunken: "#E9E9EB"
  surface-warm: "#F8F8F3"
  on-surface-variant: "#515A63"
  on-surface-subtle: "#636E73"
  outline: "#E2E4E5"
  outline-strong: "#D4D7D7"
  inverse-surface: "#1F2429"
  inverse-surface-raised: "#2B3239"
  inverse-surface-control: "#38414A"
  on-inverse-surface: "#FFFFFF"
  on-inverse-surface-variant: "#A6ADB3"
  inverse-outline: "#3A4148"
  success: "#1E7F4F"
  success-soft: "#D9FDD3"
  warning: "#9A5B00"
  warning-soft: "#FFF4D6"
  error: "#C62445"
  error-soft: "#FCEBEF"
typography:
  display-xl:
    fontFamily: Newsreader
    fontSize: 72px
    fontWeight: 300
    lineHeight: 1.06
    letterSpacing: -0.03em
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.16
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.02em
  title-lg:
    fontFamily: Inter Tight
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.02em
  title-md:
    fontFamily: Inter Tight
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter Tight
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: Inter Tight
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  body-sm:
    fontFamily: Inter Tight
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
  label-md:
    fontFamily: Inter Tight
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
  label-sm:
    fontFamily: Inter Tight
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.42
  eyebrow:
    fontFamily: Inter Tight
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  score:
    fontFamily: Inter Tight
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: -0.03em
    fontFeature: '"tnum" 1'
  code:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.55
rounded:
  xs: 2px
  sm: 8px
  md: 10px
  lg: 16px
  xl: 24px
  2xl: 32px
  full: 9999px
spacing:
  unit: 4px
  2xs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 80px
  5xl: 120px
  section-top: 80px
  section-bottom: 120px
  frame-inset: 12px
  container-max: 1296px
  text-max: 1024px
  copy-max: 660px
  gutter: 24px
  page-margin-desktop: 72px
  page-margin-mobile: 16px
  columns: 12
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.tertiary-hover}"
  button-secondary:
    backgroundColor: "{colors.surface-sunken}"
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
  button-secondary-inverse:
    backgroundColor: "{colors.inverse-surface-control}"
    textColor: "{colors.on-inverse-surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.full}"
    padding: 8px 8px 8px 20px
    height: 44px
  url-input-group:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 4px 4px 4px 14px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    height: 64px
  eyebrow-chip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.secondary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  stat-pill:
    backgroundColor: "{colors.surface-sunken}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-inverse:
    backgroundColor: "{colors.inverse-surface}"
    textColor: "{colors.on-inverse-surface}"
    rounded: "{rounded.lg}"
    padding: 24px
  section-sheet:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 80px 72px 120px
  section-band-dark:
    backgroundColor: "{colors.inverse-surface}"
    textColor: "{colors.on-inverse-surface}"
    rounded: "{rounded.lg}"
    padding: 80px 72px 120px
  section-band-tint:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.2xl}"
    padding: 80px 72px
  score-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.score}"
    rounded: "{rounded.lg}"
    padding: 24px
  badge-success:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-warning:
    backgroundColor: "{colors.warning-soft}"
    textColor: "{colors.warning}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-error:
    backgroundColor: "{colors.error-soft}"
    textColor: "{colors.error}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  quote-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px 20px
  faq-item:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 24px 28px
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-background}"
  input-placeholder:
    textColor: "{colors.on-surface-subtle}"
    typography: "{typography.body-sm}"
  divider-strong:
    backgroundColor: "{colors.outline-strong}"
    height: 1px
  card-inverse-raised:
    backgroundColor: "{colors.inverse-surface-raised}"
    textColor: "{colors.on-inverse-surface}"
    rounded: "{rounded.md}"
    padding: 16px
  info-chip:
    backgroundColor: "{colors.tertiary-soft}"
    textColor: "{colors.tertiary-hover}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.inverse-surface}"
    textColor: "{colors.on-inverse-surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 64px 72px 32px
---

# Webfix Quiet Premium

## Overview

Ruhig, redaktionell und präzise. Die Seite soll wirken wie ein gut gesetztes Magazin über ein technisches Produkt, nicht wie ein Dashboard und nicht wie ein Sicherheitstool mit Alarm-Optik.

Die Wirkung entsteht aus wenigen Entscheidungen, die konsequent durchgezogen werden:

- **Großer Kontrast in der Typo-Skala, kleiner Kontrast in der Farbe.** Eine leichte Serif-Headline mit 72px steht über einer Grotesk mit 14–18px. Dazwischen gibt es fast nichts. Farblich bleibt alles nah an Tinte und Nebel.
- **Eine einzige Akzentfarbe.** Blau erscheint nur auf der wichtigsten Aktion und auf sehr wenigen Datenpunkten. Alles andere ist Graustufe mit einem leicht kühlen Stich.
- **Die Seite ist ein Objekt.** Inhalte liegen auf weißen, gerundeten Flächen, die 12px vom Viewport-Rand eingerückt auf einem kühlen Nebelgrund liegen. So wirkt jede Sektion wie ein Blatt Papier auf einem Tisch und nicht wie eine endlose Webseite.
- **Echte Produkt-UI statt Illustration.** Scores, Prüfpunkte, Code-Ausschnitte und Statuszeilen werden als echte, fein gestaltete UI-Fragmente gezeigt. Diese Fragmente sind die Bildsprache.
- **Viel Luft, wenig Bewegung.** Großzügige Sektionsabstände (80px oben, 120px unten). Bewegung dient dem Lesen und lenkt nicht ab.

**Logo:** Eine Wortmarke „Webfix“ in Inter Tight ExtraBold (800) mit −3 % Laufweite. Einziges Merkmal ist der i-Punkt in Signalblau, der „Fix-Punkt“. Dazu gibt es ein Icon (W + Fix-Punkt im gerundeten Quadrat). Dateien liegen in `brand/logo/`, alle Regeln im Markenhandbuch `brand/index.html`. ExtraBold kommt nur im Logo vor, nie im Interface.

Zielgefühl: Kompetenz ohne Lautstärke. Seriös genug für Geschäftsführer und Kanzleien, modern genug für Agenturen.

## Colors

Die Palette ist fast monochrom. Kühle Tinte, kühler Nebel, Weiß und ein einziges Blau. Die Wärme kommt nur aus einem sehr hellen Creme-Ton, der für einzelne hervorgehobene Bänder sparsam eingesetzt wird.

- **Primary – Tinte (#1A1E23):** Fast-Schwarz mit Blau-Grau-Stich. Für Headlines, Fließtext und dunkle Pill-Buttons. Reines Schwarz wird nie verwendet.
- **Secondary – Schiefer (#515A63):** Für Navigation, Sekundärtext und Metadaten.
- **Tertiary – Signalblau (#2F68DB):** Die einzige Akzentfarbe. Nur für die primäre Aktion (Scan starten, Report anfordern), aktive Zustände und Links. Pro Viewport höchstens ein blauer Button. Hover dunkelt zu #264EB4 ab. Die Referenz nutzt #397DFF. Wir verwenden die dunklere Stufe, damit weiße Schrift WCAG AA erfüllt.
- **Neutral – Nebel (#F2F7F7):** Der Seitengrund hinter allen Sektionsflächen. Kühl und minimal grünlich, nie reines Weiß.
- **Surface – Weiß (#FFFFFF):** Für Sektionsblätter, Karten und Eingabefelder.
- **Surface Warm – Creme (#F8F8F3):** Für Eyebrow-Chips und höchstens ein hervorgehobenes Band pro Seite, etwa Preis oder Report. Dieser Ton kommt aus der Optivio-Referenz und bricht die Kühle bewusst und einmalig.
- **Inverse Surface – Graphit (#1F2429):** Für dunkle Bänder (Technik/Ablauf), den Footer und dunkle Karten. Ebenen darauf: #2B3239 (Karte) und #38414A (Control). Linien auf Dunkel sind weiß mit 12–16 % Deckkraft (≈ #3A4148).
- **Outline (#E2E4E5):** Haarlinien mit 1px. Trennlinien sind immer Haarlinien, nie dicke Linien.
- **Status:** Erfolg #1E7F4F auf #D9FDD3, Warnung #9A5B00 auf #FFF4D6, Fehler #C62445 auf #FCEBEF. Diese Farben gibt es nur in Score- und Prüfergebnis-Komponenten, immer als gedämpfte Badges und nie als Flächen oder Banner. Rot wird nie großflächig eingesetzt.

## Typography

Das Paar besteht aus einer Serif für Headlines und einer engen Grotesk für alles andere. Die Referenz setzt Tiempos Headline Light und UCity Pro (Voiceflow) bzw. Inter Tight (Optivio). Als frei lizenzierte Entsprechungen nutzen wir **Newsreader** (Light 300) und **Inter Tight**. Für Code und technische Werte kommt **JetBrains Mono** dazu.

- **Display & Headlines (Newsreader 300):** Immer Light und nie fett. Negative Laufweite (−2 bis −3 %) und eine enge Zeilenhöhe von 1.06–1.2. Die Hero-Headline mit 72px läuft über höchstens zwei Zeilen und ist zentriert. Sektions-Headlines haben 48px (Hauptsektion) bzw. 36px oder 28px (Untersektion).
- **Titles (Inter Tight 400–500, 20–24px):** Für Karten-Überschriften, mit leicht negativer Laufweite. Muster aus der Referenz: Der erste Satzteil steht in voller Tinte, die Fortsetzung im selben Satz in 50 % Deckkraft (z. B. „SEO-Check **findet, was Google nicht versteht**“).
- **Body (Inter Tight 400):** 18px für Lead-Texte unter Headlines, 16px Standard, 14px in Karten und Navigation. Zeilenhöhe 1.5–1.6. Maximale Zeilenlänge etwa 660px.
- **Labels:** 14px Semibold (600) für Buttons, 12px für Metadaten. Eyebrows haben 13px Medium in Normalschreibung. Versalien mit Sperrung werden nicht verwendet.
- **Score-Zahlen:** Inter Tight 500 mit 40px und Tabellenziffern.

Insgesamt gibt es nur drei Gewichte: 300 (Serif), 400 und 600. Die Ruhe kommt daher, dass Hierarchie über Größe und Schriftart entsteht und nicht über Fettung.

**Wichtig:** Alle Schriften werden selbst gehostet (WOFF2 vom eigenen Server) und nie von fonts.googleapis.com geladen, weil das ein DSGVO-Prüfpunkt von Webfix selbst ist.

## Layout

Das Layout ist ein **Fixed-Max-Width-Grid** mit 12 Spalten, 1296px Containerbreite und 24px Gutter. Text-Sektionen sind schmaler (1024px) und Fließtext höchstens 660px breit.

Das Abstandssystem basiert auf 4px. Die gängigen Stufen sind 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 80 / 120. Innerhalb von Komponenten werden fast nur 4, 8 und 16 genutzt. Zwischen Blöcken liegen 24–48px, zwischen Sektionen 80–120px.

**Rahmen:** Der Seitengrund ist Nebel (#F2F7F7). Jede Hauptsektion ist ein eigenes Blatt (weiß oder Graphit) mit 16px Radius, das 12px vom Viewport-Rand eingerückt ist. Zwischen zwei Blättern ist ein Streifen Nebel sichtbar. Innen haben die Blätter 72px Seitenrand (Desktop) und 16px auf Mobil.

**Rhythmus über die Sektionen hinweg:**

1. **Hero:** Weißes Blatt mit zentrierter Serif-Headline (72px), Lead-Text (18px) und URL-Eingabe mit Button inline. Darunter ein breites Bild- bzw. Produktfenster, über dem eine weiße UI-Karte schwebt.
2. **Nebel-Pause:** Kein Blatt. Zentrierte Serif-Headline (36px), Stat-Zeile mit Punkt-Trennern und ein Ghost-Button. Danach ein Mosaik aus Zitat- bzw. Logokarten.
3. **Feature-Blatt:** Weiß, linksbündige Headline (48px) mit Eyebrow, Unterzeile und Eingabe. Darunter ein großes, gerundetes Produktfenster.
4. **Dunkles Band:** Graphit, linksbündig mit Eyebrow in 50 % Weiß, Serif-Headline in Weiß und einem Bento-Grid aus dunklen Karten (2 + 3 Spalten) mit echter UI (Prüfprotokoll, Code, Fortschrittsbalken).
5. **Warmes Band (einmal):** Creme mit 32px Radius für Preis bzw. Report.
6. **Ressourcen/FAQ:** Weiß, 28px Serif-Headline links und Karten bzw. Akkordeon darunter.
7. **Footer:** Graphit-Blatt mit Serif-Claim links, E-Mail-Eingabe darunter und vier Linkspalten rechts.

Hell und dunkel wechseln sich ab. Zentriert und linksbündig wechseln sich ebenfalls ab: Hero und Pausen sind zentriert, Inhalts-Sektionen linksbündig.

## Elevation & Depth

Tiefe entsteht vor allem durch **Tonwerte** (Nebel → Weiß → Graphit) und erst danach durch Schatten. Schatten sind extrem weich, mehrlagig, mit negativem Spread und kühl getönt (Basis rgba(22,26,30)).

- **Karte/Control:** `0 1px 3px 1px rgba(22,26,30,.01), 0 4px 8px -6px rgba(22,26,30,.08), 0 1px 5px -4px rgba(22,26,30,.08)` – kaum sichtbar, wirkt fast wie eine zweite Haarlinie.
- **Schwebende UI-Karte (Hero):** `0 20px 44px -18px rgba(22,26,30,.12), 0 16px 28px -18px rgba(22,26,30,.12)`.
- **Eingabegruppe:** `inset 0 0 0 1px #E2E4E5, 0 8px 42px -16px rgba(22,26,30,.08)`.
- **Auf Dunkel:** Keine Schatten. Ebenen entstehen durch hellere Graphit-Stufen und 1px-Linien in rgba(255,255,255,.12).
- **Button-Primary:** Ein feiner Innenschatten unten (`inset 0 -1px 0 rgba(0,0,0,.16)`) lässt den Button minimal physisch wirken.

Harte Drop-Shadows, farbige Glows und Glassmorphism werden nicht verwendet.

## Shapes

Die Formensprache besteht aus weichen Rechtecken in einer klaren Hierarchie. Je größer die Fläche, desto größer der Radius.

- 2px für Mikroelemente (Fortschrittsbalken, Code-Cursor)
- 8px für Buttons, Inputs, Chips
- 10px für Zitat-/Logokarten und Eingabegruppen
- 16px für Karten, Sektionsblätter, Produktfenster
- 24px für FAQ-Items und große Feature-Karten
- 32px für das einmalige warme Band
- Voll gerundet (Pill) für Stat-Pills, Status-Badges, Avatare und den dunklen Pill-CTA mit runder Icon-Kappe rechts (Optivio-Muster)

Innerhalb einer Ebene werden scharfe und gerundete Ecken nicht gemischt.

## Components

- **Primary Button:** Blau (#2F68DB) mit weißer Schrift, 14px Semibold, 8px Radius, 40px Höhe. Er steht meist **in** einer weißen Eingabegruppe rechts (URL-Feld + Button als ein Objekt). Hover: #264EB4 in 150ms.
- **Pill-CTA (sekundär):** Tinte bzw. Creme, voll gerundet, Text links und rechts eine runde 32px-Kappe mit Pfeil-Icon. Für „Beispiel-Report ansehen“ oder „Unverbindlich anfragen“.
- **Ghost/Secondary:** Hellgrau (#E9E9EB) und kompakt, z. B. „Mehr erfahren“.
- **URL-Eingabe:** Weiß mit 1px-Innenlinie #E2E4E5, 10px Radius und 48px Höhe. Platzhalter in #636E73. Bei Fokus 2px-Ring in Blau mit 25 % Deckkraft.
- **Navigation:** 64px hoch auf Weiß. Logo links, 14px-Links in Schiefer in der Mitte, rechts „Login“ als Textlink und der blaue Button.
- **Eyebrow-Chip:** Kleiner Creme-Chip mit 13px-Text über Sektions-Headlines, z. B. „So funktioniert's“. Auf Dunkel als Text in 50 % Weiß ohne Chip.
- **Score-Karte:** Weiß, 16px Radius. Große Zahl (40px, Tabellenziffern), daneben „/100“ in Schiefer. Darunter ein 4px-Balken mit 2px Radius in Blau auf #E9E9EB und darunter Status-Badges.
- **Prüfzeile:** Eine Zeile mit Icon, Titel (14px), Unterzeile (12px, Schiefer) und rechts einem Status-Badge („Bestanden“ / „Prüfen“ / „Kritisch“), getrennt durch Haarlinien.
- **Bento-Karte (dunkel):** #1F2429 mit 1px-Linie rgba(255,255,255,.12) und 16px Radius. Titel 24px mit zweitoniger Deckkraft, rechts oben ein 32px-Quadrat-Button mit Pfeil. Unten ragt ein UI-Fragment aus der Karte, das an der Kante angeschnitten ist.
- **Stat-Zeile:** „Zahl + Label“-Paare, getrennt durch Mittelpunkte (·). Zahlen in Tinte, Labels in Schiefer.
- **FAQ-Akkordeon:** Offenes Item als hellgraue Fläche mit 24px Radius, geschlossene Items ohne Fläche. Rechts ein runder Plus/Minus-Knopf mit 24px.
- **Footer:** Graphit-Blatt mit Serif-Claim (28–36px) und E-Mail-Eingabe in dunkler Variante. Linkspalten mit 12px-Überschriften in 50 % Weiß und 14px-Links in Weiß.

## Motion

Die Bewegung ist zurückhaltend und präzise. Sie ist im Moment des Erscheinens spürbar und danach still.

- **Hero-Headline:** Wortweises Einblenden mit Opacity 0→1, translateY 8px→0 und Blur 4px→0, je Wort 500ms mit `cubic-bezier(0.2, 0.7, 0.3, 1)` und 40ms Versatz. Das ist die einzige „Inszenierung“ der Seite.
- **Scroll-Reveal:** Blöcke blenden einmalig mit Opacity, translateY 16px und leichtem Blur ein (600ms, `cubic-bezier(0.22, 1, 0.36, 1)`). Sie werden nie wiederholt, haben keinen Parallax-Effekt und keine Scroll-Bindung.
- **Hover:** Farbe bzw. Hintergrund in 150–200ms `ease`. Karten heben die Schattenstufe an, ohne zu skalieren. Buttons bekommen bei Klick translateY 1px (120ms).
- **Endlosschleifen:** Nur sehr langsam. Ein Logo- oder Zitatband driftet in 120–190s pro Durchlauf. Kleine UI-Fragmente (Scan-Fortschritt, Status „Läuft → Bestanden“) spielen ruhige 4–12s-Loops ab.
- **Score-Zähler:** Zahlen zählen beim ersten Sichtbarwerden in 800ms hoch, Balken wachsen mit.
- Bei `prefers-reduced-motion` wird alles sofort ohne Animation gezeigt.

## Do's and Don'ts

- Headlines immer in Newsreader Light setzen, nie fett und nie in Versalien.
- Pro Viewport höchstens eine blaue Fläche verwenden. Blau bedeutet „hier klicken“.
- Sektionen als eingerückte, gerundete Blätter auf dem Nebelgrund anlegen und nie randlos bis an den Viewport laufen lassen.
- Echte Produkt-Fragmente (Scores, Prüfzeilen, Code) zeigen statt Stock-Illustrationen oder 3D-Icons.
- Hell und dunkel abwechseln. Das dunkle Band nur einmal einsetzen, das warme Creme-Band ebenfalls nur einmal.
- Kontraste auf mindestens WCAG AA halten (4,5:1 für Text). Das gilt auch für Platzhalter und Text mit 50 % Deckkraft auf Dunkel.
- Schriften selbst hosten und keine externen Font-CDNs laden.
- Keine Alarm-Optik: keine roten Flächen, keine Warn-Dreiecke in Headlines, keine Countdown- oder Angst-Elemente.
- Keine Verläufe als Hintergrund und keine Neon-, Glow- oder Glaseffekte.
- Nicht mehr als drei Schriftgewichte und nicht mehr als zwei Schriftfamilien plus Mono.
- Keine zentrierten Fließtexte über drei Zeilen. Zentriert werden nur Hero, Pausen-Headlines und kurze Leads.
