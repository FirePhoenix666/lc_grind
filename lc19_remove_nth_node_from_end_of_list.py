class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node

    def __str__(self) -> str:
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.val)
            if temp_node.next:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    def get(self):
        return self.head
        

class Solution:
    def removeNthFromEnd(self, head, n: int):

        if head is None:
            return None
        
        length = 0
        temp_node = head  
        
        while temp_node:
            length+=1
            temp_node = temp_node.next
        
        if n > length:
            return head
        
        reverse_n = length - n + 1 
        
        if reverse_n == 1:
            head = head.next
        else:
            temp_node_2 = head
            pointer = 1
            while pointer<reverse_n-1: 
                # we wanna stop at node before the node we want to remove
                # if we do pointer< reverse_n: if now pointer pointing at 1
                # the node to be delete is at two, the pointer is at where it should be 
                # but 1<2 so it will go into while loop another time
                temp_node_2 = temp_node_2.next
                pointer+=1
            if temp_node_2.next.next is None:
                temp_node_2.next = None
            else:
                temp_node_2.next = temp_node_2.next.next
        return head
    
    def print_list(self, head):
        current = head
        while current:  # Traverse the list
            print(current.val, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list
                
               


SLL = LinkedList()
SLL.insert_at_end(1)
SLL.insert_at_end(2)
# SLL.insert_at_end(3)
# SLL.insert_at_end(4)
print(SLL)
head = SLL.get()
# SLL.insert_at_end(5)
Solution().print_list(head)
Solution().removeNthFromEnd(head, 1)
Solution().print_list(head)

# strategy 1: like above
# strategy 2: two pointers
# we can have first pointer (loop pointer or fast pointer) traverse thru the list
# then the second slow pointer keep a distance that is n away
# once the fast pointer reached final node, then the slow pointer will be at length -n which length -n+1 is the one to remove.   