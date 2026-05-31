# Last updated: 5/31/2026, 11:43:18 AM
1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        rows, cols = len(grid), len(grid[0])
5        q = deque()
6        fresh = 0
7     
8        for i in range(rows):
9            for j in range(cols):
10                if grid[i][j] == 2:
11                    q.append((i, j))
12                elif grid[i][j] == 1:
13                    fresh += 1
14                    
15
16        if fresh == 0:
17            return 0
18            
19        mins = 0
20        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
21        
22        while q :
23            for _ in range(len(q)):
24                r, c = q.popleft()
25                
26                for dr, dc in directions:
27                    nr, nc = r + dr, c + dc
28                    
29                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
30                        grid[nr][nc] = 2  
31                        fresh -= 1        
32                        q.append((nr, nc)) 
33            mins += 1
34
35        return mins - 1 if fresh == 0 else -1