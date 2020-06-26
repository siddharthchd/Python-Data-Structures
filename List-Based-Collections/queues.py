class Queue:

    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, newElement):
        self.storage.append(newElement)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)


# setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# test peek
print(q.peek())

# test dequeue
print(q.dequeue())

# test enqueue
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
print(q.peek())
