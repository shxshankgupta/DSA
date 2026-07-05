# Last updated: 7/5/2026, 9:38:51 PM
1class Solution:
2    def checkIfPangram(self, sentence: str) -> bool:
3        if len(sentence) < 26:
4            return False
5        
6        if 'a' in sentence and 'b' in sentence and 'c' in sentence and 'd' in sentence and 'e' in sentence and 'f' in sentence and 'g' in sentence and 'h' in sentence and 'i' in sentence and 'j' in sentence and 'k' in sentence and 'l' in sentence and 'm' in sentence and 'n' in sentence and 'o' in sentence and 'p' in sentence and 'q' in sentence and 'r' in sentence and 's' in sentence and 't' in sentence and 'u' in sentence and 'v' in sentence and 'w' in sentence and 'x' in sentence and 'y' in sentence and 'z' in sentence :
7            return True
8
9        return False
10