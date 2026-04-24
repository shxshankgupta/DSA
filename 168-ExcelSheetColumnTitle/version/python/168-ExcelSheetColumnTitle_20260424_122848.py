# Last updated: 4/24/2026, 12:28:48 PM
1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        result = []
4        
5        while columnNumber > 0:
6            columnNumber -= 1
7            
8            char = chr(columnNumber % 26 + ord('A'))
9            result.append(char)
10            
11            columnNumber //= 26
12            
13        return "".join(result[::-1])