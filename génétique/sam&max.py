import turtle
from random import shuffle, choice, randint

from math import sqrt

population = []
a_map = []


class Point(object):
    COUNT = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return sqrt(dx ** 2 + dy ** 2)


class Individu(object):
    # le constructeur de l'objet.
    # on met le score à zéro.
    # on peut aussi lui passer la liste de points
    # pour qu'il initialise une route au hasard.
    def __init__(self, init=False, map_point=[]):
        self.score = 0
        self.route = []
        if init:
            self.set_route(map_point)

    # ici on créé une route avec un mélange des points
    # on utilise shuffle pour mélanger les points.
    # ensuite on calcul le score, c'est à dire la longueur du trajet.
    def set_route(self, map_point):
        shuffle(map_point)
        self.route = map_point
        for p in range(len(map_point) - 1):
            self.score += map_point[p].distance(map_point[p + 1])

    # ici on donne à l'objet la capacité de faire un enfant
    # ça prend comme paramètre l'objet (lui même), et un autre individu.
    # on prend la moitié du trajet de l'objet et on complète avec
    # les points de l'autre individu.
    # on retourne un enfant, qui est un individu.
    def croisement(self, other):
        child = Individu()
        # je prends la moitier de moi-même.
        wdth = len(self.route) // 2
        first_segment = self.route[: wdth // 2]
        last_segment = []
        # je complète avec l'autre
        for i in range(len(self.route)):
            if other.route[i] not in first_segment:
                last_segment.append(other.route[i])
        child.set_route(first_segment + last_segment)
        return child

    # ici on défini une fonction pour que l'objet puisse se dessiner.
    # pour cela on utilisera Turtle de python.
    def show_me(self):
        turtle.clearscreen()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.up()
        pen.setpos(self.route[0].X, self.route[0].Y)
        for point in self.route:
            pen.goto(point.X, point.Y)
            pen.down()
            pen.dot()

        pen.goto(self.route[0].X, self.route[0].Y)


# initialisation des points de la carte.
# prend en paramètre un nombre de points.
def init_map(nb):
    global a_map
    del a_map[:]
    for i in range(nb):
        p = Point(randint(1, 300), randint(1, 300))
        a_map.append(p)


# initialisation de la population.
# prend en paramètre le nombre d'individus à créer.
def init_pop(nb, map_point):
    global population
    del population[:]
    for i in range(nb):
        i = Individu(True, map_point)
        population.append(i)


# fonction qui sert à trier les individus suivant leur score.
# utile pour trouver les meilleurs.
def selection(pop):
    pop.sort(key=lambda x: x.score, reverse=True)


# dans cette fonction, on sélectionne les 15 meilleurs individus de la population
# que l'on croise avec les autres individus.
# la nouvelle population est constituée des 15 meilleurs plus les enfants.
def croisement(pop):
    new_pop = []
    best_pop = population[85:]
    for i in range(len(pop) - 15):
        new_pop.append(choice(best_pop).croisement(choice(population[20:85])))
    return new_pop + best_pop


# la fonction principal.
# on passe en paramètre le nombre de générations que l'on souhaite faire
# et le nombre de points.
# Ensuite, on itère selon un algorithme précis :
# Création d'une population initiale.
# Sélection puis croisement de la population
# à chaque génération on regarde si on a un meilleur score
# si oui, on l'affiche.
def play(nb_gene, nb_point):
    init_map(nb_point)
    init_pop(100, a_map)
    best_score = 1000000
    for i in range(nb_gene):
        global population
        population = croisement(population)
        selection(population)
        if best_score > population[99].score:
            best_score = population[99].score
            print("meilleur score : " + str(population[99].score))
            population[99].show_me()


play(400, 13)
