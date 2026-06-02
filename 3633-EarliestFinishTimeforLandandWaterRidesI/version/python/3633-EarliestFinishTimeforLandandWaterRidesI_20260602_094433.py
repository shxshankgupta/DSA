# Last updated: 6/2/2026, 9:44:33 AM
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3
4        ans = float('inf')
5
6        for i in range(len(landStartTime)):
7            for j in range(len(waterStartTime)):
8
9                path_land = landStartTime[i] + landDuration[i] + waterDuration[j]
10
11                water_path = waterStartTime[i] + waterDuration[i] + landDuration[j]
12
13                ans = min(ans, path_land, water, land)
14
15
16        return ans
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33class Solution:
34    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
35        ans = float('inf')
36        n = len(landStartTime)
37        m = len(waterStartTime)
38        
39        for i in range(n):
40            for j in range(m):
41                # Option 1: Land ride i -> Water ride j
42                finish_land = landStartTime[i] + landDuration[i]
43                start_water = max(finish_land, waterStartTime[j])
44                total_1 = start_water + waterDuration[j]
45                
46                # Option 2: Water ride j -> Land ride i
47                finish_water = waterStartTime[j] + waterDuration[j]
48                start_land = max(finish_water, landStartTime[i])
49                total_2 = start_land + landDuration[i]
50                
51                # Keep track of the absolute minimum finish time found
52                ans = min(ans, total_1, total_2)
53                
54        return ans