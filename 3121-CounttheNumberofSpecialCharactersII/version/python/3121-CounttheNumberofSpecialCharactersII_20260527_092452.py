# Last updated: 5/27/2026, 9:24:52 AM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        # Dictionary to store the correct target index for each character's ASCII value
4        char_indices = {}
5        
6        for i, char in enumerate(word):
7            ascii_val = ord(char)
8            
9            if char.islower():
10                char_indices[ascii_val] = i
11            else:
12                if ascii_val not in char_indices:
13                    char_indices[ascii_val] = i
14                    
15        count = 0
16        
17        for lower_ascii in range(ord('a'), ord('z') + 1):
18            upper_ascii = lower_ascii - 32 
19            
20            if lower_ascii in char_indices and upper_ascii in char_indices:
21                if char_indices[lower_ascii] < char_indices[upper_ascii]:
22                    count += 1
23                    
24        return count