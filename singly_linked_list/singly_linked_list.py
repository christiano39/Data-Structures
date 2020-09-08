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
        while new_tail.next != self.tail:
            new_tail = new_tail.next

        old_tail = self.tail
        new_tail.next = None
        self.tail = new_tail
        self.length -= 1
        return old_tail.value
        

        
