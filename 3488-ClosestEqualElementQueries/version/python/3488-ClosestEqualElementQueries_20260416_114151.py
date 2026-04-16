# Last updated: 4/16/2026, 11:41:51 AM
1from collections import defaultdict
2import bisect
3
4class Solution:
5    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
6        n = len(nums)
7        val_to_indices = defaultdict(list)
8        for i, val in enumerate(nums):
9            val_to_indices[val].append(i)
10        
11        results = []
12        for q_idx in queries:
13            target_val = nums[q_idx]
14            indices = val_to_indices[target_val]
15            
16            if len(indices) <= 1:
17                results.append(-1)
18                continue
19            
20            pos = bisect.bisect_left(indices, q_idx)
21            
22            left_neighbor = indices[(pos - 1) % len(indices)]
23            right_neighbor = indices[(pos + 1) % len(indices)]
24            
25            def get_circular_dist(i, j, n):
26                dist = abs(i - j)
27                return min(dist, n - dist)
28            
29            min_dist = min(
30                get_circular_dist(q_idx, left_neighbor, n),
31                get_circular_dist(q_idx, right_neighbor, n)
32            )
33            
34            results.append(min_dist)
35            
36        return results