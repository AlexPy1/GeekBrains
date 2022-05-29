# Реализовать структуру данных стэк, который за О(1) выдает минимум в стэке:

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minstack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:
            return self.minstack[-1]

