# Last updated: 4/23/2026, 7:32:25 PM
1class Solution:
2    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
3        from bisect import bisect_left as bl, bisect_right as br
4        z = sorted(zip(robots, distance))
5        walls.sort()
6        left = right = ri = 0
7        for i, (robot, dist) in enumerate(z):
8            prev = z[i - 1][0] if i else 0
9            nxt = z[i + 1][0] if i < len(z) - 1 else 10 ** 18
10            l, ml = bl(walls, max(prev + 1, robot - dist)), br(walls, robot)
11            mr, r = bl(walls, robot), br(walls, min(nxt - 1, robot + dist))
12            left, right, ri = max(left + ml - l, right + ml - max(l, ri)), max(left, right) + r - mr, r
13        return max(left, right)