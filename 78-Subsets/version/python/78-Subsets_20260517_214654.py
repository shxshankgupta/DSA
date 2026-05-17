# Last updated: 5/17/2026, 9:46:54 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        n = len(nums)
4        res, curr = [], []
5        
6        def backtrack(i):
7            if i == len(nums): #append copy of leaf node aka the "subset"
8                res.append(curr[:])
9                return
10            
11            backtrack(i + 1) #exclude
12            curr.append(nums[i]) #include 
13            backtrack(i + 1)
14
15            curr.pop()
16            
17            
18        backtrack(0)
19        return res