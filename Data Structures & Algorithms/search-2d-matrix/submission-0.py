class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target > matrix[mid][-1]:
                lo = mid + 1
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = 0
                hi = len(matrix[mid]) - 1

                while lo <= hi:
                    inner_mid = (lo + hi) // 2
                    if target > matrix[mid][inner_mid]:
                        lo = inner_mid + 1
                    elif target < matrix[mid][inner_mid]:
                        hi = inner_mid - 1
                    else:
                        return True
        return False
