# Last updated: 5/1/2026, 10:15:02 AM
1class Solution:
2    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
3        n = len(positions)
4        robots = sorted(range(n), key=lambda i: positions[i])
5        stack = []
6        
7        for i in robots:
8            if directions[i] == 'R':
9                stack.append(i)
10            else:
11                while stack and directions[stack[-1]] == 'R' and healths[i] > 0:
12                    top = stack[-1]
13                    if healths[top] > healths[i]:
14                        healths[top] -= 1
15                        healths[i] = 0
16                    elif healths[top] < healths[i]:
17                        healths[i] -= 1
18                        healths[top] = 0
19                        stack.pop()
20                    else:
21                        healths[i] = 0
22                        healths[top] = 0
23                        stack.pop()
24                
25                if healths[i] > 0:
26                    stack.append(i)
27        
28        return [healths[i] for i in range(n) if healths[i] > 0]