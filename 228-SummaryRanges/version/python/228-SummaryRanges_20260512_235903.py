# Last updated: 5/12/2026, 11:59:03 PM
1class Solution:
2    def summaryRanges(self, nums: List[int]) -> List[str]:
3        ans = []
4        i = 0
5        while i < len(nums):
6            start = nums[i]
7            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
8                i += 1
9            
10            if start != nums[i]:
11                ans.append(f"{start}->{nums[i]}")
12            else:
13                ans.append(f"{start}")
14            i += 1
15        return ans