# Last updated: 5/29/2026, 9:25:13 AM
1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            sum = 0
5            num = nums[i]
6
7            while num > 0 :
8                sum += num % 10
9                num = num // 10
10            nums[i] = sum
11
12        return min(nums)
13
14        