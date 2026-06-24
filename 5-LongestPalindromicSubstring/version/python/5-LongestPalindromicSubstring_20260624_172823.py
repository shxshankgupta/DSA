# Last updated: 6/24/2026, 5:28:23 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3
4        def solve(i , j):
5            if i >= j:
6                return 1
7
8            if dp[i][j] != -1:
9                return dp[i][j]
10
11            if s[i] == s[j]:
12                dp[i][j] = solve(i+1, j-1)
13            
14            else:
15                dp[i][j] = 0
16
17            return dp[i][j]
18
19        n = len(s)
20        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
21
22        maxlen = 0
23        start_idx = 0
24
25
26        for i in range(n):
27            for j in range(i, n):
28                if solve(i, j) == 1:
29                    currlen = j - i + 1
30                    if currlen > maxlen:
31                        maxlen = currlen
32                        start_idx = i
33
34        return s[start_idx : start_idx + maxlen]
35
36            
37
38