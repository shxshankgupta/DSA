# Last updated: 4/12/2026, 10:54:48 AM
1class Solution:
2    def minimumDistance(self, word: str) -> int:
3        def get_dist(char1, char2):
4            if char1 is None or char2 is None:
5                return 0
6            c1, c2 = ord(char1) - ord('A'), ord(char2) - ord('A')
7            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
8
9        memo = {}
10
11        def solve(idx, finger_other):
12            if idx == len(word):
13                return 0
14            
15            state = (idx, finger_other)
16            if state in memo:
17                return memo[state]
18            
19            curr_char = word[idx]
20            prev_char = word[idx - 1] if idx > 0 else None
21            
22            res1 = get_dist(prev_char, curr_char) + solve(idx + 1, finger_other)
23
24            res2 = get_dist(finger_other, curr_char) + solve(idx + 1, prev_char)
25            
26            memo[state] = min(res1, res2)
27            return memo[state]
28
29        return solve(0, None)