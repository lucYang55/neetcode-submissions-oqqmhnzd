class MinStack:

    def __init__(self):
        self.stack = []       # main stack
        self.min_stack = []   # keeps track of minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
    
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
    
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]
