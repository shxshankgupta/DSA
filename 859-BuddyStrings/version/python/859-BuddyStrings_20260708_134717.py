# Last updated: 7/8/2026, 1:47:17 PM
1class Solution:
2    def buddyStrings(self, s: str, goal: str) -> bool:
3        if len(s) != len(goal):
4            return False
5        
6        if s == goal:
7            return len(set(s)) < len(s)
8            
9        mismatches = []
10        for i in range(len(s)):
11            if s[i] != goal[i]:
12                mismatches.append(i)
13                
14        if len(mismatches) == 2:
15            i, j = mismatches[0], mismatches[1]
16            return s[i] == goal[j] and s[j] == goal[i]
17            
18        return False