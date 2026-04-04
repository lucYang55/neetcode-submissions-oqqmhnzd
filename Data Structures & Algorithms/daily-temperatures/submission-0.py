class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        # we append to the stack when there is a day
        # we loop throught until we see a bigger day and sub trat the index 

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
                print(stack)
            stack.append([t,i])
            print(stack)
        return res