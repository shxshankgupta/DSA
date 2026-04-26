# Last updated: 4/26/2026, 9:01:21 AM
1class Solution:
2    def minOperations(self, nums: list[int]) -> int:
3        res = 0
4        for i in range(len(nums) - 1):
5            if nums[i] > nums[i+1]:
6                res += nums[i] - nums[i+1]
7        return res