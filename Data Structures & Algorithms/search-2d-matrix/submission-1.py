class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                left = 0
                right = len(matrix[row]) - 1

                while left <= right:
                    col = (left + right) // 2
                    if target > matrix[row][col]:
                        left = col + 1
                    elif target < matrix[row][col]:
                        right = col - 1
                    else:
                        return True
                return False
        return False
