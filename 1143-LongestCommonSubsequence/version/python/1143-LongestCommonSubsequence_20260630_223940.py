# Last updated: 6/30/2026, 10:39:40 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m, n = len(text1), len(text2)
4
5        dp = [[-1] * (n+1) for _ in range(m+1)]
6
7        def solve(i, j):
8            if i >= m or j >= n:
9                return 0
10
11            if dp[i][j] != -1:
12                return dp[i][j]
13
14            if text1[i] == text2[j]:
15                dp[i][j] = 1 + solve(i + 1, j + 1)
16            else:
17                dp[i][j] = max(solve(i + 1, j), solve(i, j + 1))
18                
19            return dp[i][j]
20            
21        return solve(0, 0)