"""
System monitor panel for eDEX-UI
"""

import tkinter as tk
from tkinter import Canvas
import random
import time
from config import COLORS, FONTS
from ui.widgets.bordered_frame import BorderedFrame

class SystemMonitorPanel:
    """System monitoring panel with animations"""
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        
        # Create main frame with border
        self.frame = BorderedFrame(
            parent,
            title="[ SYSTEM MONITOR ]",
            bg=COLORS["bg_dark"],
            border_color=COLORS["accent_orange"]
        )
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas for graphs
        self.canvas = Canvas(
            self.frame.content,
            bg=COLORS["bg_darker"],
            fg=COLORS["accent_orange"],
            highlightthickness=0,
            relief=tk.FLAT,
            width=300,
            height=150
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Monitor data
        self.cpu_history = [random.randint(20, 60) for _ in range(50)]
        self.memory_history = [random.randint(30, 70) for _ in range(50)]
        self.network_history = [random.randint(10, 40) for _ in range(50)]
        
        self.animation_frame = 0
    
    def update_animation(self):
        """Update system monitor animation"""
        self.animation_frame += 1
        
        # Update data
        self.cpu_history.append(random.randint(20, 80))
        self.memory_history.append(random.randint(30, 75))
        self.network_history.append(random.randint(10, 60))
        
        # Keep only last 50 values
        self.cpu_history = self.cpu_history[-50:]
        self.memory_history = self.memory_history[-50:]
        self.network_history = self.network_history[-50:]
        
        # Draw graphs
        self._draw_graphs()
    
    def _draw_graphs(self):
        """Draw system monitor graphs"""
        self.canvas.delete("all")
        
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        if width < 2 or height < 2:
            return
        
        # Draw grid
        for i in range(0, width, 20):
            self.canvas.create_line(i, 0, i, height, fill=COLORS["grid_line"], dash=(2, 2))
        
        for i in range(0, height, 20):
            self.canvas.create_line(0, i, width, i, fill=COLORS["grid_line"], dash=(2, 2))
        
        # Draw CPU graph
        self._draw_graph(self.cpu_history, COLORS["accent_orange"], "CPU", 0)
        
        # Draw Memory graph
        self._draw_graph(self.memory_history, COLORS["accent_cyan"], "MEM", 1)
        
        # Draw Network graph
        self._draw_graph(self.network_history, COLORS["accent_green"], "NET", 2)
    
    def _draw_graph(self, data, color, label, offset):
        """Draw a single graph line"""
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        if not data or len(data) < 2:
            return
        
        # Draw line
        x_step = width / len(data)
        points = []
        
        for i, value in enumerate(data):
            x = i * x_step
            y = height - (value / 100 * height)
            points.extend([x, y])
        
        if len(points) >= 4:
            self.canvas.create_line(*points, fill=color, width=2)
        
        # Draw label
        label_y = 20 + (offset * 15)
        self.canvas.create_text(
            10, label_y,
            text=f"[{label}] {data[-1]:.0f}%",
            fill=color,
            font=FONTS["mono_small"],
            anchor="nw"
        )
