class Joueur:

    def __init__(self):
        from random import randint as randint
        self.rand = randint
        self.capital_depart = 1000
        self.historique_random = []
        self.historique_partie = []
        self.gain_moyen = None

    def miser(self, case, mise):
        bonne = self.rand(1, 51)
        self.historique_random.append(bonne)
        if case == bonne:
            return mise * 3
        elif case % 2 == bonne % 2:
            return mise * 0.5
        else:
            return -mise

    def determiner_mise(self, capital):
        test = len([i for i in self.historique_random[-3:] if i % 2 == 0])
        if test == 0 or test == 3:
            return round(2 * capital / 3, 2)
        else:
            return 2

    def jouer(self):
        capital = self.capital_depart
        historique = [capital]
        while capital > 1:
            if capital >= 2000:
                break
            capital += self.miser(5, self.determiner_mise(capital))
            historique.append(capital)
        self.historique_partie.append(historique)

    def jouer_beaucoup(self, nbr_parties):
        for i in range(nbr_parties):
            self.historique_random = []
            self.jouer()

    def calculer_gain_moyen(self):
        try:
            somme = 0
            for i in self.historique_partie:
                somme += i[-1]
            self.gain_moyen = round((somme / len(self.historique_partie)) - 1000, 2)
        except ZeroDivisionError:
            self.gain_moyen = None

    def main(self):
        self.jouer_beaucoup(50000)
        self.calculer_gain_moyen()

j = Joueur()
j.main()
print(j.gain_moyen)
print(j.historique_random)
