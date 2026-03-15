# Last updated: 3/15/2026, 9:35:44 AM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        low = 0
7        mid = 0
8        high = len(nums) - 1
9        
10        while mid <= high:
11            if nums[mid] == 0:
12                nums[low], nums[mid] = nums[mid], nums[low]
13                low += 1
14                mid += 1
15            elif nums[mid] == 1:
16                mid += 1
17            else: 
18                nums[mid], nums[high] = nums[high], nums[mid]
19                high -= 1