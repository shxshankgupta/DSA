class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        
        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1

        num = 1
        
        while left <= right and top <= bottom:
            # 1. top row from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # 2. right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # 3. bottom row from right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
            # 4. left column from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
        return matrix