class Color:
    def __init__(self, r, g, b):
        self.v = (r, g, b) # vecteur couleur

    def __add__(self, c):
        return (self.v[0] + c.v[0], self.v[1] + c.v[1], self.v[2] + c.v[2])

    def __mul__(self, n):
        return (self.v[0] * n, self.v[1] * n, self.v[2] * n)
