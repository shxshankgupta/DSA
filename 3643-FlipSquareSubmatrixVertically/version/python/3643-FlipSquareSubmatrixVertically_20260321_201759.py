# Last updated: 3/21/2026, 8:17:59 PM
1class Solution:
2    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
3        top = x
4        bottom = x + k - 1
5        
6        while top < bottom:
7            for j in range(y, y + k):
8                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
9            top += 1
10            bottom -= 1
11            
12        return grid