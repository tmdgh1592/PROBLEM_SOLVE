class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []


    # input 1 2 3 4 5
    # output [] + 5 4 3 2 1
    def push(self, x: int) -> None:
        self.input.append(x)

    # 5 4 3 2 1
    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
                
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()