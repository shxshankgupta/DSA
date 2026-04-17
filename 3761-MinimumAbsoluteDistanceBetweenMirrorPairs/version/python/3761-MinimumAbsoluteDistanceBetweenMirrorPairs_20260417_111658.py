# Last updated: 4/17/2026, 11:16:58 AM
1class Solution:
2    def minMirrorPairDistance(self, nums: List[int]) -> int:
3        last_seen = {}
4        min_dist = float('inf')
5        
6        for j, val in enumerate(nums):
7            if val in last_seen:
8                min_dist = min(min_dist, j - last_seen[val])
9            
10            reversed_val = int(str(val)[::-1])
11            
12            last_seen[reversed_val] = j
13            
14        return min_dist if min_dist != float('inf') else -1