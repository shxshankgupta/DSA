# Last updated: 6/3/2026, 7:50:30 AM
1class Solution:
2    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
3        land_finish, water_finish, land_path, water_path = float('inf'), float('inf'), float('inf'), float('inf')
4        for i in range(len(landStartTime)):
5            land_finish = min(land_finish, landStartTime[i] + landDuration[i])
6
7        for j in range(len(waterStartTime)):
8            water_finish = min(water_finish, waterStartTime[j] + waterDuration[j])
9
10        for j in range(len(waterStartTime)):
11            land_path = min(land_path, max(land_finish, waterStartTime[j]) + waterDuration[j])
12
13        for i in range(len(landStartTime)):
14            water_path = min(water_path, max(water_finish, landStartTime[i]) + landDuration[i])
15
16        return min(land_path, water_path)
17