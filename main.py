#!/usr/bin/env python3
"""
eDEX-UI - Inspired by Watch Dogs 2
A futuristic hacker interface in Python
"""

import tkinter as tk
from ui.main_window import MainWindow

def main():
    """Main entry point"""
    root = tk.Tk()
    root.title("eDEX-UI - Watch Dogs 2 Style")
    root.geometry("1600x900")
    root.resizable(True, True)
    
    # Create main application
    app = MainWindow(root)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
