# Last updated: 4/7/2026, 8:45:09 AM
1class Robot:
2    def __init__(self, width: int, height: int):
3        self.w = width
4        self.h = height
5        self.pos = 0
6        self.moved = False
7        # The total number of unique steps along the perimeter
8        self.perimeter = 2 * (width + height) - 4
9
10    def step(self, num: int) -> None:
11        self.moved = True
12        self.pos = (self.pos + num) % self.perimeter
13
14    def getPos(self) -> List[int]:
15        p = self.pos
16        if p < self.w:
17            return [p, 0]
18        if p < self.w + self.h - 1:
19            return [self.w - 1, p - (self.w - 1)]
20        if p < 2 * self.w + self.h - 2:
21            return [self.w - 1 - (p - (self.w + self.h - 2)), self.h - 1]
22        return [0, self.h - 1 - (p - (2 * self.w + self.h - 3))]
23
24    def getDir(self) -> str:
25        p = self.pos
26        # Special case for origin after at least one move
27        if self.moved and p == 0:
28            return "South"
29        
30        if 1 <= p < self.w:
31            return "East"
32        if self.w <= p < self.w + self.h - 1:
33            return "North"
34        if self.w + self.h - 1 <= p < 2 * self.w + self.h - 2:
35            return "West"
36        return "South" if self.moved else "East"
37
38# Your Robot object will be instantiated and called as such:
39# obj = Robot(width, height)
40# obj.step(num)
41# param_2 = obj.getPos()
42# param_3 = obj.getDir()