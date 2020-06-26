"""
"insertFirst" : insert new element as the head of the stack
"deleteFirst" : delete the first from the stack
"push" :  push a new element onto the top of stack
"pop" : pop the first element off the top of the stack 
"""

"""

This is a Linked List implementation of Stack
Stacks can be implemented using a list as it comes built in with python but the
append method traverses the entire list to add a new element costing linear time

"""

class Element(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    
    def __init__(self, head = None):
        self.head = head

    def append(self, newElement):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newElement
        else:
            self.head = newElement

    def insertFirst(self, newElement):
        newElement.next = self.head
        self.head = newElement

    def deleteFirst(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

class Stack(object):
    
    def __init__(self, top = None):
        self.linklist = LinkedList(top)

    def push(self, newElement):
        self.linklist.insertFirst(newElement)

    def pop(self):
        return self.linklist.deleteFirst()

# Test cases
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

stack = Stack(e1)

stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)