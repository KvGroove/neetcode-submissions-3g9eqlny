# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # Handle empty edge case
        if not pairs:
            return pairs

        self.mergeSortHelper(pairs, 0, len(pairs) - 1)

        return pairs
        
    def mergeSortHelper(self, pairs, lo, hi):
        # Base case
        if lo >= hi:
            return

        mid = (lo + hi) // 2

        self.mergeSortHelper(pairs, lo, mid)
        self.mergeSortHelper(pairs, mid + 1, hi)

        self.merge(pairs, lo, mid, hi)


    def merge(self, pairs, lo, mid, hi):
        left_array = pairs[lo:mid + 1]
        right_array = pairs[mid + 1:hi + 1]

        i = 0
        j = 0
        k = lo
        len_left = len(left_array)
        len_right = len(right_array)

        while i < len_left and j < len_right:
            if left_array[i].key <= right_array[j].key:
                pairs[k] = left_array[i]
                i += 1
            else:
                pairs[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len_left:
            pairs[k] = left_array[i]
            i += 1
            k += 1
        while j < len_right:
            pairs[k] = right_array[j]
            j += 1
            k += 1