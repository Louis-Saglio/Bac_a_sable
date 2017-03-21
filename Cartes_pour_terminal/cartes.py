class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.create_map()

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def get_map(self):
        return self.map

    def afficher_matrice(self):
        pass

    def set_map(self, new_map):
        self.map = new_map

    def create_map(self):
        return [['*' for n in range(self.height)] for i in range(self.width)]


if __name__ == '__main__':
    test = Map(15, 7)
    test.afficher_matrice()
