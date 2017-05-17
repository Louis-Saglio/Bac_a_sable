from time import time


def monsieur(func):
    def rep(param):
        nom_objet = func.__name__.title() if 'test_' not in func.__name__ else func.__name__[5:]
        print("Test de", nom_objet, '...', end='\t')
        # noinspection PyBroadException
        try:
            for i in range(param):
                func(param)
            print('OK')
        except Exception:
            print('KO')
    return rep


def chronometre(func):
    def decorated(*param):
        debut = time()
        res = func(*param)
        nom = str(func).split()[1] if str(func).split()[1] != 'tests' else 'de test'
        temps = round(time() - debut)
        print("Temps d'execution de la fonction", nom, ":", temps, "seconde" + ("s" if temps >= 2 else ''))
    return decorated
