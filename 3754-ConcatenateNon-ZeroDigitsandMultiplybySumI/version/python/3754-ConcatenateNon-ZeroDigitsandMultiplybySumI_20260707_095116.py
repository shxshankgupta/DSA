# Last updated: 7/7/2026, 9:51:16 AM
1class Solution:
2    def sumAndMultiply(self, n: int) -> int:
3        digits = [c for c in str(n) if c != '0']
4        
5        if not digits:
6            return 0
7            
8        x = int("".join(digits))
9        dig_sum = sum(int(d) for d in digits)
10        
11        return x * dig_sum