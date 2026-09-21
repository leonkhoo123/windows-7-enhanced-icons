# Windows 7 Enhanced Icons

Scalable Windows 7 icon theme for Linux desktops (KDE Plasma, GTK, and others).

Original work: *Plasma SVG Win7 Theme* by **Blackcrack /
[Blackysgate.de](https://www.blackysgate.de)**.
Enhanced edition by **Leon Khoo**.

> This is the **icon theme only**. The matching Plasma global theme, color
> scheme, window decoration and Aero components live in the companion repo
> `windows-7-enhanced`.

## Install

```bash
./install.sh              # install / update the icon theme
./install.sh --uninstall  # remove it
```

Installs to `${XDG_DATA_HOME:-$HOME/.local/share}/icons/windows-7-enhanced`
(no username hardcoded). Then select **Windows 7 Enhanced** in
**System Settings → Appearance → Icons**.

## Contents

```
windows-7-enhanced/     the icon theme (index.theme + scalable/ + size symlinks)
install.sh              user-level installer
docs/                   original author's technical notes
extras/  tools/         helper files and the SVG build script
```

## License

**CC BY-NC-SA 4.0** (Attribution-NonCommercial-ShareAlike) — see `COPYING`.
Non-commercial: you may share and adapt with credit, but not sell it.

The theme also contains **third-party artwork** that keeps its own copyright,
e.g. weather applet icons from `deviantart.com/jackseller` and various
vendor/application logos. See `docs/` and `AUTHORS`.
