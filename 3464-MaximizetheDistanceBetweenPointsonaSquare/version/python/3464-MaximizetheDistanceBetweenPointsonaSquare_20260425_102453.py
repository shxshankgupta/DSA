# Last updated: 4/25/2026, 10:24:53 AM
1from bisect import bisect_left
2
3class Solution:
4    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
5        coords = []
6        for x, y in points:
7            if y == 0:
8                coords.append(x)
9            elif x == side:
10                coords.append(side + y)
11            elif y == side:
12                coords.append(2 * side + (side - x))
13            else:
14                coords.append(3 * side + (side - y))
15        
16        coords.sort()
17        n = len(coords)
18        perimeter = 4 * side
19
20        def get_manhattan_dist(p1_idx, p2_idx):
21            def rev(d):
22                if d <= side: return (d, 0)
23                if d <= 2 * side: return (side, d - side)
24                if d <= 3 * side: return (3 * side - d, side)
25                return (0, 4 * side - d)
26            
27            x1, y1 = rev(coords[p1_idx] % perimeter)
28            x2, y2 = rev(coords[p2_idx] % perimeter)
29            return abs(x1 - x2) + abs(y1 - y2)
30
31        def check(mid):
32            for i in range(n):
33                if coords[i] > coords[0] + (perimeter // k) + 1:
34                    break
35                
36                count = 1
37                last_idx = i
38                first_idx = i
39                
40                curr_idx = i
41                for _ in range(k - 1):
42                    target_val = coords[last_idx] + mid
43                    next_idx = bisect_left(coords, target_val)
44                    
45                    while next_idx < n and get_manhattan_dist(last_idx, next_idx) < mid:
46                        next_idx += 1
47                        
48                    if next_idx >= n:
49                        count = -1
50                        break
51                    
52                    last_idx = next_idx
53                    count += 1
54                
55                if count == k and get_manhattan_dist(last_idx, first_idx) >= mid:
56                    return True
57            return False
58
59        low, high = 0, 2 * side
60        ans = 0
61        while low <= high:
62            mid = (low + high) // 2
63            if mid == 0:
64                low = 1
65                continue
66            if check(mid):
67                ans = mid
68                low = mid + 1
69            else:
70                high = mid - 1
71        return ans