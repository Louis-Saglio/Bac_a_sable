from GravitySimulator.main import Position, Particle


def test_position_compute_distance():
    assert Position.compute_distance(Position(0, 0), Position(3, 4)) == 5


def test_particle_compute_attraction():
    p1, p2 = Particle(1.989e30, Position(0, 0)), Particle(5.98e24, Position(0, 1.49e8))
    assert Particle.compute_attraction(p1, p2) == 3.573462789964416e28
