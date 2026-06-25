# Last updated: 6/25/2026, 11:02:25 AM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4        dp = [-1] * (n+1)
5
6        def solve(i):
7            if dp[i] != -1:
8                return dp[i]
9
10            if i == len(s):
11                dp[i] = 1
12                return dp[i]
13
14            if s[i] == '0':
15                dp[i] = 0
16                return dp[i]
17
18            count = solve(i + 1)
19            if i < len(s) - 1:
20                if (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
21                    count += solve(i + 2)
22
23            dp[i] = count
24            return dp[i]
25
26        return solve(0)