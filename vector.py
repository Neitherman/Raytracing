import numpy as np

class Vector:
    #Initialisation par Points
    def __init__(self, Og, Ex):
        self.Vec = [Ex[0] - Og[0], Ex[1] - Og[1], Ex[2] - Og[2]]


    #Initialisation par Vecteur
    @classmethod
    def VecCp(cls, other):
        return cls([0,0,0], other)

    #Addition
    def __add__(self, other):
        return self.VecCp([self.Vec[0] + other.Vec[0],
                        self.Vec[1] + other.Vec[1],
                        self.Vec[2] + other.Vec[2]])

    #Soustraction
    def __sub__(self, other):
        return self.VecCp([self.Vec[0] - other.Vec[0],
                        self.Vec[1] - other.Vec[1],
                        self.Vec[2] - other.Vec[2]])

    #Multiplication par scalaire
    def __mul__(self, other):
        return self.VecCp([self.Vec[0] * other,
                        self.Vec[1] * other,
                        self.Vec[2] * other])

    #Overload des brackets
    def __getitem__(self, key):
        return self.Vec[key]

    #Produit Scalaire
    def dot_product(self, other):
        return np.dot(self.Vec, other.Vec)

    #Produit Vectoriel
    def cross_product(self, other):
        return self.VecCp(np.cross(self.Vec, other.Vec))


    #Norme Euclidienne
    def norm(self):
        return np.sqrt(pow(self.Vec[0], 2)+pow(self.Vec[1], 2)+pow(self.Vec[2], 2))

    #Normalisation
    def normalize(self):
        return [self.Vec[0] / self.norm(),self.Vec[1] / self.norm(),self.Vec[2] / self.norm()]


    def __repr__(self):
        return "Vec:(" + str(self.Vec) + ")"

    def __str__(self):
        return "Vec:(" + str(self.Vec) + ")"


if __name__ == "__main__":
    Vx = Vector([5,2,3], [6,4,6])
    Vy = Vector([5,2,3], [9,7,9]) # 4, 5, 6
    Vz = Vx + Vy
    #print(Vz)
    print(Vy.normalize())
