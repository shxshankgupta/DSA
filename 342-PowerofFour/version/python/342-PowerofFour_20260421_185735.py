# Last updated: 4/21/2026, 6:57:35 PM
1import math
2
3class Solution:
4    def isPowerOfFour(self, n: int) -> bool:
5        if n <= 0:
6            return False
7        
8        res = math.log(n, 4)
9        return res.is_integer()