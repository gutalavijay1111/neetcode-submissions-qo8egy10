class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)

    def pop(self) -> None:
        if self.s:
            self.s.pop()

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def getMin(self) -> int:
        min_found = float('inf')
        for val in self.s:
            if val < min_found:
                min_found = val
        return min_found
