# Last updated: 4/12/2026, 4:48:34 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        min_open = 0
4        max_open = 0
5        
6        for char in s:
7            if char == '(':
8                min_open += 1
9                max_open += 1
10            elif char == ')':
11                min_open -= 1
12                max_open -= 1
13            else: 
14                min_open -= 1
15                max_open += 1
16            
17            if max_open < 0:
18                return False
19            
20            if min_open < 0:
21                min_open = 0
22                
23        return min_open == 0