class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        return self.bstHelper(nums, target, 0, len(nums) - 1)

    def bstHelper(self, nums, target, s, e) -> int:
        if s > e:
            return -1
            
        mid = (s + e) // 2

        if nums[mid] < target:
            mid = self.bstHelper(nums, target, mid + 1, e)
        elif nums[mid] > target:
            mid = self.bstHelper(nums, target, s, mid - 1)
        
        if nums[mid] == target:
            return mid
        else:
            return -1


# nums = [-1,0,2,4,6,8], target = 4

# bstHelper(s = 0, e = 5)
# mid = 2, num[mid] = 2 < target
# s = 3, e = 5

# bstHelper(s = 3, e = 5) 
# mid = 4, num[mid] = 6 > target
# s = 3, e = 3

# bstHelper(s = 3, e = 3)
# mid = 3, num[3] = 4 == target
# return mid

