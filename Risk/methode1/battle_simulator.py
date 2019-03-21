def lancer_des(nbr_des):
    from random import randint

    a = []
    for i in range(nbr_des):
        a.append(randint(1, 6))
    a.sort()
    a.reverse()
    return a


def evaluer_pertes(des_attak, des_deff):
    # On initialise les variables à incrémenter
    nbr_morts_attak = 0
    nbr_morts_deff = 0
    # On détermine qui a le moins de des
    if len(des_attak) > len(des_deff):
        plus_petit_nbr_des = len(des_deff)
    else:
        plus_petit_nbr_des = len(des_attak)
    # On compare les des un par un
    for i in range(plus_petit_nbr_des):
        if des_attak[i] > des_deff[i]:
            nbr_morts_deff += 1
        else:
            nbr_morts_attak += 1
    return nbr_morts_attak, nbr_morts_deff


def determiner_nbr_des(nbr_unites, role, des_attak=None):
    if role == "attak":
        if nbr_unites > 3:
            return 3
        else:
            return nbr_unites - 1
    else:
        if sum(des_attak) <= 8:
            return 2
        else:
            return 1


def combattre(nbr_attak, nbr_deff):
    compt = 0
    while nbr_attak != 1 and nbr_deff != 0:
        compt += 1
        nbr_des_attak = determiner_nbr_des(nbr_attak, "attak")
        des_attak = lancer_des(nbr_des_attak)
        nbr_des_deff = determiner_nbr_des(nbr_deff, "deff", des_attak)
        des_deff = lancer_des(nbr_des_deff)
        morts = evaluer_pertes(des_attak, des_deff)
        nbr_attak -= morts[0]
        nbr_deff -= morts[1]
    if nbr_attak > nbr_deff:
        gagnant = "attack"
        perdant = "deff"
    else:
        gagnant = "deff"
        perdant = "attack"
    return {
        "nbr_tours": compt,
        "reste_attak": nbr_attak,
        "reste_deff": nbr_deff,
        "gagnant": gagnant,
        "perdant": perdant,
    }


if __name__ == "__main__":
    print(combattre(20, 15))
