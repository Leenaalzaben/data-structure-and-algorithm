class MaxStack:
    def __init__(self):
        self.stack = []  
        self.max_stack = []  

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def getMax(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]
stack = MaxStack()

stack.push(55)
stack.push(30)
stack.push(8)
stack.push(20)

print(stack.getMax()) 


