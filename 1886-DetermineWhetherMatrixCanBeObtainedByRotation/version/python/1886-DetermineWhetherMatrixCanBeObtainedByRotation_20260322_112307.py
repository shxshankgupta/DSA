# Last updated: 3/22/2026, 11:23:07 AM
1class Solution:
2    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
3        for _ in range(4):
4            if mat == target:
5                return True
6            
7            n = len(mat)
8            for i in range(n):
9                for j in range(i, n):
10                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
11
12            for row in mat:
13                row.reverse()
14                
15        return False