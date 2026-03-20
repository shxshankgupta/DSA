# Last updated: 3/20/2026, 8:39:23 PM
1class Solution:
2    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
3        res, cur, num_of_letters = [], [], 0
4        
5        for w in words:
6            if num_of_letters + len(w) + len(cur) > maxWidth:
7                for i in range(maxWidth - num_of_letters):
8                    cur[i % (len(cur) - 1 or 1)] += ' '
9                res.append("".join(cur))
10                cur, num_of_letters = [], 0
11            
12            cur.append(w)
13            num_of_letters += len(w)
14            
15        last_line = " ".join(cur)
16        remainder = maxWidth - len(last_line)
17        res.append(last_line + ' ' * remainder)
18        
19        return res