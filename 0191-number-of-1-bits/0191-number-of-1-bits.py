class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        res = 1
        while (n != 1):
            if n % 2 == 1 :
                res += 1
            n = n // 2
        return res