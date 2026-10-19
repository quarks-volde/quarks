# Review of the supplied Quarks website

Source: `/home/iitm/Documents/spec/website/rr/quarks-main.zip`.
The findings below describe that archive, not a verified current GitHub checkout.

## Changes prepared in the local draft

| Original finding | Draft response |
| --- | --- |
| Home page contains an unmatched closing `div`. | Rebuilt the page with complete HTML structure. |
| Home includes a blog list, but the ZIP contains no posts. | Replaced the empty section with links to the three existing research projects. |
| Navigation is manually listed inside the original home content. | Added consistent navigation and a current-page indicator on all four pages. |
| Research images use fixed `/quarks/` paths and no image presentation rules are supplied. | Used relative links, responsive figures, descriptive alternative text, and full-size image links. |
| About and Projects use justified paragraphs. | Used left-aligned paragraphs with a readable line length and spacing. |
| Project descriptions are lengthy and have no on-page navigation. | Added project anchors and an on-page contents list; retained all original paragraphs. |
| `_config.yml` repeats `github_username`. | The draft uses static HTML and has no Jekyll configuration dependency; the original remains unchanged. |

## Content to confirm

1. **Regional model name:** the original heading says “ROMS-WRF Coupled Model,”
   but its paragraphs say “CROCO-WRF.” The original wording is retained in the
   project detail. Confirm the intended name before a release.
2. **Precipitation figure:** the filename and original image label identify
   1950–2021. The archive does not supply a dataset citation, units, averaging
   period/method, or a detailed scientific caption. The draft does not invent
   these details. Add them before treating this as a self-contained research
   figure.
3. **Methods wording:** the original describes KNN as being applied for
   clustering. Confirm the exact method and intended wording. The paragraph is
   preserved, and this review does not validate the scientific claims.
4. **Profile and contact:** confirm whether “Quarks” is the desired public name
   and whether the supplied email and social account should remain visible.
   The archive contains no CV, publication list, institutional affiliation, or
   update brief to incorporate.
5. **Private access:** decide whether the desired outcome is local-only work,
   a private source repository, or an authenticated website. This draft implements
   local-only work; existing remote visibility settings have not been changed.

## Validation

- All four generated HTML files were parsed successfully.
- Local navigation, image and stylesheet links, and project anchors resolve.
- Each page has one main heading, a main landmark, and an active navigation item.
- All displayed images have alternative text.
- No automatic external resource URLs were found in the generated pages.
- All original About and Projects paragraphs are present in the draft.
- Extracted original files match the ZIP byte-for-byte.

- Headless Chrome checked all four pages at 1440, 390, and 320 CSS pixels.
- No horizontal overflow, unloaded images, or missing stylesheets were detected.
- Browser clicks successfully navigated between pages and to project sections.
- Browser resource entries showed no automatic external requests from the pages.
- Desktop and mobile screenshots were visually reviewed. A spacing issue when
  headings reflowed on mobile was corrected before the final check.

See `browser-check-results.json` for the browser results, and
`desktop-preview.png` / `mobile-preview.png` for the visual previews.
External email/social destinations and the current live website have not been
tested.
