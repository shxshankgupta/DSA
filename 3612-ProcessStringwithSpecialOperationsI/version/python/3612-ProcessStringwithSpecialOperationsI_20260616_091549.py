# Last updated: 6/16/2026, 9:15:49 AM
1class Solution:
2    def processStr(self, s: str) -> str:
3        res = []
4        for char in s:
5            if char.isalpha():
6                res.append(char)
7            elif char == '*':
8                if res:
9                    res.pop()
10            elif char == '#':
11                res = res + res
12            elif char == '%':
13                res.reverse()
14
15        return "".join(res)
16