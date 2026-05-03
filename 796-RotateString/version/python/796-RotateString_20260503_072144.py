# Last updated: 5/3/2026, 7:21:44 AM
1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        if len(s) != len(goal):
4            return False
5
6        return goal in (s + s)