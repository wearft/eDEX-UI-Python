"""
Main window for eDEX-UI application
"""

import tkinter as tk
from tkinter import ttk
import threading
from ui.panels.terminal import TerminalPanel
from ui.panels.file_browser import FileBrowserPanel
from ui.panels.system_monitor import SystemMonitorPanel
from ui.panels.code_editor import CodeEditorPanel
from ui.panels.visualizer import VisualizerPanel
from config import COLORS, FONTS, UI

class MainWindow:
    """Main application window"""
    
    def __init__(self, root):
        self.root = root
        self.root.configure(bg=COLORS["bg_darker"])
        
        # Configure style
        self.setup_style()
        
        # Create main container
        self.setup_ui()
        
        # Start animations
        self.animate()
    
    def setup_style(self):
        """Setup ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure background
        style.configure('Dark.TFrame', background=COLORS["bg_dark"])
        style.configure('Darker.TFrame', background=COLORS["bg_darker"])
    
    def setup_ui(self):
        """Setup main UI layout"""
        # Main container with grid background
        main_container = tk.Frame(self.root, bg=COLORS["bg_darker"])
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Header with scanlines effect
        header = self.create_header(main_container)
        header.pack(fill=tk.X, padx=10, pady=10)
        
        # Main content area (3 columns)
        content = tk.Frame(main_container, bg=COLORS["bg_darker"])
        content.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(1, weight=1)
        content.grid_columnconfigure(2, weight=1)
        
        # Left panel - File Browser
        left_frame = tk.Frame(content, bg=COLORS["bg_darker"])
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5)
        self.file_browser = FileBrowserPanel(left_frame)
        
        # Center panel - Terminal
        center_frame = tk.Frame(content, bg=COLORS["bg_darker"])
        center_frame.grid(row=0, column=1, sticky="nsew", padx=5)
        self.terminal = TerminalPanel(center_frame)
        
        # Right panel - System Monitor & Visualizer
        right_frame = tk.Frame(content, bg=COLORS["bg_darker"])
        right_frame.grid(row=0, column=2, sticky="nsew", padx=5)
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        
        # System Monitor (top-right)
        monitor_frame = tk.Frame(right_frame, bg=COLORS["bg_darker"])
        monitor_frame.grid(row=0, column=0, sticky="nsew", pady=5)
        self.system_monitor = SystemMonitorPanel(monitor_frame)
        
        # Visualizer (bottom-right)
        viz_frame = tk.Frame(right_frame, bg=COLORS["bg_darker"])
        viz_frame.grid(row=1, column=0, sticky="nsew", pady=5)
        self.visualizer = VisualizerPanel(viz_frame)
        
        # Code Editor (bottom, full width)
        footer = tk.Frame(main_container, bg=COLORS["bg_darker"])
        footer.pack(fill=tk.BOTH, expand=False, padx=10, pady=5)
        self.code_editor = CodeEditorPanel(footer)
    
    def create_header(self, parent):
        """Create header with title and info"""
        header = tk.Frame(parent, bg=COLORS["bg_dark"], height=60)
        header.pack_propagate(False)
        
        # Add border effect
        border = tk.Frame(header, bg=COLORS["accent_green"], height=2)
        border.pack(fill=tk.X, side=tk.TOP)
        
        # Title
        title = tk.Label(
            header,
            text="[ eDEX-UI ] -- SYSTEM INTERFACE v2.0",
            bg=COLORS["bg_dark"],
            fg=COLORS["accent_green"],
            font=FONTS["mono_title"]
        )
        title.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Status info
        status = tk.Label(
            header,
            text="[●] ONLINE | STATUS: ACTIVE",
            bg=COLORS["bg_dark"],
            fg=COLORS["accent_cyan"],
            font=FONTS["mono_normal"]
        )
        status.pack(side=tk.RIGHT, padx=20, pady=10)
        
        return header
    
    def animate(self):
        """Main animation loop"""
        # Update all panels
        self.terminal.update_animation()
        self.system_monitor.update_animation()
        self.visualizer.update_animation()
        
        # Schedule next frame
        self.root.after(50, self.animate)
