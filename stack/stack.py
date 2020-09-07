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
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# # Array implementation
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.insert(0, value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None

#         self.size -= 1
#         return self.storage.pop(0)


# LinkedList implementation
class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()
