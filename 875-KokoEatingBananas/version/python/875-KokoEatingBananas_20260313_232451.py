# Last updated: 3/13/2026, 11:24:51 PM
1import math
2class Solution:
3    def minEatingSpeed(self, piles: list[int], h: int) -> int:
4        minSpeed = 1
5        maxSpeed = max(piles)
6        
7        while minSpeed < maxSpeed:
8            mid = minSpeed + (maxSpeed - minSpeed) // 2
9            
10            if self.canEatInTime(piles, h, mid):
11                maxSpeed = mid
12            else:
13                minSpeed = mid + 1
14                
15        return minSpeed
16
17    def canEatInTime(self, piles: list[int], h: int, speed: int) -> bool:
18        hours = 0
19        for pile in piles:
20            hours += math.ceil(pile / speed)
21        return hours <= h
22