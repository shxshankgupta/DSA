# Last updated: 3/23/2026, 6:38:03 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res = []
4        
5        def backtrack(current_str, open_count, close_count):
6            if len(current_str) == 2 * n:
7                res.append(current_str)
8                return
9            
10            if open_count < n:
11                backtrack(current_str + "(", open_count + 1, close_count)
12            
13            if close_count < open_count:
14                backtrack(current_str + ")", open_count, close_count + 1)
15        
16        backtrack("", 0, 0)
17        return res