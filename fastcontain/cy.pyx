# distutils: language = c++

from libcpp.string cimport string
from libcpp.vector cimport vector

cdef class FastContain:
    cdef int n, base1, base2, mod
    cdef string chars
    cdef vector[long long] hash1, hash2, pw1, pw2

    def __init__(self, str chars, int base1=101, int base2=-1, int mod=10**9+7):
        self.n = len(chars)
        self.chars = bytes(chars, 'utf-8')
        self.base1 = base1
        self.base2 = base2
        self.mod = mod

        self._build()

    cdef void _build(self):
        cdef int i

        self.hash1.assign(self.n + 1, 0)
        self.pw1.assign(self.n + 1, 1)
        for i in range(1, self.n + 1):
            self.hash1[i] =  (self.hash1[i - 1] * self.base1 + self.chars[i - 1]) % self.mod
            self.pw1[i] = (self.pw1[i - 1] * self.base1) % self.mod

        if self.base2 > 0:
            self.hash2.assign(self.n + 1, 0)
            self.pw2.assign(self.n + 1, 1)
            for i in range(1, self.n + 1):
                self.hash2[i] =  (self.hash2[i - 1] * self.base2 + self.chars[i - 1]) % self.mod
                self.pw2[i] = (self.pw2[i - 1] * self.base2) % self.mod

    cdef int _contains(self, string other):
        cdef int i, l, r

        cdef int m = len(other)
        if m > self.n:
            return 0

        cdef int use_base2 = self.base2 > 0

        cdef long long other_hash1 = 0
        cdef long long other_hash2 = 0
        for i in range(m):
            other_hash1 = (other_hash1 * self.base1 + other[i]) % self.mod
        if use_base2:
            for i in range(m):
                other_hash2 = (other_hash2 * self.base2 + other[i]) % self.mod

        cdef int sub_hash1, sub_hash2
        for l in range(1, self.n - m + 2):
            r = l + m - 1
            sub_hash1 = (
                self.hash1[r] - self.hash1[l - 1] * self.pw1[r - l + 1]
            ) % self.mod
            if sub_hash1 == other_hash1:
                if use_base2:
                    sub_hash2 = (
                        self.hash2[r] - self.hash2[l - 1] * self.pw2[r - l + 1]
                    ) % self.mod
                    if sub_hash2 == other_hash2:
                        return 1
                else:
                    return 1
        return 0

    def __contains__(self, other: str):
        return self._contains(bytes(other, "utf-8"))

