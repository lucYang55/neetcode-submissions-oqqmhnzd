class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = dict()
        map2 = dict()

        if len(s) != len(t):
            return False 

        for i in s:
            if i in map1:
                map1[i] += 1 
            else:
                map1[i] = 1 
    
        for j in t:
            if j in map2:
                map2[j] += 1 
            else:
                map2[j] = 1 
        
        if map1 == map2:
            return True

        return False
                
        

                