class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0
my_stack = Stack()

my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

print(my_stack.pop())  # Output: 15
print(my_stack.pop())  # Output: 10
print(my_stack.isEmpty())  # Output: False
print(my_stack.pop())  # Output: 5
print(my_stack.isEmpty())  # Output: True
