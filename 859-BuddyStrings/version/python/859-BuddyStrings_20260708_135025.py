# Last updated: 7/8/2026, 1:50:25 PM
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
13                if len(mismatches) > 2:
14                    return False
15                
16        if len(mismatches) == 2:
17            return s[mismatches[0]] == goal[mismatches[1]] and s[mismatches[1]] == goal[mismatches[0]]
18            
19        return False