# Last updated: 5/30/2026, 9:36:36 AM
1from sortedcontainers import SortedList
2
3class SegmentTree:
4    def __init__(self, mx):
5        self.mx = mx
6        # Initialize segment tree array with 4 * size to accommodate all nodes
7        self.st = [0] * (4 * mx + 1)
8
9    def insert(self, index, value, node=1, left=0, right=None):
10        if right is None:
11            right = self.mx
12            
13        # Base Case: Leaf node reached
14        if left == right:
15            self.st[node] = value
16            return
17            
18        mid = left + (right - left) // 2
19        if index <= mid:
20            self.insert(index, value, node * 2, left, mid)
21        else:
22            self.insert(index, value, node * 2 + 1, mid + 1, right)
23            
24        # Push up the maximum consecutive empty spaces to parent node
25        self.st[node] = max(self.st[node * 2], self.st[node * 2 + 1])
26
27    def check(self, q_left, q_right, node=1, left=0, right=None):
28        if right is None:
29            right = self.mx
30            
31        # No overlap condition
32        if right < q_left or left > q_right:
33            return 0
34            
35        # Total overlap condition
36        if q_left <= left and q_right >= right:
37            return self.st[node]
38            
39        # Partial overlap condition
40        mid = left + (right - left) // 2
41        return max(
42            self.check(q_left, q_right, node * 2, left, mid),
43            self.check(q_left, q_right, node * 2 + 1, mid + 1, right)
44        )
45
46
47class Solution:
48    def getResults(self, queries: list[list[int]]) -> list[bool]:
49        # Define the maximum boundary specified in the video constraints
50        MX = 10**5 
51        result = []
52        
53        # Initialize SortedList to trace obstacles, adding bounds dynamically
54        obs = SortedList([0, MX])
55        
56        # Initialize Segment Tree instance
57        st = SegmentTree(MX)
58        st.insert(0, MX) # The initial entire range has an empty space of size MX
59        
60        for q in queries:
61            if q[0] == 1:
62                # Type 1: Insert an Obstacle at position x
63                x = q[1]
64                i = obs.bisect_left(x)
65                
66                left = obs[i - 1]
67                right = obs[i]
68                
69                # Split the existing interval at x and update the segment tree
70                st.insert(left, x - left)
71                st.insert(x, right - x)
72                
73                # Permanently store the new obstacle position
74                obs.add(x)
75                
76            else:
77                # Type 2: Query for size availability
78                _, x, size = q
79                i = obs.bisect_left(x)
80                
81                left_bound = 0
82                right_bound = obs[i - 1]
83                
84                # Check maximum size available among prior complete segments
85                prev_max = st.check(left_bound, right_bound - 1)
86                
87                # Check size available at the tail segment up to x
88                tail_max = x - right_bound
89                
90                # Final evaluation if required block size fits
91                actual_max = max(prev_max, tail_max)
92                result.append(actual_max >= size)
93                
94        return result