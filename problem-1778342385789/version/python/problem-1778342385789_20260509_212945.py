# Last updated: 5/9/2026, 9:29:45 PM
1class Solution:
2    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
3        
4        target_tuple = tuple(target)
5        current_points = {tuple(p) for p in points}
6        
7        if target_tuple in current_points:
8            return 0
9        
10        generation = 0
11        while True:
12            new_points_in_this_gen = set()
13            point_list = list(current_points)
14            n = len(point_list)
15            
16            for i in range(n):
17                for j in range(i + 1, n):
18                    p1 = point_list[i]
19                    p2 = point_list[j]
20                    
21                    mid = (
22                        (p1[0] + p2[0]) // 2,
23                        (p1[1] + p2[1]) // 2,
24                        (p1[2] + p2[2]) // 2
25                    )
26                    
27                    if mid not in current_points:
28                        new_points_in_this_gen.add(mid)
29            
30            if not new_points_in_this_gen:
31                return -1
32            
33            generation += 1
34            
35            if target_tuple in new_points_in_this_gen:
36                return generation
37            
38            current_points.update(new_points_in_this_gen)