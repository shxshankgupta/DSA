from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque() # This will store INDICES of numbers
        
        for i in range(len(nums)):
            # 1. Pop from back: If current number is bigger than what's in the queue,
            # the smaller ones in the queue will NEVER be the max. Kick 'em out!
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            # 2. Pop from front: If the oldest index is out of the window range, 
            # remove it. (Example: window is size 3, index 0 is too old for index 3)
            if q[0] < i - k + 1:
                q.popleft()
            
            # 3. If we've moved far enough to fill a window, the front of 'q' is our max!
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res


        # res = []

        # for i in range(len(nums) - k + 1):
        #     window = nums[i : i + k]
        #     current_max = max(window)
        #     res.append(current_max)
            
        # return res