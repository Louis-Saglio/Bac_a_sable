import random
from pprint import pprint


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
        self.delta = random.randint(8, 9)
        self.role = role
        self.nbr_morts = 0
        self.nbr_des = 0
        self.statut = None

    def choisir_nbr_des(self):
        if self.role == "attack":
            if self.nbr > 3:
                self.nbr_des = 3
            elif self.nbr < 2:
                self.nbr_des = self.nbr
            else:
                raise ArmyError(f"Une armée doit être composée d'au moins 2 unités pour attaquer. Essayé {self.nbr}")
        elif self.role == "def":
            if (sum(self.ennemi.des) < self.delta) and self.nbr > 1:
                self.nbr_des = 2
            elif (sum(self.ennemi.des) >= self.delta) or self.nbr == 1:
                self.nbr_des = 1
            else:
                raise ArmyError(f"{self.__dict__}{self.ennemi.des}")
        else:
            raise NotImplementedError(f"Rôle non géré : {self.role}")

    def lancer_des(self):
        self.des = [random.randint(1, 6) for _ in range(self.nbr_des)]
        self.des.sort(reverse=True)
        return self.des

    def compter_morts(self):
        # fonction de comparaison externe
        self.nbr_morts = 0
        self.ennemi.nbr_morts = 0
        for de_attack, de_def in zip(self.des, self.ennemi.des):
            if de_attack > de_def:
                self.ennemi.nbr_morts += 1
            else:
                self.nbr_morts += 1

    def enregistrer_morts(self):
        self.nbr -= self.nbr_morts
        self.ennemi.nbr -= self.ennemi.nbr_morts
        self.manage_statut()

    def manage_statut(self):
        if self.role == "attack" and self.nbr == 1:
            # fonction externe
            self.statut = "Perdant"
            self.ennemi.statut = "Gagnant"
        elif self.role == "def" and self.nbr == 0:
            self.statut = "Perdant"
            self.ennemi.statut = "Gagnant"

    def attaquer(self, other=None):
        """
        :type other Armee
        """
        if other.ennemi is not None:
            self.ennemi = other
        self.role = "attack"
        self.ennemi.role = "def"
        self.lancer_des()
        self.ennemi.lancer_des()
        self.compter_morts()
        self.ennemi.compter_morts()
        self.enregistrer_morts()
        self.ennemi.enregistrer_morts()

    def usque_ad_mortem(self):
        pass


if __name__ == '__main__':

    a = Armee(24)
    a.role = "attack"

    b = Armee(13, ennemi=a, role="def")
    assert b.ennemi is a

    a.ennemi = b

    for _ in range(100):
        a.choisir_nbr_des()
        des = a.lancer_des()
        assert len(des) == 3
        assert max(des) < 7
        assert min(des) > 0
        assert des[0] >= des[-1]
        b.choisir_nbr_des()
        des = b.lancer_des()
        assert len(des) in (1, 2)
        assert max(des) < 7
        assert min(des) > 0

    a.attaquer(b)
    assert a.ennemi is b

    pprint(a.__dict__)
    pprint(b.__dict__)
