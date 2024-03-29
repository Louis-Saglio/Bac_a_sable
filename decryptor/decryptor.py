import os
import pickle
import random
import time
from pprint import pprint
from typing import Callable, Any


DECYPHERED_STRINGS = "abcdefghijklmnopqrstuvwxyzàéèêîôâçùûï!\"%&'()+,-./:;? ’œ"


def clean_text(text: str, accepted: str) -> str:
    text = text.lower()
    text = " ".join(text.split())
    for to_replace, by in {'º': '°', '“': '"', '”': '"', '…': '...', '«': '"', '»': '"', '’': "'"}.items():
        text = text.replace(to_replace, by)
    cleaned_text = []
    accepted_chars = set(accepted)
    for char in text:
        if char in accepted_chars:
            cleaned_text.append(char)
    cleaned_text = "".join(cleaned_text)
    return cleaned_text


def compute_sequence_probability(text: str, use_cache=False) -> dict[tuple[str, str, str], float]:
    cache_path = 'data/seq_proba_table.pkl'
    if use_cache and os.path.exists(cache_path):
        print("loading seq proba table from cache")
        with open(cache_path, "rb") as f:
            result = pickle.load(f)
    else:
        occurrences_count = {}
        result = {}
        for triplet in zip(text, text[1:], text[2:]):
            if triplet not in occurrences_count:
                occurrences_count[triplet] = 0
            occurrences_count[triplet] += 1
        for triplet, count in occurrences_count.items():
            result[triplet] = count / len(text)
        with open(cache_path, "wb") as f:
            pickle.dump(result, f)
    return result


def build_possible_words_list(text: str) -> set[str]:
    return set(text.split())


def build_stat_models() -> tuple[dict[tuple[str, str, str], float], set[str]]:
    with open('data/text_en') as f:
        text = clean_text(f.read(), DECYPHERED_STRINGS)
    return compute_sequence_probability(text, use_cache=False), build_possible_words_list(text)


SEQ_PROBA_TABLE, POSSIBLE_WORDS = build_stat_models()


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


def build_random_individual(c_strings, d_strings) -> Individual:
    assert len(c_strings) == len(d_strings), (len(c_strings), len(d_strings))
    c_strings = list(c_strings)
    d_strings = list(d_strings)
    random.shuffle(c_strings)
    random.shuffle(d_strings)
    return Individual({c_string: d_string for c_string, d_string in zip(c_strings, d_strings)})


def evolve(
    text: str,
    pop_size: int,
    duration: int,
    mutation_proba: float,
    selection_pressure: int,
    build_func: Callable[[Any, ...], Individual],
    build_func_kwargs: dict[str, Any]
) -> Individual:
    population = [build_func(**build_func_kwargs) for _ in range(pop_size)]
    for gen in range(duration):
        try:
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
            print(
                str(len(population)).center(6), str(gen).center(6),
                *[f"{f(scores):.9f}" for f in (max,)] + [decypher_text(text, population[0].table)],
            )
        except KeyboardInterrupt:
            break
    return population[0]


def build_random_cypher_table(decyphered_strings: str) -> dict[str, str]:
    c_strings, i = [], 21
    while len(c_strings) != len(decyphered_strings):
        char = chr(i)
        if char not in decyphered_strings:
            c_strings.append(char)
        i += 1
    d_strings = list(decyphered_strings)
    random.shuffle(c_strings)
    random.shuffle(d_strings)
    return dict(zip(d_strings, c_strings))


def cypher_text(text: str, table: dict[str, str]) -> str:
    cyphered_text = []
    for char in text.replace('\n', ' '):
        cyphered_text.append(table[char])
    return "".join(cyphered_text)


def decypher_text(cyphered_text: str, table: dict[str, str],) -> str:
    text = []
    for char in cyphered_text:
        text.append(table[char])
    return "".join(text)


def score_text(text: str) -> float:
    occurrences_count = {}
    for triplet in zip(text, text[1:], text[2:]):
        if triplet not in occurrences_count:
            occurrences_count[triplet] = 0
        occurrences_count[triplet] += 1
    score = 0
    for triplet, count in occurrences_count.items():
        score += -abs(count / len(text) - SEQ_PROBA_TABLE.get(triplet, 0))
    words = []
    len_words = 0
    for word in text.split(' '):
        if len(word) > 3:
            words.append(word)
            len_words += 1
    for word in words:
        if word in POSSIBLE_WORDS:
            score += 100 / len_words
    score = score
    # todo : understand why its less than 100 when success
    return score


def main():
    with open('data/text_to_encrypt_2') as f:
        text = f.read()
    text = clean_text(text, DECYPHERED_STRINGS)
    cypher_table = build_random_cypher_table(DECYPHERED_STRINGS)
    cyphered_text = cypher_text(text, cypher_table)
    solution = evolve(
        text=cyphered_text,
        pop_size=300,
        duration=300,
        mutation_proba=0.9,
        selection_pressure=100,
        build_func=build_random_individual,
        build_func_kwargs={'c_strings': cypher_table.values(), 'd_strings': DECYPHERED_STRINGS},
    )
    print(cyphered_text)
    decyphered_text = decypher_text(cyphered_text, solution.table)
    print(decyphered_text)
    print(text)
    print(score_text(decyphered_text))
    print(score_text(text))


def test():
    to_remove = "…äü°ºæаñ}“”↑*—/‘ëï79()84536ûù2ôœî0«ç[]»1â_:ê’!?;zèàxjk-\"qé'ybvw.,gfpcmhdulronisate "
    replace = {'º': '°', '“': '"', '”': '"', '…': '...', '«': '"', '»': '"', '’': "'"}
    with open('data/text_fr') as f:
        s = f.read()
    with open('data/text_en') as f:
        s += f.read()
    # s = " ".join(s.lower().split('\n'))
    s = clean_text(s, DECYPHERED_STRINGS)
    letters = set(s)
    print("".join(sorted(letters)))
    count = {}
    for letter in s:
        if letter not in count:
            count[letter] = 0
        count[letter] += 1
    letters = sorted(count.items(), key=lambda x: x[1])
    pprint(letters)
    letters = "".join([x[0] for x in letters])
    print(letters)

    # pprint(sorted(SEQ_PROBA_TABLE.items(), key=lambda x: x[1], reverse=True))


if __name__ == '__main__':
    random.seed(10)
    start = time.time()
    main()
    # test()
    print('\n', '-' * 50, round(time.time() - start, 4), sep='\n')
    # todo : allow to associate two different encrypted chars with one decrypted char
