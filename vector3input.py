import tkinter as tk
from theme import Theme
from tooltip import CreateTooltip
from vector3 import Vector3

class CreateVector3Input(object):
    """Creates labels and entries for defining a 3-dimensional vector"""

    def __init__(self, root, theme, label_text, vertical_offset = 0, tooltip_text = "", default_entry = Vector3(0, 0, 0)):
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
        self.header_x = 20
        self.header_y = vertical_offset
        self.header_height = 20
        label.place(x = self.header_x, y = self.header_y, height = self.header_height)
        self.header = label

        if (tooltip_text != ""):
            tooltip = CreateTooltip(label, tooltip_text)

        # Create axes
        self.label_x, self.label_x_x, self.label_x_y, self.label_x_height, self.entry_x, self.entry_x_x, self.entry_x_y, self.entry_x_height = self.create_axis(0, "X:")
        self.label_y, self.label_y_x, self.label_y_y, self.label_y_height, self.entry_y, self.entry_y_x, self.entry_y_y, self.entry_y_height = self.create_axis(1, "Y:")
        self.label_z, self.label_z_x, self.label_z_y, self.label_z_height, self.entry_z, self.entry_z_x, self.entry_z_y, self.entry_z_height = self.create_axis(2, "Z:")

    def create_axis(self, column_index, label_text):
        column_index += 1
        axis_label = tk.Label(self.root, text = label_text, foreground = self.theme.foreground, background = self.theme.background, font = self.theme.font)
        axis_label_x = 80 + 100 * column_index
        axis_label_y = self.vertical_offset
        axis_label_height = 24
        axis_label.place(x = axis_label_x, y = axis_label_y, height = axis_label_height, width = 40)
        axis_entry = tk.Entry(self.root, background = self.theme.background, foreground = self.theme.foreground, font = self.theme.font, insertbackground = self.theme.foreground)
        axis_entry.insert(2, self.default_entry.v[column_index - 1])
        axis_entry_x = 115 + 100 * column_index
        axis_entry_y = self.vertical_offset
        axis_entry_height = 24
        axis_entry.place(x = axis_entry_x, y = axis_entry_y, height = axis_entry_height, width = 60)
        return axis_label, axis_label_x, axis_label_y, axis_label_height, axis_entry, axis_entry_x, axis_entry_y, axis_entry_height
    
    def show(self):
        self.header.place(x = self.header_x, y = self.header_y, height = self.header_height)
        self.label_x.place(x = self.label_x_x, y = self.label_x_y, height = self.label_x_height)
        self.label_y.place(x = self.label_y_x, y = self.label_y_y, height = self.label_y_height)
        self.label_z.place(x = self.label_z_x, y = self.label_z_y, height = self.label_z_height)
        self.entry_x.place(x = self.entry_x_x, y = self.entry_x_y, height = self.entry_x_height)
        self.entry_y.place(x = self.entry_y_x, y = self.entry_y_y, height = self.entry_y_height)
        self.entry_z.place(x = self.entry_z_x, y = self.entry_z_y, height = self.entry_z_height)

    def hide(self):
        self.header.place(x = 0, y = 0, height = 0)
        self.label_x.place(x = 0, y = 0, height = 0)
        self.label_y.place(x = 0, y = 0, height = 0)
        self.label_z.place(x = 0, y = 0, height = 0)
        self.entry_x.place(x = 0, y = 0, height = 0)
        self.entry_y.place(x = 0, y = 0, height = 0)
        self.entry_z.place(x = 0, y = 0, height = 0)
    