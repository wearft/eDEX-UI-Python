"""
Code editor panel for eDEX-UI
"""

import tkinter as tk
from tkinter import scrolledtext
from config import COLORS, FONTS
from ui.widgets.bordered_frame import BorderedFrame

class CodeEditorPanel:
    """Code editor panel with syntax highlighting"""
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        
        # Create main frame with border
        self.frame = BorderedFrame(
            parent,
            title="[ CODE EDITOR ]",
            bg=COLORS["bg_dark"],
            border_color=COLORS["accent_purple"],
            height=150
        )
        self.frame.pack(fill=tk.BOTH, expand=False, pady=5)
        self.frame.pack_propagate(False)
        
        # Create text editor
        self.text = scrolledtext.ScrolledText(
            self.frame.content,
            bg=COLORS["bg_darker"],
            fg=COLORS["accent_green"],
            font=FONTS["mono_normal"],
            insertbackground=COLORS["accent_cyan"],
            relief=tk.FLAT,
            highlightthickness=0,
            height=10
        )
        self.text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configure tags
        self.text.tag_config("keyword", foreground=COLORS["accent_purple"])
        self.text.tag_config("string", foreground=COLORS["accent_green"])
        self.text.tag_config("comment", foreground=COLORS["text_muted"])
        self.text.tag_config("function", foreground=COLORS["accent_cyan"])
        self.text.tag_config("number", foreground=COLORS["accent_orange"])
        
        # Sample code
        sample_code = """def hack_network():
    # Initialize connection
    target = "192.168.1.100"
    port = 8080
    payload = "XOR_CIPHER_256"
    return execute_exploit(target, port, payload)
"""
        self.text.insert("1.0", sample_code)
        self.text.bind("<KeyRelease>", self._on_text_change)
    
    def _on_text_change(self, event=None):
        """Handle text changes with syntax highlighting"""
        # Simple syntax highlighting (can be enhanced)
        pass
