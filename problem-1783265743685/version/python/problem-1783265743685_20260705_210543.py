# Last updated: 7/5/2026, 9:05:43 PM
1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        i = 0
4        idx = 0
5        
6        while i < len(chars):
7            curr = chars[i]
8            count = 0
9            
10            # saare consecutive characters count 
11            while i < len(chars) and chars[i] == curr:
12                count += 1
13                i += 1
14            
15            chars[idx] = curr
16            idx += 1
17            
18            if count > 1:
19                for digit in str(count):
20                    chars[idx] = digit
21                    idx += 1
22                    
23        return idx