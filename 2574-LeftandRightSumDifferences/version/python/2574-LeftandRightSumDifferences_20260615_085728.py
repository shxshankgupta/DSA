# Last updated: 6/15/2026, 8:57:28 AM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        ans = []
4        leftSum = 0
5        totalSum = sum(nums)
6
7        for num in nums:
8            rightSum = totalSum - leftSum - num
9            ans.append(abs(leftSum - rightSum))
10            leftSum += num
11
12        return ans 