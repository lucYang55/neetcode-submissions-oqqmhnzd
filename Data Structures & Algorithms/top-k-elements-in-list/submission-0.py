class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = dict()
        for num in nums:
            if num in map1:
                map1[num] += 1
            else:
                map1[num] = 1
        
        sorted_items = sorted(map1.items(), key=lambda x: x[1], reverse=True)

        result = [key for key, value in sorted_items[:k]]
        
        return result
