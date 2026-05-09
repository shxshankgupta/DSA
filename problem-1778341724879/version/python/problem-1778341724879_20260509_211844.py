# Last updated: 5/9/2026, 9:18:44 PM
1class Solution:
2    def scoreValidator(self, events: list[str]) -> list[int]:
3        score = 0
4        counter = 0
5        
6        for event in events:
7            if counter == 10:
8                break
9                
10            if event in ["0", "1", "2", "3", "4", "6"]:
11                score += int(event)
12            elif event == "W":
13                counter += 1
14            elif event == "WD":
15                score += 1
16            elif event == "NB":
17                score += 1
18                
19        return [score, counter]