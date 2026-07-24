"""
File browser panel for eDEX-UI
"""

import tkinter as tk
from tkinter import ttk
import os
from config import COLORS, FONTS
from ui.widgets.bordered_frame import BorderedFrame

class FileBrowserPanel:
    """File browser panel"""
    
    def __init__(self, parent):
        self.parent = parent
        self.current_path = os.path.expanduser("~")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        
        # Create main frame with border
        self.frame = BorderedFrame(
            parent,
            title="[ FILE SYSTEM ]",
            bg=COLORS["bg_dark"],
            border_color=COLORS["accent_cyan"]
        )
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview for file browser
        self.tree = ttk.Treeview(
            self.frame.content,
            height=20,
            show='tree headings'
        )
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configure treeview colors
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Treeview",
            background=COLORS["bg_darker"],
            foreground=COLORS["accent_cyan"],
            fieldbackground=COLORS["bg_darker"],
            font=FONTS["mono_small"]
        )
        style.map('Treeview', background=[('selected', COLORS["accent_purple"])])
        
        # Populate initial directory
        self._populate_directory(self.current_path)
        self.tree.bind("<<TreeviewOpen>>", self._on_item_open)
    
    def _populate_directory(self, path):
        """Populate tree with directory contents"""
        try:
            items = os.listdir(path)
            items.sort()
            
            # Clear tree
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Add parent directory
            if path != os.path.abspath(os.sep):
                self.tree.insert("", 0, text="[ .. ]", open=False)
            
            # Add directories first
            for item in items:
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path) and not item.startswith('.'):
                    self.tree.insert("", "end", text=f"[ {item} ]", open=False)
            
            # Add files
            for item in items:
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path) and not item.startswith('.'):
                    self.tree.insert("", "end", text=f"< {item} >", open=False)
        
        except PermissionError:
            pass
    
    def _on_item_open(self, event):
        """Handle item open event"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            text = self.tree.item(item)['text']
            
            # Navigate
            if text.startswith("[ "):
                if text == "[ .. ]":
                    self.current_path = os.path.dirname(self.current_path)
                else:
                    folder_name = text.strip("[ ]")
                    self.current_path = os.path.join(self.current_path, folder_name)
                
                self._populate_directory(self.current_path)
