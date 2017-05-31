"""
Taille : grand, moyen, petit
Intelligence : faible, moyen, fort
Couleur : blanc, noir, jaune
Force : 1, 2, 3
Agilité : 1, 2, 3
se reproduire
attaquer
mourrir
se déplacer
"""
from random import randint, choice
from copy import deepcopy
from statistics import mean
from time import time
from idugh import aleatoire


def pause(temps):
    debut = time()
    while time() - debut < temps:
        pass


def give_name():
    rep = ''
    nbr = randint(4, 8)
    consonnes = "zrtypqsdfghjklmwxcvbn"
    voyelles = "aeyuio"
    # noinspection PyShadowingNames
    for i in range(nbr):
        rep += choice(consonnes) if i % 2 == 0 else choice(voyelles)
    return rep.title()


class Espece:

    tailles_possibles = [1, 2, 3]
    intelligences_possibles = [1, 2, 3]
    agilites_possibles = [1, 2, 3]
    fecondites_possibles = [1, 2, 3]

    def __init__(self, nom):
        self.nom = nom
        self.tailles = (choice(Espece.tailles_possibles), choice(Espece.tailles_possibles))
        self.intelligences = (choice(Espece.intelligences_possibles), choice(Espece.intelligences_possibles))
        self.agilites = (choice(Espece.agilites_possibles), choice(Espece.agilites_possibles))
        self.fecondite = (choice(Espece.fecondites_possibles), choice(Espece.fecondites_possibles))

    def create(self):
        """
        :return: Une instance d'individue de l'espece self
        """
        taille = self.tailles[0 if randint(0, 4) <= 3 else 1]
        intelligence = self.intelligences[0 if randint(0, 4) <= 3 else 1]
        agilite = self.agilites[0 if randint(0, 4) <= 3 else 1]
        fecondite = self.fecondite[0 if randint(0, 4) <= 3 else 1]
        return Individu(self, taille, intelligence, agilite, fecondite)


class Individu:

    def __init__(self, espece, taille, intelligence, agilite, fecondite):
        # self.nom = str([choice(list("azertyuiopqsdfghjklmwxcvbn")) for i in range(randint(5, 8))]).title()
        self.nom = give_name()
        self.espece = espece
        self.population = None
        self.taille = taille
        self.intelligence = intelligence
        self.agilite = agilite
        self.fecondite = fecondite

    def __add__(self, other):
        """
        :param other: Un Individu
        :return: Un individu héritant des gênes de ses parents ou None
        """
        espece = self.espece if randint(0, 1) == 0 else other.espece
        taille = self.taille if randint(0, 1) == 0 else other.taille
        intelligence = self.intelligence if randint(0, 1) == 0 else other.intelligence
        agilite = self.agilite if randint(0, 1) == 0 else other.agilite
        fecondite = self.fecondite if randint(0, 1) == 0 else other.fecondite
        if self.fecondite + other.fecondite > 2:
            return Individu(espece, taille, intelligence, agilite, fecondite)
        else:
            return None

    def attaquer(self, other):
        s = (self.taille + self.agilite + self.intelligence)
        o = (other.taille + other.agilite + other.intelligence)
        if s > o:
            other.mourrir()
        elif o > s:
            self.mourrir()

    def __str__(self):
        rep = ''
        for attribut, valeur in self.__dict__.items():
            attr = f"{attribut}".ljust(15, ' ')
            if attribut == "espece":
                val = f"{valeur.nom}".ljust(15, ' ')
            elif attribut != "population":
                val = f"{valeur}".ljust(15, ' ')
            if attribut != "population":
                rep += f"{attr}\t:\t{val}\n"
        return rep + '\n'

    def mourrir(self):
        if self.population is not None:
            self.population.remove(self)
        del self


class Population(list):

    def reproduire(self):
        rep = deepcopy(self)
        for n in rep:
            bebe = n + choice(self)
            if bebe is not None:
                self.append(bebe)

    def attaquer(self, ennemis):
        for n in range(min((len(self), len(ennemis)))):
            choice(self).attaquer(choice(ennemis))

    def append(self, obj: Individu):
        super().append(obj)
        obj.population = self

    def auto_peupler(self, espece, nbr):
        # noinspection PyShadowingNames
        for i in range(nbr):
            self.append(espece.create())

    def bilan(self):
        indivs = [i.nom for i in self]
        nbr = len(indivs)
        taille = mean([i.taille for i in self])
        agilite = mean([i.agilite for i in self])
        intelligence = mean([i.intelligence for i in self])
        fecondite = mean([i.fecondite for i in self])
        liste_spc = []
        for e in self:
            if e.espece not in liste_spc:
                liste_spc.append(e.espece)
        rep = ''
        for e in liste_spc:
            rep += f"{e.nom.title()} : {len([i for i in self if i.espece == e])}\n"
        return f"{indivs}\nNombre total : {nbr}\n{rep}Taille : {taille}\nIntelligence : {intelligence}\n" \
               f"Agilité : {agilite}\nFécondité : {fecondite}"

    def __str__(self):
        self.bilan()
        rep = self.bilan() + '\n\n'
        for indiv in self:
            rep += indiv.__str__()
        return rep


def tester():
    homme = Espece("homme")
    elfe = Espece("elfe")
    h = Population()
    e = Population()
    print("populations créées")
    for i in range(10):
        h.append(homme.create())
        e.append(elfe.create())
    print("populations peuplées")
    h.reproduire()
    e.reproduire()

    h.attaquer(e)

    print(len(h))
    print(len(e))

    pause(1)


def observer():
    espece_humaine = Espece("Hommes")
    population = Population()
    population.auto_peupler(espece_humaine, 4)
    print(population)
    pause(10)
    population.reproduire()
    print(population)
    espece_elfe = Espece("Elfes")
    pop_elfes = Population()
    pop_elfes.auto_peupler(espece_elfe, 4)
    print(pop_elfes)
    pause(10)
    pop_elfes.reproduire()
    print(pop_elfes)
    pause(10)


if __name__ == '__main__':
    # tester()
    observer()
