# Last updated: 4/24/2026, 12:26:03 PM
1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        column_number = 0
4        for char in columnTitle:
5            value = ord(char) - ord('A') + 1
6            column_number = column_number * 26 + value
7            
8        return column_number