import random


class ArmyError(BaseException):
    pass


class Armee:

    def __init__(self, nbr, ennemi=None, des=None, role=None):
        """
        :type nbr int
        :type ennemi Armee
        :type des tuple
        :type role str
        """
        self.nbr = nbr
        self.ennemi = ennemi
        self.des = des
        self.delta = 7
        self.role = role

    def choisir_nbr_des(self):
        if self.role == "attack":
            if self.nbr > 3:
                return 3
            elif self.nbr < 2:
                return self.nbr
            else:
                raise ArmyError(f"Une armée doit être composée d'au moins 2 unités pour attaquer. Essayé {self.nbr}")
        elif self.role == "def":
            return 0
        else:
            raise NotImplementedError

    def attaquer(self, other=None):
        """
        :type other Armee
        """
        if other.ennemi is not None:
            self.ennemi = other
        pass


if __name__ == '__main__':
    a = Armee(24)
    a.role = "attack"
    b = Armee(13, ennemi=a)
    a.attaquer(b)
    assert a.ennemi is b
