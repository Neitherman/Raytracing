from object import *
from vector import *

class Plane(Object):
    def __init__(self, pos, color, d, s, p, shadow=False, normal):
        super(Object, self).__init__(pos, color, d, s, p, shadow=False)
        self.normal = normal


    def intersect(self, P, V):

        ray_vec = V.normalize()

        t = -(self.normal[0] * P[0] + self.normal[0] * P[0] + self.normal[0] * P[0])/()

        RP = Vector(P, P + V * t)

        print("virtual method not implemented yet")

    def normal(self):
        print("virtual method not implemented yet")
