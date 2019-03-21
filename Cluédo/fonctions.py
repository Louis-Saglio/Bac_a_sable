from copy import copy
from random import shuffle
from decorateurs import monsieur, chronometre


def intermingle(liste):
    rep = copy(liste)
    shuffle(rep)
    return rep


def in_matrice(matrice, item):
    return len([True for liste in matrice if item in liste]) > 0


@chronometre
def tests():
    @monsieur
    def test_intermingle(nbr_test):
        for i in intermingle([8, 9, 6, 3]):
            assert i in [8, 9, 6, 3]

    @monsieur
    def test_in_matrice(nbr_test):
        assert in_matrice([["e"]], "e") is True

    test_intermingle(10)
    test_in_matrice(10)


if __name__ == "__main__":
    tests()
