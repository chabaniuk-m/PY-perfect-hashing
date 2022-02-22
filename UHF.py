import numpy as np

import util


class UHF:
    """
    Represents universal hash function
    with parameter m,
    p is set to 4294967291 (prime number)
    a and b are chosen randomly
    """
    def __init__(self, m: int):
        self.m = m
        self.a = np.random.randint(1, util.P)
        self.b = np.random.randint(0, util.P)

    def _hash_clx(self, c: complex) -> int:
        """
        Identical hash codes for equals numbers.
        Return hash code for a complex number
        """
        k = c.__hash__()
        return (self.a * k + self.b) % util.P % self.m

    def hash_vct(self, v: np.array) -> int:
        k = 0
        for clx in v:
            k = k * 31 + self._hash_clx(clx)
        return (self.a * k + self.b) % util.P % self.m

