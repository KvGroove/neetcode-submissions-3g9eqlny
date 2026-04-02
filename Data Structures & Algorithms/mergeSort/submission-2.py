# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def mergeSortHelper(self, pairs: List[Pair], lo, hi) -> None:
        if lo >= hi:
            return

        mid = (lo + hi) // 2

        self.mergeSortHelper(pairs, lo, mid)
        self.mergeSortHelper(pairs, mid + 1, hi)

        left = pairs[lo: mid + 1]
        right = pairs[mid + 1: hi + 1]

        self.merge(pairs, left, right, lo)

    def merge(self, arr, left, right, lo):
        i, j, k = 0, 0, lo

        lenL = len(left)
        lenR = len(right)
        while i < lenL and j < lenR:
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i >= lenL and j < lenR:
            arr[k] = right[j]
            j += 1
            k += 1

        while j >= lenR and i < lenL:
            arr[k] = left[i]
            i += 1
            k += 1
