def afficher(a, b, c):
    print(a, b, c)


def bidule(*g):
    print(g)


lf = lambda fert: "fert * 5 {0}".format(fert * 5)


if __name__ == '__main__':
    d = ("e", "r", "t")
    afficher(*d)
    bidule(1, 'm', True, 1.3)
    print(lf(7))
