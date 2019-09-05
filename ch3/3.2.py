import sys
from collections import deque

# Stack implementation with min() functionality
class stack_w_min(deque):
    def __init__(self):
        self.min_stack = deque([sys.maxsize])
        super().__init__()
    def append(self, value):
        if value <= self.min_stack[-1]:
            self.min_stack.append(value)
        super().append(value)
        self._last = value
    def pop(self):
        if self._last == self.min_stack[-1]:
            self.min_stack.pop()
        popped = super().pop()
        self._last = super().pop()
        super().append(self._last)
        return popped
    def min(self):
        return self.min_stack[-1]

