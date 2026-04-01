import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSortHelper(nums, 0, len(nums) - 1)
        return nums
    
    def quickSortHelper(self, arr: List[int], lo, hi) -> None:
        if lo >= hi:
            return


        rand_ele = random.randint(lo,hi)
        arr[rand_ele], arr[hi] = arr[hi], arr[rand_ele]

        left = lo
        pivot = hi

        for curr in range(left, pivot):
            if arr[curr] < arr[pivot]:
                arr[left], arr[curr] = arr[curr], arr[left]
                left += 1

        arr[left], arr[pivot] = arr[pivot], arr[left]


        self.quickSortHelper(arr, lo, left - 1)
        self.quickSortHelper(arr, left + 1, hi)

