from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.append(val)

    def dequeues(self):
        return self.container.popleft()

    def peek(self):
        return self.container[-1]

    def iEempty(self):
        return len(self.container) == 0

    def sizeOfStack(self):
        return len(self.container)

    def printEle(self):
        for ele in self.container:
            print(ele)

