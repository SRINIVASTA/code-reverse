<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pinterest | Discover Ideas to Try</title>
    <style>
        :root {
            --color-brand-red: #e60023;
            --color-canvas-bg: #ffffff;
            --color-text-main: #211922;
            --color-text-muted: #5f5760;
            --color-neutral-fill: #efedf1;
            --color-neutral-hover: #e2e0e5;
            --color-border: #e5e7eb;
            --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: var(--font-stack); background-color: var(--color-canvas-bg); color: var(--color-text-main); -webkit-font-smoothing: antialiased; }

        /* Sticky Navigation Header Component Layout */
        .global-header { position: sticky; top: 0; background: var(--color-canvas-bg); height: 80px; display: flex; align-items: center; padding: 0 16px; z-index: 1000; }
        .header-inner { width: 100%; display: flex; align-items: center; gap: 12px; }
        .brand-logo { display: flex; align-items: center; gap: 6px; text-decoration: none; color: var(--color-brand-red); font-weight: 700; font-size: 20px; }
        
        .search-bar-wrap { flex-grow: 1; position: relative; display: flex; align-items: center; }
        .search-input { width: 100%; background: var(--color-neutral-fill); border: none; border-radius: 24px; height: 48px; padding: 0 44px; font-size: 16px; transition: background 0.2s; }
        .search-input:hover { background: var(--color-neutral-hover); }
        .search-input:focus { outline: 2px solid var(--color-text-main); background: var(--color-canvas-bg); }

        .btn { border: none; font-size: 16px; font-weight: 600; height: 48px; padding: 0 16px; border-radius: 24px; cursor: pointer; transition: background 0.2s, transform 0.1s; white-space: nowrap; }
        .btn:active { transform: scale(0.96); }
        .btn-primary { background: var(--color-brand-red); color: white; }
        .btn-primary:hover { background: #b6001a; }
        .btn-secondary { background: var(--color-neutral-fill); color: var(--color-text-main); }
        .btn-secondary:hover { background: var(--color-neutral-hover); }

        /* Hero Container Component */
        .hero-showcase { text-align: center; padding: 40px 24px; }
        .hero-title { font-size: 56px; font-weight: 700; letter-spacing: -1.5px; margin-bottom: 8px; }
        .hero-subtitle { font-size: 18px; color: var(--color-text-muted); }

        /* Responsive Columns Masonry Discovery Canvas */
        .discovery-canvas { padding: 0 16px 40px 16px; }
        .masonry-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 16px; }
        .pin-card { background: var(--color-canvas-bg); border-radius: 16px; overflow: hidden; cursor: zoom-in; }
        .img-wrapper { width: 100%; border-radius: 16px; overflow: hidden; background: var(--color-neutral-fill); position: relative; }
        .pin-img { width: 100%; height: auto; display: block; transition: filter 0.2s; }
        .pin-card:hover .pin-img { filter: brightness(0.85); }
        .pin-meta { padding: 8px 4px; font-size: 14px; font-weight: 700; }
        .pin-author { font-size: 12px; color: var(--color-text-muted); font-weight: 500; margin-top: 2px; }

        @media (max-width: 768px) {
            .search-bar-wrap, .brand-logo span { display: none; }
            .hero-title { font-size: 36px; }
        }
    </style>
</head>
<body>

    <header class="global-header">
        <div class="header-inner">
            <a href="#" class="brand-logo">
                <svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 0a12 12 0 0 0-4.37 23.17c-.07-.35-.13-.88 0-1.27l1.39-5.88s-.35-.7-.35-1.74c0-1.63.95-2.85 2.13-2.85 1 0 1.49.75 1.49 1.66 0 1-.64 2.51-.97 3.91-.28 1.18.54 2.13 1.7 2.13 2.05 0 3.63-2.61 3.63-5.69 0-2.35-1.55-4.09-4.46-4.09-3.05 0-4.94 2.27-4.94 4.8 0 .87.25 1.5.64 1.95a.39.39 0 0 1 .09.37c-.03.14-.1.57-.14.73a.28.38 0 0 1-.4.22c-2-.82-2.92-3-2.92-5.41 0-4 3.37-8.77 10-8.77 5.25 0 8.71 3.79 8.71 7.91 0 5.4-3 9.49-7.51 9.49-1.5 0-2.92-.82-3.41-1.72l-1 3.78c-.32 1.25-.94 2.5-1.46 3.32A12 12 0 1 0 12 0z"/></svg>
                <span>Pinterest</span>
            </a>
            <div class="search-bar-wrap">
                <input type="text" class="search-input" placeholder="Search for recipes, home ideas, fashion inspiration...">
            </div>
            <button type="button" class="btn btn-secondary">Log in</button>
            <button type="button" class="btn btn-primary">Sign up</button>
        </div>
    </header>

    <section class="hero-showcase">
        <h1 class="hero-title">Discover ideas to try</h1>
        <p class="hero-subtitle">What do you want to explore today?</p>
    </section>

    <main class="discovery-canvas">
        <div class="masonry-grid">
            <div class="pin-card"><div class="img-wrapper"><img src="https://picsum.photos" class="pin-img"></div><div class="pin-meta">Creamy Garlic Tuscan Pasta<div class="pin-author">Gourmet Feed</div></div></div>
            <div class="pin-card"><div class="img-wrapper"><img src="https://picsum.photos" class="pin-img"></div><div class="pin-meta">Minimalist Japandi Bedroom Decor<div class="pin-author">Design Nest</div></div></div>
            <div class="pin-card"><div class="img-wrapper"><img src="https://picsum.photos" class="pin-img"></div><div class="pin-meta">Autumn Knitwear Capsule Wardrobe<div class="pin-author">Style Ensemble</div></div></div>
            <div class="pin-card"><div class="img-wrapper"><img src="https://picsum.photos" class="pin-img"></div><div class="pin-meta">DIY Textured Abstract Art Canvas<div class="pin-author">Craft Studio</div></div></div>
        </div>
    </main>

</body>
</html>
