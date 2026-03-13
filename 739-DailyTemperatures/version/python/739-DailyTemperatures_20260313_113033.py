# Last updated: 3/13/2026, 11:30:33 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
3        
4        stack = []
5        n = len(temperatures)
6        result = [0] * n
7        
8        for i in range(n - 1, -1, -1):
9            
10            while stack and temperatures[i] >= temperatures[stack[-1]]:
11                stack.pop()
12                
13            if stack:
14                result[i] = stack[-1] - i
15                
16            stack.append(i)
17            
18        return result