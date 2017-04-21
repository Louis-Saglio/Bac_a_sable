def monsieur(func):
    def rep(param):
        print("Test de", func.__name__.title(), '...', end='\t')
        # noinspection PyBroadException
        try:
            for i in range(param):
                func(param)
            print('OK /')
        except Exception:
            print('KO X')
    return rep
