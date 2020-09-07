class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, ):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        if not self.head:
            return None
        
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value

        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        return current_head.value


    def remove_tail(self):
        if not self.tail:
            return None

        if self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return current_tail.value

        new_tail = self.head
        while new_tail.next != None:
            if new_tail.next == self.tail:
                break
            new_tail = new_tail.next

        old_tail = self.tail
        new_tail.next = None
        self.tail = new_tail
        self.length -= 1
        return old_tail.value

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# # Array implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if self.size == 0:
#             return None

#         self.size -= 1
#         return self.storage.pop()

# LinkedList implementation
class Queue:
    def __init__(self):
        self.storage = LinkedList()
    
    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_head()
