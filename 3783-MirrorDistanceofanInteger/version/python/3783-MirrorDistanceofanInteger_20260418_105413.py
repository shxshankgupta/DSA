# Last updated: 4/18/2026, 10:54:13 AM
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        reversed_str = str(n)[::-1]
4        reversed_n = int(reversed_str)
5        return abs(n - reversed_n)