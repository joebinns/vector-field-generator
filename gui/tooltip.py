# Based on a function from Jan Kaluza and Taizyd Korambayil's Easy Vector Fields: https://github.com/LuggLD/EasyVectorFields

import tkinter as tk
from theme import Theme

class CreateTooltip(object):
   """Create a tooltip widget"""

   def __init__(self, widget, text = 'Widget Info', theme = Theme()):
      self.widget = widget
      self.text = text
      self.theme = theme
      self.widget.bind("<Enter>", self.open)
      self.widget.bind("<Leave>", self.close)

   def open(self, event = None):
      x = y = 0
      x, y, cx, cy = self.widget.bbox("insert")
      x += self.widget.winfo_rootx() + 25
      y += self.widget.winfo_rooty() + 20

      # Creates a toplevel window
      self.tw = tk.Toplevel(self.widget)

      # Leaves only the label and removes the app window
      self.tw.wm_overrideredirect(True)
      self.tw.wm_geometry("+%d+%d" % (x, y))
      label = tk.Label(self.tw, text = self.text, justify = 'left', foreground = self.theme.foreground,
         background = self.theme.background, relief = 'solid', borderwidth = 1,
         font = self.theme.font)
      label.pack(ipadx = 1)

   def close(self, event = None):
      if self.tw:
         self.tw.destroy()
