"""
The Linked List contains five functions
"__init__" : initializes the linked list with a head
"append" : adds a new element to the linked list
"getPosition" : returns the element at the given position
"insert"  : adds an element to a particular spot on the linked list
"delete" : deletes the first element with the given value
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
            
    def getPosition(self, position):
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current.next and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        #return None
    
    def insert(self, newElement, position):
        current = self.head
        counter = 1
        if position == 1:
            newElement.next = self.head
            self.head = newElement
        elif position > 1:
            while current.next and counter < position:
                if counter == position - 1:
                    newElement.next = current.next
                    current.next = newElement
                current = current.next
                counter += 1
    
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if previous:
            previous.next = current.next
        else:
            self.head = current.next
            
# Test Cases
element1 = Element(1)
element2 = Element(2)
element3 = Element(3)
element4 = Element(4)

#print(element1, element2, element3, element4)

linkList = LinkedList(element1)
linkList.append(element2)
linkList.append(element3)

print(linkList.head.next.value)

linkList.insert(element4, 3)
print(linkList.getPosition(3).value)

linkList.delete(1)
print(linkList.getPosition(1).value)
print(linkList.getPosition(2).value)
