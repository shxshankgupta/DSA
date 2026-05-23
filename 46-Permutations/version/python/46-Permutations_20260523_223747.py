# Last updated: 5/23/2026, 10:37:47 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        n = len(nums)
5        
6        def backtrack(first):
7            if first == n:  
8                res.append(nums[:])
9                return
10            
11            for i in range(first, n):
12                nums[first], nums[i] = nums[i], nums[first]
13                
14                backtrack(first + 1)
15                
16                nums[first], nums[i] = nums[i], nums[first]
17                
18        backtrack(0)
19        return res