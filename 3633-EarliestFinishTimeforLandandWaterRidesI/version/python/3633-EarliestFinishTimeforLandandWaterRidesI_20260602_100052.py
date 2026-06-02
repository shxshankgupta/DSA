# Last updated: 6/2/2026, 10:00:52 AM
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3
4        ans = float('inf')
5
6        for i in range(len(landStartTime)):
7            for j in range(len(waterStartTime)):
8
9                # land --> water :
10                finish_land = landStartTime[i] + landDuration[i] 
11                
12                if finish_land > waterStartTime[j]:
13                    land_path = finish_land + waterDuration[j]
14                
15                else:
16                    wait_time = waterStartTime[j] - finish_land
17                    land_path = finish_land = finish_land + waterDuration[j] + wait_time
18
19                # water --> land : 
20                finish_water = waterStartTime[j] + waterDuration[j]
21
22                if finish_water > landStartTime[i]:
23                    water_path = finish_water + landDuration[i]
24
25                else:
26                    wait_time = landStartTime[i] - finish_water
27                    water_path = finish_water + landDuration[i] + wait_time
28
29                ans = min(ans, land_path, water_path)
30
31
32        return ans
33
34
35
36
37
38
39