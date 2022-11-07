from typing import Optional


class FastContainPy:
    def __init__(
        self,
        chars: str,
        base1: int = 101,
        base2: Optional[int] = None,
        mod: int = 10**9 + 7,
    ):
        self.chars = chars
        self.base1 = base1
        self.base2 = base2
        self.mod = mod
        self.hash1 = []
        self.hash2 = []
        self.pw1 = []
        self.pw2 = []

        self.build()

    def build(self):
        n = len(self.chars)

        self.hash1 = [0] * (n + 1)
        self.pw1 = [1] * (n + 1)
        if self.base2 is not None:
            self.hash2 = [0] * (n + 1)
            self.pw2 = [1] * (n + 1)

        for i in range(1, n + 1):
            self.hash1[i] = (
                self.hash1[i - 1] * self.base1 + ord(self.chars[i - 1])
            ) % self.mod
            self.pw1[i] = self.pw1[i - 1] * self.base1 % self.mod
        if self.base2 is not None:
            for i in range(1, n + 1):
                self.hash2[i] = (
                    self.hash2[i - 1] * self.base2 + ord(self.chars[i - 1])
                ) % self.mod
                self.pw2[i] = self.pw2[i - 1] * self.base2 % self.mod

    def __contains__(self, other: str) -> bool:
        n = len(self.chars)
        m = len(other)
        if m > n:
            return False

        use_base2 = bool(self.hash2)

        other_hash1 = 0
        other_hash2 = 0
        for i in range(m):
            other_hash1 = (other_hash1 * self.base1 + ord(other[i])) % self.mod
        if use_base2:
            for i in range(m):
                other_hash2 = (other_hash2 * self.base2 + ord(other[i])) % self.mod

        for l in range(1, n - m + 2):
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
                        return True
                else:
                    return True
        return False