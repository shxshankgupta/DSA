# Last updated: 6/25/2026, 12:04:24 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4        dp = [0] * (n+1)
5
6        dp[n] = 1
7        for i in range (n-1, -1, -1):
8            if s[i] == '0':
9                dp[i] = 0
10
11            else:
12                dp[i] = dp[i+1]
13
14                if i < len(s) - 1:
15                    if (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
16                        dp[i] += dp[i + 2]
17
18
19        return dp[0]