# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], s, e) -> None:
        # Base case
        if e <= s:
            return


        pivot = e
        left = s
        curr = s

        while curr < pivot:
            if pairs[curr].key < pairs[pivot].key:
                # swap left and curr
                tmp = pairs[left]
                pairs[left] = pairs[curr]
                pairs[curr] = tmp
                # increment left
                left += 1
            # increment curr
            curr += 1

        # Swap pivot and left
        tmp = pairs[left]
        pairs[left] = pairs[pivot]
        pairs[pivot] = tmp

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)
