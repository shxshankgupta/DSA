# Last updated: 3/16/2026, 9:30:11 AM
1class Solution:
2    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
3        m, n = len(grid), len(grid[0])
4        sums = set()
5
6        for r in range(m):
7            for c in range(n):
8                sums.add(grid[r][c])
9                for k in range(1, 50):
10                    if r + 2*k >= m or c - k < 0 or c + k >= n:
11                        break
12                    
13                    current_sum = 0
14                    for i in range(k):
15                        current_sum += grid[r + i][c + i]
16                    for i in range(k):
17                        current_sum += grid[r + k + i][c + k - i]
18                    for i in range(k):
19                        current_sum += grid[r + 2*k - i][c - i]
20                    for i in range(k):
21                        current_sum += grid[r + k - i][c - k + i]
22                        
23                    sums.add(current_sum)
24        
25        return sorted(list(sums), reverse=True)[:3]