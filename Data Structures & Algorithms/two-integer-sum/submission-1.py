class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, n in enumerate(nums):
            comp = target - n 
            if comp in hashmap:
                    return [hashmap[comp], i] if hashmap[comp] < i else [i, hashmap[comp]]
            else:
                hashmap[n] = i

             
