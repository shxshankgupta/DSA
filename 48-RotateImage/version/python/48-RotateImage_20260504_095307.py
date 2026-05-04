# Last updated: 5/4/2026, 9:53:07 AM
1class Solution:
2    def rotate(self, matrix: list[list[int]]) -> None:
3        n = len(matrix)
4        
5        for i in range(n):
6            for j in range(i + 1, n):
7                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
8        
9        for i in range(n):
10            matrix[i].reverse()