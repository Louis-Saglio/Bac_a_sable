import multiprocessing as mp
import threading as th
from random import random
from time import sleep


def parallel(func):
    def wrapper(*args, **kwargs):
        process = mp.Process(target=func, args=args, kwargs=kwargs)
        process.start()

    return wrapper


def thread(func):
    def wrapper(*args, **kwargs):
        thread_ = th.Thread(target=func, args=args, kwargs=kwargs)
        thread_.start()

    return wrapper


@thread
def run(name):
    for i in range(10):
        sleep(random())
        print(name, i)


run("a")
run("b")
