# Last updated: 3/17/2026, 10:18:37 PM
1class Solution:
2    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
3        m, n = len(matrix), len(matrix[0])
4        ans = 0
5        
6        for r in range(m):
7            for c in range(n):
8                if matrix[r][c] > 0 and r > 0:
9                    matrix[r][c] += matrix[r-1][c]
10            
11            curr_row = sorted(matrix[r], reverse=True)
12            
13            for i in range(n):
14                ans = max(ans, curr_row[i] * (i + 1))
15                
16        return ans