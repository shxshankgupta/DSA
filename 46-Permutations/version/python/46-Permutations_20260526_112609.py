# Last updated: 5/26/2026, 11:26:09 AM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res, sol = [], []
4        n = len(nums)
5        
6        def backtrack():
7            if len(sol) == n:  
8                res.append(sol[:])
9                return
10            
11            for x in nums:
12                if x not in sol:
13                    sol.append(x)
14                    backtrack()
15                    sol.pop()
16                
17        backtrack()
18        return res