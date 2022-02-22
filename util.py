import numpy as np

P = 2_147_483_647
COMPLEX_BOUND = 100
DIMENSIONS_BOUND = 5


def input_vect(prompt: str) -> list:
    s = input(prompt)[1:-2]
    return [complex(c) for c in s.split(';')]


def rand_data(size: int) -> np.array:
    res = np.zeros(size, dtype=list)
    for i in range(size):
        d = np.random.randint(1, DIMENSIONS_BOUND)
        res[i] = list(
            np.random.randint(-COMPLEX_BOUND + 1, COMPLEX_BOUND, d) +
            np.random.randint(-COMPLEX_BOUND + 1, COMPLEX_BOUND, d) * 1j)

    return res
