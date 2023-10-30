class MinStack:

    def __init__(self):
        self.list = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.list.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if self.minStack[-1] < val:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)

    def pop(self) -> None:
        self.list.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()