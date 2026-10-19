#!/usr/bin/env python3
"""Build Rahul Raghudhas's private static website from local HTML content."""
from pathlib import Path
import html
import shutil

ROOT = Path(__file__).resolve().parent
ORIGINAL = ROOT / 'original' / 'quarks-main'
SITE = ROOT / 'site'
SITE.mkdir(exist_ok=True)
(SITE / 'assets').mkdir(exist_ok=True)
for name in ['project.jpg']:
    if (ORIGINAL / name).exists():
        shutil.copy2(ORIGINAL / name, SITE / 'assets' / name)
CV_SOURCE = Path('/home/iitm/Documents/spec/per/cv/Rahul_Raghudhas_Corporate_Research_CV_Aug_2026.docx.pdf')
CV_TARGET = SITE / 'assets' / 'Rahul_Raghudhas_CV_Aug_2026.pdf'
if CV_SOURCE.exists():
    shutil.copy2(CV_SOURCE, CV_TARGET)
if not CV_TARGET.is_file():
    raise FileNotFoundError('The local CV PDF is required for the download links.')


def arrow():
    return '<span aria-hidden="true">↗</span>'


def page(name, title, description, body):
    prefix = '' if name == 'home' else '../'
    links = [('home', 'Home', 'index.html'), ('about', 'Profile', 'about/index.html'),
             ('projects', 'Research', 'projects/index.html'),
             ('publications', 'Publications', 'publications/index.html'), ('contact', 'Contact', 'contact/index.html')]
    nav = ''.join(f'<a href="{prefix}{url}"' + (' aria-current="page"' if key == name else '')
                  + f'>{label}</a>' for key, label, url in links)
    body = body.replace('@@', prefix).replace('<br>', '<br> ')
    result = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <meta name="robots" content="noindex, nofollow">
  <meta name="referrer" content="no-referrer">
  <title>{html.escape(title)} | Rahul Raghudhas · Quarks</title>
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header wrap">
    <a class="brand" href="{prefix}index.html" aria-label="Rahul Raghudhas · Quarks home"><span class="brand-mark" aria-hidden="true">q.</span><span>quarks<span class="brand-subtitle">Rahul Raghudhas · Climate Scientist</span></span></a>
    <nav aria-label="Main navigation">{nav}</nav>
  </header>
  <main id="main" tabindex="-1">{body}</main>
  <footer class="site-footer wrap">
    <div><a class="footer-brand" href="{prefix}index.html">quarks.</a><p>Rahul Raghudhas · Climate Scientist</p></div>
    <div class="footer-links"><a href="{prefix}projects/index.html">Research</a><a href="{prefix}publications/index.html">Publications</a><a href="{prefix}contact/index.html">Contact {arrow()}</a></div>
    <p class="footer-note">Profile &amp; research details · <a href="{prefix}assets/Rahul_Raghudhas_CV_Aug_2026.pdf">CV, August 2026</a></p>
  </footer>
</body>
</html>
'''
    path = SITE / ('index.html' if name == 'home' else f'{name}/index.html')
    path.parent.mkdir(exist_ok=True)
    path.write_text(result)


PAGES = [
    ('home', 'Climate Scientist & Earth-System Modelling', 'Rahul Raghudhas: climate scientist at IITM Pune, working on Earth-system modelling, tropical climate dynamics, and climate AI.'),
    ('about', 'Profile & Experience', 'Rahul Raghudhas: professional experience, education, technical expertise, and research background.'),
    ('projects', 'Research & Model Development', 'Research in UFS, CICE6, DCPP-C, Pacific–monsoon teleconnections, MJO, tropical cyclones, and climate AI.'),
    ('publications', 'Publications & Research Outputs', 'Peer-reviewed publications and ongoing research by Rahul Raghudhas on monsoon, MJO, tropical cyclones, and climate predictability.'),
    ('contact', 'Contact', 'Contact Rahul Raghudhas, Project Scientist-I at IITM Pune, and download his research CV.'),
]
for name, title, description in PAGES:
    page(name, title, description, (ROOT / 'content' / (name + '.html')).read_text())
(SITE / '.nojekyll').write_text('')
(SITE / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('Built', len(PAGES), 'static pages at', SITE)
