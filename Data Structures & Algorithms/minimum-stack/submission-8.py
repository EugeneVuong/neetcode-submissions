class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currentMin = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.currentMin is None or val < self.currentMin:
            self.currentMin = val
        self.minStack.append(self.currentMin) 
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        print(self.minStack)
        if self.minStack == []:
            self.currentMin = None
        else:
            self.currentMin = self.minStack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
