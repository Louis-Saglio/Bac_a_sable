def premier(vmax):
    from time import time
    from math import sqrt

    # compteur = 0
    debut = time()
    premiers = []
    est_premier = True
    for nombre in range(vmax):
        for test in range(2, nombre):
            # compteur += 1
            if nombre % test == 0:
                est_premier = False
                break
            elif test ** 2 > sqrt(nombre):
                est_premier = True
                break
            else:
                est_premier = True
        if est_premier:
            premiers.append(nombre)
    # print(compteur)
    fin = time()
    # duree = ("Durée :" + str(round(fin - debut, 3)) + "secondes")
    duree = str(fin - debut)
    return {"premiers": premiers[2:], "duree": duree}


def pourcentage_premiers(val):
    if val == 0:
        return "Infini"
    z = val
    a = premier(z)
    b = len(a)
    c = round((b / z) * 100, 10)
    return c


def temps():
    from time import time

    debut = time()
    for i in range(0, 100000, 1000):
        print(i, pourcentage_premiers(i))
    fin = time()
    print("Durée totale :", fin - debut)


def sum_str(string):
    total = int(string)
    while len(string) != 1:
        total = 0
        for i in string:
            total += int(i)
        string = str(total)
    return total


def aleatoire():
    nbr = sum_str(
        (str(pourcentage_premiers(sum([int(i) for i in list(premier(1000)["duree"].split(".")[1])]))).split("."))[1]
    )
    return nbr


# a = [aleatoire() for i in range(1000)]
# for i in a:
#     if a.count(i) > 1:
#         a.remove(i)
# for i in range(10):
#     print(i, a.count(i))
# print(len(a))

if __name__ == "__main__":
    a = premier(1000000)
    print(a["premiers"])
    print(a["duree"])
