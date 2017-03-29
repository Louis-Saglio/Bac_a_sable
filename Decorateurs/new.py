from main import premier as sdf
from time import time


def chronometre(function):
    def decorated():
        debut = time()
        res = function()
        print("Temps d'execution de la fonction", str(function).split()[1], ":", round(time() - debut, 3), "secondes")
        return res
    return decorated


@chronometre
def fonction():
    print("fonction")


@chronometre
def premier():
    return sdf()

print(premier())
