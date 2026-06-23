# Last updated: 6/23/2026, 11:40:24 PM
1class Solution:
2
3    def rob(self, nums: List[int]) -> int:
4        n = len(nums)
5        dp = [-1] * (n + 1)
6
7        def solve(i):
8            if i >= n:
9                return 0
10
11            if dp[i] != -1:
12                return dp[i]
13
14            steal = nums[i] + solve(i + 2)
15
16            skip = solve(i + 1)
17
18            dp[i] = max(steal, skip)
19            return dp[i]
20
21        return solve(0)