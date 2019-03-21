from random import randint
from secrets import randbelow
from time import time


def rand(chars: str):
    chars = chars.replace(".", "0")
    rep = 0
    for l in chars:
        rep += int(l)
    return rep


def pause(tmp):
    debut = time()

    while time() - debut < tmp:
        pass


def choose1():
    return randint(1, 3)


def choose2():
    return randint(1, 3)


def run():

    nbr_tours = 10000

    vct1 = 0
    vct2 = 0

    points1 = 0
    points2 = 0

    for i in range(nbr_tours):

        if i % 100 == 0:
            pause(0.01)

        while True:

            play1 = choose1()
            play2 = choose2()

            if abs(play1 - play2) == 1:
                # print("1 de dif")
                if play1 > play2:
                    # print("p1 gagne 2 points")
                    points1 += 2
                else:
                    # print("p2 gagne 2 points")
                    points2 += 2

            elif play1 - play2 != 0:
                # print("plus de 1 de dif")
                if play1 < play2:
                    # print("p1 gagne 1 points")
                    points1 += 1
                else:
                    # print("p2 gagne 1 points")
                    points2 += 1

            if play1 == play2:
                # print("égalité")
                pass

            # print(f"Joueur 1 -> Joué : {play1}, Points : {points1}")
            # print(f"Joueur 2 -> Joué : {play2}, Points : {points2}\n")

            if points1 > 4 or points2 > 4:
                if points1 > points2:
                    gagnant = 1
                    vct1 += 1
                else:
                    vct2 += 1
                    gagnant = 2
                # print(f"Le joueur {gagnant} a gagné.\nJoueur 1 :\t{points1}\nJoueur 2 :\t{points2}")
                break

    # if abs(vct1 - vct2) > 200:
    #     run()
    #     return

    print(f"Joueur 1 :\t {vct1} victoire soit\t{(100 * vct1) / nbr_tours}%")
    print(f"Joueur 2 :\t {vct2} victoire soit\t{(100 * vct2) / nbr_tours}%")


run()
