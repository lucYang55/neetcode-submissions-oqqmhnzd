class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # save the index and the value 
        map1 = dict()

        for i, n in enumerate(nums):
            comp = target - n
            print(comp, "!!!")
            if comp in map1:
                if map1[comp] < i:
                    return list([map1[comp], i])
                else:
                    return list([i, map1[comp]])
            else:
                print(map1)
                map1[n] = i
            

        