#!/usr/bin/env python3
"""
build-user-desktop-svg.py

Compose a TRUE-VECTOR "user-desktop" (Windows 7 style) icon for the
windows-7-enhanced icon theme, from two existing vector sources:

    monitor : scalable/places/desktop.svg                         (this theme)
    folder  : Win7-plasma5up-...-blackysgate.de/.../folder_stock.svg

The folder SVG is split into its back panel (g7) and front cover (g13) so the
monitor can be sandwiched between them, exactly like the original Win7 icon.

Layer order (bottom -> top):  folder-back  ->  monitor  ->  folder-front

Both sources share 35 colliding gradient/element IDs, so every id (and every
url(#...) / href="#..." reference) is namespaced with a prefix ("m_"/"f_").

Positioning was derived by measuring the blue (monitor) and yellow (folder)
pixel bounds of the authentic 128px raster and matching the transform.

Run:   python3 build-user-desktop-svg.py
Output: scalable/places/user-desktop-W7.svg   (user-desktop.svg symlinks here)
"""

import os
import re

# --- paths ------------------------------------------------------------------
HOME = os.path.expanduser("~")
ICONS = os.path.join(HOME, ".local/share/icons")
THEME = os.path.join(ICONS, "windows-7-enhanced")

MONITOR = os.path.join(THEME, "scalable/places/desktop.svg")
FOLDER = os.path.join(
    ICONS,
    "Win7-plasma5up-scalable-icontheme-blackysgate.de/scalable/places/folder_stock.svg",
)
# user-desktop.svg is a symlink to this file
OUT = os.path.join(THEME, "scalable/places/user-desktop-W7.svg")

# --- geometry:  p  ->  s*p + t   (in 256-unit viewBox space) ----------------
FS, FTX, FTY = 1.00, -8.0, 5.0    # folder  (both halves)
MS, MTX, MTY = 0.77, 45.0, 55.0   # monitor (sandwiched)


def strip_svg(path):
    """Return (defs, body) with prolog / svg wrapper / editor cruft removed."""
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<svg\b[^>]*>", s, re.S)
    body = s[m.end(): s.rfind("</svg>")]
    body = re.sub(r"<sodipodi:namedview\b.*?/>", "", body, flags=re.S)
    body = re.sub(r"<metadata\b.*?</metadata>", "", body, flags=re.S)
    d = re.search(r"<defs\b[^>]*>.*?</defs>", body, re.S)
    defs = d.group(0) if d else ""
    return defs, (body.replace(defs, "") if defs else body)


def extract_group(body, gid):
    """Extract a top-level <g id="gid">...</g> including nested groups."""
    i = body.find(f'id="{gid}"')
    start = body.rfind("<g", 0, i)
    depth = 0
    for mm in re.finditer(r"<(/?)g\b", body[start:]):
        if mm.group(1) == "":
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return body[start: start + mm.end() + 1]
    return ""


def namespace(frag, prefix):
    """Prefix every id and every reference to an id (avoids collisions)."""
    frag = re.sub(r'id="([A-Za-z0-9_.:-]+)"',
                  lambda m: f'id="{prefix}{m.group(1)}"', frag)
    frag = re.sub(r'url\(#([A-Za-z0-9_.:-]+)\)',
                  lambda m: f'url(#{prefix}{m.group(1)})', frag)
    frag = re.sub(r'(xlink:href|href)="#([A-Za-z0-9_.:-]+)"',
                  lambda m: f'{m.group(1)}="#{prefix}{m.group(2)}"', frag)
    return frag


def main():
    mdefs, mbody = strip_svg(MONITOR)
    fdefs, fbody = strip_svg(FOLDER)
    fback = extract_group(fbody, "g7")     # folder back panel
    ffront = extract_group(fbody, "g13")   # folder front cover

    mdefs, mbody = namespace(mdefs, "m_"), namespace(mbody, "m_")
    fdefs = namespace(fdefs, "f_")
    fback, ffront = namespace(fback, "f_"), namespace(ffront, "f_")

    out = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
     xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
     width="256" height="256" viewBox="0 0 256 256" version="1.1">
  <title>user-desktop (Windows 7 style, true vector)</title>
  <defs>
    {mdefs}
    {fdefs}
  </defs>
  <g id="folder-back" transform="translate({FTX},{FTY}) scale({FS})">
    {fback}
  </g>
  <g id="monitor" transform="translate({MTX},{MTY}) scale({MS})">
    {mbody}
  </g>
  <g id="folder-front" transform="translate({FTX},{FTY}) scale({FS})">
    {ffront}
  </g>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"wrote {OUT}")
    print(f"  folder  = scale {FS}, translate ({FTX}, {FTY})")
    print(f"  monitor = scale {MS}, translate ({MTX}, {MTY})")


if __name__ == "__main__":
    main()
