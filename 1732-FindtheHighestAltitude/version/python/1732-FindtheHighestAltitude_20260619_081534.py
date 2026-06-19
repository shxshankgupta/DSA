# Last updated: 6/19/2026, 8:15:34 AM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        alt = 0
4        curr_alt = 0
5        for g in gain:
6            curr_alt += g
7            alt = max(alt, curr_alt) 
8
9        return alt
10