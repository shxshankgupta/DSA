# Last updated: 4/11/2026, 9:00:34 PM
1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        pos = {}
4        min_dist = float('inf')
5        
6        for idx, val in enumerate(nums):
7            if val not in pos:
8                pos[val] = [idx]
9            elif len(pos[val]) == 1:
10                pos[val].append(idx)
11            else:
12                first_idx = pos[val][0]
13                min_dist = min(min_dist, 2 * (idx - first_idx))
14                
15                pos[val][0] = pos[val][1]
16                pos[val][1] = idx
17                
18        return min_dist if min_dist != float('inf') else -1