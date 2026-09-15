class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()

        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Typical test case
stack = MinStack()

stack.push(-2)
stack.push(0)
stack.push(-3)

print("Typical test case:", stack.getMin())

stack.pop()

print("Top after pop:", stack.top())
print("Minimum after pop:", stack.getMin())


# Edge case
stack = MinStack()

stack.push(5)

print("Edge case:", stack.getMin())