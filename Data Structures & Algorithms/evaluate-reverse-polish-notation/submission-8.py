class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0

        stack = []

        for t in tokens:
            print(stack)
            if stack and t == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif stack and t == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif stack and t == "/":
                a = stack.pop()
                b = stack.pop()
                res = b / a
                stack.append(int(res))
            elif stack and t == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]
