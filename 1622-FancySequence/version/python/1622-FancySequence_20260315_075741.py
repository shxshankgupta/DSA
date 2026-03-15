# Last updated: 3/15/2026, 7:57:41 AM
1class Fancy:
2    def __init__(self):
3        self.nums = []
4        self.mul = 1
5        self.add = 0
6        self.MOD = 10**9 + 7
7
8    def append(self, val: int) -> None:
9        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
10        transformed_val = ((val - self.add) * inv_mul) % self.MOD
11        self.nums.append(transformed_val)
12
13    def addAll(self, inc: int) -> None:
14        self.add = (self.add + inc) % self.MOD
15
16    def multAll(self, m: int) -> None:
17        self.mul = (self.mul * m) % self.MOD
18        self.add = (self.add * m) % self.MOD
19
20    def getIndex(self, idx: int) -> int:
21        if idx >= len(self.nums):
22            return -1
23        return (self.nums[idx] * self.mul + self.add) % self.MOD