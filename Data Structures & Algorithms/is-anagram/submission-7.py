class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = dict() 

        if len(s) != len(t):
            return False

        for let in s:
            if let in map1:
                map1[let] += 1
            else:
                map1[let] = 1

        for let in t:
            if let in map1:
                map1[let] -= 1
            else:
                return False

            if map1[let] < 0:
                return False

        return True