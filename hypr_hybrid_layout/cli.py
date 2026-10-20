"""
Hypr-Hybrid-Layout CLI
"""

import sys
import argparse
from .switcher import apply_mode, toggle_mode, get_current_mode

def main():
    parser = argparse.ArgumentParser(
        prog="hypr-hybrid-layout",
        description="Zero-Restart 1-Click Tiling to Traditional Floating Desktop Switcher for Hyprland"
    )
    parser.add_argument("mode", nargs="?", choices=["tiling", "traditional", "floating", "toggle", "status"], default="toggle",
                        help="Mode to set (default: toggle between tiling and traditional)")
    args = parser.parse_args()

    if args.mode == "status":
        print(get_current_mode())
        sys.exit(0)

    if args.mode == "toggle":
        new_mode = toggle_mode()
        print(f"✓ Toggled desktop layout to: {new_mode}")
    else:
        apply_mode(args.mode)
        print(f"✓ Applied desktop layout: {args.mode}")

if __name__ == "__main__":
    main()
