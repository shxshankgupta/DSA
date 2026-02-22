class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_arr= 0
        cur_prefix_sum = 0
        dictionary = {0:1} #cur_prefix_sum , count

        for num in nums:
            cur_prefix_sum = cur_prefix_sum + num
            diff = cur_prefix_sum - k
            if diff in dictionary:
                total_arr += dictionary[diff]

            dictionary[cur_prefix_sum] = dictionary.get(cur_prefix_sum, 0) + 1

        return total_arr