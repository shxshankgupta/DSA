# Last updated: 6/13/2026, 8:58:33 PM
1class Solution:
2    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
3        res = []
4        for word in words:
5            sum = 0
6            for char in word:
7                sum += weights[ord(char) - ord('a')]
8            mod = sum % 26
9            mapped_char = chr(ord('z') - mod)
10
11            res.append(mapped_char)
12
13        return "".join(res)