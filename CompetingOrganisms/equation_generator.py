from math import sin
from random import randint, random, choices
from typing import List, Union

Number = Union[int, float]


class Function:

    @staticmethod
    def combine(functions: List["Function"], subject: Number) -> Number:
        for func in functions:
            subject = func.compute(subject)
        return subject

    def compute(self, subject: Number) -> Number:
        raise NotImplementedError


class Sum(Function):
    def __init__(self):
        self.number = randint(-100, 100)

    def compute(self, subject: Number) -> Number:
        print(f"{subject} + {self.number} == {subject + self.number}")
        return subject + self.number


class Sin(Function):
    def compute(self, subject: Number) -> Number:
        print(f"sin({subject}) == {sin(subject)}")
        return sin(subject)


class Expo(Function):
    def __init__(self):
        self.expo = random() * 4

    def compute(self, subject: Number) -> Number:
        print(f"{subject} ^ {self.expo} == {subject ** self.expo}")
        return subject ** self.expo


class Equation:
    def __init__(self, term_nbr: int):
        self.terms: List[List[Function]] = [[klass() for klass in choices(Function.__subclasses__(), k=3)] for _ in range(term_nbr)]

    def compute(self, variables: List[Number]) -> List[Number]:
        assert len(variables) == len(self.terms)
        return [Function.combine(term, variable) for variable, term in zip(variables, self.terms)]


print(Equation(2).compute([5, 3]))
