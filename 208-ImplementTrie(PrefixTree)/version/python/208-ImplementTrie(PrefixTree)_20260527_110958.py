# Last updated: 5/27/2026, 11:09:58 AM
1class Trie:
2
3    def __init__(self):
4        self.root = {}
5
6    def insert(self, word: str) -> None:
7        current = self.root
8        for char in word:
9            if char not in current:
10                current[char] = {}
11            current = current[char]
12        current['*'] = True
13
14    def search(self, word: str) -> bool:
15        current = self.root
16        for char in word:
17            if char not in current:
18                return False
19            current = current[char]
20
21        return '*' in current
22
23    def startsWith(self, prefix: str) -> bool:
24        current = self.root
25        for char in prefix:
26            if char not in current:
27                return False
28            current = current[char]
29        return True
30
31# Your Trie object will be instantiated and called as such:
32# obj = Trie()
33# obj.insert(word)
34# param_2 = obj.search(word)
35# param_3 = obj.startsWith(prefix)