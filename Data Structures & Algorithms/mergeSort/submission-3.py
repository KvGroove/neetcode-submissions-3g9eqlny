class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def mergeSortHelper(self, pairs: List[Pair], lo, hi) -> None:
        if lo >= hi:
            return

        mid = (lo + hi) // 2

        self.mergeSortHelper(pairs, lo, mid)
        self.mergeSortHelper(pairs, mid + 1, hi)


        self.merge(pairs, lo, mid, hi)

    def merge(self, pairs, lo, mid, hi):
        i, j = lo, mid + 1
        tmp = []

        while i <= mid and j <= hi:
            if pairs[i].key <= pairs[j].key: 
                tmp.append(pairs[i])
                i += 1
            else:
                tmp.append(pairs[j])
                j += 1
        
        if i <= mid:
            tmp.extend(pairs[i:mid + 1])
        if j <= hi:
            tmp.extend(pairs[j:hi + 1])

        pairs[lo:hi + 1] = tmp