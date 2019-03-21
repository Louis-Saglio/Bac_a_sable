from time import time


def show_distribution(numbers):
    print(numbers)
    numbers = str(numbers)
    for i in range(9):
        print(i, round(numbers.count(str(i)) / len(numbers), 2) * 100, sep="\t")


def gen():
    while True:
        seeds = str(time())[-3:]
        while "." in seeds or len(seeds) != 3:
            seeds = str(time())[-3:]
        numbers = str(((int(seeds[0]) % 4) + 1) ** ((int(seeds[1]) % 4) + 1) ** ((int(seeds[2]) % 4) + 1))
        for number in numbers:
            yield int(number)


b = []
a = gen()
for i in range(20):
    b.append(str(i))


show_distribution("".join(b))
