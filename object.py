class Object:
    def __init__(self, pos, color, d, s, p, shadow=False):
        self.pos = pos # vecteur position
        self.color = color # objet couleur

        self.p = r # facteur de reflexion (reflets)
        self.d = d # facteur de reflexion diffus
        self.s = s # facteur de reflexion speculaire

        self.shadow = shadow # booleen pour l'ombre

    def intersect(self, A, D):
        print("virtual method not implemented yet")

    def normal(self):
        print("virtual method not implemented yet")
