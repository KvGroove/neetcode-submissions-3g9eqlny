# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # Empty Case

        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    
    def quickSortHelper(self, pairs, lo, hi):
        # Base Case
        if lo >= hi:
            return
        
        left = lo
        curr = left

        while curr < hi:
            if pairs[curr].key < pairs[hi].key:
                pairs[left], pairs[curr] = pairs[curr], pairs[left]
                left += 1
            curr += 1
        
        pairs[left], pairs[hi] = pairs[hi], pairs[left]

        self.quickSortHelper(pairs, lo, left - 1)
        self.quickSortHelper(pairs, left + 1, hi)
