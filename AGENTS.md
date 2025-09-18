# Agent Instructions

## Repository-wide guidelines
- Do **not** commit binary artifacts (PDFs, ZIPs, etc.). Generate them during the build instead.
- Offline download assets are produced by `scripts/build_offline_assets.py` and should remain untracked output.
- The combined offline kit **must not** be packaged as a ZIP (leave the PDF/CSV as individual downloads).
