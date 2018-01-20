import multiprocessing as mp
from pprint import pprint
from random import random
from time import sleep

from Risk.methode3.main import Armee


class Process(mp.Process):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        super().__init__(group, target, name, args, kwargs)
        self.queue = kwargs["queue"]

    def run(self):
        self.queue.put(self.name + " channel 1")
        for i in range(10):
            sleep(random())
            print(self.name, i)
        self.queue.put(self.name + " channel 2")

    # def run(self):
    #     a = Armee(1000000)
    #     b = Armee(1000000)
    #     a.usque_ad_mortem(b)
    #     a.attaquer()
    #     print(f"\nRapport {self.name}")
    #     pprint(a.__dict__)
    #     pprint(b.__dict__)


queue = mp.Queue(1)

Process(name="a", kwargs={"queue": queue}).start()
Process(name="b", kwargs={"queue": queue}).start()
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
# Process(name="b").start()
# Process(name="c").start()
# Process(name="d").start()
# Process(name="e").start()
# Process(name="f").start()
# Process(name="g").start()
# Process(name="h").start()
# Process(name="i").start()
# Process(name="j").start()
# Process().run()
