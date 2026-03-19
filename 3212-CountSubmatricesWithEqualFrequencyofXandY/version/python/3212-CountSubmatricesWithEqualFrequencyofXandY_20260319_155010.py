# Last updated: 3/19/2026, 3:50:10 PM
1class Solution:
2    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        diff_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
5        x_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
6        
7        count = 0
8        
9        for r in range(rows):
10            for c in range(cols):
11                val_diff = 1 if grid[r][c] == 'X' else (-1 if grid[r][c] == 'Y' else 0)
12                val_x = 1 if grid[r][c] == 'X' else 0
13                
14                diff_prefix[r + 1][c + 1] = (val_diff + diff_prefix[r][c + 1] + 
15                                             diff_prefix[r + 1][c] - diff_prefix[r][c])
16                
17                x_prefix[r + 1][c + 1] = (val_x + x_prefix[r][c + 1] + 
18                                          x_prefix[r + 1][c] - x_prefix[r][c])
19                
20                if diff_prefix[r + 1][c + 1] == 0 and x_prefix[r + 1][c + 1] > 0:
21                    count += 1
22                    
23        return count