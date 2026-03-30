# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, s = 0, e = len(pairs) - 1)
        return pairs
        
    def mergeSortHelper(self, pairs: List[Pair], s, e):
        if e - s + 1 <= 1:
            return

        m = (s + e) // 2
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

    def merge(self, pairs: List[Pair], s, m, e) -> None:
        L = pairs[s: m + 1]
        R = pairs[m + 1: e + 1]

        i = 0
        j = 0
        k = s
        lenL = len(L)
        lenR = len(R)

        while i < lenL and j < lenR:
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1
        
        while i < lenL:
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < lenR:
            pairs[k] = R[j]
            j += 1
            k += 1

