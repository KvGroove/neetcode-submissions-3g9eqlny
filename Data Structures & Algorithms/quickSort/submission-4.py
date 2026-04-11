# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair], s=None, e=None) -> List[Pair]:
        if s is None:
            s, e = 0, len(pairs) - 1

        if e - s + 1 <= 1:
            return pairs
        
        left = s
        pivot = pairs[e]

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSort(pairs, s, left - 1)
        self.quickSort(pairs, left + 1, e)

        return pairs
