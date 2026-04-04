class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i, n in enumerate(nums):
            comp = target - n
            if comp in hash_map:
                return [hash_map[comp], i]
            hash_map[n] = i
        