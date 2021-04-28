import os
import pickle
import string

import numba

three_strings_numba_tuple = numba.types.UniTuple(numba.types.string, 3)


DECYPHERED_STRINGS = string.ascii_lowercase + " " + "àéèêîôâçùû"
CYPHERED_STRINGS = string.ascii_uppercase + "&" + "àéèêîôâçùû".upper()


def compute_sequence_probability() -> dict[tuple[str, str, str], float]:
    with open('data/text_fr') as f:
        text = clean_text(f.read(), DECYPHERED_STRINGS)
    cache_path = 'data/seq_proba_table.pkl'
    if os.path.exists(cache_path):
        print("loading seq proba table from cache")
        with open(cache_path, "rb") as f:
            result = pickle.load(f)
    else:
        result = numba.typed.Dict.empty(key_type=three_strings_numba_tuple, value_type=numba.float64)
        letters = set(text)
        for i in letters:
            for j in letters:
                for k in letters:
                    pair = f"{i}{j}{k}"
                    result[(i, j, k)] = text.count(pair) / (len(text) / 2)
        with open(cache_path, "wb") as f:
            pickle.dump(result, f)
    return result


SEQ_PROBA_TABLE: dict[tuple[str, str, str], float] = compute_sequence_probability()


@numba.njit
def score_text(text: str) -> float:
    occurrences_count = numba.typed.Dict.empty(
        key_type=three_strings_numba_tuple,
        value_type=numba.int64,
    )
    return 4.2


score_text('hello')
