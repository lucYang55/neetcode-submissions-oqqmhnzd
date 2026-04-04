class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = dict()

        for i, num in enumerate(nums):
            comp = target - num
            if comp in map1:
                if map1[comp] < i:
                    return list([map1[comp], i])
                else:
                    return list([i, map1[comp]])
            else:
                map1[num] = i