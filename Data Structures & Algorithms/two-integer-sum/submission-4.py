class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = dict()

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in map1:
                if map1[compliment] < i:
                    return [map1[compliment], i]
                return [i, map1[compliment]]
            map1[num] = i