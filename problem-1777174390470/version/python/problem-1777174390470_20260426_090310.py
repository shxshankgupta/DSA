# Last updated: 4/26/2026, 9:03:10 AM
1class Solution:
2    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        if n == 0: return 0
5        
6        # Coordinate compression for the segment tree
7        unique_vals = sorted(list(set(nums)))
8        val_map = {v: i + 1 for i, v in enumerate(unique_vals)}
9        m = len(unique_vals)
10        
11        # Two segment trees: one for endings as valleys, one for peaks
12        tree_low = [0] * (4 * m + 1)
13        tree_high = [0] * (4 * m + 1)
14        
15        def update(tree, node, start, end, idx, val):
16            if start == end:
17                tree[node] = max(tree[node], val)
18                return
19            mid = (start + end) // 2
20            if idx <= mid:
21                update(tree, 2 * node, start, mid, idx, val)
22            else:
23                update(tree, 2 * node + 1, mid + 1, end, idx, val)
24            tree[node] = max(tree[2 * node], tree[2 * node + 1])
25            
26        def query(tree, node, start, end, l, r):
27            if r < start or end < l:
28                return 0
29            if l <= start and end <= r:
30                return tree[node]
31            mid = (start + end) // 2
32            return max(query(tree, 2 * node, start, mid, l, r),
33                       query(tree, 2 * node + 1, mid + 1, end, l, r))
34
35        dp_high = [0] * n
36        dp_low = [0] * n
37        overall_max = 0
38        
39        for i in range(n):
40            val = nums[i]
41            idx = val_map[val]
42            
43            # Base case: subsequence of length 1
44            dp_high[i] = val
45            dp_low[i] = val
46            
47            # Distance k constraint: Update segment trees only for elements at least k away
48            if i >= k:
49                prev_val = nums[i - k]
50                prev_idx = val_map[prev_val]
51                update(tree_high, 1, 1, m, prev_idx, dp_high[i - k])
52                update(tree_low, 1, 1, m, prev_idx, dp_low[i - k])
53            
54            # To be a peak, current must be > previous valley
55            max_prev_low = query(tree_low, 1, 1, m, 1, idx - 1)
56            if max_prev_low > 0:
57                dp_high[i] = max(dp_high[i], max_prev_low + val)
58                
59            # To be a valley, current must be < previous peak
60            max_prev_high = query(tree_high, 1, 1, m, idx + 1, m)
61            if max_prev_high > 0:
62                dp_low[i] = max(dp_low[i], max_prev_high + val)
63            
64            overall_max = max(overall_max, dp_high[i], dp_low[i])
65            
66        return overall_max