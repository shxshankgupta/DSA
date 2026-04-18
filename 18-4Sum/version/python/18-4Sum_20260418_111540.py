# Last updated: 4/18/2026, 11:15:40 AM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        n = len(nums)
5        res = []
6        
7        for i in range(n):
8            if i > 0 and nums[i] == nums[i-1]:
9                continue
10                
11            for j in range(i + 1, n):
12                if j > i + 1 and nums[j] == nums[j-1]:
13                    continue
14                left, right = j + 1, n - 1
15                while left < right:
16                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
17                    
18                    if curr_sum == target:
19                        res.append([nums[i], nums[j], nums[left], nums[right]])
20                        
21                        while left < right and nums[left] == nums[left + 1]:
22                            left += 1
23                        while left < right and nums[right] == nums[right - 1]:
24                            right -= 1
25                        
26                        left += 1
27                        right -= 1
28                    elif curr_sum < target:
29                        left += 1
30                    else:
31                        right -= 1
32        return res