class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def size(self):
        return len(self.queue)



my_queue = Queue()

my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(15)

print(my_queue.dequeue())  # Output: 5
print(my_queue.dequeue())  # Output: 10
print(my_queue.is_empty())  # Output: False
print(my_queue.dequeue())  # Output: 15
print(my_queue.is_empty())  # Output: True
print(my_queue.peek())  # Output: None
print(my_queue.size())  # Output: 0
