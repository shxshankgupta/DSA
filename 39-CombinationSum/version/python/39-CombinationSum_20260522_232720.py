# Last updated: 5/22/2026, 11:27:20 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res, subset = [], []
4        n = len(candidates)
5        
6        def back(i, total):
7            if total == target:
8                res.append(subset[:])
9                return
10
11            if total > target or i >= n:
12                return
13            
14            back(i+1, total) #exclude
15            
16            subset.append(candidates[i]) # include
17            
18            back(i, total + candidates[i])
19            subset.pop()
20        
21        back(0,0)
22        return res