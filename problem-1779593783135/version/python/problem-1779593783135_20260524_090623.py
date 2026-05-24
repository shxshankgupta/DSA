# Last updated: 5/24/2026, 9:06:23 AM
1class Solution:
2    def passwordStrength(self, password: str) -> int:
3        return sum(
4            1 if 'a' <= ch <='z' else
5            2 if 'A' <= ch <='Z' else
6            3 if '0' <= ch <='9' else
7            5 if ch in '!@#$' else 0
8            for ch in set(password)
9        )