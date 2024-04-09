import numpy as np
import vector

class Camera:
    def __init__(self, dim, pos, lookat, up, foc):
        self.dim = dim # vecteur dimension (largeur, hauteur)
        self.pos = pos # vecteur position

        self.lookat = lookat # vecteur de direction
        self.up = up # vecteur d'orientation

        self.foc = foc # distance focale

    def ray(self, x, y):
        # Calcul du point P0, le point dans le coin sur le plan de projection
        P0 = [self.pos[0] - (self.dim[0] - 1) / 2,
              self.pos[1] + (self.dim[1] - 1) / 2,
              0]

        # Calcul du point P1(x, y, 0)
        P1 = [P0[0] + x, P0[1] - y, P0[2]]

        # Calcul du point focal
        F = [self.pos[0], self.pos[1], self.pos[2] + self.foc]

        # Calcul du vecteur directeur du rayon de vue passant par P0
        V = vecteur.Vector(F, P1).normalize()

        return V

if __name__ == "__main__":
    x, y = 5, 0

    dim = [11, 11]
    pos = [0, 0, 0]
    lookat = [0, 0, 0]
    up = [0, 0, 0]
    foc = (5)

    camera = Camera(dim, pos, lookat, up, foc)

    print(camera.ray(x, y))
