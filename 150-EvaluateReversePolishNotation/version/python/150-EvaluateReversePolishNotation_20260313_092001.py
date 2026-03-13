# Last updated: 3/13/2026, 9:20:01 AM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4        for token in tokens:
5            if token == "+":
6                stack.append(stack.pop() + stack.pop())
7            elif token == "*":
8                stack.append(stack.pop() * stack.pop())
9            elif token == "-":
10                a = stack.pop()
11                b = stack.pop()
12                stack.append(b - a)
13            elif token == "/":
14                a = stack.pop()
15                b = stack.pop()
16                stack.append(int(b / a))
17            else:
18                stack.append(int(token))
19        return stack.pop()