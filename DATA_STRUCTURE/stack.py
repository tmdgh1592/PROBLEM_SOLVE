class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        return item


stack = Stack()

for i in range(1, 6):
    stack.push(i)
for _ in range(5, 0, -1):
    print(stack.pop())