class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = dict()

        if len(s) != len(t):
            return False

        for l in s:
            if l in hash1:
                hash1[l] += 1
            else:
                hash1[l] = 1

        for l in t:
            if l in hash1:
                hash1[l] -= 1
            else:
                return False
            if hash1[l] < 0:
                return False
        
        return True
    