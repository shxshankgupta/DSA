class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:] 
        last_idx = -1
        gap = 0
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_idx != -1:
                    gap = max(gap, i - last_idx)
                last_idx = i
        return gap