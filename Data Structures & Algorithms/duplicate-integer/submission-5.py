class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set(nums)

        if len(l) == len(nums):
            return False 
        return True
