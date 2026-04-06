class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = dict()

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        
        i = 0
        for i in range(k):
            max_key = max(hashmap, key=hashmap.get)
            res.append(max_key)
            hashmap.pop(max_key)
            
        return res