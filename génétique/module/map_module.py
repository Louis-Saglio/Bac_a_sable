from random import randint
import turtle
from tkinter import *


# noinspection PyShadowingNames
class Case:

    def __init__(self, value, owning_map, coordinates):
        self.value = value
        self.owning_map = owning_map
        self.coordinates = coordinates
        self.border = self.get_border_type()

    def __str__(self):
        return str(self.value)

    def debug(self):
        return '\n'.join(['\t'.join([str(val) for val in [clef.ljust(max([len(key) for key in self.__dict__])), valeur]]) for clef, valeur in self.__dict__.items()])

    def get_border_type(self):
        l, h = self.coordinates
        return {
            "is_top": h == 0 or False,
            "is_left": l == 0 or False,
            "is_bottom": h == self.owning_map.height - 1 or False,
            "is_right": l == self.owning_map.width - 1 or False
        }

    def is_border_position(self):
        return len([True for value in self.border.values() if value]) != 0

    def get_distance_with(self, case):
        a, b, x, y = self.coordinates + case.coordinates
        return ((a - x) ** 2 + (b - y) ** 2) ** (1 / 2)


class Map:

    def __init__(self, width, height, filling='M', border='B'):
        self.nodes = []
        self.width = width
        self.height = height
        self.border_type = border
        self.filling_type = filling
        self.map = self.create_map()

    def __iter__(self):
        iterator = []
        for h in range(self.height):
            for l in range(self.width):
                iterator.append(self[l, h])
        return iter(iterator)

    def __getitem__(self, pos):
        l, h = pos
        return self.map[l][h]

    def __setitem__(self, key, value):
        index1, index2 = key
        self.map[index1][index2] = Case(value, self, key)

    def __str__(self):
        rep = ''
        for case in self:
            rep += str(case.value) + ' ' + ('\n' if case.border["is_right"] else '')
        return rep

    def create_map(self):
        return [[Case(self.filling_type, self, (l, h)) for h in range(self.height)] for l in range(self.width)]

    def create_border(self):
        for case in self:
            if case.is_border_position():
                self[case.coordinates] = Case(self.border_type, self, case.coordinates)

    def get_random_case(self):
        return self[randint(0, self.width-1), randint(0, self.height-1)]

    def create_random_nodes(self, nbr, node_value="N"):
        for n in range(nbr):
            self.nodes.append(Node(self.get_random_case(), node_value))


class Pawn:

    def __init__(self, owning_map, position, look):
        """
        :type owning_map Map
        :type position tuple
        :type look str
        """
        self._position = position
        self.look = look
        self.owning_map = owning_map
        self._case = self.owning_map[self.position]
        self.owning_map[self.position] = self

    def __str__(self):
        return str(self.look)

    @property
    def case(self):
        return self._case

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position
        self._case = self.owning_map[self.position]
        self.owning_map[self.position] = self

    def move(self, direction):
        directions = {"up": (0, -1), "down": (0, 1), "right": (1, 0), "left": (-1, 0)}
        self.owning_map[self.position] = self.case
        self.position = self.position[0]+directions[direction][0], self.position[1]+directions[direction][1]


class Node:

    def __init__(self, case: Case, value='N'):
        self.case = case
        self.value = value
        self.linkeds = []
        self.case.owning_map[case.coordinates] = self

    def __str__(self):
        return str(self.value)

    def get_nearest_nodes(self, nbr: int):
        def key(val: Node):
            return val.case.get_distance_with(self.case)
        rep = []
        for node in self.case.owning_map.nodes:
            if node != self:
                rep.append(node)
        return sorted(rep, key=key)[:nbr:]

    def link_with(self, node):
        if node not in self.linkeds:
            self.linkeds.append(node)
        if self not in node.linkeds:
            node.linkeds.append(self)

    def auto_link(self, nbr_links: int):
        for node in self.get_nearest_nodes(nbr_links):
            self.link_with(node)

    def get_distance_with(self, node):
        return self.case.get_distance_with(node.case)


if __name__ == '__main__':
    from time import time
    debut = time()
    test = Map(10, 6)
    test.create_border()
    test[2, 3] = "P"
    pawn = Pawn(test, (5, 4), "O")
    pawn.move("up")
    pawn.move("left")
    pawn.move("down")
    pawn.move("right")
    pawn.move("right")
    pawn.move("up")
    print(test)
    test = Map(15, 7, ".")
    test.create_random_nodes(8)
    for node in test.nodes:
        node.auto_link(2)
    for node in test.nodes:
        for n in node.linkeds:
            n.value = "M"
    casse = True
    # node = test.nodes[0]
    # while True:
    #     for n in node.linkeds:
    #         if n.value == "N":
    #             casse = True
    #         else:
    #             n.value = "N"
    #             casse = False
    #             node = n
    #             break
    #     if casse:
    #         break
    
    print(test)
    print("Tests executés en", round(time()-debut, 3), "seconde(s) avec succès.")
