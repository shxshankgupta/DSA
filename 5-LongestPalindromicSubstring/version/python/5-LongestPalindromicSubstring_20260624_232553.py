# Last updated: 6/24/2026, 11:25:53 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n = len(s)
4        dp = [[False for _ in range(n+1)] for _ in range(n+1)]
5
6        maxlen = 1
7        start_idx = 0
8
9        for i in range(n):
10            dp[i][i] = True
11
12        for L in range(2, n + 1):
13            for i in range(n - L + 1):
14                j = i + L - 1
15                if s[i] == s[j]:
16                    if L == 2:
17                        dp[i][j] = True
18                        if L > maxlen:
19                            maxlen = L
20                            start_idx = i
21
22                    elif dp[i+1][j-1]:
23                        dp[i][j] = True
24                        if L > maxlen:
25                            maxlen = L
26                            start_idx = i
27                else:
28                    dp[i][j] = False
29
30        return s[start_idx : start_idx + maxlen]
31
32            
33
34