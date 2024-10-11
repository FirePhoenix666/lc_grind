class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_start(self, value):
        new_node = Node(value=value, next=None)
        current = self.head
        if current is None:
            self.head = new_node
        else:
            new_node.next = current
            self.head = new_node
    
    def insert_at_tail(self, value):
        new_node = Node(value=value, next=None)
        current = self.head
        if current is None:
            self.head = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node
                
    def __str__(self) -> str:
        current = self.head
        result = ""
        if current is not None:
            result = ""
            while current:
                result += str(current.value) + "->"
                current = current.next
        result += str("None")
        return result
    
    def get_head(self):
        return self.head
    
class Solution:
    def reverseBetween(self, head, left, right):

        if left >= right:
            return head
        
        temp_list = LinkedList()

        current = head
        idx = 1
        while idx<= right:
            if idx>=left:
                temp_list.insert_at_start(current.val)
            current = current.next
            idx+=1
        tail = current
        
        count_ = 1 
        current, start = head
        while current and count_+1<left:
            current = current.next
            count_+=1
        
        new_head = temp_list.get_head()
        new_head.next = tail
        current.next = new_head
        return start

def modify(head, val):
    current = head
    count_ = 1
    while current:
        if count_ == 2:
            current.value = 100
        else:
            current = current.next
        count_+=1
    return head

def print_(head):
    current = head
    result = ""
    if current is not None:
        result = ""
        while current:
            result += str(current.value) + "->"
            current = current.next
    result += str("None")
    print(result)
    

SLL = LinkedList()
SLL.insert_at_start(1)
SLL.insert_at_tail(2)
SLL.insert_at_tail(3)
SLL.insert_at_tail(4)
SLL.insert_at_tail(5)

head = SLL.get_head()
modified_head = modify(head, 2)
print_(modified_head)
# print(SLL)