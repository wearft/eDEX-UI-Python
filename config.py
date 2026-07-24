"""
Configuration file for eDEX-UI theme and settings
"""

# Color scheme (Cyberpunk/Watch Dogs 2 style)
COLORS = {
    # Primary colors
    "bg_dark": "#0a0e27",           # Deep dark blue-black
    "bg_darker": "#050812",         # Even darker background
    "accent_green": "#00ff41",      # Neon green (primary)
    "accent_cyan": "#00d4ff",       # Neon cyan
    "accent_purple": "#d946ef",     # Neon purple
    "accent_orange": "#ff6600",     # Neon orange
    "text_primary": "#00ff41",      # Green text
    "text_secondary": "#00d4ff",    # Cyan text
    "text_muted": "#004d00",        # Muted green
    "grid_line": "#1a2f4d",         # Grid lines
    "error": "#ff0055",             # Error red
    "success": "#00ff41",           # Success green
    "warning": "#ffaa00",           # Warning orange
}

# Font settings
FONTS = {
    "mono_small": ("Courier New", 9, "normal"),
    "mono_normal": ("Courier New", 10, "normal"),
    "mono_bold": ("Courier New", 10, "bold"),
    "mono_large": ("Courier New", 14, "bold"),
    "mono_title": ("Courier New", 16, "bold"),
    "sans_normal": ("Arial", 10, "normal"),
    "sans_bold": ("Arial", 10, "bold"),
}

# UI Settings
UI = {
    "border_width": 2,
    "corner_radius": 8,
    "padding": 10,
    "animation_speed": 50,  # ms per frame
    "glow_intensity": 0.8,
}

# Animation settings
ANIMATION = {
    "text_scan_speed": 0.05,  # seconds per character
    "pulse_speed": 0.5,        # seconds per pulse
    "transition_duration": 0.3, # seconds
}
