import tkinter as tk
from tkinter import messagebox
from theme import Theme
from tooltip import CreateTooltip

class CreateFloatInput(object):
    """Creates labels and entries for defining a float"""

    def __init__(self, root, theme, label_text, vertical_offset = 0, tooltip_text = "", default_entry = 0):
        # Root
        self.root = root
        
        # Theme
        self.theme = theme

        # Vertical offset
        self.vertical_offset = vertical_offset

        # Default entry
        self.default_entry = default_entry

        # Header
        label = tk.Label(root, text = label_text, foreground = self.theme.foreground, background = self.theme.background, font = self.theme.font)
        self.label_x = 20
        self.label_y = vertical_offset
        self.label_height = 20
        label.place(x = self.label_x, y = self.label_y, height = self.label_height)
        self.label = label

        if (tooltip_text != ""):
            tooltip = CreateTooltip(label, tooltip_text)

        # Create entry
        entry = tk.Entry(self.root, background = self.theme.background, foreground = self.theme.foreground, font = self.theme.font, insertbackground = self.theme.foreground)
        entry.insert(2, self.default_entry)
        self.entry_x = 190
        self.entry_y = vertical_offset
        self.entry_height = 20
        entry.place(x = self.entry_x, y = self.entry_y, height = self.entry_height, width = 60)
        self.entry = entry

    def show(self):
        self.label.place(x = self.label_x, y = self.label_y, height = self.label_height)
        self.entry.place(x = self.entry_x, y = self.entry_y, height = self.entry_height)

    def hide(self):
        self.label.place(x = 0, y = 0, height = 0)
        self.entry.place(x = 0, y = 0, height = 0)

    def getentry(self):
        entry = None
        try:
            entry = float(self.entry.get())
        except:
            messagebox.showerror("Invalid Input", "Ensure inputs are valid")
        return entry
    