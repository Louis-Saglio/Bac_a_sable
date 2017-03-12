from math import trunc

from Risk.methode1.battle_simulator import combattre


def batailler_jusque_attak_gagne(nbr_deff, commencer_avec=2):
    nbr_attak = commencer_avec
    gagnant = "deff"
    while gagnant == "deff":
        data = combattre(nbr_attak, nbr_deff)
        gagnant = data["gagnant"]
        if gagnant == "deff":
            nbr_attak += 1
    return nbr_attak


def determiner_nbr_attak_gagne_vs_nbr_deff(nbr_deff, commencer_avec=1, precision=1000):
    moyenne_nbr_attack = 0
    for i in range(precision):
        nbr_attak = batailler_jusque_attak_gagne(nbr_deff, commencer_avec=commencer_avec)
        moyenne_nbr_attack += nbr_attak
    return trunc(moyenne_nbr_attack / precision) + 1


def determiner_si_bonne_precision(nbr_deff, precision):
    echantillon = []
    for i in range(100):
        echantillon.append(determiner_nbr_attak_gagne_vs_nbr_deff(nbr_deff, precision))
    if round(sum(echantillon) / 100) == echantillon[0]:
        return True
    else:
        return False


def tout_tester():
    nbr_attak = 2
    for nbr_def in range(1, 100):
        nbr_attak = determiner_nbr_attak_gagne_vs_nbr_deff(nbr_def, commencer_avec=nbr_attak-1)
        print(nbr_attak, "attaquants gagnent vs", nbr_def, "deffenseurs")


if __name__ == "__main__":
    # print(determiner_si_bonne_precision(3, 1000))
    tout_tester()
