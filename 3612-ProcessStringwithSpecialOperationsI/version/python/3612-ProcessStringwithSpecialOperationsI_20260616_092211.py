# Last updated: 6/16/2026, 9:22:11 AM
1class Solution:
2    def processStr(self, s: str) -> str:
3        res = ''
4        for char in s:
5            if char == '*':
6                res = res[:-1]
7            elif char == '#':
8                res = res + res
9            elif char == '%':
10                res = res[::-1]
11            else:
12                res += char
13
14        return res