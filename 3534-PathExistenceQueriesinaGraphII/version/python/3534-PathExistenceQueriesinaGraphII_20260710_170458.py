# Last updated: 7/10/2026, 5:04:58 PM
1class Solution:
2    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:        
3        # furthest_jump[i][v] = the furthest node we can reach in 2^i moves from a node v
4        furthest_jump = []
5        nodes = sorted(nums)
6
7        # initialize for jump = 1
8        furthest_jump.append({})
9        for node in nodes:
10            idx = bisect_right(nodes, node + maxDiff) - 1
11            furthest_jump[0][node] = nodes[idx]
12        
13        # build for jumps = 2, 4, 8, ...
14        i = 1
15        while True:
16            new_jumps = {}
17            for node in nodes:
18                halfway_node = furthest_jump[-1][node]
19                final_node = furthest_jump[-1][halfway_node]
20                new_jumps[node] = final_node
21            if new_jumps == furthest_jump[-1]:
22                break
23            else:
24                furthest_jump.append(new_jumps)
25                i += 1
26        
27        # compute answers
28        ans = []
29        for idx1, idx2 in queries:
30            u, v = nums[idx1], nums[idx2]
31            if u > v:
32                u, v = v, u
33            if u == v:
34                ans.append(0 if idx1 == idx2 else 1)
35            elif furthest_jump[-1][u] < v:
36                ans.append(-1)
37            else:
38                this_ans = 0
39                while True:
40                    if furthest_jump[0][u] >= v:
41                        this_ans += 1
42                        break
43                    i = 0
44                    while furthest_jump[i][u] < v:
45                        i += 1
46                    this_ans += 1 << (i - 1)
47                    u = furthest_jump[i - 1][u]
48                ans.append(this_ans)
49        return ans