class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s: 
            if c in closeToOpen:
                print(c, "??")
                if stack and stack[-1] == closeToOpen[c]:
                    pop = stack.pop()
                    print(pop, "!")
                else:
                    return False
            else:
                stack.append(c)
                print(c)
        return True if not stack else False
