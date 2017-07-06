import random
from pprint import pprint

DEFENSEUR = "Defenseur"
ATTAQUANT = "Attaquant"
PERDANT = "Perdant"
GAGNANT = "Gagnant"


class ArmyError(BaseException):
    pass


class Armee:
    # Todo Ajouter des @property et @x.setter

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
        if self.role is ATTAQUANT:
            if self.nbr > 3:
                self.nbr_des = 3
            elif self.nbr < 2:
                self.nbr_des = self.nbr
            else:
                raise ArmyError(f"Une armée doit être composée d'au moins 2 unités pour attaquer. Essayé {self.nbr}")
        elif self.role is DEFENSEUR:
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
        # Todo Standardiser sur le model de manage_statut()
        self.nbr_morts = 0
        for son_de, de_ennemi in zip(self.des, self.ennemi.des):
            if self.role is ATTAQUANT:
                if son_de <= de_ennemi:
                    self.nbr_morts += 1
            elif self.role is DEFENSEUR:
                if son_de < de_ennemi:
                    self.nbr_morts += 1
            else:
                raise NotImplementedError(f"Role non géré {self.role}")

    def enregistrer_morts(self):
        self.nbr -= self.nbr_morts
        self.manage_statut()

    def manage_statut(self):
        if self.role is ATTAQUANT and self.nbr == 1:
            self.statut = PERDANT
            self.ennemi.statut = GAGNANT
        elif self.role is DEFENSEUR and self.nbr == 0:
            self.statut = PERDANT
            self.ennemi.statut = GAGNANT

    def attaquer(self, other=None):
        """
        :type other Armee
        """
        if other.ennemi is not None:
            self.ennemi = other

        self.role = ATTAQUANT
        self.ennemi.role = DEFENSEUR

        self.lancer_des()
        self.ennemi.lancer_des()

        self.compter_morts()
        self.ennemi.compter_morts()

        self.enregistrer_morts()
        self.ennemi.enregistrer_morts()

        self.manage_statut()
        self.ennemi.manage_statut()

    def usque_ad_mortem(self):
        pass


if __name__ == '__main__':

    a = Armee(24)
    a.role = ATTAQUANT

    b = Armee(13, ennemi=a, role=DEFENSEUR)
    assert b.ennemi is a

    a.ennemi = b

    # Test de choisir_nbr_des
    pass

    # Test de lancer_des
    for _ in range(100):
        a.choisir_nbr_des()
        les_des = a.lancer_des()
        assert len(les_des) == 3
        assert max(les_des) < 7
        assert min(les_des) > 0
        assert les_des[0] >= les_des[-1]
        b.choisir_nbr_des()
        les_des = b.lancer_des()
        assert len(les_des) in (1, 2)
        assert max(les_des) < 7
        assert min(les_des) > 0

    # Test de compter_morts
    a.des = (5, 2, 2)
    b.des = (5, 1)
    a.compter_morts()
    b.compter_morts()
    assert a.nbr_morts == 1
    assert b.nbr_morts == 1

    # Test de enregistrer morts
    a.role = ATTAQUANT
    b.role = DEFENSEUR
    a.nbr = 7
    b.nbr = 5
    a.nbr_morts = 2
    b.nbr_morts = 0
    a.enregistrer_morts()
    b.enregistrer_morts()
    assert a.nbr == 5
    assert b.nbr == 5

    # Test de manage_statut
    a.role = ATTAQUANT
    b.role = DEFENSEUR
    a.nbr = 1
    b.nbr = 5
    a.manage_statut()
    b.manage_statut()
    assert a.statut is PERDANT
    assert b.statut is GAGNANT

    a.attaquer(b)
    assert a.ennemi is b

    pprint(a.__dict__)
    pprint(b.__dict__)
