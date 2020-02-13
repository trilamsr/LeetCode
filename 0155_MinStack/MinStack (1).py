class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        if not self.stack: return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min: return None
        return self.min[-1]


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = [float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min.append(min(x, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        

