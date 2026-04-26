# Last updated: 4/26/2026, 8:55:18 AM
1from collections import Counter
2
3class Solution:
4    def sortVowels(self, s: str) -> str:
5        vowel_set = set("aeiou")
6        char_counts = Counter(s)
7        first_seen = {}
8        
9        for idx, char in enumerate(s):
10            if char in vowel_set and char not in first_seen:
11                first_seen[char] = idx
12        
13        extracted_vowels = [char for char in s if char in vowel_set]
14        extracted_vowels.sort(key=lambda v: (-char_counts[v], first_seen[v]))
15        
16        result_chars = list(s)
17        vowel_ptr = 0
18        for i in range(len(result_chars)):
19            if result_chars[i] in vowel_set:
20                result_chars[i] = extracted_vowels[vowel_ptr]
21                vowel_ptr += 1
22                
23        return "".join(result_chars)