"""
Data visualizer panel for eDEX-UI
"""

import tkinter as tk
from tkinter import Canvas
import random
import math
from config import COLORS, FONTS
from ui.widgets.bordered_frame import BorderedFrame

class VisualizerPanel:
    """Data visualization panel with animated graphs"""
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        
        # Create main frame with border
        self.frame = BorderedFrame(
            parent,
            title="[ VISUALIZER ]",
            bg=COLORS["bg_dark"],
            border_color=COLORS["accent_green"]
        )
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas for visualization
        self.canvas = Canvas(
            self.frame.content,
            bg=COLORS["bg_darker"],
            highlightthickness=0,
            relief=tk.FLAT
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Animation state
        self.animation_frame = 0
        self.nodes = self._generate_nodes(10)
    
    def _generate_nodes(self, count):
        """Generate random nodes for visualization"""
        nodes = []
        for i in range(count):
            node = {
                'x': random.random(),
                'y': random.random(),
                'vx': (random.random() - 0.5) * 0.02,
                'vy': (random.random() - 0.5) * 0.02,
                'color': random.choice([
                    COLORS["accent_green"],
                    COLORS["accent_cyan"],
                    COLORS["accent_purple"],
                    COLORS["accent_orange"]
                ])
            }
            nodes.append(node)
        return nodes
    
    def update_animation(self):
        """Update visualizer animation"""
        self.animation_frame += 1
        
        # Update node positions
        for node in self.nodes:
            node['x'] += node['vx']
            node['y'] += node['vy']
            
            # Bounce off edges
            if node['x'] < 0 or node['x'] > 1:
                node['vx'] *= -1
            if node['y'] < 0 or node['y'] > 1:
                node['vy'] *= -1
            
            # Keep in bounds
            node['x'] = max(0, min(1, node['x']))
            node['y'] = max(0, min(1, node['y']))
        
        # Draw visualization
        self._draw_visualization()
    
    def _draw_visualization(self):
        """Draw the network visualization"""
        self.canvas.delete("all")
        
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        if width < 2 or height < 2:
            return
        
        # Draw connections between nearby nodes
        for i, node1 in enumerate(self.nodes):
            x1 = node1['x'] * width
            y1 = node1['y'] * height
            
            for node2 in self.nodes[i+1:]:
                x2 = node2['x'] * width
                y2 = node2['y'] * height
                
                # Calculate distance
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                # Draw line if close enough
                if dist < 150:
                    alpha = int(255 * (1 - dist / 150))
                    self.canvas.create_line(
                        x1, y1, x2, y2,
                        fill=COLORS["grid_line"],
                        dash=(1, 1)
                    )
        
        # Draw nodes
        for node in self.nodes:
            x = node['x'] * width
            y = node['y'] * height
            size = 5
            
            self.canvas.create_oval(
                x - size, y - size,
                x + size, y + size,
                fill=node['color'],
                outline=node['color']
            )
            
            # Draw glow effect
            self.canvas.create_oval(
                x - size*2, y - size*2,
                x + size*2, y + size*2,
                outline=node['color'],
                width=1
            )
