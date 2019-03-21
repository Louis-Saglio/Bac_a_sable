import random
from os import system
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
        self.nbr_initial = nbr
        self.nbr = nbr
        self.ennemi = ennemi
        self._des = des
        self.delta = 9
        self._role = role
        self._nbr_morts = None
        self._nbr_des = None
        self._statut = None

    @property
    def statut(self):
        return self._statut

    def choisir_nbr_des(self):
        if self._role is ATTAQUANT:
            if self.nbr > 2:
                self._nbr_des = 3
            elif self.nbr <= 2:
                self._nbr_des = self.nbr - 1
            else:
                raise ArmyError(f"Une armée doit être composée d'au moins 2 unités pour attaquer. Essayé {self.nbr}")
        elif self._role is DEFENSEUR:
            if (sum(self.ennemi._des) < self.delta) and self.nbr > 1:
                self._nbr_des = 2
            elif (sum(self.ennemi._des) >= self.delta) or self.nbr == 1:
                self._nbr_des = 1
            else:
                return 1
                # raise ArmyError(f"{self.__dict__}{self.ennemi.des}")
        else:
            raise NotImplementedError(f"Rôle non géré : {self._role}")

    def lancer_des(self):
        self._des = [random.randint(1, 6) for _ in range(self._nbr_des)]
        self._des.sort(reverse=True)
        return self._des

    def compter_morts(self):
        # Todo Standardiser sur le model de manage_statut()
        self._nbr_morts = 0
        for son_de, de_ennemi in zip(self._des, self.ennemi._des):
            if self._role is ATTAQUANT:
                if son_de <= de_ennemi:
                    self._nbr_morts += 1
            elif self._role is DEFENSEUR:
                if son_de < de_ennemi:
                    self._nbr_morts += 1
            else:
                raise NotImplementedError(f"Role non géré {self._role}")

    def enregistrer_morts(self):
        self.nbr -= self._nbr_morts
        self.manage_statut()

    def manage_statut(self):
        if self._role is ATTAQUANT and self.nbr == 1:
            self._statut = PERDANT
            self.ennemi._statut = GAGNANT
        elif self._role is DEFENSEUR and self.nbr == 0:
            self._statut = PERDANT
            self.ennemi._statut = GAGNANT

    def initialise_attaque(self, other):
        """
        :type other Armee
        """
        self.ennemi = other
        self.ennemi.ennemi = self
        self._role = ATTAQUANT
        self.ennemi._role = DEFENSEUR

    def attaquer(self):

        self.choisir_nbr_des()
        self.lancer_des()

        self.ennemi.choisir_nbr_des()
        self.ennemi.lancer_des()

        self.compter_morts()
        self.ennemi.compter_morts()

        self.enregistrer_morts()
        self.ennemi.enregistrer_morts()

        self.manage_statut()
        self.ennemi.manage_statut()

    def usque_ad_mortem(self, ennemi=None, afficher=False):
        self.initialise_attaque(ennemi)
        i = 0
        while not (self._statut and self.ennemi._statut):
            self.attaquer()
            if afficher:
                if i % (int(self.nbr_initial / 20)) == 0 or GAGNANT in (self.statut, self.ennemi.statut):
                    system("clear")
                    self.afficher_avancement()
                    self.ennemi.afficher_avancement()
            i += 1
        if self._statut is GAGNANT:
            return self
        return self.ennemi

    def afficher_avancement(self):
        pct = int((self.nbr * 100) / self.nbr_initial)
        print(("|" * pct).ljust(100), pct, "%")


if __name__ == "__main__":

    def test_choisir_nbr_des():
        a = Armee(12)
        b = Armee(8)
        a.ennemi = b
        b.ennemi = a
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        b.delta = 9
        a.choisir_nbr_des()
        a._des = (6, 5, 2)
        b.choisir_nbr_des()
        assert a._nbr_des == 3
        assert b._nbr_des == 1

    test_choisir_nbr_des()

    def test_lancer_des():
        # Test de lancer_des
        for _ in range(100):
            a = Armee(12)
            b = Armee(8)
            a.ennemi = b
            b.ennemi = a
            a._role = ATTAQUANT
            b._role = DEFENSEUR
            a.choisir_nbr_des()
            a.lancer_des()
            b.choisir_nbr_des()
            b.lancer_des()
            assert max(a._des + b._des) < 7
            assert min(a._des + b._des) > 0

    test_lancer_des()

    def test_compter_morts():
        # Test de compter_morts
        a = Armee(12)
        b = Armee(8)
        a.ennemi = b
        b.ennemi = a
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        a._des = (5, 2, 2)
        b._des = (5, 1)
        a.compter_morts()
        b.compter_morts()
        assert a._nbr_morts == 1
        assert b._nbr_morts == 1

    test_compter_morts()

    def test_enregistrer_morts():
        # Test de enregistrer morts
        a = Armee(12)
        b = Armee(8)
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        a._nbr_morts = 2
        b._nbr_morts = 0
        a.enregistrer_morts()
        b.enregistrer_morts()
        assert a.nbr == 10
        assert b.nbr == 8

    test_enregistrer_morts()

    def test_manage_statut():
        # Test de manage_statut
        a = Armee(12)
        b = Armee(8)
        a.ennemi = b
        b.ennemi = a
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        a.nbr = 1
        b.nbr = 5
        a.manage_statut()
        b.manage_statut()
        assert a.statut is PERDANT
        assert b.statut is GAGNANT

    test_manage_statut()

    def test_initialise_attaque():
        a = Armee(12)
        b = Armee(8)
        a.initialise_attaque(b)
        assert a._role is ATTAQUANT
        assert b._role is DEFENSEUR
        assert a.ennemi is b
        assert b.ennemi is a

    def test_attaquer():
        a = Armee(12)
        b = Armee(8)
        a.initialise_attaque(b)
        a.attaquer()
        assert a.ennemi is b

    test_attaquer()

    def test_usque_ad_mortem():
        Armee.omnia = []
        nbr = 1_000_000
        a = Armee(nbr)
        b = Armee(nbr)
        from time import time

        debut = time()
        gagnant = a.usque_ad_mortem(b, True)
        fin = time()
        pprint(gagnant.__dict__)
        print(round(fin - debut, 3), "secondes")

    test_usque_ad_mortem()
