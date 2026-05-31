# Last updated: 5/31/2026, 10:21:12 AM
1class Solution:
2    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
3        asteroids.sort()
4        for asteroid in asteroids:
5            if mass < asteroid:
6                return False
7            mass += asteroid
8        return True