import time
from random import randint
import pygame


class Counter:
    _i = 0

    def incr(self):
        self._i += 1

    def __repr__(self):
        return str(self._i)


class Particle:
    def __init__(self, position, mass):
        self.mass = mass
        self.position = position


def center_attraction_law(particle):
    for i, axe in enumerate(particle.position):
        if axe != 0:
            particle.position[i] -= (axe / abs(axe)) * (particle.mass ** (1/3))


def display_particles(window, particles, color, size=1):
    for particle in particles:
        pygame.draw.rect(
            window,
            color,
            (
                particle.position[0] + (window.get_width() / 2) - (size / 2),
                particle.position[1] + (window.get_height() / 2) - (size / 2),
                size,
                size,
            ),
        )


def main(time_counter):
    laws = [center_attraction_law]
    particles = {Particle([randint(-500, 500), randint(-500, 500)], randint(0, 99)) for _ in range(1000)}

    pygame.display.init()
    window = pygame.display.set_mode((1000, 1000))

    while True:
        time.sleep(0.05)
        display_particles(window, particles, (0, 0, 0))
        for law in laws:
            for particle in particles:
                law(particle)
        time_counter.incr()
        display_particles(window, particles, (255, 255, 255))
        pygame.display.flip()


if __name__ == "__main__":
    _i = Counter()
    try:
        main(_i)
    except KeyboardInterrupt:
        print(_i)
