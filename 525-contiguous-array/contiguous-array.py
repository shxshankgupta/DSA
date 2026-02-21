class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_indices = {0: -1} 
        count = 0
        max_length = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in diff_indices:
                max_length = max(max_length, i - diff_indices[count])
            else:
                diff_indices[count] = i
                
        return max_length