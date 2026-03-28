# Last updated: 3/28/2026, 11:19:46 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        if not s or s[0] == '0':
4            return 0
5        
6        n = len(s)
7        dp = [0] * (n + 1)
8        
9        dp[0] = 1 
10        dp[1] = 1
11        
12        for i in range(2, n + 1):
13            if s[i-1] != '0':
14                dp[i] += dp[i-1]
15                
16            two_digit = int(s[i-2:i])
17            if 10 <= two_digit <= 26:
18                dp[i] += dp[i-2]
19                
20        return dp[n]