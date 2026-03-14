# Last updated: 3/14/2026, 10:36:07 AM
1class Solution:
2    def getHappyString(self, n: int, k: int) -> str:
3        self.result = ""
4        self.count = 0
5        
6        def backtrack(current_string):
7            if len(current_string) == n:
8                self.count += 1
9                if self.count == k:
10                    self.result = current_string
11                return
12            
13            for char in ['a', 'b', 'c']:
14                if not current_string or current_string[-1] != char:
15                    backtrack(current_string + char)
16                    if self.result:
17                        return
18
19        backtrack("")
20        return self.result