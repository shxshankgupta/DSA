# Last updated: 6/26/2026, 1:22:09 PM
1class Solution:
2    def lengthOfLIS(self, nums: list[int]) -> int:
3        n = len(nums)
4        dp = [1] * (n+1)
5
6        maxLIS = 1
7
8        for i in range(n):
9            for j in range(i):
10                if nums[i] > nums[j]:
11                    dp[i] = max( dp[i], dp[j] + 1)
12            
13            maxLIS = max(maxLIS, dp[i])
14        
15        return maxLIS
16                