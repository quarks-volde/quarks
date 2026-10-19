#!/usr/bin/env python3
"""Build a local static design draft from the unmodified archived pages."""
from pathlib import Path
import html
import re
import shutil

import markdown

ROOT = Path(__file__).resolve().parent
ORIGINAL = ROOT / 'original' / 'quarks-main'
SITE = ROOT / 'site'
SITE.mkdir(exist_ok=True)
(SITE / 'assets').mkdir(exist_ok=True)
for name in ['precipitation_1950_2021.png', 'research.jpg', 'project.jpg', 'project.png']:
    shutil.copy2(ORIGINAL / name, SITE / 'assets' / name)


def original_body(name):
    text = (ORIGINAL / name).read_text()
    text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.S)
    text = re.sub(r'^# .*\n', '', text, count=1, flags=re.M)
    text = re.sub(r'^!\[.*?\]\(.*?\)\s*$', '', text, flags=re.M)
    return markdown.markdown(text.strip()).replace(' style="text-align: justify;"', '')


def arrow():
    return '<span aria-hidden="true">↗</span>'


def page(name, title, description, body):
    prefix = '' if name == 'home' else '../'
    links = [('home', 'Overview', 'index.html'), ('about', 'About', 'about/index.html'),
             ('projects', 'Projects', 'projects/index.html'), ('contact', 'Contact', 'contact/index.html')]
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
  <title>{html.escape(title)} | Quarks</title>
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header wrap">
    <a class="brand" href="{prefix}index.html" aria-label="Quarks home"><span class="brand-mark" aria-hidden="true">q.</span><span>quarks<span class="brand-subtitle">Ocean–Atmospheric Research</span></span></a>
    <nav aria-label="Main navigation">{nav}</nav>
  </header>
  <main id="main" tabindex="-1">{body}</main>
  <footer class="site-footer wrap">
    <div><a class="footer-brand" href="{prefix}index.html">quarks.</a><p>Exploring ocean, atmosphere, and climate.</p></div>
    <div class="footer-links"><a href="{prefix}projects/index.html">Research projects</a><a href="{prefix}contact/index.html">Get in touch {arrow()}</a></div>
    <p class="footer-note">Ocean–Atmospheric Research</p>
  </footer>
</body>
</html>
'''
    path = SITE / ('index.html' if name == 'home' else f'{name}/index.html')
    path.parent.mkdir(exist_ok=True)
    path.write_text(result)


home = '''
<section class="hero wrap" aria-labelledby="hero-title">
  <div class="hero-copy"><p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> Ocean · Atmosphere · Climate</p>
    <h1 id="hero-title">Understanding a<br><em>connected climate.</em></h1>
    <p class="hero-description">Research in ocean–atmosphere interactions, climate change, and variability. Bringing coupled models and machine learning to complex climate questions.</p>
    <div class="actions"><a class="button button-dark" href="@@projects/index.html">Explore the research <span aria-hidden="true">↗</span></a><a class="text-link" href="@@about/index.html">About Quarks <span aria-hidden="true">→</span></a></div>
  </div>
  <aside class="hero-aside" aria-label="Research approaches"><span class="small-label">RESEARCH APPROACHES</span><ol><li><span>01</span> Coupled modelling</li><li><span>02</span> Climate variability</li><li><span>03</span> Machine learning</li></ol><p>Connecting physical processes<br>with data-driven methods.</p></aside>
</section>
<section class="feature-band" aria-labelledby="figure-title"><div class="wrap feature-grid">
  <div class="feature-copy"><p class="eyebrow">A view of the climate</p><h2 id="figure-title">Patterns across<br>the Indian Ocean.</h2><p>The ocean and atmosphere are studied together to explore climate variability and changing environmental conditions.</p><a class="text-link light-link" href="@@assets/precipitation_1950_2021.png">View full-size figure <span aria-hidden="true">↗</span></a></div>
  <figure class="feature-figure"><a href="@@assets/precipitation_1950_2021.png" aria-label="Open the precipitation map at full resolution"><img src="@@assets/precipitation_1950_2021.png" width="2500" height="1300" alt="Precipitation map covering the Indian Ocean and surrounding regions, with a colour scale from 5 to 23." fetchpriority="high"></a><figcaption><span>Precipitation</span><span>1950–2021</span></figcaption></figure>
</div></section>
<section class="wrap research-section" aria-labelledby="research-title"><div class="section-heading"><div><p class="eyebrow">Research directions</p><h2 id="research-title">Three ways into<br>a complex system.</h2></div><a class="text-link" href="@@projects/index.html">All projects <span aria-hidden="true">↗</span></a></div>
<div class="research-cards">
  <article class="research-card"><span class="card-number">01 / COUPLED MODELS</span><h3>Cyclones &amp;<br>ocean interactions</h3><p>Using COAWST to investigate cyclone formation, intensification, and propagation.</p><a href="@@projects/index.html#coawst">Explore COAWST <span aria-hidden="true">↗</span></a></article>
  <article class="research-card"><span class="card-number">02 / REGIONAL DYNAMICS</span><h3>Regional coupling &amp;<br>climate variability</h3><p>Exploring ocean–atmosphere coupling and the relationship between MJO and cyclonic activity.</p><a href="@@projects/index.html#regional-coupling">Explore regional modelling <span aria-hidden="true">↗</span></a></article>
  <article class="research-card"><span class="card-number">03 / DATA &amp; LEARNING</span><h3>Machine learning<br>for climate</h3><p>Investigating spatial patterns and temporal dependencies in ocean and atmospheric data.</p><a href="@@projects/index.html#climate-ml">Explore climate research <span aria-hidden="true">↗</span></a></article>
