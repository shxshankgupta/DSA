# Last updated: 4/26/2026, 8:49:37 AM
1class Solution:
2    def findValidElements(self, nums: list[int]) -> list[int]:
3        n_size = len(nums)
4        if n_size <= 1:
5            return nums
6        
7        valid_indices = set([0, n_size - 1])
8        
9        current_max_left = nums[0]
10        for i_idx in range(1, n_size - 1):
11            if nums[i_idx] > current_max_left:
12                valid_indices.add(i_idx)
13            if nums[i_idx] > current_max_left:
14                current_max_left = nums[i_idx]
15        
16        current_max_right = nums[-1]
17        for j_idx in range(n_size - 2, 0, -1):
18            if nums[j_idx] > current_max_right:
19                valid_indices.add(j_idx)
20            if nums[j_idx] > current_max_right:
21                current_max_right = nums[j_idx]
22                
23        result_elements = []
24        for k_idx in range(n_size):
25            if k_idx in valid_indices:
26                result_elements.append(nums[k_idx])
27                
28        return result_elements