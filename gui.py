import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from theme import Theme
from callback import callback
from tooltip import CreateTooltip
from vector3input import CreateVector3Input
from vector3 import Vector3
from floatinput import CreateFloatInput

""" Version """
# Define version number
version = "v0.1.0"

""" Theme """
# Generate theme
theme = Theme()

""" Window """
# Create window
root = tk.Tk()
root.title("Vector Field Generator (" + version + ")")
root.configure(background = theme.background)
root.minsize(400, 500)
root.geometry("500x500+50+50")  # width x height + x + y
root.iconbitmap("./icon.ico")

""" Credits """
# Create a Label to display the credits
credits_label = tk.Label(root, text="joebinns.com", font = theme.font, foreground = theme.foreground, cursor = "hand2", background = theme.background)
credits_label.pack()
credits_label.bind("<Button-1>", lambda e:
    callback("http://joebinns.com"))

""" Row Layout """
initial_row_y = 16
row_height = 32
row_index = 0

def getrowy(index):
    return initial_row_y + index * row_height

""" Generation Mode """
# Create generation mode dropdown widget
row_index += 1
generation_mode_options = ["Signed Distance Field"]
generation_mode_label = tk.Label(root, text = "Generation Mode:", foreground = theme.foreground, background = theme.background, font = theme.font)
generation_mode_label.place(x = 20, y = getrowy(row_index), height = 24)
generation_mode_tooltip = CreateTooltip(generation_mode_label, "Choose the method used for generating vector fields.")
generation_mode_selection = ttk.Combobox(root, values = generation_mode_options, takefocus = True, state = "readonly", font = theme.font)
generation_mode_selection.set(generation_mode_options[0])
generation_mode_selection.place(x = 190, y = getrowy(row_index), height = 24, width = 285)

""" Grid Dimensions """
row_index += 1
grid_dimensions_input = CreateVector3Input(root, theme, "Grid Dimensions:", getrowy(row_index), "Use values no lower than 2. High values take longer to generate, and cost more memory.", Vector3(16, 16, 16))

""" Extents """
# Lower bound
row_index += 1
lower_extent_input = CreateVector3Input(root, theme, "Lower Grid Extent:", getrowy(row_index), "The minimum coordinate, for which the bottom left back corner of the grid will assume.", Vector3(-100., -100., -100.))

# Upper bound
row_index += 1
upper_extent_input = CreateVector3Input(root, theme, "Upper Grid Extent:", getrowy(row_index), "The maximum coordinate, for which the upper right front corner of the grid will assume.", Vector3(100., 100., 100.))

""" Signed Distance Field """
# Create signed distance field dropdown widget
row_index += 1
sdf_options = ["Circle", "Box"]
sdf_label = tk.Label(root, text = "Signed Distance Field:", foreground = theme.foreground, background = theme.background, font = theme.font)
sdf_label.place(x = 20, y = getrowy(row_index), height = 24)
sdf_tooltip = CreateTooltip(sdf_label, "Choose the signed distance field to use.")
sdf_selection = ttk.Combobox(root, values = sdf_options, takefocus = True, state = "readonly", font = theme.font)
sdf_selection.set(sdf_options[0])
sdf_selection.place(x = 190, y = getrowy(row_index), height = 24, width = 285)

# Temporary rows
row_index = row_index
row_index += 1 

# Circle
radius_input = CreateFloatInput(root, theme, "Radius:", getrowy(row_index), "", 10)

# Box
extents_input = CreateVector3Input(root, theme, "Scale:", getrowy(row_index), "", Vector3(10, 10, 10))

def hideallsdfdependentwidgets():
    # Sphere
    # Radius
    radius_input.hide()

    # Cube
    # Extents
    extents_input.hide()

def updatesdfwidgets():
    hideallsdfdependentwidgets()

    if (sdf_selection.get() == "Circle"):
        # Radius
        radius_input.show()

    elif (sdf_selection.get() == "Box"):
        # Radius
        extents_input.show()

def sdfselectionchanged(event):
    updatesdfwidgets()

updatesdfwidgets()
sdf_selection.bind('<<ComboboxSelected>>', sdfselectionchanged)

""" Save To """
def saveto():
    file_entry.delete(0, 'end')
    files = [('All Files', '*.*'),
             ('Vector Field', '*.fga'),
             ('Text Document', '*.txt')]
    save_dir = asksaveasfile(filetypes = files, defaultextension = '.fga')
    file_entry.insert(2, save_dir.name)

# Create File Dialog
row_index_end = row_index
row_index_end += 4
file_label = tk.Label(root, text = "Save To:", foreground = theme.foreground, background = theme.background, font = theme.font)
file_label.place(x = 20, y = getrowy(row_index_end), height = 24)
file_tooltip = CreateTooltip(file_label, "Path to save the generated .fga file.", theme)
file_entry = tk.Entry(root, foreground = theme.foreground, background = theme.background, font = theme.font)
file_entry.place(x = 190, y = getrowy(row_index_end), height = 24, width = 285)
file_button = tk.Button(root, text = "...", foreground = theme.foreground, background = theme.background, font = theme.font, command = saveto)
file_button.place(x = 450, y = getrowy(row_index_end), height = 24)

""" Generate """

def writefile():
    '''
    gridsize = [int(ceil(float(grids_x.get()))),int(ceil(float(grids_y.get()))),int(ceil(float(grids_z.get())))]
    generator = getGenType(GenType_dpd.get())
    minbounds = [int(MinB_x.get()),int(MinB_y.get()),int(MinB_z.get())]
    maxbounds = [int(MaxB_x.get()),int(MaxB_y.get()),int(MaxB_z.get())]
    directionbias = [float(DirB_x.get()),float(DirB_y.get()),float(DirB_z.get())]
    directionstrength = float(DirStr.get())
    scalenoiseamount = float(SclNAmt.get())
    directionnoiseamount = float(DirNAmt.get())
    mainscalefactor = float(Scl_F.get())
    filename = File_Entry.get()

    filecheck = os.path.isfile(filename)
    pathcheck = os.path.split(filename)
    pathbool = os.path.isdir(pathcheck[0])

    if(pathbool):
        core.makeVectorField(gridsize, minbounds, maxbounds, generator, filename, directionbias, directionstrength,scalenoiseamount, directionnoiseamount, mainscalefactor)
    else:
        showerror("Save Location", "Invalid save location")

    #print(gridsize)
    #print(generator)
    #print(File_Entry.get())
    #print(minbounds)
    #print(maxbounds)
    #print(directionbias)
    #print(directionstrength)
    #print(scalenoiseamount)
    #print(directionnoiseamount)
    #print(mainscalefactor)
    '''

row_index_end += 1.60
create_button = tk.Button(root, text = "Generate Vector Field", background = theme.background, foreground = theme.foreground, font = theme.font, command = writefile)
create_button.place(x = 20, y = getrowy(row_index_end), height = 24, width = 200)
create_tooltip = CreateTooltip(create_button, "Generates the file and opens for preview in a text editor.", theme)

""" Render """
root.mainloop()
