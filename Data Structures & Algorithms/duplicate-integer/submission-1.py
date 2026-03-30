class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        duplicate = set()
        for i in nums:
            if i not in check:
                check.add(i)
            else:
                return True
        return False