import random

class Solution:
    def __init__(self, n: int, blacklist: list[int]):
        self.valid_count = n - len(blacklist)
        self.mapping = {}
        blacklist_set = set(blacklist)
        upper_range_clean = []
        for x in range(self.valid_count, n):
            if x not in blacklist_set:
                upper_range_clean.append(x)
        idx = 0
        for b in blacklist:
            if b < self.valid_count:
                self.mapping[b] = upper_range_clean[idx]
                idx += 1

    def pick(self) -> int:
        idx = random.randint(0, self.valid_count - 1)
        return self.mapping.get(idx, idx)