# Last updated: 4/12/2026, 7:49:23 PM
1class Solution:
2    def removeDuplicateLetters(self, s: str) -> str:
3        last_occurrence = {char: i for i, char in enumerate(s)}
4        
5        stack = []
6        visited = set()
7        
8        for i, char in enumerate(s):
9            if char in visited:
10                continue
11            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
12                removed_char = stack.pop()
13                visited.remove(removed_char)
14            
15            stack.append(char)
16            visited.add(char)
17            
18        return "".join(stack)