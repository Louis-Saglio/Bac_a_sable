from random import randint


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

    def find_nearest_equal_case(self):
        for case in self.owning_map:
            if case.value == self.value and case != self:
                try:
                    if self.get_distance_with(case) < self.get_distance_with(rep):
                        rep = case
                except NameError:
                    rep = case
        return rep


class Map:

    def __init__(self, width, height, filling='M', border='B'):
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
        self.position = (self.position[0]+directions[direction][0], self.position[1]+directions[direction][1])


if __name__ == '__main__':
    from time import time
    x, y, a, b = 10, 6, 2, 3
    debut = time()
    test = Map(x, y)
    test.create_border()
    test[a, b] = "P"
    pawn = Pawn(test, (5, 4), "O")
    pawn.move("up")
    pawn.move("left")
    pawn.move("down")
    pawn.move("right")
    pawn.move("right")
    pawn.move("up")
    print(test)
    test = Map(x, y, ".")
    for i in range(4):
        test.get_random_case().value = "S"
    la_case = test.get_random_case()
    la_case.value = "S"
    la_case.find_nearest_equal_case().value = "G"
    la_case.value = "X"
    print(test)
    print("Tests executés en", round(time()-debut, 3), "seconde(s) avec succès.")
