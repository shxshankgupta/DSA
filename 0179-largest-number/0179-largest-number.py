from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strs = [str(num) for num in nums]
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        num_strs.sort(key=cmp_to_key(compare))
        
        result = "".join(num_strs)
        
        return "0" if result[0] == "0" else result