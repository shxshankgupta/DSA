# Last updated: 6/25/2026, 12:05:33 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4        dp = [0] * (n + 1)
5        dp[n] = 1
6        
7        for i in range(n - 1, -1, -1):
8            if s[i] == '0':
9                dp[i] = 0
10            else:
11                dp[i] = dp[i + 1]
12                
13                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
14                    dp[i] += dp[i + 2]
15                    
16        return dp[0]