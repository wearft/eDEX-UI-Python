# eDEX-UI - Watch Dogs 2 Style Interface in Python

A futuristic hacker interface inspired by Watch Dogs 2's eDEX-UI system, built with Python and Tkinter.

## Features

✨ **Cyberpunk Aesthetic**
- Neon green and cyan color scheme
- Futuristic typography with monospace fonts
- Grid backgrounds and glowing effects

📊 **Interactive Panels**
- **Terminal**: Command-line interface with colored output
- **File Browser**: Navigate your file system
- **System Monitor**: Real-time CPU, memory, and network graphs
- **Code Editor**: Python syntax highlighting
- **Visualizer**: Animated network node visualization

🎨 **Visual Effects**
- Animated scanlines
- Pulsing text effects
- Smooth transitions
- Grid patterns

## Installation

```bash

# Clone the repositorygit 
clone https://github.com/wearft/eDEX-UI-Python.git
cd eDEX-UI-Python

# Install dependenciespip
install -r requirements.txt

#lancementpython
main.py

## coding 

Running
bash

python main.py

Project Structure
Code

eDEX-UI-Python/
├── main.py              # Entry point
├── config.py            # Theme and configuration
├── requirements.txt     # Python dependencies
│
├── ui/
│   ├── main_window.py   # Main application window
│   ├── panels/
│   │   ├── terminal.py       # Terminal panel
│   │   ├── file_browser.py   # File browser
│   │   ├── system_monitor.py # System monitoring
│   │   ├── code_editor.py    # Code editor
│   │   └── visualizer.py     # Data visualizer
│   └── widgets/
│       ├── bordered_frame.py # Bordered frame widget
│       └── scanlines.py      # Scanline effect

Customization
Colors

Edit config.py to change the color scheme:
Python

COLORS = {
    "accent_green": "#00ff41",
    "accent_cyan": "#00d4ff",
    # ... more colors
}

Fonts

Modify font settings in config.py:
Python

FONTS = {
    "mono_normal": ("Courier New", 10, "normal"),
    # ... more fonts
}

Animation Speed

Adjust animation parameters in config.py:
Python

ANIMATION = {
    "text_scan_speed": 0.05,
    "pulse_speed": 0.5,
}

Features to Add

    Enhanced syntax highlighting
    File content viewer with hex dump
    Network graph with real data
    Command execution system
    Dark/Light theme toggle
    Draggable panels
    Fullscreen mode
    Custom bash commands
    Recording/Playback features

Screenshots

(Coming soon)
Credits
wearft the creator

Inspired by the eDEX-UI from Watch Dogs 2 (Ubisoft).
License

MIT License

Made with ❤️

