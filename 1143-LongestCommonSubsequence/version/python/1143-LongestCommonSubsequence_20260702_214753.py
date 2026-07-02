# Last updated: 7/2/2026, 9:47:53 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m, n = len(text1), len(text2)
4
5        dp = [[0] * (n+1) for _ in range(m+1)]
6
7        for i in range(m-1, -1, -1):
8            for j in range(n-1, -1, -1):
9                    if text1[i] == text2[j]:
10                        dp[i][j] = 1 + dp[i + 1][j + 1]
11                    else:
12                        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
13                
14        return dp[0][0]
15            