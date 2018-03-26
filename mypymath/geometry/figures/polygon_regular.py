import math

from mypymath.geometry.figures import Point, Plane
from mypymath.geometry.functions import DistanceCalculator

class PolygonRegular:
    """
    A special case of a polygon.

    """
    def __init__(self,
                 param1): # vertices
        if isinstance(param1, tuple) or isinstance(param1, list):
            if len(param1) < 3:
                print('Error in Polygon.__init__:',
                      'vertives number < 3.')
                return None
            vertices = param1
        self.__init_primitive(vertices)

    def __init_primitive(self, vertices):
        self.vertices = vertices
        x = 0
        y = 0
        z = 0
        for pt in vertices:
            x += pt.x
            y += pt.y
            z += pt.z
        self.N = len(vertices)
        self.central_angle = math.pi / self.N
        self.center = Point(x / self.N, y / self.N, z / self.N)
        dc = DistanceCalculator()
        self.edge_length = dc.distance(vertices[0], vertices[1])
        self.outer_radius = self.edge_length / 2 / math.sin(self.central_angle)
        self.inner_radius = (self.outer_radius**2 - self.edge_length**2 / 4)**0.5
        self.containing_plane = Plane(vertices[0], vertices[1], vertices[2])
