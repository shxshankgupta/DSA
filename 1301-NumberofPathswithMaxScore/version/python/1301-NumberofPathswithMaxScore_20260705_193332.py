# Last updated: 7/5/2026, 7:33:32 PM
1from functools import lru_cache
2
3class Solution:
4    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
5        n = len(board)
6        MOD = 10**9 + 7
7
8        def isValid(i, j):
9            return 0 <= i < n and 0 <= j < n and board[i][j] != 'X'
10        
11        def intValue(ch):
12            if ch == 'S' or ch == 'E':
13                return 0
14            return int(ch)
15        
16        @lru_cache(None)
17        def solve(i, j):
18            if i == 0 and j == 0:
19                return [0, 1]  
20            
21            bestScore = -1
22            bestPaths = 0
23            
24            directions = [(i - 1, j), (i, j - 1), (i - 1, j - 1)]
25            
26            for ni, nj in directions:
27                if isValid(ni, nj):
28                    score, paths = solve(ni, nj)
29     
30                    if paths > 0:
31                        if score > bestScore:
32                            bestScore = score
33                            bestPaths = paths
34                        elif score == bestScore:
35                            bestPaths = (bestPaths + paths) % MOD
36
37            if bestScore == -1:
38                return [-1, 0]
39            
40            return [bestScore + intValue(board[i][j]), bestPaths]
41        
42        ansScore, ansPaths = solve(n - 1, n - 1)
43        
44        if ansScore == -1 or ansPaths == 0:
45            return [0, 0]
46            
47        return [ansScore, ansPaths]