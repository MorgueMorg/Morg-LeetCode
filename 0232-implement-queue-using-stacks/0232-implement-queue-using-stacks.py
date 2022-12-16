class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        self.frontToBack()
        return self.front.pop()

    def peek(self) -> int:
        self.frontToBack()
        return self.front[-1]

    def empty(self) -> bool:
        return len(self.back) + len(self.front) == 0
    
    def frontToBack(self):
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()