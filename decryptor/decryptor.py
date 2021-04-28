import os
import pickle
import random
import string
import time
from statistics import mean

DECYPHERED_STRINGS = string.ascii_lowercase + " " + "àéèêîôâçùû"
CYPHERED_STRINGS = string.ascii_uppercase + "&" + "àéèêîôâçùû".upper()


def clean_text(text: str, accepted: str) -> str:
    cleaned_text = []
    accepted_chars = set(accepted)
    for char in text:
        if char in accepted_chars:
            cleaned_text.append(char)
    cleaned_text = "".join(cleaned_text)
    cleaned_text = cleaned_text.replace("  ", "")
    return cleaned_text


def compute_sequence_probability() -> dict[tuple[str, str, str], float]:
    with open('data/text_fr') as f:
        text = clean_text(f.read(), DECYPHERED_STRINGS)
    cache_path = 'data/seq_proba_table.pkl'
    if os.path.exists(cache_path):
        print("loading seq proba table from cache")
        with open(cache_path, "rb") as f:
            result = pickle.load(f)
    else:
        result = {}
        letters = set(text)
        for i in letters:
            for j in letters:
                for k in letters:
                    pair = f"{i}{j}{k}"
                    result[(i, j, k)] = text.count(pair) / (len(text) / 2)
        with open(cache_path, "wb") as f:
            pickle.dump(result, f)
    return result


SEQ_PROBA_TABLE = compute_sequence_probability()


class Individual:
    def __init__(self, table: dict[str, str]):
        self._table = table
        self._score_cache = None

    @property
    def table(self):
        return self._table.copy()

    def score(self, text) -> float:
        if self._score_cache is None:
            self._score_cache = score_text(decypher_text(text, self._table))
        return self._score_cache

    def clone(self):
        return Individual(self._table.copy())

    def mutate(self):
        keys = list(self._table)
        key0, key1 = random.choice(keys), random.choice(keys)
        self._table[key0], self._table[key1] = self._table[key1], self._table[key0]
        self._score_cache = None


def build_random_solution() -> Individual:
    c_strings = list(CYPHERED_STRINGS)
    d_strings = list(DECYPHERED_STRINGS)
    random.shuffle(c_strings)
    random.shuffle(d_strings)
    return Individual({c_string: d_string for c_string, d_string in zip(c_strings, d_strings)})


def evolve(
    pop_size: int,
    duration: int,
    mutation_proba: float,
    selection_pressure: int,
    text: str,
) -> Individual:
    population = [build_random_solution() for _ in range(pop_size)]
    for gen in range(duration):
        population: list[Individual] = sorted(population, key=lambda x: x.score(text), reverse=True)
        population = population[:len(population) // selection_pressure]
        new_individuals = []
        for i in range(selection_pressure - 1):
            new_individuals.extend([indiv.clone() for indiv in population])
        population.extend(new_individuals)
        for indiv in population[1:]:
            if random.random() < mutation_proba:
                indiv.mutate()
        scores = [i.score(text) for i in population]
        print(str(len(population)).center(6), str(gen).center(6), *[f"{f(scores):.3e}" for f in (max, mean, min)] + [decypher_text(text, population[0].table)])
    return population[0]


def build_random_cypher_table(cyphered_strings: str, decyphered_strings: str) -> dict[str, str]:
    c_strings = list(cyphered_strings)
    d_strings = list(decyphered_strings)
    random.shuffle(c_strings)
    random.shuffle(d_strings)
    return dict(zip(d_strings, c_strings))


def cypher_text(text: str, table: dict[str, str], unknown_char="?") -> str:
    cyphered_text = []
    for char in text:
        cyphered_text.append(table.get(char, unknown_char))
    return "".join(cyphered_text)


def decypher_text(cyphered_text: str, table: dict[str, str], unknown_char="?") -> str:
    text = []
    for char in cyphered_text:
        text.append(table.get(char, unknown_char))
    return "".join(text)


def score_text(text: str) -> float:
    occurrences_count = {}
    for triplet in zip(text, text[1:], text[2:]):
        if triplet not in occurrences_count:
            occurrences_count[triplet] = 0
        occurrences_count[triplet] += 1
    score = 0
    for triplet, count in occurrences_count.items():
        # todo : if a group of letters appears more frequently than in normal french it will be rewarded
        score += count * SEQ_PROBA_TABLE.get(triplet, 0)
    score = (score / len(text) * 100)
    return score


def main(cyphered_text: str):
    cyphered_text = clean_text(cyphered_text, CYPHERED_STRINGS)
    solution = evolve(
        pop_size=300, duration=20, mutation_proba=0.8, text=cyphered_text, selection_pressure=100,
    )
    print(cyphered_text)
    decyphered_text = decypher_text(cyphered_text, solution.table)
    print(decyphered_text)
    print(clean_text(text_, DECYPHERED_STRINGS))
    print(score_text(decyphered_text))
    print(score_text(text_))


if __name__ == '__main__':
    random.seed(1)
    text_ = "david avait dû s’asseoir lorsqu’il avait entendu le prénom florence. il était devenu blanc un instant. " \
            "il allait peut-être perdre florence avant même de lui avoir avoué son amour. il devait empêcher prélude " \
            "de continuer dans son délire. mais comment pouvait-il stopper ce parasite créé par lui quelques années " \
            "auparavant ? ce n’était pas un adversaire ordinaire. david avait déjà détruit plus d’un virus, " \
            "mais il s’agissait de virus installés sur des machines isolées. aujourd’hui, c’est une sorte de virus " \
            "qui a pris place sur tous les ordinateurs de la planète. et en plus, ce virus, nommé prélude, " \
            "avait un soupçon, non négligeable, d’intelligence. "
    start = time.time()
    main(
        cypher_text(
            clean_text(text_, DECYPHERED_STRINGS),
            build_random_cypher_table(CYPHERED_STRINGS, DECYPHERED_STRINGS),
        )
    )
    print(round(time.time() - start, 3))
