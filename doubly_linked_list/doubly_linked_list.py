"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if not self.head:
            new_head = ListNode(value, None, None)
            self.head = new_head
            self.tail = new_head
        else:
            new_head = ListNode(value, None, self.head)
            self.head.prev = new_head
            self.head = new_head
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        else:
            old_head = self.head
            new_head = self.head.next
            self.head = new_head
            new_head.prev = None
            self.length -= 1
            return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if not self.tail:
            new_tail = ListNode(value, None, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = ListNode(value, self.tail, None)
            self.tail.next = new_tail
            self.tail = new_tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        elif self.head == self.tail:
            old_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return old_tail.value
        else:
            old_tail = self.tail
            new_tail = self.tail.prev
            self.tail = new_tail
            new_tail.next = None
            self.length -= 1
            return old_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node != self.head and node != self.tail:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
        elif node == self.tail and node != self.head:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node


        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node != self.head and node != self.tail:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        elif node == self.head and node != self.tail:
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        elif node == self.head:
            new_head = node.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
        elif node == self.tail:
            new_tail = node.prev
            new_tail.next = None
            self.tail = new_tail
            self.length -= 1
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value
        node = self.head

        while node.next != None:
            if node.next.value > max_value:
                max_value = node.next.value
            node = node.next
        
        return max_value