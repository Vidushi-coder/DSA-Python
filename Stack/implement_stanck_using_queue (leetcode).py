class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

        # Rotate the previous elements
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop(0)

    def top(self) -> int:
        if not self.empty():
            return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

obj = MyStack()

obj.push(1)
print(obj.queue)

obj.push(2)
print(obj.queue)

print("Pop:", obj.pop())
print(obj.queue)

print("Top:", obj.top())
print("Empty:", obj.empty())

# OPTIMAL APPROACH

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        # Rotate previous elements
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

obj = MyStack()

obj.push(1)
print(obj.queue)

obj.push(2)
print(obj.queue)

print("Pop:", obj.pop())
print(obj.queue)

print("Top:", obj.top())
print("Empty:", obj.empty())