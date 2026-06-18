# Last updated: 6/18/2026, 11:30:58 AM
1from collections import deque
2
3class Solution:
4    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
5        wordSet = set(wordList) 
6        if endWord not in wordSet:
7            return 0
8        
9        q = deque()
10        q.append((beginWord, 1)) 
11        
12        while q:
13            u, count = q.popleft()
14            
15            if u == endWord:
16                return count
17            
18            for i in range(len(u)):
19                for c in 'abcdefghijklmnopqrstuvwxyz':
20                    next_word = u[:i] + c + u[i+1:]
21                    
22                    if next_word in wordSet:
23                        wordSet.remove(next_word) 
24                        q.append((next_word, count + 1))
25                        
26        return 0 