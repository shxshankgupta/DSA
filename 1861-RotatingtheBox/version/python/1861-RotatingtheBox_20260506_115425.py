# Last updated: 5/6/2026, 11:54:25 AM
1class Solution:
2    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
3        m = len(boxGrid)
4        n = len(boxGrid[0])
5        
6        for r in range(m):
7            empty_pos = n - 1  
8            for c in range(n - 1, -1, -1):
9                if boxGrid[r][c] == '#':
10                    boxGrid[r][c], boxGrid[r][empty_pos] = boxGrid[r][empty_pos], boxGrid[r][c]
11                    empty_pos -= 1
12                elif boxGrid[r][c] == '*':
13                    empty_pos = c - 1
14        
15        res = [["" for _ in range(m)] for _ in range(n)]
16        for r in range(m):
17            for c in range(n):
18                res[c][m - 1 - r] = boxGrid[r][c]
19                
20        return res