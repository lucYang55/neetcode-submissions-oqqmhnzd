class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = dict()

        for i, n in enumerate(nums):
            comp = target - n
            if comp in dic:
                if i < dic[comp]:
                    return [i, dic[comp]]
                else:
                    return [dic[comp], i]
            else:
                dic[n] = i
            