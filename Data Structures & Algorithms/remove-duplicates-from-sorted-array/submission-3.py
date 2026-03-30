class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = sorted(set(nums))
        nums[:len(duplicates)] = duplicates

        return len(duplicates)