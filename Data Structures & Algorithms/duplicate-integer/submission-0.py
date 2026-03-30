class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        duplicate = set()
        for i in nums:
            if i not in check:
                check.add(i)
            else:
                duplicate.add(i)
        if len(duplicate) > 0:
            return True
        else:
            return False