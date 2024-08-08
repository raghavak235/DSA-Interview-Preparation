# stack implementation using the dynamic array/list in python is slower

stack=[
    'leetcode',
    'leetcode/123',
    'leetcode/456'
]
stack.pop()
print(stack)

from collections import deque
stack= deque()

stack=[
    'leetcode',
    'leetcode/123',
    'leetcode/456'
]
stack.pop()
print(stack)

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def iEempty(self):
        return len(self.container) == 0

    def sizeOfStack(self):
        return len(self.container )

    def printEle(self):
        for ele in self.container:
            print(ele)



def balanced_parenthesis(string):
        stack=[]
        bracket_mapping={"{":"}", "(":")", "[":"]"}
        open_bracket = set(['(', '{', '['])
        for str in string:
            if str in open_bracket:
                stack.append(str)

            # Closing bracket str and stack top open bracket - closing bracket [are they same]
            elif stack and str == bracket_mapping[stack[-1]]:
                stack.pop()


        if len(stack) ==0:
            print(True)
        else:
            print(False)


balanced_parenthesis('[{()}')