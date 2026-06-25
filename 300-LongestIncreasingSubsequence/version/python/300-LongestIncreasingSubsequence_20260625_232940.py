# Last updated: 6/25/2026, 11:29:40 PM
1class Solution:
2    def lengthOfLIS(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        dp = [[-1] * n for _ in range(n)]
6
7        def solve(i, p):
8            if i >= n:
9                return 0
10
11            if p != -1 and dp[i][p] != -1:
12                return dp[i][p]
13
14            skip = solve(i + 1, p)
15
16            take = 0
17            if p == -1 or nums[i] > nums[p]:
18                take = 1 + solve(i + 1, i)
19
20            if p != -1:
21                dp[i][p] = max(take, skip)
22                return dp[i][p]
23
24            return max(take, skip)
25
26        return solve(0, -1)