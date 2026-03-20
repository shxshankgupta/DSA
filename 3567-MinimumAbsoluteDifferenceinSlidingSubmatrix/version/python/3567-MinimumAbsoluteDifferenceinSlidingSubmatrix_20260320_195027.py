# Last updated: 3/20/2026, 7:50:27 PM
1class Solution:
2    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m, n = len(grid), len(grid[0])
4        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
5        
6        for i in range(m - k + 1):
7            for j in range(n - k + 1):
8                unique_elements = set()
9                for r in range(i, i + k):
10                    for c in range(j, j + k):
11                        unique_elements.add(grid[r][c])
12                
13                if len(unique_elements) <= 1:
14                    res[i][j] = 0
15                    continue
16                
17                sorted_elements = sorted(list(unique_elements))
18                
19                min_diff = float('inf')
20                for p in range(len(sorted_elements) - 1):
21                    diff = sorted_elements[p+1] - sorted_elements[p]
22                    if diff < min_diff:
23                        min_diff = diff
24                
25                res[i][j] = min_diff
26                
27        return res