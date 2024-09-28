class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def insert(self, val):
        new_node = Node(val, next=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node

    def get(self):
        return self.head
    
    def __str__(self) -> str:
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.val)
            if temp_node.next:
                result += " -> "
            temp_node = temp_node.next
        return result
    
class Solution:
    def __init__(self, list1, list2) -> None:
        self.list1 = list1
        self.list2 = list2

    def mergeTwoLists(self):
        current1 = self.list1
        current2 = self.list2

        if current1 is None and current2 is None:
            return None 
        elif current1 is None:
            return current2
        elif current2 is None:
            return current1
        else:
            while current2:
                if current2.val <= current1.val:
                    temp = current2
                    current2 = current2.next
                    temp.next = current1
                    current1 = temp
                else:
                    pointer = current1
                    while pointer.next and current2.val > pointer.next.val:
                        pointer = pointer.next
                    temp = current2
                    temp.next = pointer.next
                    pointer.next = temp
                current2 = current2.next
        return current1

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
    
SLL1 = LinkedList()
SLL1.insert(1)
SLL1.insert(2)
SLL1.insert(3)
SLL2 = LinkedList()
SLL2.insert(1)
SLL2.insert(3)
SLL2.insert(4)
print(SLL1)
print(SLL2)
sll1 = SLL1.get()
sll2 = SLL2.get()
sol = Solution(sll1, sll2).mergeTwoLists()
print_list(sol)

