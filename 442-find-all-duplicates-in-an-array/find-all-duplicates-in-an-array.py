class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map = set(nums)
        ans = []
        for num in nums:
            if num in map:
                map.remove(num)
            else:
                ans.append(num)
        return ans