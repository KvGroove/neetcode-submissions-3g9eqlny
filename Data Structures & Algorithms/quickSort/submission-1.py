# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], lo, hi) -> None:
        if lo >= hi:
            return
        
        pivot = hi
        left = lo
        curr = left

        while curr < pivot:
            if pairs[curr].key < pairs[pivot].key:
                pairs[curr], pairs[left] = pairs[left], pairs[curr]
                left += 1
            curr += 1

        # Swap `pivot` with `left`
        pairs[pivot], pairs[left] = pairs[left], pairs[pivot]

        self.quickSortHelper(pairs, lo, left - 1)
        self.quickSortHelper(pairs, left + 1, hi)