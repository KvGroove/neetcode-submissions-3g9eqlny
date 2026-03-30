class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        pop_val = self.stack.pop()
        if pop_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# if __name__ == "__main__":
#     # Dry Run 1:
#     minStack = MinStack()

#     minStack.push(3)
#     # self.stack = [3]
#     # self.min_stack = [3]

#     minStack.push(2)
#     # self.stack = [3,2]
#     # self.min_stack = [3,2]

#     minStack.push(1)
#     # self.stack = [3,2,1]
#     # self.min_stack = [3,2,1]

#     minStack.push(2)
#     # self.stack = [3,2,1,2]
#     # self.min_stack = [3,2,1]


#     minStack.push(1)
#     # self.stack = [3,2,1,2,1]
#     # self.min_stack = [3,2,1,1]


#     minStack.pop()
#     # self.stack = [3,2,1,2]; pop_val = 1
#     # self.min_stack = [3,2,1,1]
#     # if pop_val == min_stack[-1], self.min_stack = [3,2,1]

#     minStack.pop()
#     # self.stack = [3,2,1]; pop_val = 2
#     # self.min_stack = [3,2,1]
#     # if pop_val == min_stack[-1], self.min_stack = [3,2,1]

#     minStack.getMin()
#     # return 1