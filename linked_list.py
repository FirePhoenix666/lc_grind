class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # the existing last node now point to new node
            self.tail = new_node # tail pointer point to new node
        self.length += 1

    def insert_at_start(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, location, value):
        new_node = Node(value)
        temp_node = self.head
        if self.head is None:
            self.insert_at_start(value)
        elif location == 0:
            self.insert_at_start(value)
        else:
            index = 0
            while index < location-1: # insert at location so stop at location-2
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
        return False

    def __str__(self) -> str:
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " -> "
            temp_node = temp_node.next
        return result
    
SLL =LinkedList()
SLL.insert_at_end(10)
SLL.insert_at_end(20)
SLL.insert_at_end(30)
SLL.insert_at_end(40)
print(SLL)