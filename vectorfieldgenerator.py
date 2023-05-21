import numpy as np
import os
from vector3 import Vector3
from signeddistancefunctions import Circle, Box, Torus

box = Box(Vector3(50., 50., 50.))
sd = box.sample(Vector3(2., 2., 2.))
print(sd)

circle = Circle(1.)
sd = circle.sample(Vector3(1., 1., 0.))
print(sd)

torus = Torus(25., 10.)

""" Fill array by sampling a given Signed Distance Function """

grid_dimensions = (5, 5, 5) # Note: Should be odd if it is to be centered at 0, 0, 0
lower_extent = Vector3(-100., -100., -100.)
upper_extent = Vector3(100., 100., 100.)
sdf = np.empty(grid_dimensions)

delta_extents = upper_extent - lower_extent
delta_extent = Vector3(delta_extents.x / (grid_dimensions[0] - 1), delta_extents.y / (grid_dimensions[1] - 1), delta_extents.z / (grid_dimensions[2] - 1))

print(delta_extents)
print(delta_extent)

completed = 0
total_calculations = grid_dimensions[0] * grid_dimensions[1] * grid_dimensions [2]

print(str(round(completed * 100)) + "%")
for i in range(0, grid_dimensions[0]):
    x = lower_extent.x + i * delta_extent.x
    completed += (grid_dimensions[1] * grid_dimensions[2]) / total_calculations
    print(str(round(completed * 100)) + "%")
    for j in range(grid_dimensions[1]):
        y = lower_extent.y + j * delta_extent.y
        for k in range(grid_dimensions[2]):
            z = lower_extent.z + k * delta_extent.z
            sdf[i, j, k] = box.sample(Vector3(x, y, z))

print(sdf)

sdf_gradients = np.gradient(sdf)


print(sdf_gradients)

print(np.shape(sdf))
print(np.shape(sdf_gradients))


""" Write and open file """

def writevector3(file, vector):
	file.write(str(vector.z) + ", " + str(vector.y) + ", " + str(vector.x) + ",\n")

filename = "C:/Users/joebi/Desktop/swag.fga"

file = open(filename, 'w')
file.truncate()

writevector3(file, Vector3(grid_dimensions[0], grid_dimensions[1], grid_dimensions[2]))
writevector3(file, lower_extent)
writevector3(file, upper_extent)

for i in range(0, grid_dimensions[0]):
    for j in range(grid_dimensions[1]):
        for k in range(grid_dimensions[2]):
            vector = Vector3(sdf_gradients[0][i][j][k], sdf_gradients[1][i][j][k], sdf_gradients[2][i][j][k])
            writevector3(file, vector)

os.startfile(filename)
