# Last updated: 5/28/2026, 9:17:06 AM
1class TrieNode:
2    def __init__(self, idx: int):
3        self.children = {}
4        self.idx = idx
5
6class Solution:
7    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
8        min_len_idx = 0
9        for i in range(1, len(wordsContainer)):
10            if len(wordsContainer[i]) < len(wordsContainer[min_len_idx]):
11                min_len_idx = i
12                
13        root = TrieNode(min_len_idx)
14        
15        def insert(word_idx: int):
16            word = wordsContainer[word_idx]
17            n = len(word)
18            curr = root
19            
20            for j in range(n - 1, -1, -1):
21                ch = word[j]
22                if ch not in curr.children:
23                    curr.children[ch] = TrieNode(word_idx)
24                
25                curr = curr.children[ch]
26                
27                if len(wordsContainer[curr.idx]) > n:
28                    curr.idx = word_idx
29
30        for i in range(len(wordsContainer)):
31            insert(i)
32            
33        def search(query_word: str) -> int:
34            curr = root
35            res_idx = root.idx
36            for j in range(len(query_word) - 1, -1, -1):
37                ch = query_word[j]
38                if ch in curr.children:
39                    curr = curr.children[ch]
40                    res_idx = curr.idx
41                else:
42                    break
43            return res_idx
44
45        return [search(q) for q in wordsQuery]