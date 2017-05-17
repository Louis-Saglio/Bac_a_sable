from carte import Case
from decorateurs import monsieur, chronometre
from random import choice
from time import time
from fonctions import intermingle


class Carte:

    cartes_possibles = {"suspect": ["rose", "moutarde", "pervanche", "leblanc", "olive", "violet"],
                        "piece": ["salon", "salle-à-manger", "bibliothèque", "véranda", "cuisine", "hall", "petit-salon", "studio", "bureau"],
                        "arme": ["poignard", "revolver", "matraque", "clef", "chandelier", "corde"]
                        }

    def __init__(self, nom):
        self.nom = nom
        for sorte, valeurs in Carte.cartes_possibles.items():
            if nom in valeurs:
                self.type = sorte
                return
        raise ValueError

    def __str__(self):
        return "Nom \t:\t" + str(self.nom) + "\nType\t:\t" + str(self.type)


class Joueur:

    positions_initiales = dict(zip(Carte.cartes_possibles["suspect"], [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))

    def __init__(self, nom):
        assert nom in Carte.cartes_possibles["suspect"]
        self.nom = nom
        self.position = Joueur.positions_initiales[self.nom]
        # todo test.cartes_connu(es) à transformer en dictionnaire avec de joueurs comme clef
        self.cartes_connu = []

    def __str__(self):
        return '\n'.join(['\t'.join([str(val) for val in [clef.ljust(max([len(key) for key in self.__dict__])), valeur]]) for clef, valeur in self.__dict__.items()])

    def choisir(self, quoi):
        for carte in intermingle([Carte.cartes_possibles[quoi]]):
            if carte not in self.cartes_connu:
                print(Carte.cartes_possibles[quoi])
                return carte


@chronometre
def tests():

    @monsieur
    def carte(nbr_tests):
        test = Carte(choice(Carte.cartes_possibles[choice([key for key in Carte.cartes_possibles])]))
        assert test.nom in Carte.cartes_possibles[test.type]
        try:
            test = Carte("test")
        except ValueError:
            pass

    @monsieur
    def joueur(nbr_tests):
        test = Joueur("moutarde")
        assert Joueur.positions_initiales[test.nom] == test.position
        temp = choice([key for key in Carte.cartes_possibles])
        assert test.choisir(temp) in Carte.cartes_possibles[temp]
        try:
            test = Joueur(choice(Carte.cartes_possibles["suspect"]))
        except ValueError:
            pass

    carte(10)
    joueur(10)

if __name__ == '__main__':
    tests()
    a = Joueur("rose")
    print(a)
