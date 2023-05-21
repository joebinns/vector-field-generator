import abc
from vector3 import Vector3

class SDF:
    def sample(self, x, y):
        pass

class Circle(SDF):
    def __init__(self, radius):
        self.radius = radius

    def sample(self, point):
        return point.length() - self.radius

class Box(SDF):
    def __init__(self, extents):
        self.extents = extents

    def sample(self, point):
        q = point.absolute() - self.extents
        return (q.max(0)).length() + min(max(q.x, max(q.y, q.z)), 0)

class Torus(SDF):
    def __init__(self, greater_radius, lesser_radius):
        self.greater_radius = greater_radius
        self.lesser_radius = lesser_radius

    def sample(self, point):
        q = Vector3(Vector3(point.x, 0, point.z).length() - self.greater_radius, point.y, 0)
        return q.length() - self.lesser_radius
