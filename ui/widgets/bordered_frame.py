"""
Bordered frame widget with title for eDEX-UI
"""

import tkinter as tk
from config import COLORS, FONTS

class BorderedFrame(tk.Frame):
    """Custom frame with border and title"""
    
    def __init__(self, parent, title="", bg=COLORS["bg_dark"], 
                 border_color=COLORS["accent_green"], height=None, **kwargs):
        super().__init__(parent, bg=bg, **kwargs)
        
        self.title = title
        self.border_color = border_color
        
        # Create header with title
        if title:
            header = tk.Frame(self, bg=border_color, height=25)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            
            title_label = tk.Label(
                header,
                text=title,
                bg=border_color,
                fg=COLORS["bg_darker"],
                font=FONTS["mono_bold"],
                padx=10
            )
            title_label.pack(side=tk.LEFT, pady=3)
        
        # Create content frame
        self.content = tk.Frame(self, bg=COLORS["bg_darker"])
        self.content.pack(fill=tk.BOTH, expand=True)
        
        # Add left border
        left_border = tk.Frame(self, bg=border_color, width=3)
        left_border.pack(side=tk.LEFT, fill=tk.Y)
        
        # Add right border
        right_border = tk.Frame(self, bg=border_color, width=3)
        right_border.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add bottom border
        bottom_border = tk.Frame(self, bg=border_color, height=2)
        bottom_border.pack(side=tk.BOTTOM, fill=tk.X)
