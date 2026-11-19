/* Trinita Roy — site behaviour. No dependencies. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmtDate = d => new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });

  /* ── Nav ── */
  const btn = $('.menu-btn'), menu = $('#menu');
  if (btn && menu) {
    btn.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
    menu.addEventListener('click', e => { if (e.target.closest('a')) { menu.classList.remove('open'); btn.setAttribute('aria-expanded', false); } });
  }
  const yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* ── Scroll reveal ── */
  const rv = $$('.rv');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .08, rootMargin: '0px 0px -6% 0px' });
    rv.forEach(el => io.observe(el));
  } else rv.forEach(el => el.classList.add('in'));

  /* ── Project index hover preview ── */
  const peek = $('#peek');
  if (peek && matchMedia('(hover:hover) and (min-width: 961px)').matches) {
    const COL = { sage: ['#7f9475', '#43594a'], clay: ['#c9744f', '#a8492a'], ink: ['#44524a', '#1d2820'] };
    const art = (type, [a, b]) => {
      let g = '';
      if (type === 'wave') for (let i = 0; i < 46; i++) { const h = 14 + Math.abs(Math.sin(i * .55) * 46) + (i % 5) * 4; g += `<rect x="${6 + i * 6.3}" y="${75 - h / 2}" width="3" height="${h}" rx="1.5" fill="rgba(245,241,229,${.35 + (i % 7) / 12})"/>`; }
      if (type === 'nodes') { const p = [[40, 40], [110, 100], [170, 36], [230, 108], [270, 52]]; p.forEach((q, i) => { if (p[i + 1]) g += `<line x1="${q[0]}" y1="${q[1]}" x2="${p[i + 1][0]}" y2="${p[i + 1][1]}" stroke="rgba(245,241,229,.6)"/>`; g += `<circle cx="${q[0]}" cy="${q[1]}" r="${i % 2 ? 9 : 5}" fill="rgba(245,241,229,.9)"/>`; }); }
      if (type === 'rings') for (let i = 1; i < 7; i++) g += `<circle cx="95" cy="75" r="${i * 17}" fill="none" stroke="rgba(245,241,229,${.7 - i * .09})" stroke-width="${i % 2 ? 1 : 2}"/>`;
      if (type === 'grid') for (let y = 0; y < 8; y++) for (let x = 0; x < 17; x++) g += `<circle cx="${14 + x * 17.5}" cy="${14 + y * 18}" r="${((x * 3 + y * 5) % 7) / 2.2 + .8}" fill="rgba(245,241,229,.75)"/>`;
      if (type === 'spikes') for (let i = 0; i < 38; i++) { const h = i === 17 ? 120 : 8 + (i * 37 % 29); g += `<rect x="${8 + i * 7.6}" y="${150 - h}" width="4" height="${h}" fill="rgba(245,241,229,${i === 17 ? 1 : .5})"/>`; }
      return `<svg viewBox="0 0 300 150" preserveAspectRatio="xMidYMid slice" style="background:linear-gradient(135deg,${a},${b})">${g}</svg>`;
    };
    let x = 0, y = 0, tx = 0, ty = 0, raf;
    const loop = () => { x += (tx - x) * .16; y += (ty - y) * .16; peek.style.transform = `translate3d(${x}px,${y}px,0) scale(${peek.classList.contains('on') ? 1 : .92}) rotate(${(tx - x) * .04 - 2}deg)`; raf = requestAnimationFrame(loop); };
    const show = el => {
      const c = COL[el.dataset.c] || COL.sage;
      $('.art', peek).innerHTML = art(el.dataset.art, c) + `<b>${el.closest('.row').querySelector('.i').textContent}</b>`;
      $('.stat', peek).textContent = el.dataset.stat || '';
      $('p', peek).textContent = el.dataset.text || '';
      peek.classList.add('on'); cancelAnimationFrame(raf); loop();
    };
    $$('#index .row > *').forEach(el => {
      el.addEventListener('mouseenter', () => show(el));
      el.addEventListener('mouseleave', () => { peek.classList.remove('on'); setTimeout(() => !peek.classList.contains('on') && cancelAnimationFrame(raf), 300); });
      el.addEventListener('focus', () => show(el));
      el.addEventListener('blur', () => peek.classList.remove('on'));
    });
    addEventListener('mousemove', e => {
      const w = 300, h = 280;
      tx = Math.min(e.clientX + 28, innerWidth - w - 16);
      ty = Math.min(Math.max(e.clientY - h / 2, 70), innerHeight - h - 10);
      if (!peek.classList.contains('on')) { x = tx; y = ty; }
    }, { passive: true });
  }

  /* ───────────────────────── Hashnode blog ───────────────────────── */
  const HOST = 'nlp-nerd.hashnode.dev';
  const GQL = 'https://gql.hashnode.com';
  const FALLBACK = [
    ['everything-you-should-know-about-anthropics-model-context-protocol-mcp', "Everything You Should Know About Anthropic's Model Context Protocol (MCP)"],
    ['mixture-of-experts-moe-explained', 'Mixture of Experts (MoE) Explained'],
    ['faster-inference-in-large-language-models-llms', 'Faster Inference in Large Language Models (LLMs)'],
    ['machine-learning-fundamentals', 'Machine Learning Fundamentals'],
    ['look-into-a-news-ai-agent-project', 'Look into a News AI Agent Project'],
    ['lost-in-translation-understanding-parallel-corpora-in-machine-translation', 'Lost in Translation: Understanding Parallel Corpora in Machine Translation']
  ].map(([slug, title]) => ({ slug, title, brief: '', url: `https://${HOST}/${slug}`, tags: [] }));

  const gql = async (query, variables) => {
    const ctl = new AbortController(); const t = setTimeout(() => ctl.abort(), 9000);
    try {
      const r = await fetch(GQL, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ query, variables }), signal: ctl.signal });
      if (!r.ok) throw new Error(r.status);
      const j = await r.json(); if (j.errors) throw new Error(j.errors[0].message);
      return j.data;
    } finally { clearTimeout(t); }
  };

  const list = $('#posts');
  if (list) {
    const status = $('#status'), filters = $('#filters');
    const draw = (posts, live) => {
      list.innerHTML = posts.map(p => `
        <li class="post rv in" data-tags="${esc((p.tags || []).join('|'))}">
          <time datetime="${esc(p.publishedAt || '')}">${p.publishedAt ? fmtDate(p.publishedAt) : 'Hashnode'}</time>
          <div>
            <h2><a href="post.html?slug=${encodeURIComponent(p.slug)}">${esc(p.title)}</a></h2>
            ${p.brief ? `<p>${esc(p.brief)}</p>` : ''}
            <div class="tags">${(p.tags || []).slice(0, 4).map(t => `<span class="chip">${esc(t)}</span>`).join('')}${p.readTime ? `<span class="chip">${p.readTime} min</span>` : ''}</div>
          </div>
          <div class="thumb">${p.cover ? `<img src="${esc(p.cover)}" alt="" loading="lazy">` : ''}</div>
        </li>`).join('');
      status.textContent = live ? `${posts.length} posts · synced live from ${HOST}` : `Showing saved list · couldn't reach Hashnode just now`;
      const tags = [...new Set(posts.flatMap(p => p.tags || []))].sort();
      if (tags.length) {
        filters.innerHTML = ['All', ...tags].map((t, i) => `<button type="button" aria-pressed="${i === 0}" data-t="${esc(t)}">${esc(t)}</button>`).join('');
        filters.onclick = e => {
          const b = e.target.closest('button'); if (!b) return;
          $$('button', filters).forEach(x => x.setAttribute('aria-pressed', x === b));
          $$('.post', list).forEach(li => li.hidden = b.dataset.t !== 'All' && !li.dataset.tags.split('|').includes(b.dataset.t));
        };
      }
    };
    status.textContent = 'Loading from Hashnode…';
    gql(`query($h:String!){publication(host:$h){posts(first:50){edges{node{title slug brief publishedAt readTimeInMinutes coverImage{url} tags{name}}}}}}`, { h: HOST })
      .then(d => {
        const posts = d.publication.posts.edges.map(({ node: n }) => ({ slug: n.slug, title: n.title, brief: n.brief, publishedAt: n.publishedAt, readTime: n.readTimeInMinutes, cover: n.coverImage?.url, tags: (n.tags || []).map(t => t.name) }));
        draw(posts, true);
      }).catch(() => draw(FALLBACK, false));
  }

  /* ── Single post ── */
  const art = $('#article');
  if (art) {
    const slug = new URLSearchParams(location.search).get('slug');
    const orig = slug ? `https://${HOST}/${encodeURIComponent(slug)}` : `https://${HOST}/`;
    const fail = () => { art.innerHTML = `<p class="status mono">Couldn't load this post inline.</p><a class="btn solid" href="${esc(orig)}" target="_blank" rel="noopener">Read it on Hashnode ↗</a>`; };
    const clean = html => {
      const doc = new DOMParser().parseFromString(html, 'text/html');
      $$('script,style,iframe,object,embed,form,link,meta', doc).forEach(n => n.remove());
      $$('*', doc).forEach(n => [...n.attributes].forEach(a => { if (/^on/i.test(a.name) || (/^(href|src)$/i.test(a.name) && /^\s*javascript:/i.test(a.value))) n.removeAttribute(a.name); }));
      $$('a', doc).forEach(a => { a.target = '_blank'; a.rel = 'noopener'; });
      return doc.body.innerHTML;
    };
    if (!slug) fail(); else
      gql(`query($h:String!,$s:String!){publication(host:$h){post(slug:$s){title publishedAt readTimeInMinutes url coverImage{url} tags{name} content{html}}}}`, { h: HOST, s: slug })
        .then(d => {
          const p = d.publication.post; if (!p) return fail();
          document.title = `${p.title} — Trinita Roy`;
          art.innerHTML = `
            <a class="back mono" href="blog.html">← All writing</a>
            <h1>${esc(p.title)}</h1>
            <div class="byline mono"><span>${fmtDate(p.publishedAt)}</span><span>${p.readTimeInMinutes} min read</span><a href="${esc(p.url)}" target="_blank" rel="noopener">Original on Hashnode ↗</a></div>
            ${p.coverImage?.url ? `<img class="cover" src="${esc(p.coverImage.url)}" alt="">` : ''}
            <div class="prose">${clean(p.content.html)}</div>`;
        }).catch(fail);
  }

  /* ───────────────────────── Notes ───────────────────────── */
  const grid = $('#notes');
  if (grid) {
    const notes = (window.NOTES || []).slice().sort((a, b) => new Date(b.date) - new Date(a.date));
    const kind = f => /\.(png|jpe?g|webp|gif|avif|svg)$/i.test(f) ? 'image' : /\.pdf$/i.test(f) ? 'pdf' : 'file';
    const filters = $('#filters'), dlg = $('#viewer');
    const draw = tag => {
      const items = notes.filter(n => !tag || tag === 'All' || (n.tag || '') === tag);
      grid.innerHTML = items.length ? items.map(n => {
        const k = kind(n.file), thumb = n.thumb || (k === 'image' ? n.file : '');
        return `<button class="note rv in" type="button" data-i="${notes.indexOf(n)}" aria-label="Open ${esc(n.title)}">
          <div class="paper">${k !== 'image' ? `<span class="kind mono">${k === 'pdf' ? 'PDF' : 'File'}</span>` : ''}
            ${thumb ? `<img src="${esc(thumb)}" alt="" loading="lazy">` : `<div class="ph">${esc(n.title[0])}</div>`}
            <div class="meta"><h3>${esc(n.title)}</h3><span class="mono" style="color:var(--ink-2)">${n.date ? fmtDate(n.date) : ''}</span></div>
            ${n.desc ? `<p class="desc">${esc(n.desc)}</p>` : ''}</div></button>`;
      }).join('') : '<p class="status mono">No notes yet.</p>';
    };
    const tags = [...new Set(notes.map(n => n.tag).filter(Boolean))];
    if (tags.length > 1) {
      filters.innerHTML = ['All', ...tags].map((t, i) => `<button type="button" aria-pressed="${i === 0}" data-t="${esc(t)}">${esc(t)}</button>`).join('');
      filters.onclick = e => { const b = e.target.closest('button'); if (!b) return; $$('button', filters).forEach(x => x.setAttribute('aria-pressed', x === b)); draw(b.dataset.t); };
    }
    $('#count').textContent = `${notes.length} note${notes.length === 1 ? '' : 's'}`;
    draw();
    grid.addEventListener('click', e => {
      const b = e.target.closest('.note'); if (!b) return;
      const n = notes[+b.dataset.i], k = kind(n.file);
      $('h3', dlg).textContent = n.title;
      $('#vopen').href = n.file;
      $('.vbody', dlg).innerHTML = k === 'image' ? `<img src="${esc(n.file)}" alt="${esc(n.title)}">`
        : k === 'pdf' ? `<iframe src="${esc(n.file)}" title="${esc(n.title)}"></iframe>`
        : `<p style="padding:30px"><a class="btn solid" href="${esc(n.file)}" download>Download ${esc(n.file.split('/').pop())}</a></p>`;
      dlg.showModal();
    });
    $('#vclose').addEventListener('click', () => dlg.close());
    dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener('close', () => { $('.vbody', dlg).innerHTML = ''; });
  }
})();
