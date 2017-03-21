class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.create_map()

    def __iter__(self):
        iterator = []
        for h in range(self.height - 1):
            for l in range(self.width - 1):
                iterator.append(self.map[l][h])
            iterator.append("\n")
        return iter(iterator)

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

    def print_map(self):
        print(' ', end='')
        for case in self:
            print(case + ' ', end='', sep='')

    def set_map(self, new_map):
        self.map = new_map

    def create_map(self):
        return [['M' for n in range(self.height)] for i in range(self.width)]

    @staticmethod
    def clear():
        from os import system
        system("cls")


if __name__ == '__main__':
    test = Map(15, 7)
    test.print_map()
