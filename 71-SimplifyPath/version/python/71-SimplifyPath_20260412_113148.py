# Last updated: 4/12/2026, 11:31:48 AM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        components = path.split('/')
4        stack = []
5        
6        for part in components:
7            if part == "..":
8                if stack:
9                    stack.pop()
10            elif part == "." or part == "":
11                continue
12            else:
13                stack.append(part)
14        
15        return "/" + "/".join(stack)