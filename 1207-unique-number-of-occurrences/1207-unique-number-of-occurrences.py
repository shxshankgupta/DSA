class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = {}
        for x in arr:
            counts[x] = counts.get(x, 0) + 1

        freq_list = list(counts.values())
        return len(freq_list) == len(set(freq_list))