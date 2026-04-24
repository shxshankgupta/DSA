# Last updated: 4/24/2026, 4:06:59 PM
1class Solution:
2    def mirrorFrequency(self, s: str) -> int:
3        freq = Counter(s)
4        total_sum = 0
5
6        for i in range(13):
7            c = chr(ord('a') + i)
8            m = chr(ord('z') - i)
9            total_sum += abs(freq[c] - freq[m])
10            
11        for i in range(5): 
12            c = str(i)
13            m = str(9-i)
14            total_sum += abs(freq[c] - freq[m])
15
16        return total_sum