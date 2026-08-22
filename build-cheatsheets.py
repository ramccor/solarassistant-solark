#!/usr/bin/env python3
"""Render cheatsheet-*.md to US-letter PDFs via headless Chrome.

    python3 build-cheatsheets.py            # all sheets
    python3 build-cheatsheets.py generator  # one sheet

Requires python-markdown and Google Chrome. Output: cheatsheet-<name>.pdf
"""
import glob, os, re, subprocess, sys, tempfile
import markdown

CSS = """
@page { size: letter; margin: 0.45in 0.5in 0.5in 0.5in; }
html { font-family: "Segoe UI", "Noto Sans", "DejaVu Sans", Arial, sans-serif; font-size: 9.2pt; line-height: 1.28; color: #111; }
body { margin: 0; }
h1 { font-size: 15pt; margin: 0 0 4pt 0; border-bottom: 2.5px solid #222; padding-bottom: 2pt; }
h2 { font-size: 11.5pt; margin: 9pt 0 3pt 0; color: #1c2c4c; border-bottom: 1px solid #777; padding-bottom: 1pt; break-after: avoid; }
h3 { font-size: 10pt; margin: 7pt 0 2pt 0; break-after: avoid; }
p { margin: 2.5pt 0; }
ul, ol { margin: 2pt 0 2pt 16pt; padding: 0; }
li { margin: 1pt 0; }
li > p { margin: 1pt 0; }
table { border-collapse: collapse; width: 100%; margin: 3pt 0 5pt 0; font-size: 8.4pt; break-inside: auto; }
th, td { border: 1px solid #999; padding: 1.5pt 4pt; vertical-align: top; text-align: left; }
th { background: #e6e6e6; color: #000; }
tr { break-inside: avoid; }
blockquote { margin: 4pt 0; padding: 3pt 8pt; border-left: 4px solid #444; background: #f3f3f3; break-inside: avoid; }
/* Warning boxes: colour is never the only cue — thick black double border, ⚠ glyph, bold label, hatched edge. */
blockquote.warn { border: 3px double #000; border-left: 10px solid #000; background: repeating-linear-gradient(135deg, #fff, #fff 6px, #f0f0f0 6px, #f0f0f0 12px); padding: 5pt 9pt; }
blockquote.warn strong:first-child { font-size: 10pt; letter-spacing: 0.02em; }
.chk { font-family: "DejaVu Sans", sans-serif; }
li.step { margin: 2pt 0 2pt 0; list-style: none; text-indent: -16pt; padding-left: 16pt; }
blockquote p { margin: 1pt 0; }
code { font-family: "DejaVu Sans Mono", Consolas, monospace; font-size: 8.3pt; background: #f1f1f1; padding: 0 2pt; }
hr { border: 0; border-top: 1px solid #bbb; margin: 6pt 0; }
img { display: block; max-width: 100%; height: auto; margin: 3pt auto 1pt auto; break-inside: avoid; }
em.cap { display: block; font-size: 7.8pt; color: #444; text-align: center; margin: 0 0 5pt 0; }
p > em:only-child { display: block; font-size: 7.8pt; color: #444; text-align: center; margin: 0 0 5pt 0; }
.imgrow { display: flex; gap: 8pt; justify-content: center; align-items: flex-start; break-inside: avoid; }
.imgrow img { margin: 3pt 0 1pt 0; }
"""

# Per-image print widths (inches). Anything not listed gets the default.
WIDTHS = {
    "cheat-gen-table37.png": 6.0,
    "cheat-gen-dse-controller.png": 3.2,
    "cheat-solark-force-charge-steps.png": 5.4,
    "cheat-pytes-led-table.png": 4.6,
    "cheat-pytes-solark-comm-cable.png": 3.4,
    "cheat-pytes-solark-dip.png": 3.6,
    "cheat-solark-batt-setup-pytes.png": 2.6,
    "cheat-solark-libatt-info.png": 2.9,
    "cheat-solark-parallel-dip.png": 4.2,
    "cheat-solark-parallel-capacity.png": 4.4,
    "cheat-solark-parallel-tab.png": 2.4,
    "cheat-array-string-layout-photo.png": 3.4,
    "cheat-gen-distribution-panel.png": 3.6,
    "cheat-gen-table22-distribution.png": 4.2,
}
DEFAULT_W = 4.0
# Images that should sit side by side when adjacent in the source.
ROWS = [
    ("cheat-pytes-solark-comm-cable.png", "cheat-pytes-solark-dip.png"),
    ("cheat-solark-batt-setup-pytes.png", "cheat-solark-libatt-info.png"),
]

def size_images(html):
    def rep(m):
        src = m.group(1); name = os.path.basename(src)
        w = WIDTHS.get(name, DEFAULT_W)
        return f'<img src="{src}" style="width:{w}in" alt="">'
    html = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', rep, html)
    for a, b in ROWS:
        pat = re.compile(r'<p>(<img src="images/%s"[^>]*>)\s*(<img src="images/%s"[^>]*>)</p>' % (re.escape(a), re.escape(b)))
        html = pat.sub(r'<div class="imgrow">\1\2</div>', html)
    return html

def build(md_path):
    name = os.path.basename(md_path)[:-3]
    text = open(md_path, encoding="utf-8").read()
    text = re.sub(r"^(\s*)- \[ \] ", r"\1- &#9744;&nbsp; ", text, flags=re.M)
    body = markdown.markdown(text, extensions=["tables", "sane_lists"])
    body = size_images(body)
    body = re.sub(r"<blockquote>(\s*<p>\s*<strong>⚠)", r'<blockquote class="warn">\1', body)
    html = f'<!doctype html><html><head><meta charset="utf-8"><title>{name}</title><style>{CSS}</style></head><body>{body}</body></html>'
    html_path = os.path.join(os.getcwd(), f".{name}.print.html")
    open(html_path, "w", encoding="utf-8").write(html)
    pdf_path = os.path.join(os.getcwd(), f"{name}.pdf")
    subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", "file://" + html_path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(html_path)
    pages = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True).stdout
    n = re.search(r"Pages:\s+(\d+)", pages).group(1)
    print(f"{pdf_path}: {n} pages")

if __name__ == "__main__":
    sel = sys.argv[1:]
    files = sorted(glob.glob("cheatsheet-*.md"))
    if sel:
        files = [f for f in files if any(s in f for s in sel)]
    for f in files:
        build(f)
