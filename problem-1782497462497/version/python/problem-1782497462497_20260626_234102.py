# Last updated: 6/26/2026, 11:41:02 PM
1class Solution:
2    def findLongestChain(self, pairs: List[List[int]]) -> int:
3        pairs.sort()
4
5        n = len(pairs)
6        dp = [1] * n
7
8        maxChain = 1
9
10        for i in range(n):
11            for j in range(i):
12                if pairs[i][0] > pairs[j][1]:
13                    dp[i] = max(dp[i], 1 + dp[j])
14
15            maxChain = max(maxChain, dp[i])
16        
17        return maxChain
18
19                