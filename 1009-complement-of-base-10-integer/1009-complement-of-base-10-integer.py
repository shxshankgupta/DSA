class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        # n.bit_length() for 5 (101) is 3. 
        # (1 << 3) is 8 (1000). 
        # 8 - 1 is 7 (111).
        mask = (1 << n.bit_length()) - 1
        return n ^ mask