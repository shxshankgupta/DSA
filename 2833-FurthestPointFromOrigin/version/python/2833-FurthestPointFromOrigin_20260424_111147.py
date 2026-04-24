# Last updated: 4/24/2026, 11:11:47 AM
1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3        L_count = moves.count('L')
4        R_count = moves.count('R')
5        wildcard_count = moves.count('_')
6        
7        return abs(L_count - R_count) + wildcard_count