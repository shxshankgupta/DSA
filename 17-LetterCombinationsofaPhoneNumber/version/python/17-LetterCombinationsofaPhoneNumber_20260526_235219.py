# Last updated: 5/26/2026, 11:52:19 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        if digits == "" :
4            return [] 
5
6        res, sol = [], []
7        n = len(digits)
8
9        charMap = { '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno','7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
10
11        def back(i):
12            if i == n:
13                res.append(''.join(sol))
14                return
15            
16            for char in charMap[digits[i]]:
17                sol.append(char)
18                back(i+1)
19                sol.pop()
20
21        back(0)
22        return res
23