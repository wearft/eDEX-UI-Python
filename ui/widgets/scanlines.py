"""
Scanline effect for eDEX-UI
"""

import tkinter as tk
from config import COLORS

class ScanlineCanvas(tk.Canvas):
    """Canvas with scanline effect"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.scanline_image = None
        self._create_scanlines()
    
    def _create_scanlines(self):
        """Create scanline pattern"""
        width = self.winfo_width()
        height = self.winfo_height()
        
        if width < 2 or height < 2:
            return
        
        # Draw horizontal lines for scanline effect
        for y in range(0, height, 2):
            self.create_line(0, y, width, y, fill=COLORS["grid_line"], dash=(1, 1))
