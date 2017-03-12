from statistics import mean

from Risk.methode1.analyzer import batailler_jusque_attak_gagne

for n in range(10):
    rep = []
    for i in range(10000):
        rep.append(batailler_jusque_attak_gagne(10, n))
    print(n, mean(rep))
