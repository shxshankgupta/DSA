# Last updated: 6/18/2026, 10:00:37 AM
1class Solution:
2    def angleClock(self, hour: int, minutes: int) -> float:
3        min_angle = minutes * 6
4
5        hour_angle = (hour % 12) * 30 + minutes * 0.5
6
7        diff = diff = abs(hour_angle - min_angle)
8
9        return min(diff, 360 - diff)