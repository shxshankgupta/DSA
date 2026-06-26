# Last updated: 6/26/2026, 11:37:03 PM
1class Solution:
2    def findLongestChain(self, pairs: List[List[int]]) -> int:
3        pairs.sort()
4
5        n = len(pairs)
6
7        dp = [[-1] *(n+1) for _ in range(n)]
8
9        def solve(i , p):
10            if i >= n:
11                return 0
12            
13            if dp[i][p+1] != -1:
14                return dp[i][p+1]
15
16            skip = solve(i+1, p)
17            take = 0
18            if p == -1 or (pairs[i][0] > pairs[p][1]):
19                take = 1 + solve(i+1, i)
20
21            dp[i][p+1] = max(skip, take)
22            return dp[i][p+1]
23
24        return solve(0, -1)
25