# Last updated: 5/15/2026, 7:57:21 AM
1class Solution:
2    def findMin(self, nums: list[int]) -> int:
3        low = 0
4        high = len(nums) - 1
5        
6        if nums[low] <= nums[high]:
7            return nums[low]
8            
9        while low <= high:
10            mid = low + (high - low) // 2
11            
12            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
13                return nums[mid + 1]
14            
15            if mid > 0 and nums[mid] < nums[mid - 1]:
16                return nums[mid]
17
18            if nums[mid] >= nums[low]:
19                low = mid + 1
20            else:
21                high = mid - 1
22                
23        return -1