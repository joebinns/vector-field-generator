import numpy as np
from vector3 import Vector3
from signeddistancefunctions import Circle, Box

# TODO: Fill array by sampling a given Signed Distance Function
box = Box(Vector3(1, 1, 1))
sd = box.sample(Vector3(2, 2, 2))
print(sd)

circle = Circle(1)
sd = circle.sample(Vector3(1, 1, 0))
print(sd)


#np.empty(100, 100, 100)

# TODO: Take the gradient
#np.gradient()


