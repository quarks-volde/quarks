# Quarks — Rahul Raghudhas’s private local website

Open `site/index.html` in a browser. All five pages work directly from disk:
Home, Profile, Research, Publications, and Contact. No installation or server is
needed to view the website.

The content is based on Rahul Raghudhas’s August 2026 research CV, supplied at:
`/home/iitm/Documents/spec/per/cv/Rahul_Raghudhas_Corporate_Research_CV_Aug_2026.docx.pdf`.
The contact address is now `rahulraghudhas@gmail.com`, as listed in that CV.

## Editing

- `content/`: editable page content in HTML.
- `site/assets/style.css`: shared design and responsive layout.
- `build_site.py`: generates the five complete HTML pages using Python’s standard library.
- `site/assets/Rahul_Raghudhas_CV_Aug_2026.pdf`: unchanged copy of the supplied CV.

After editing `content/`, run `python3 build_site.py` from this directory.
Edit the stylesheet directly; rebuilding preserves it. The generator uses the
original CV file when available, or retains the bundled PDF when it is not.

## Privacy and preservation

Everything remains on this computer. Nothing was pushed to GitHub or published,
and the existing repository and live website’s access settings were not changed.
The website uses local images and styles, without scripts, analytics, external
fonts, embedded services, or automatic external resource requests. DOI and email
links act only when clicked. The CV download is also local.

This directory is owner-accessible only (mode 700). The HTML has `noindex,
nofollow`, and robots.txt discourages crawling. These settings are not website
authentication: the site is private here because it is local and has not been
hosted. Any future private hosting needs its own access control.

The supplied ZIP and PDF remain unchanged. `original/quarks-main/` retains the
original website; `archive-before-cv-update/` preserves the previous local draft.
The older generic profile and contact information have been replaced in the
active website by the supplied CV information. The MJO figure is retained from
the original website. No portrait, affiliations, credentials, or research results
beyond the supplied materials have been added.

## Local deliverables

- `quarks-cv-website.zip`: website files only, including the local CV download.
- `quarks-private-draft.zip`: current editable source and website bundle.
- `desktop-preview.png` / `mobile-preview.png`: homepage previews.
- `browser-check-results.json`: browser verification results.
- `REVIEW.md`: content source and verification notes.
