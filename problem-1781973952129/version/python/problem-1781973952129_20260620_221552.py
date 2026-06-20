# Last updated: 6/20/2026, 10:15:52 PM
1class Solution:
2    def createGrid(self, m: int, n: int) -> list[str]:
3        grid = []
4
5        grid.append("." * n)
6
7        for _ in range(m - 1):
8            grid.append("#" * (n - 1) + ".")
9
10        return grid