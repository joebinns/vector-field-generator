import tkinter as tk
from theme import Theme
from tooltip import CreateTooltip
from vector3 import Vector3

class CreateVector3Input(object):
    """Creates labels and entries for defining a 3-dimensional vector"""

    def __init__(self, root, theme, label_text, vertical_offset = 0, tooltip_text = "", default_entries = Vector3(0, 0, 0)):
        # Root
        self.root = root
        
        # Theme
        self.theme = theme

        # Vertical offset
        self.vertical_offset = vertical_offset

        # Default entires
        self.default_entries = default_entries

        # Header
        label = tk.Label(root, text = label_text, foreground = self.theme.foreground, background = self.theme.background, font = self.theme.font)
        label.place(x = 20, y = vertical_offset, height = 20)

        if (tooltip_text != ""):
            tooltip = CreateTooltip(label, tooltip_text)

        # Create axes
        self.create_axis(0, "X:")
        self.create_axis(1, "Y:")
        self.create_axis(2, "Z:")

    def create_axis(self, column_index, label_text):
        column_index += 1
        axis_label = tk.Label(self.root, text = label_text, foreground = self.theme.foreground, background = self.theme.background, font = self.theme.font)
        axis_label.place(x = 80 + 100 * column_index, y = self.vertical_offset, height = 24, width = 40)
        axis_entry = tk.Entry(self.root, background = self.theme.background, foreground = self.theme.foreground, font = self.theme.font, insertbackground = self.theme.foreground)
        axis_entry.insert(2, self.default_entries.v[column_index - 1])
        axis_entry.place(x = 115 + 100 * column_index, y = self.vertical_offset, height = 24, width = 60)
    