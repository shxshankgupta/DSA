class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        mask = 0
        while mask < num :
            mask = (mask << 1) | 1

        return mask ^ num