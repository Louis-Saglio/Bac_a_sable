from data import terrains, joueurs
from classes import Terrain, Joueur
from itertools import cycle

Joueur.PLATEAU = terrains


def compter(liste, limite=20):
    compt = 0
    rep = []
    for item in cycle(liste):
        if compt == limite:
            break
        compt += 1
        rep.append(item)
    return rep

for joueur in compter(joueurs):
    joueur.avancer()

for i in joueurs:
    print(i)
