from random import choice, shuffle


def find_joueur(tours, nbr_joueurs):
    return tours % nbr_joueurs


def is_in_list_2d(liste2d, item):
    for liste in liste2d:
        if item in liste:
            return True
    return False


class Joueur:
    liste_des_joueurs = []
    liste_des_cartes = {
        "suspects": ["rose", "moutarde", "pervanche", "leblanc", "olive", "violet"],
        "pieces": [
            "salon",
            "salle-à-manger",
            "bibliothèque",
            "véranda",
            "cuisine",
            "hall",
            "petit-salon",
            "studio",
            "bureau",
        ],
        "armes": ["poignard", "revolver", "matraque", "clef", "chandelier", "corde"],
    }

    @classmethod
    def init(cls):
        for joueur in Joueur.liste_des_joueurs:
            joueur.cartes_possedees_par.append([])

    def __init__(self, nom):
        Joueur.init()
        assert nom in Joueur.liste_des_cartes["suspects"]
        assert nom not in [j_nom.nom for j_nom in Joueur.liste_des_joueurs]
        self.nom = nom
        self.numero = len(Joueur.liste_des_joueurs)
        Joueur.liste_des_joueurs.append(self)
        self.cartes_possedees_par = [[] for i in range(len(Joueur.liste_des_joueurs))]

    def choisir(self, quoi):
        while 1:
            a = choice(Joueur.liste_des_cartes[quoi + "s"])
            if not is_in_list_2d(self.cartes_possedees_par, a):
                return a

    def accuser(self):
        accusation = {
            "accusateur": self.nom,
            "piece": self.choisir("piece"),
            "arme": self.choisir("arme"),
            "suspect": self.choisir("suspect"),
        }
        reponse = None

    def repondre(self, accusation):
        try:
            return choice(
                [
                    accusation[key]
                    for key in accusation
                    if key != "accusateur" and not is_in_list_2d(self.cartes_possedees_par, accusation[key])
                ]
            )
        except ValueError:
            return None


class ListeDeJoueur(list):
    def find_joueur(self, nom):
        for joueur in self:
            if nom == joueur.nom:
                return joueur


if __name__ == "__main__":
    Joueur.liste_des_cartes["pieces"].append("salon")
    Joueur.liste_des_cartes["pieces"].append("cuisine")
    Joueur.liste_des_cartes["pieces"].append("hall")
    a, b, c = Joueur("rose"), Joueur("moutarde"), Joueur("olive")
    a.cartes_possedees_par[1].append("salon")
    d = Joueur("violet")
    print(a.choisir("piece"))
