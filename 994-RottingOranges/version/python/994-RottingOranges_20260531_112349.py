# Last updated: 5/31/2026, 11:23:49 AM
1from collections import deque
2from typing import List
3
4class Solution:
5    def orangesRotting(self, grid: List[List[int]]) -> int:
6        rows, cols = len(grid), len(grid[0])
7        q = deque()
8        fresh = 0
9     
10        for i in range(rows):
11            for j in range(cols):
12                if grid[i][j] == 2:
13                    q.append((i, j))
14                elif grid[i][j] == 1:
15                    fresh += 1
16                    
17
18        if fresh == 0:
19            return 0
20            
21        mins = 0
22        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
23        
24        while q :
25            for _ in range(len(q)):
26                r, c = q.popleft()
27                
28                for dr, dc in directions:
29                    nr, nc = r + dr, c + dc
30                    
31                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
32                        grid[nr][nc] = 2  
33                        fresh -= 1        
34                        q.append((nr, nc)) 
35            mins += 1
36
37        return mins - 1 if fresh == 0 else -1