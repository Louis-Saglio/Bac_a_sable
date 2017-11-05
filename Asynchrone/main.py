import asyncio

async def boucle(limite: int):
    for i in range(1000 * limite):
        a = i ** (1/3.14)
        if int(a) % 1000 == 0:
            print('aaaaaaaa', a)
    return 333

def funct():
    p = boucle(100)
    for i in range(10):
        print("hello")
