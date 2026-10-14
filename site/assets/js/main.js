/* Webfix – Landingpage
   Ohne Abhängigkeiten. Alle Inhalte sind ohne JavaScript sichtbar und bedienbar. */
(() => {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hier die Adresse des echten Scan-Dienstes eintragen, z. B. 'https://app.webfix.de/scan'.
  // Solange leer, zeigt das Formular einen Hinweis und das Beispiel-Ergebnis.
  const SCAN_ENDPOINT = '';

  const DOMAIN_RE = /^(?:[a-z0-9äöüß](?:[a-z0-9äöüß-]{0,61}[a-z0-9äöüß])?\.)+[a-z]{2,}$/i;

  function normaliseUrl(value) {
    return value.trim()
      .replace(/^https?:\/\//i, '')
      .replace(/[/?#].*$/, '')
      .toLowerCase();
  }

  /* ---------- Header state ---------- */
  const header = document.querySelector('.site-header');
  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 24);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- Links that lead to the scan field ---------- */
  const heroInput = document.getElementById('scan-url-hero');
  const heroMsg = document.getElementById('scan-msg-hero');
  document.querySelectorAll('[data-focus-scan]').forEach((link) => {
    link.addEventListener('click', (e) => {
      if (!heroInput) return;
      e.preventDefault();
      document.getElementById('start').scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
      if (link.dataset.scanNote && heroMsg) {
        heroMsg.textContent = link.dataset.scanNote;
        heroMsg.className = 'form-msg';
      }
      setTimeout(() => heroInput.focus({ preventScroll: true }), reduceMotion ? 0 : 450);
      history.replaceState(null, '', '#start');
    });
  });

  /* ---------- Scan forms ---------- */
  const fixUrl = document.getElementById('f-url');
  document.querySelectorAll('[data-scan-form]').forEach((form) => {
    const input = form.querySelector('input');
    const msg = form.querySelector('.form-msg');
    input.addEventListener('input', () => {
      if (input.getAttribute('aria-invalid')) {
        input.removeAttribute('aria-invalid');
        msg.className = 'form-msg';
      }
    });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const domain = normaliseUrl(input.value);
      if (!DOMAIN_RE.test(domain)) {
        input.setAttribute('aria-invalid', 'true');
        msg.className = 'form-msg err';
        msg.textContent = 'Bitte geben Sie eine Website-Adresse ein, z. B. ihre-website.de.';
        input.focus();
        return;
      }
      input.removeAttribute('aria-invalid');
      if (fixUrl && !fixUrl.value) fixUrl.value = domain;
      try { sessionStorage.setItem('webfix-url', domain); } catch (err) { /* privat-Modus */ }

      if (SCAN_ENDPOINT) {
        msg.className = 'form-msg ok';
        msg.textContent = `Wir prüfen ${domain}. Das dauert meist wenige Minuten.`;
        window.location.href = `${SCAN_ENDPOINT}?url=${encodeURIComponent(domain)}`;
        return;
      }
      msg.className = 'form-msg ok';
      msg.textContent = `Danke. Der Live-Scan für ${domain} wird gerade angebunden. Unten sehen Sie, wie Ihr Ergebnis aussehen wird.`;
      setTimeout(() => {
        document.getElementById('ergebnis').scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
      }, 900);
    });
  });

  /* ---------- Hero scan demo (loops while visible) ---------- */
  const demo = document.querySelector('[data-scan-demo]');
  if (demo && !reduceMotion) {
    const rows = [...demo.querySelectorAll('.scan-row')];
    const status = demo.querySelector('[data-scan-status]');
    const badges = rows.map((r) => r.querySelector('.badge'));
    let timers = [];
    let running = false;

    const reset = () => {
      rows.forEach((row, i) => {
        row.classList.add('pending');
        badges[i].className = 'badge b-run';
        badges[i].textContent = 'Wartet';
      });
    };
    const run = () => {
      timers.forEach(clearTimeout);
      timers = [];
      reset();
      status.textContent = 'Prüfung läuft …';
      rows.forEach((row, i) => {
        timers.push(setTimeout(() => {
          row.classList.remove('pending');
          badges[i].textContent = 'Läuft …';
        }, 500 + i * 1100));
        timers.push(setTimeout(() => {
          badges[i].className = 'badge ' + badges[i].dataset.final;
          badges[i].textContent = badges[i].dataset.label;
        }, 1300 + i * 1100));
      });
      timers.push(setTimeout(() => { status.textContent = 'Fertig · 4 Scores'; }, 1400 + rows.length * 1100));
      timers.push(setTimeout(() => { if (running) run(); }, 9000));
    };
    badges.forEach((b) => { b.dataset.final = b.dataset.final || b.className.replace('badge ', ''); });

    const io = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && !running) { running = true; run(); }
      if (!entry.isIntersecting && running) {
        running = false;
        timers.forEach(clearTimeout);
        rows.forEach((row, i) => {
          row.classList.remove('pending');
          badges[i].className = 'badge ' + badges[i].dataset.final;
          badges[i].textContent = badges[i].dataset.label;
        });
        status.textContent = 'Fertig · 4 Scores';
      }
    }, { threshold: 0.35 });
    io.observe(demo);
  }

  /* ---------- Result tabs (WAI-ARIA tabs pattern) ---------- */
  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const select = (tab, focus) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
  };
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => select(tab, false));
    tab.addEventListener('keydown', (e) => {
      let next = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') next = tabs[(i + 1) % tabs.length];
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (e.key === 'Home') next = tabs[0];
      if (e.key === 'End') next = tabs[tabs.length - 1];
      if (next) { e.preventDefault(); select(next, true); }
    });
  });

  /* ---------- Count-up for the example scores ---------- */
  const counters = [...document.querySelectorAll('[data-count]')];
  if (counters.length && !reduceMotion && 'IntersectionObserver' in window) {
    const bars = [...document.querySelectorAll('.tabs .bar i')];
    bars.forEach((b) => { b.style.width = '0%'; });
    counters.forEach((c) => { c.textContent = '0'; });
    const io = new IntersectionObserver((entries) => {
      if (!entries.some((en) => en.isIntersecting)) return;
      io.disconnect();
      const start = performance.now();
      const dur = 900;
      const ease = (t) => 1 - Math.pow(1 - t, 3);
      const tick = (now) => {
        const p = Math.min(1, (now - start) / dur);
        counters.forEach((c) => { c.textContent = String(Math.round(ease(p) * Number(c.dataset.count))); });
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      bars.forEach((b) => { b.style.width = ''; });
    }, { threshold: 0.4 });
    io.observe(document.querySelector('.tabs'));
  }

  /* ---------- Section reveals ---------- */
  const reveals = [...document.querySelectorAll('[data-reveal]')];
  if ('IntersectionObserver' in window && !reduceMotion) {
    reveals.forEach((el) => {
      [...el.children].forEach((child, i) => {
        if (!child.style.getPropertyValue('--d')) child.style.setProperty('--d', String(i));
      });
    });
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach((el) => io.observe(el));
    // Sicherheitsnetz: nichts bleibt unsichtbar
    setTimeout(() => reveals.forEach((el) => el.classList.add('in')), 4000);
  } else {
    reveals.forEach((el) => el.classList.add('in'));
  }

  /* ---------- Fix form ---------- */
  const form = document.getElementById('fix-form');
  if (form) {
    try {
      const saved = sessionStorage.getItem('webfix-url');
      if (saved && fixUrl && !fixUrl.value) fixUrl.value = saved;
    } catch (err) { /* privat-Modus */ }

    const status = document.getElementById('fix-status');
    const fields = {
      name: { el: form.elements.name, test: (v) => v.trim().length > 1, msg: 'Bitte geben Sie Ihren Namen ein.' },
      email: { el: form.elements.email, test: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()), msg: 'Bitte geben Sie eine gültige E-Mail-Adresse ein, z. B. name@firma.de.' },
      url: { el: form.elements.url, test: (v) => DOMAIN_RE.test(normaliseUrl(v)), msg: 'Bitte geben Sie die Adresse Ihrer Website ein, z. B. ihre-website.de.' },
      consent: { el: form.elements.consent, test: (_, el) => el.checked, msg: 'Bitte stimmen Sie der Verarbeitung Ihrer Angaben zu, damit wir antworten können.' },
    };
    const showError = (key, text) => {
      const f = fields[key];
      const err = document.getElementById(`f-${key}-err`);
      if (text) f.el.setAttribute('aria-invalid', 'true'); else f.el.removeAttribute('aria-invalid');
      if (err) err.textContent = text || '';
    };
    Object.keys(fields).forEach((key) => {
      const f = fields[key];
      f.el.addEventListener(key === 'consent' ? 'change' : 'input', () => {
        if (f.el.getAttribute('aria-invalid') && f.test(f.el.value, f.el)) showError(key, '');
      });
    });

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      let first = null;
      Object.keys(fields).forEach((key) => {
        const f = fields[key];
        const ok = f.test(f.el.value, f.el);
        showError(key, ok ? '' : f.msg);
        if (!ok && !first) first = f.el;
      });
      if (first) {
        status.className = 'form-status err';
        status.textContent = 'Bitte prüfen Sie die markierten Felder.';
        first.focus();
        return;
      }

      const data = Object.fromEntries(new FormData(form).entries());
      data.url = normaliseUrl(data.url);
      const endpoint = form.dataset.endpoint;

      if (endpoint) {
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        status.className = 'form-status';
        status.textContent = 'Wird gesendet …';
        try {
          const res = await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
          if (!res.ok) throw new Error(String(res.status));
          form.reset();
          status.className = 'form-status ok';
          status.textContent = 'Danke, Ihre Anfrage ist angekommen. Wir melden uns persönlich bei Ihnen.';
        } catch (err) {
          status.className = 'form-status err';
          status.textContent = `Das Senden hat nicht geklappt. Bitte versuchen Sie es erneut oder schreiben Sie an ${form.dataset.mailto}.`;
        } finally {
          btn.disabled = false;
        }
        return;
      }

      // Ohne Formular-Backend: E-Mail mit allen Angaben vorbereiten.
      const body = [
        `Name: ${data.name}`,
        `E-Mail: ${data.email}`,
        `Website: ${data.url}`,
        data.phone ? `Telefon: ${data.phone}` : '',
        '',
        data.message ? `Was sollen wir beheben?\n${data.message}` : '',
      ].filter((l, i, a) => l !== '' || a[i - 1] !== '').join('\n');
      const href = `mailto:${form.dataset.mailto}?subject=${encodeURIComponent(`Fix-Anfrage für ${data.url}`)}&body=${encodeURIComponent(body)}`;
      status.className = 'form-status ok';
      status.innerHTML = '';
      status.append('Ihr E-Mail-Programm öffnet sich mit Ihrer Anfrage. Falls nicht, schreiben Sie an ');
      const a = document.createElement('a');
      a.href = `mailto:${form.dataset.mailto}`;
      a.textContent = form.dataset.mailto;
      status.append(a, '.');
      window.location.href = href;
    });
  }

  /* ---------- Mobile sticky CTA ---------- */
  const sticky = document.querySelector('[data-sticky-cta]');
  const hero = document.getElementById('start');
  const finalForm = document.getElementById('scan-url-final');
  if (sticky && hero && 'IntersectionObserver' in window) {
    let heroVisible = true;
    let finalVisible = false;
    const update = () => sticky.classList.toggle('show', !heroVisible && !finalVisible);
    new IntersectionObserver(([en]) => { heroVisible = en.isIntersecting; update(); }, { threshold: 0.05 }).observe(hero.querySelector('.scan-form'));
    if (finalForm) new IntersectionObserver(([en]) => { finalVisible = en.isIntersecting; update(); }).observe(finalForm.closest('section'));
    const fixSection = document.getElementById('fix');
    if (fixSection) new IntersectionObserver(([en]) => { sticky.toggleAttribute('data-hide', en.isIntersecting); sticky.classList.toggle('show', !heroVisible && !finalVisible && !en.isIntersecting); }).observe(fixSection);
  }
})();
