class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        s = 0
        e = len(matrix) - 1

        while s <= e:
            mid = (s + e) // 2

            if matrix[mid][0] > target:
                e = mid - 1
            elif matrix[mid][-1] < target:
                s = mid + 1
            else:
                return self.searchRow(matrix[mid], target)

        return False

    def searchRow(self, row, target):
        if not row:
            return False

        s = 0
        e = len(row) - 1    
        
        while s <= e:
            mid = (s + e) // 2

            if row[mid] < target:
                s = mid + 1
            elif row[mid] > target:
                e = mid - 1
            elif row[mid] == target:
                return True
        
        return False

     
