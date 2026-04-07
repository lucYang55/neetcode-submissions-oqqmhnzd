class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ''
        for s in strs:
            newString += s + ';'
        print(newString)
        return newString

    
    def decode(self, s: str) -> List[str]:
        res = []
        newString = ''

        for c in s:
            if c != ';':
                newString += c 
            else:
                res.append(newString)
                newString = ''
                
        return res