from random import randint, random, choices


class Organism:

    def __init__(self):
        self.x = randint(-100, 100)
        self.y = randint(-100, 100)
        self.age = 0
        self.vitality = 100
        self.genome = {action: random() for action in Organism.actions}

    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, age={self.age}, vitality={self.vitality})"

    def move_up(self):
        self.vitality -= 1
        self.y -= 1

    def move_down(self):
        self.vitality -= 1
        self.y += 1

    def move_left(self):
        self.vitality -= 1
        self.x -= 1

    def move_right(self):
        self.vitality -= 1
        self.x += 1

    def run(self):
        return choices(list(self.genome.keys()), weights=list(self.genome.values()))[0](self)

    actions = (move_down, move_left, move_right, move_up)


population = {Organism() for _ in range(1000)}


for i in range(100):
    for organism in population:
        if organism.vitality > 0:
            organism.age += 1
        organism.run()
    print(organism)

