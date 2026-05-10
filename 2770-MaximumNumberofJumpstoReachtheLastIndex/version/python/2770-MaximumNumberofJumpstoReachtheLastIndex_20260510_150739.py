# Last updated: 5/10/2026, 3:07:39 PM
1class Solution:
2    def maximumJumps(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        dp = [-1] * n
5        dp[0] = 0
6        
7        for j in range(1, n):
8            for i in range(j):
9                if dp[i] != -1 and -target <= nums[j] - nums[i] <= target:
10                    dp[j] = max(dp[j], dp[i] + 1)
11        
12        return dp[n - 1]