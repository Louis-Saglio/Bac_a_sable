import time
import threading
import random


class Afficheur(threading.Thread):

    def __init__(self, lettre):
        super().__init__()
        self.lettre = lettre

    def run(self):
        for i in range(15):
            time.sleep(0.2 + random.randint(1, 60) / 300)
            print(self.lettre)


class Chatter(threading.Thread):

    def __init__(self, client=None):
        super().__init__()
        self.client = client
        self.message = None
        self.num = str(random.randint(0, 9))

    def run(self):
        while True:
            if self.message:
                print(self.client.num + " dit à " + self.num + self.message)
            message = input(self.num + ">>> ")
            self.client.message = message


if __name__ == '__main__':
    a = Chatter()
    b = Chatter(a)
    a.client = b
    a.start()
    b.start()
    a.join()
    b.join()
