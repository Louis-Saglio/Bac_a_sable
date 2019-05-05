from __future__ import annotations


class Position:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def compute_distance(position1: Position, position2: Position):
        return ((position1.x - position2.x) ** 2 + (position1.y - position2.y) ** 2) ** (1 / 2)


class Force:
    def __init__(self, x_part, y_part, intensity):
        self.x_part = x_part
        self.y_part = y_part
        self.intensity = intensity


class Particle:
    def __init__(self, mass, position: Position):
        self.mass = mass
        self.position = position
        self.forces = []

    @staticmethod
    def compute_attraction(particle1: Particle, particle2: Particle, g=6.67e-11):
        return (g * particle1.mass * particle2.mass) / Position.compute_distance(
            particle1.position, particle2.position
        ) ** 2

    def apply_forces(self):
        for force in self.forces:
            self.position.x += force.x_part * force.intensity
            self.position.y += force.y_part * force.intensity


def run_simulation(particles):
    for particle in particles:
        for other_particle in particles:
            x_part = (particle.position.x - other_particle.position.x) / (
                particle.position.y - other_particle.position.y
            )
            y_part = (particle.position.y - other_particle.position.y) / (
                particle.position.x - other_particle.position.x
            )
            force = Force(x_part, y_part)
            particle.forces.append(force)