</div></section>
<section class="wrap contact-strip" aria-labelledby="contact-title"><div><p class="eyebrow">Start a conversation</p><h2 id="contact-title">Interested in this research?</h2><p>Get in touch about ocean–atmosphere modelling and climate science.</p></div><a class="button button-dark" href="@@contact/index.html">Get in touch <span aria-hidden="true">↗</span></a></section>
'''
page('home', 'Ocean–Atmospheric Research', 'Quarks: research in ocean–atmosphere interactions, coupled modelling, climate variability, and machine learning.', home)

about = '''
<section class="wrap page-intro"><p class="eyebrow">About Quarks</p><h1>Exploring the links<br>between <em>ocean and sky.</em></h1><p class="intro-description">Ocean–atmospheric science, climate change, and variability.</p></section>
<section class="wrap article-layout"><aside class="section-aside"><span class="small-label">RESEARCH PROFILE</span><p>Climate dynamics<br>Coupled modelling<br>Machine learning</p><a class="text-link" href="@@projects/index.html">View projects <span aria-hidden="true">↗</span></a></aside><div class="prose"><h2>About me</h2>
''' + original_body('about.md') + '''
<figure class="content-figure"><a href="@@assets/research.jpg" aria-label="Open the world map at full resolution"><img src="@@assets/research.jpg" width="1000" height="600" alt="World map showing the distribution of oceans and continents." loading="lazy"></a><figcaption>A global perspective on ocean–atmosphere research.</figcaption></figure>
<h2>Research interests</h2><ul class="interest-list"><li>El Niño–Southern Oscillation (ENSO)</li><li>Pacific Decadal Oscillation (PDO)</li><li>Madden–Julian Oscillation (MJO)</li><li>Indian Ocean Dipole (IOD)</li></ul>
<div class="inline-callout"><h3>From physical models to data</h3><p>Research combines coupled modelling with machine learning approaches, including CNNs and RNNs, to study climate dynamics.</p><a class="text-link" href="@@contact/index.html">Get in touch <span aria-hidden="true">↗</span></a></div>
</div></section>
'''
page('about', 'About', 'Research interests in climate dynamics, ocean–atmosphere coupling, and machine learning.', about)

project_html = original_body('projects.md')
pieces = re.split(r'<h2>(.*?)</h2>', project_html)
anchors = ['coawst', 'regional-coupling', 'climate-ml']
project_sections = []
for index, anchor in enumerate(anchors):
    title, paragraphs = pieces[index * 2 + 1:index * 2 + 3]
    project_sections.append(f'<article class="project-article" id="{anchor}" aria-labelledby="{anchor}-title"><p class="eyebrow">Project 0{index + 1}</p><h2 id="{anchor}-title">{title}</h2>{paragraphs}</article>')
projects = '''
<section class="wrap page-intro"><p class="eyebrow">Research projects</p><h1>Models, patterns,<br><em>and connections.</em></h1><p class="intro-description">Investigating climate processes through coupled models and data-driven methods.</p></section>
<div class="wrap article-layout"><aside class="section-aside"><nav class="project-nav" aria-label="On this page"><span class="small-label">ON THIS PAGE</span><a href="#coawst"><span>01</span> COAWST</a><a href="#regional-coupling"><span>02</span> Regional coupling</a><a href="#climate-ml"><span>03</span> Climate &amp; machine learning</a></nav></aside><div class="prose">
''' + ''.join(project_sections) + '''
<figure class="content-figure"><a href="@@assets/project.jpg" aria-label="Open the MJO phase diagram at full resolution"><img src="@@assets/project.jpg" width="1200" height="800" alt="World map titled Eastward Propagation of MJO, with phases 1 to 8 labelled along the tropics." loading="lazy"></a><figcaption>Eastward propagation of the Madden–Julian Oscillation (MJO).</figcaption></figure>
<div class="inline-callout"><h3>Continue the conversation</h3><p>For questions about the projects or research methods, get in touch.</p><a class="text-link" href="@@contact/index.html">Contact Quarks <span aria-hidden="true">↗</span></a></div>
</div></div>
'''
page('projects', 'Research projects', 'Research projects in COAWST, regional ocean–atmosphere modelling, and machine learning for climate variability.', projects)

contact = '''
<section class="wrap page-intro"><p class="eyebrow">Contact</p><h1>Let’s talk<br><em>climate science.</em></h1><p class="intro-description">Get in touch about the research, coupled modelling, and ocean–atmosphere interactions.</p></section>
<section class="wrap contact-grid" aria-label="Contact details"><article class="contact-card"><span class="small-label">01 / EMAIL</span><h2>Start a conversation.</h2><p>For research questions and enquiries.</p><a class="contact-address" href="mailto:workofmine.rahul@gmail.com">workofmine.rahul@gmail.com <span aria-hidden="true">↗</span></a></article><article class="contact-card contact-card-secondary"><span class="small-label">02 / SOCIAL</span><h2>Connect online.</h2><p>Follow the account linked on the original site.</p><a class="contact-address" href="https://twitter.com/RRaghudhas" rel="noreferrer">@RRaghudhas <span aria-hidden="true">↗</span></a><span class="contact-platform">X / Twitter</span></article></section>
<div class="wrap contact-end"><p>Explore the research before getting in touch.</p><a class="text-link" href="@@projects/index.html">Browse projects <span aria-hidden="true">→</span></a></div>
'''
page('contact', 'Contact', 'Contact Quarks about ocean–atmospheric research, climate science, and coupled modelling.', contact)
(SITE / '.nojekyll').write_text('')
(SITE / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('Built 4 static pages at', SITE)
