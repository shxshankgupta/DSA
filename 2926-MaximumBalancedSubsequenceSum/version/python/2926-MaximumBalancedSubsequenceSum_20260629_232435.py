# Last updated: 6/29/2026, 11:24:35 PM
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        arr = [num-i for i, num in enumerate(nums)]
        res, keys, values = max(nums), SortedList(), dict()

        for i in range(len(nums)):
            if nums[i] <= 0:
                continue

            idx = keys.bisect(arr[i])
            prev_max = 0 if idx == 0 else values[keys[idx-1]]
            curr_max = prev_max + nums[i]
            while idx < len(keys) and values[keys[idx]] <= curr_max:
                keys.remove(keys[idx])
            
            if arr[i] in keys:
                values[arr[i]] = max(values[arr[i]], curr_max)
            else:
                keys.add(arr[i])
                values[arr[i]] = curr_max
                
            res = max(res, curr_max)
            
        return res