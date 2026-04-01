class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSortHelper(nums, 0, len(nums) - 1)
        return nums
    
    def quickSortHelper(self, arr: List[int], lo, hi) -> None:
        if lo >= hi:
            return

        mid = (lo + hi) // 2
        if arr[lo] > arr[mid]:
            arr[lo], arr[mid] = arr[mid], arr[lo]
        if arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[mid] > arr[hi]:
            arr[mid], arr[hi] = arr[hi], arr[mid]

        left = lo
        pivot = hi

        for curr in range(left, pivot):
            if arr[curr] < arr[pivot]:
                arr[left], arr[curr] = arr[curr], arr[left]
                left += 1

        arr[left], arr[pivot] = arr[pivot], arr[left]


        self.quickSortHelper(arr, lo, left - 1)
        self.quickSortHelper(arr, left + 1, hi)

