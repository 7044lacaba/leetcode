class MinStack:

    def __init__(self):
        self.list = []
        
    def push(self, val: int) -> None:
        self.list.append(val)

    def pop(self) -> None:
        self.list.pop(-1)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        current = self.list[0]
        for item in self.list:
            if item < current:
                current = item
        return current



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()