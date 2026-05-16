# Last updated: 5/16/2026, 9:19:26 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        low, high = 0, len(nums) - 1
4        
5        while low < high:
6            mid = (low + high) // 2
7            
8            if nums[mid] > nums[high]:
9                low = mid + 1
10            elif nums[mid] < nums[high]:
11                high = mid
12            else:
13                high -= 1
14                
15        return nums[low]