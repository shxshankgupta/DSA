class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [friend for friend in order if friend in friends]