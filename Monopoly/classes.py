from random import randint


class Terrain:
    def __init__(self, nom, prix, couleur):
        self.nom = nom
        self.prix = prix
        self.couleur = couleur
        self.proprietaire = None

    def __str__(self):
        return '\n'.join(['\t'.join([str(val) for val in [clef.ljust(max([len(key) for key in self.__dict__])), valeur]]) for clef, valeur in self.__dict__.items()])


class Joueur:

    PLATEAU = []

    def __init__(self, nom, capital=100):
        self.nom = nom
        self.capital = capital
        self.position = 0

    def __str__(self):
        return '\n'.join(['\t'.join([str(val) for val in [clef.ljust(max([len(key) for key in self.__dict__])), valeur]]) for clef, valeur in self.__dict__.items()]) + '\n'

    def acheter(self, terrain: Terrain):
        self.capital -= terrain.prix["achat"]
        terrain.proprietaire = self.nom

    def avancer(self):
        self.position = (self.position + randint(1, 6) + randint(1, 6)) % len(Joueur.PLATEAU)


if __name__ == '__main__':
    a = Terrain("paix", {"achat": 40}, "bleu")
    j = Joueur("moi", 100)
    j.acheter(a)
    assert a.proprietaire == "moi"
