class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                sum = sum + nums[i]
            else:
                sum = sum - nums[i]
        return sum