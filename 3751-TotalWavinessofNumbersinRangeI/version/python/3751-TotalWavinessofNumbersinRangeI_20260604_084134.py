# Last updated: 6/4/2026, 8:41:34 AM
1class Solution:
2    def totalWaviness(self, num1: int, num2: int) -> int:
3        sol = 0
4
5        for num in range(num1, num2 + 1):
6            s = str(num)
7            if len(s) < 3:
8                continue
9
10            for j in range(1,len(s) - 1):
11                if s[j] > s[j-1] and s[j] > s[j + 1]:
12                    sol += 1
13                elif s[j] < s[j-1] and s[j] < s[j + 1]:
14                    sol += 1
15        
16        return sol
17