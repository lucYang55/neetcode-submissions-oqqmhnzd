class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = dict()

        if len(s) != len(t):
            return False

        for char in s:
            if char in check:
                check[char] += 1
            else:
                check[char] = 1
        
        for char in t:
            if char in check:
                check[char] -= 1
            else:
                return False
            if check[char] < 0:
                return False
        
        return True

        

        


        