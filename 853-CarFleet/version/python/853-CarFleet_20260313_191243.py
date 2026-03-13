# Last updated: 3/13/2026, 7:12:43 PM
1class Solution:
2    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
3        cars = sorted(zip(position, speed), reverse=True)
4        
5        stack = []
6        
7        for p, s in cars:
8            time = (target - p) / s
9            if not stack:
10                stack.append(time)
11            else:
12                if time > stack[-1]:
13                    stack.append(time)
14                    
15        return len(stack)