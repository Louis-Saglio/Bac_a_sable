def premier(vmax):
    from math import sqrt

    # compteur = 0
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
    return premiers[2:]
