from random import randint
from time import time


# Runtime values

# i, j, k = randint(0, 9), randint(0, 9), randint(0, 9)
i, j, k = 4, 5, 6

start = time()
for _ in range(10_000_000):
    1 in {i, j, k}

print("Set in with runtime values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    8 in {i, j, k}

print("Set not in with runtime values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    1 in [i, j, k]

print("List in with runtime values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    8 in [i, j, k]

print("List not in with runtime values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    1 in (i, j, k)

print("Tuple in with runtime values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    8 in (i, j, k)

print("Tuple not in with runtime values", round(time() - start, 2))


# Compile-time values

start = time()
for _ in range(10_000_000):
    1 in {4, 5, 6}

print("Set in with compile-time values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    8 in {4, 5, 6}

print("Set not in with compile-time values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    1 in [4, 5, 6]

print("List in with compile-time values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    8 in [4, 5, 6]

print("List not in with compile-time values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    1 in (4, 5, 6)

print("Tuple in with compile-time values", round(time() - start, 2))

start = time()
for _ in range(10_000_000):
    8 in (4, 5, 6)

print("Tuple not in with compile-time values", round(time() - start, 2))
