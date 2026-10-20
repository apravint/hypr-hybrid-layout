<div align="center">

# 🪟 hypr-hybrid-layout

**Zero-Restart 1-Click Tiling ⇄ Traditional Floating Desktop Switcher for Hyprland**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Compositor: Hyprland](https://img.shields.io/badge/Compositor-Hyprland%200.50%2B-cyan.svg)](https://hyprland.org)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)

<p align="center">
  <b>Switch between strict geometric tiling and a traditional floating desktop in &lt;50ms without restarting Hyprland.</b>
</p>

</div>

---

## ⚡ The Problem

Users transitioning from macOS or Windows often struggle with dynamic tiling window managers because every app is forced into strict tiled splits. 

When you want to show your desktop to family or coworkers, or simply prefer floating overlapping windows with rounded corners and drop shadows for creative workflows, Hyprland previously required manually editing config files and restarting the session.

**`hypr-hybrid-layout` provides an instant hotkey/CLI toggle between:**
1. **Dynamic Tiling Mode:** Sharp geometric tiling with 0px gaps and focused window prominence.
2. **Traditional Floating Mode:** 8px rounded window corners, subtle drop shadows, and automatic centered floating window spawning (`windowrulev2 = float, class:^(.*)$`).

---

## 🚀 Quickstart

### 1. Installation

```bash
pip install hypr-hybrid-layout
```

### 2. Integration with `hyprland.conf`

Add this line to your `~/.config/hypr/hyprland.conf`:
```ini
# Include the dynamic layout switch configuration
source = ~/.config/hypr/layout.conf
```

Bind a shortcut to toggle layouts (e.g. `Super + Alt + Space` or `Super + L`):
```ini
bind = SUPER_ALT, Space, exec, hypr-hybrid-layout toggle
```

### 3. Command-Line Usage

```bash
# Toggle between Tiling and Traditional Floating
hypr-hybrid-layout toggle

# Explicitly switch to Traditional Floating Mode
hypr-hybrid-layout traditional

# Explicitly switch to Tiling Mode
hypr-hybrid-layout tiling

# Query current desktop layout
hypr-hybrid-layout status
```

---

## 🧪 Testing

```bash
python -m unittest discover -s tests
```

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details. Created by [Ayyappa Pravin (@apravint)](https://github.com/apravint).
