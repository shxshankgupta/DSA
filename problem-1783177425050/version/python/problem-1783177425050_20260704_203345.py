# Last updated: 7/4/2026, 8:33:45 PM
1class Solution:
2    def isMiddleElementUnique(self, nums: list[int]) -> bool:
3        mid = nums[len(nums)//2]
4        return nums.count(mid) == 1