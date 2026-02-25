class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_diff = 0
        nums.sort()
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            max_diff = max(max_diff, diff)
        return max_diff