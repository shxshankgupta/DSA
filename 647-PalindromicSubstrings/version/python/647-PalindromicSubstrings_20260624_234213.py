# Last updated: 6/24/2026, 11:42:13 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s)
4        dp = [[False] * n for _ in range(n)]
5
6        count = 0
7
8        for L in range(1, n+1):
9            for i in range(n - L + 1):
10                j = i + L - 1
11
12                if L == 1:
13                    dp[i][i] = True
14                    count += 1
15                
16                if s[i] == s[j]:
17                    if L == 2:
18                        dp[i][j] = True
19                        count += 1
20
21                    elif L > 2:
22                        if dp[i+1][j-1]:
23                            dp[i][j] = True
24                            count += 1
25
26                else:
27                    dp[i][j] = False
28
29        return count
30
31
32