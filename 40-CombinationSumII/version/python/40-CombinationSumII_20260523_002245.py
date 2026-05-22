# Last updated: 5/23/2026, 12:22:45 AM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        res, subset = [], []
4        n = len(candidates)
5        candidates.sort()
6        
7        def back(index, total):
8            if total == target:
9                res.append(subset[:])
10                return
11
12            if index >= n or total + candidates[index] > target :
13                return
14            
15            for i in range(index, n):
16                if i > index and candidates[i] == candidates[i - 1]:
17                    continue
18                subset.append(candidates[i]) 
19                back(i+1, total + candidates[i])
20                subset.pop()
21        
22        back(0,0)
23        return res