# Last updated: 4/23/2026, 7:13:20 PM
1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        pos_map = collections.defaultdict(list)
4        min_dist = float('inf')
5        
6        for idx, val in enumerate(nums):
7            pos_map[val].append(idx)
8            
9            if len(pos_map[val]) >= 3:
10                current_span = 2 * (pos_map[val][-1] - pos_map[val][-3])
11                min_dist = min(min_dist, current_span)
12        
13        return min_dist if min_dist != float('inf') else -1