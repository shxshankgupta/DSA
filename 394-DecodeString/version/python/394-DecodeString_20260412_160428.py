# Last updated: 4/12/2026, 4:04:28 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4        curr_str = ""
5        curr_num = 0
6        
7        for char in s:
8            if char.isdigit():
9                curr_num = curr_num * 10 + int(char)
10            elif char == '[':
11                stack.append((curr_str, curr_num))
12                curr_str = ""
13                curr_num = 0
14            elif char == ']':
15                prev_str, num = stack.pop()
16                curr_str = prev_str + (curr_str * num)
17            else:
18                curr_str += char
19                
20        return curr_str