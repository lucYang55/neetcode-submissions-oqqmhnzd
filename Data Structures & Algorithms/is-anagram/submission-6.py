class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = dict()

        if len(s) != len(t):
            return False 

        for i in s:
            if i in map1:
                map1[i] += 1 
            else:
                map1[i] = 1 
    
        for j in t:
            if j in map1:
                map1[j] -= 1 
            else:
                return False

            if map1[j] < 0:
                return False

        print(map1)
        
        return True
                

        
        

                