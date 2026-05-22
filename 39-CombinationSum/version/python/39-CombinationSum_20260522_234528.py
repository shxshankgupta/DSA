# Last updated: 5/22/2026, 11:45:28 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res, subset = [], []
4        n = len(candidates)
5        candidates.sort()
6        
7        def back(i, total):
8            if total == target:
9                res.append(subset[:])
10                return
11
12            if i >= n or total + candidates[i] > target :
13                return
14            
15            subset.append(candidates[i]) # include
16            back(i, total + candidates[i])
17            subset.pop()
18
19            back(i+1, total) #exclude
20        
21        back(0,0)
22        return res