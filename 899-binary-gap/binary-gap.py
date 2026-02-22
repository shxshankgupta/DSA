class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:] # Convert to '10110'
        last_idx = -1
        res = 0
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_idx != -1:
                    res = max(res, i - last_idx)
                last_idx = i
        return res