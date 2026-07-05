# Last updated: 7/5/2026, 10:57:52 PM
1class Solution:
2    def countAndSay(self, n: int) -> str:
3        if n == 1:
4            return '1'
5        
6        say = self.countAndSay(n-1)
7
8        res = []
9        i = 0
10        l = len(say)
11
12        while i < l: #1211
13            ch = say[i]
14            count = 0
15
16            while i < l and say[i] == ch:
17                count += 1
18                i += 1
19
20            res.append(str(count))
21            res.append(ch)
22
23        return "".join(res)
24
25