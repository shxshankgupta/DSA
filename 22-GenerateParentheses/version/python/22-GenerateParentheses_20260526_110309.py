# Last updated: 5/26/2026, 11:03:09 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res, string = [], []
4        
5        def backtrack(open_count, close_count):
6            if len(string) == 2 * n:
7                res.append(''.join(string))
8                return
9            
10            if open_count < n:
11                string.append('(')
12                backtrack(open_count + 1, close_count)
13                string.pop()
14            
15            if close_count < open_count:
16                string.append(')')
17                backtrack (open_count, close_count + 1)
18                string.pop()
19        
20        backtrack(0, 0)
21        return res