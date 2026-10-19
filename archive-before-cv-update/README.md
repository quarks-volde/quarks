# Quarks — private local draft

Open `site/index.html` in your browser to review the website. The About,
Projects, and Contact links work directly from disk. No server, account,
installation, or internet connection is needed to view the pages.

## Files

- `site/`: the updated static website, including all four pages and local assets.
- `original/quarks-main/`: an unchanged copy of the supplied ZIP contents.
- `REVIEW.md`: findings and content questions to resolve before a future release.
- `build_site.py`: regenerates the HTML from the archived research content.
- `site/assets/style.css`: the shared layout, colours, typography, and responsive rules.
- `desktop-preview.png` and `mobile-preview.png`: screenshots of the draft.
- `browser-check-results.json`: results for all four pages at three screen widths.
- `quarks-private-draft.zip`: a local bundle of this review folder, including the
  website, original source, generator, notes, and previews.

The original ZIP at `../quarks-main.zip` has not been modified.

## What changed

The draft adds a research-focused home page, consistent navigation, a mobile
layout, project anchor links, readable article widths, accessible focus styles,
a skip link, descriptive image text, and links to full-size research figures.
The empty blog section is omitted. The original About and Projects paragraphs,
email address, and social account are preserved. No publications, affiliations,
qualifications, or new research results have been invented.

This draft is plain HTML and CSS instead of a Jekyll build. Relative links let it
work directly from disk or under a subdirectory. `.nojekyll` is included in the
static output for a possible later GitHub Pages release. No release has been made.
The original Jekyll source remains available in `original/`.

## Privacy

The website files were created locally. No files were pushed to GitHub or sent
to a hosting service. No hosting account or hosted Site was created. The draft
contains no analytics, remote fonts, embedded third-party widgets, JavaScript,
or automatic external resource requests. The email and social links use the
details already present in the supplied ZIP and act only when clicked.

The review directory is owner-accessible only (mode `700`). This does not change
permissions on the original ZIP or on any existing remote repository or website.
The current GitHub repository visibility and live-site access were not verified.

The HTML contains `noindex, nofollow`, and `robots.txt` discourages crawling.
These are **not access controls**. This draft has no login or visitor
authentication. If it is later hosted, private access must be configured and
verified with the hosting service before uploading private material.

## Editing

For a small edit, edit the corresponding `site/…/index.html` directly. These
files are the complete working website. Shared styling is in
`site/assets/style.css`.

For regeneration, edit `build_site.py` and run:

```bash
python3 build_site.py
```

The generator uses the Python `markdown` package, which is available on this
computer. Viewing the generated website has no Python dependency. Regeneration
overwrites the HTML files and recopies the source images; it does not overwrite
the stylesheet. Keep content changes in the generator if you plan to rebuild.
