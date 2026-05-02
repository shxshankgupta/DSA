# Last updated: 5/2/2026, 8:37:37 AM
1class Solution:
2    def rotatedDigits(self, n: int) -> int:
3        count = 0
4        for i in range(1, n + 1):
5            s = str(i)
6            # Must not contain 3, 4, or 7
7            if '3' in s or '4' in s or '7' in s:
8                continue
9            # Must contain at least one of 2, 5, 6, or 9
10            if any(d in s for d in '2569'):
11                count += 1
12        return count