"""
Terminal-like panel for eDEX-UI
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import time
import random
from config import COLORS, FONTS
from ui.widgets.bordered_frame import BorderedFrame

class TerminalPanel:
    """Terminal panel with hacker aesthetic"""
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        
        # Create main frame with border
        self.frame = BorderedFrame(
            parent,
            title="[ TERMINAL ]",
            bg=COLORS["bg_dark"],
            border_color=COLORS["accent_green"]
        )
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Terminal text widget
        self.text = scrolledtext.ScrolledText(
            self.frame.content,
            bg=COLORS["bg_darker"],
            fg=COLORS["accent_green"],
            font=FONTS["mono_small"],
            insertbackground=COLORS["accent_cyan"],
            relief=tk.FLAT,
            highlightthickness=0,
            state=tk.DISABLED
        )
        self.text.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for different text types
        self.text.tag_config("command", foreground=COLORS["accent_green"])
        self.text.tag_config("error", foreground=COLORS["error"])
        self.text.tag_config("success", foreground=COLORS["success"])
        self.text.tag_config("info", foreground=COLORS["accent_cyan"])
        self.text.tag_config("path", foreground=COLORS["accent_purple"])
        
        # Animation state
        self.animation_frame = 0
        self.lines_queue = []
        
        # Initial messages
        self._add_initial_messages()
    
    def _add_initial_messages(self):
        """Add initial boot messages"""
        messages = [
            (">>> eDEX-UI v2.0 - System Interface", "info"),
            (">>> Initializing quantum processors...", "command"),
            (">>> Loading neural networks...", "command"),
            (">>> Authentication required", "error"),
            (">>> User: ACCESS GRANTED", "success"),
            (">>> System ready. Awaiting commands.", "info"),
            ("", "info"),
        ]
        
        for msg, tag in messages:
            self._write_line(msg, tag)
    
    def _write_line(self, text, tag="info"):
        """Write a line to terminal"""
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, text + "\n", tag)
        self.text.see(tk.END)
        self.text.config(state=tk.DISABLED)
    
    def add_command(self, command):
        """Add a command to terminal"""
        self._write_line(f"$ {command}", "command")
    
    def add_output(self, output, tag="info"):
        """Add output to terminal"""
        self._write_line(output, tag)
    
    def update_animation(self):
        """Update terminal animation"""
        self.animation_frame += 1
        
        # Randomly add system messages
        if self.animation_frame % 100 == 0:
            messages = [
                (">>> Network packet received", "info"),
                (">>> Security check passed", "success"),
                (">>> Cache updated", "command"),
                (">>> Buffer optimized", "command"),
            ]
            msg, tag = random.choice(messages)
            self._write_line(msg, tag)
            
            # Keep only last 50 lines
            lines = self.text.get("1.0", tk.END).split("\n")
            if len(lines) > 50:
                self.text.config(state=tk.NORMAL)
                self.text.delete("1.0", "51.0")
                self.text.config(state=tk.DISABLED)
