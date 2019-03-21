import threading


threads = {}


def asynchrone(func):
    def wrapper(*param):
        class Thread(threading.Thread):
            def run(self):
                return func(*param)

        # thread = Thread()
        # threads[func] = thread.__dict__
        return Thread().start()

    # return func
    return wrapper


if __name__ == "__main__":
    from random import randint
    from time import sleep

    @asynchrone
    def afficher(lettre):
        # lettre = "a"
        for _ in range(10):
            print(lettre)
            sleep(randint(20, 100) / 100)
        return "marche"

    @asynchrone
    def entree():
        message = input(">>>")
        print(message)

    # entree()
    # threads[afficher]["start"]("a")
    afficher("a")
    afficher("b")
