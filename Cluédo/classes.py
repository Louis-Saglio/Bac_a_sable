from carte import Case
from decorateurs import monsieur
from random import choice


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


if __name__ == '__main__':
    from time import time
    debut = time()

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
        try:
            test = Carte(choice(Carte.cartes_possibles["suspect"]))
        except ValueError:
            pass

    carte(10)
    joueur(10)

    print("\nLes tests ont été passés en", round(time() - debut, 3), "secondes")
