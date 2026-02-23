class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        appeared = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            appeared[c].append(n)   #appeared nth time 

        res = []
        for i in range(len(appeared) - 1, 0, -1):
            for n in appeared[i]:
                res.append(n)
                if len(res) == k:
                    return res