# Last updated: 6/19/2026, 11:31:11 AM
1class Solution:
2    def fib(self, n: int) -> int:
3        if n <= 1:
4            return n
5        
6        a = 0
7        b = 1
8
9        for _ in range(2, n+1):
10            c = a + b
11            a = b
12            b = c
13
14        return c