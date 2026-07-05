# Last updated: 7/5/2026, 9:46:23 PM
1class Solution:
2    def checkIfPangram(self, sentence: str) -> bool:
3        visited = [False] * 26
4        count = 0
5        
6        for char in sentence:
7            index = ord(char) - ord('a')
8            
9            if not visited[index]:
10                visited[index] = True
11                count += 1
12                
13                if count == 26:
14                    return True
15                    
16        return False