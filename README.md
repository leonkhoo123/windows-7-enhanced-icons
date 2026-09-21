# Windows 7 Enhanced Icons

Scalable Windows 7 icon theme for Linux desktops (KDE Plasma, GTK, and others).

> This is the **icon theme only**. The matching Plasma global theme, color
> scheme, window decoration and Aero components live in the companion repo
> [`windows-7-enhanced`](https://github.com/leonkhoo123/windows-7-enhanced).

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

**Changes in this edition:** not all icons are the original author's work.
This edition **replaces a number of the original icons** — some with newly
drawn artwork and some with hand-picked Windows 7 artwork converted from
`.ico` sources. This covers, for example, the archive/compressed-file
mimetypes, the installer/package mimetypes (`application-x-apple-diskimage`,
`application-vnd.debian.binary-package`, `application-x-rpm`,
`application-x-msi`, `application-vnd.android.package-archive`,
`application-x-xpinstall`, `package-x-generic`), the standard user folders
(`user-home`/`folder-home`, `user-desktop`, `folder-documents`,
`folder-download(s)`, `folder-music`, `folder-pictures`, `folder-videos`,
`folder-games`), the file-manager icons (`org.kde.dolphin`,
`system-file-manager`), the notification/status icons (the bell family,
e.g. `notification`, `notifications`, `preferences-desktop-notification-bell`
and the notification states, plus `dialog-error`) and the KDE Connect family
(`kdeconnect`, `preferences-kde-connect` and the `kdeconnect-tray` /
`-symbolic` variants, replaced with the supplied KDE Connect artwork), the
Disks & Devices tray icon (`device-notifier`, switched to the removable-media
USB artwork, also installed as `media-removable`), the firewall icons
(`firewall`, `firewall-config`, `preferences-security-firewall`), the
Clipboard tray icon (`klipper-symbolic`), the Configure action
(`configure`, used by the System Tray's "Configure System Tray..." entry) and
the right-click "Open With" action (`system-run`) and the opened-folder icon
(`folder-open`). The System Tray symbolic icons were also refreshed with
supplied Windows 7 artwork: the audio set
(`audio-volume-{high,medium,low,muted}-symbolic`), the network/Wi-Fi/LAN set
(the `network-*` family under both the `-symbolic` and plain names, including
the wireless signal-strength bars and the
offline/error/no-route/idle/receive states), the battery levels
(`battery-NNN` and `battery-NNN-charging` `-symbolic`, where the 10% steps
that have no source artwork are snapped up to the next level and `010` reuses
the `000` art), the BlueDevil Bluetooth tray family (`network-bluetooth*` and
`preferences-system-bluetooth*`, the inactive state greyed out and the locked
state given a padlock badge). Power-profile variants of every battery level are
also added under both the `-symbolic` and plain names
(`battery-NNN[-charging]-profile-{powersave,performance,balanced}`), with the
`powersave` profile drawn in yellow and `performance`/`balanced` left as the
normal charge icon. The originals that were swapped out are kept in `_backup/`
(this batch under `_backup/system-tray-symbolic/`). See **Credits** below.

The theme also contains **third-party artwork** that keeps its own copyright,
e.g. weather applet icons from `deviantart.com/jackseller` and various
vendor/application logos. See `docs/` and `AUTHORS`.

## Credits

* Original work: *Plasma SVG Win7 Theme* by **Blackcrack (Blacky)** —
  [Blackysgate.de](https://www.blackysgate.de). Most icons remain the original
  author's work.
* Windows 7 Enhanced edition — **Leon Khoo**. Based on the original by
  Blackcrack; this edition **replaces some of the original icons with newly
  drawn ones**, adds touched-up metadata, and includes a user-level install
  script. The replaced icons are © Leon Khoo; the rest keep the original
  author's copyright.
