class Stack:
    def __init__(self):
        self.stack=[]
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the stack")
        else:
            return self.stack.pop()
AStack=Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
print(AStack.remove())
AStack.add("Thur")
print(AStack.peek())
print(AStack.peek())
print(AStack.remove())