# Last updated: 5/31/2026, 10:33:40 AM
1class Solution:
2    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
3        asteroids.sort()
4
5        for asteroid in asteroids:
6            if mass >= asteroid :
7                mass += asteroid
8            else:
9                return False
10        return True
11
12
13
14
15
16
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
33
34
35
36
37        steroids.sort()
38        for asteroid in asteroids:
39            if mass < asteroid:
40                return False
41            mass += asteroid
42        return True