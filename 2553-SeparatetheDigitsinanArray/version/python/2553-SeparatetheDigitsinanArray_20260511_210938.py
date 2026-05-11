# Last updated: 5/11/2026, 9:09:38 PM
1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        answer = []
4        for num in nums:
5            digits = []
6            while num > 0:
7                digits.append(num % 10)
8                num //= 10
9            answer.extend(digits[::-1])
10        return answer