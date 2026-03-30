# Last updated: 3/30/2026, 11:27:28 PM
1class CustomStack:
2
3    def __init__(self, maxSize: int):
4        self.stack = []
5        self.maxSize = maxSize
6
7    def push(self, x: int) -> None:
8        if len(self.stack) < self.maxSize:
9            self.stack.append(x)
10
11    def pop(self) -> int:
12        if not self.stack:
13            return -1
14        return self.stack.pop()
15
16    def increment(self, k: int, val: int) -> None:
17        limit = min(k, len(self.stack))
18        for i in range(limit):
19            self.stack[i] += val
20
21
22# Your CustomStack object will be instantiated and called as such:
23# obj = CustomStack(maxSize)
24# obj.push(x)
25# param_2 = obj.pop()
26# obj.increment(k,val)