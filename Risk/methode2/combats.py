def lancer_des(nbr_des):
    """
    :param nbr_des: nombre de dés à lancer.
    :type nbr_des: int [1, infinit]
    :return Une liste de taille nbr_des contenant des int compris dans [1,6]
    """
    if nbr_des < 1 or not isinstance(nbr_des, int):
        raise ValueError("Le parametre nbr_des doit être supèrieur à 0. Pas {0}".format(nbr_des))
    from random import randint
    resultats_des = [randint(1, 6) for i in range(nbr_des)]
    resultats_des.sort(reverse=True)
    return resultats_des


def determiner_nombre_des(nbr_unites, role, des_attaquant=None):
    """
    :param nbr_unites: Nombre d'unités dont on souhaite déterminer le nombre de dés à lancer
    :type nbr_unites: int si role='attaquant' [2, infinit] si role='defenseur' [1, infinit]
    :param role: role du joueur
    :type role: str 'attaquant' ou 'defenseur'
    :param des_attaquant: Des de l'attaquant
    :type des_attaquant: list
    :return: int nombre de dés à lancer
    """
    assert isinstance(nbr_unites, int)
    assert (isinstance(des_attaquant, list) and len(des_attaquant) in [1, 2, 3]) or des_attaquant is None
    if role == "attaquant":
        if nbr_unites > 3:
            nbr_des = 3
        elif nbr_unites > 1:
            nbr_des = nbr_unites - 1
        else:
            raise ValueError("L'{0} ne peut pas lancer de dé avec {1} troupes".format(role, nbr_unites))
        return nbr_des
    elif role == "defenseur":
        if nbr_unites == 1 or sum(des_attaquant[:2]) < 8:
            nbr_des = 1
        elif nbr_unites >= 2:
            nbr_des = 2
        else:
            raise ValueError("Le {0} ne peut pas lancer de dé avec {1} troupes".format(role, nbr_unites))
        return nbr_des
    else:
        raise Warning("Le role doit être attaquant ou defenseur. Pas {0}".format(role))


def comparer_des(des_attaquant, des_defenseur):
    """
    :param des_attaquant: dés de l'attaquant
    :type des_attaquant: list
    :param des_defenseur: dés du defenseur
    :type des_defenseur: list
    :return: {'nbr_morts_attaquant': int, 'nbr_morts_defenseur': int}
    """
    nbr_morts_attaquant = 0
    nbr_morts_defenseur = 0
    nbr_des_min = len(des_attaquant) if len(des_attaquant) < len(des_defenseur) else len(des_defenseur)
    for num_de in range(nbr_des_min):
        if des_attaquant[num_de] > des_defenseur[num_de]:
            nbr_morts_defenseur += 1
        else:
            nbr_morts_attaquant += 1
    return {"morts_attaquant": nbr_morts_attaquant, "morts_defenseur": nbr_morts_defenseur}


def combatre(nbr_attaquants, nbr_defenseurs):
    from time import time
    debut = time()
    stat_unites = {"attaquant": [], "defenseur": []}
    while nbr_attaquants != 1 and nbr_defenseurs != 0:
        stat_unites["attaquant"].append(nbr_attaquants)
        stat_unites["defenseur"].append(nbr_defenseurs)
        des_attaquant = lancer_des(determiner_nombre_des(nbr_attaquants, "attaquant"))
        des_defenseur = lancer_des(determiner_nombre_des(nbr_defenseurs, "defenseur", des_attaquant))
        morts = comparer_des(des_attaquant, des_defenseur)
        nbr_attaquants -= morts["morts_attaquant"]
        nbr_defenseurs -= morts["morts_defenseur"]
    if nbr_defenseurs == 0:
        gagnant = 'attaquant'
    else:
        gagnant = 'defenseur'
    stat_unites["attaquant"].append(nbr_attaquants)
    stat_unites["defenseur"].append(nbr_defenseurs)
    fin = time()
    return {"stat_unites": stat_unites, "temps_combat": fin - debut, "gagnant": gagnant}


def lancer_x_combats(nbr_combats, nbr_attaquants, nbr_defenseurs):
    """
    :return: [{'stat_unites': {'attaquant': [5, 4, 3, 2, 1, 0], 'defenseur': [6, 5, 4, 3, 2, 1]}, 'temps_combat': float}, ...]
    data[num_combat]['stat_unites']['defenseur'][étape_combat]
    data[num_combat]['gagnant']
    """
    data = []
    for i in range(nbr_combats):
        data.append(combatre(nbr_attaquants, nbr_defenseurs))
    return data


def probabilite_gagner(nbr_attaquants, nbr_defenseurs, nbr_combats=10000):
    data = lancer_x_combats(nbr_combats, nbr_attaquants, nbr_defenseurs)
    nbr_victoires_attaquant = len([combat['gagnant'] for combat in data if combat['gagnant'] == 'attaquant'])
    nbr_victoires_defenseur = len([combat['gagnant'] for combat in data if combat['gagnant'] == 'defenseur'])
    probabilite_attaquant = round((nbr_victoires_attaquant / nbr_combats) * 100, 1)
    probabilite_defenseur = round((nbr_victoires_defenseur / nbr_combats) * 100, 1)
    return {"probabilite_attaquant": probabilite_attaquant, "probabilite_defenseur": probabilite_defenseur}


def trouver_combien_gagnent_contre(nbr_defenseurs, nbr_attaquants=2, probabilite_minimale=51):
    victoire = False
    while victoire is False:
        victoire = (probabilite_gagner(nbr_attaquants, nbr_defenseurs)["probabilite_attaquant"] > probabilite_minimale)
        if victoire is False:
            nbr_attaquants += 1
    return nbr_attaquants


def main(mini=1, maxi=100, sortie='log', mode='a'):
    if sortie == 'log':
        sortie = open('log', mode)
    else:
        sortie = None
    nbr_attaquants = 2
    for nbr_defenseurs in range(mini, maxi):
        nbr_attaquants = trouver_combien_gagnent_contre(nbr_defenseurs, nbr_attaquants)
        print("{0} gagnent contre {1}".format(nbr_attaquants, nbr_defenseurs), file=sortie)


if __name__ == "__main__":
    from time import time
    debut = time()
    from random import randint
    # Test de lancer_des()
    for i in range(-5, 10):
        try:
            test = lancer_des(i)
            assert len(test) == i or i < 1
            assert len([n for n in test if n not in range(1, 7)]) == 0
            assert len([k for k in range(1, 7) if k not in [c for c in lancer_des(100)]]) == 0
        except ValueError:
            assert i < 1
    # Test de determiner_nombre_des()
    for i in range(-100, 100):
        try:
            determiner_nombre_des(i, "defenseur", des_attaquant=lancer_des(determiner_nombre_des(i, "attaquant")))
        except ValueError:
            assert i < 2
    morts = comparer_des([randint(1, 6) for i in range(3)], [randint(1, 6) for i in range(2)])
    assert morts["morts_attaquant"] + morts["morts_defenseur"] == 2
    main(1, 100, 'log')
    print("Les tests ont duré {0} secondes et se sont déroulés avec succès.".format(round(time() - debut, 3)))
