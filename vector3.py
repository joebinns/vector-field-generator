import numpy as np

class Vector3:

    def __init__(self, x, y, z):
        self.v = [x, y, z]
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return np.sqrt(np.power(self.x, 2) + np.power(self.y, 2) + np.power(self.z, 2))
    
    def absolute(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))
    
    def max(self, other):
        return Vector3(max(self.x, other), max(self.y, other), max(self.z, other))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3(x, y, z)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3(x, y, z)
    
    def __repr__(self) -> str:
        return str(self.x) + " " + str(self.y) + " " + str(self.z)
    