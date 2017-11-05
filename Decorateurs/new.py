from main import premier as sdf
from time import time


def chronometre(func):
    def decorated(*param):
        debut = time()
        res = func(*param)
        print("Temps d'execution de la fonction", str(func).split()[1], ":", round(time() - debut, 3), "secondes")
        return res
    return decorated


@chronometre
def premier(vmax):
    return sdf(vmax)

print(premier(9875))
