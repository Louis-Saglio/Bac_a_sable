from classes import Terrain, Joueur

data = {
    "terrains": {
        "nom": ["paix", "pigalle", "courcelles"],
        "prix": [40, 18, 14],
        "couleur": ["bleu", "orange", "bleu clair"],
    },
    "joueurs": {"nom": ["moi", "toi"], "capital": [100, 100]},
}

# donnees = {
#     Terrain: {
#         "nom": ["paix", "pigalle", "courcelles"],
#         "prix": [40, 18, 14],
#         "couleur": ["bleu", "orange", "bleu clair"]
#     },
#     Joueur: {
#         "nom": ["moi", "toi"],
#         "capital": [100, 100]
#     }
# }
#
# rep = {}
# for classe, attributs in donnees.items():
#     nbr_objets = len(attributs[list(attributs)[0]])
#     nom_liste_objets = str(classe.__name__).lower() + 's'
#     rep[nom_liste_objets] = []
#
#
# print(rep)

terrains = []
for i in range(len(data["terrains"])):
    terrains.append(Terrain(data["terrains"]["nom"][i], data["terrains"]["prix"][i], data["terrains"]["couleur"][i]))

joueurs = []
for i in range(len(data["joueurs"])):
    # noinspection PyArgumentList
    joueurs.append(Joueur(data["joueurs"]["nom"][i], data["joueurs"]["capital"][i]))
