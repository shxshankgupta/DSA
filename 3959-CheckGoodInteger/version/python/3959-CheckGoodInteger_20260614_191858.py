# Last updated: 6/14/2026, 7:18:58 PM
1class Solution:
2    def checkGoodInteger(self, n: int) -> bool:
3        diff = 0
4        while n > 0 :
5            d = n % 10
6            diff += d * d - d
7            n = n // 10
8
9        return diff >= 50
10