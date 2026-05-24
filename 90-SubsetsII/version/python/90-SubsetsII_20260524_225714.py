# Last updated: 5/24/2026, 10:57:14 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res, subset = [], []
5
6        def backtrack(index):
7            res.append(subset[:])
8            for i in range (index, len(nums)):
9                if i > index and nums[i] == nums[i-1]:
10                    continue
11                
12                subset.append(nums[i])
13                backtrack(i + 1)
14                subset.pop()
15        
16        backtrack(0)
17
18        return res
19