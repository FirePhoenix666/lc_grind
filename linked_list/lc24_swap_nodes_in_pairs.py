class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next


class SLL:
    def __init__(self) -> None:
        self.head = None
        
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
    def swapPairs(self, head):
        
        temp_node = head

        if temp_node is None:
            return head
        
        pointer1 = temp_node
        pointer2 = temp_node.next
        
        if pointer2 is None:
            return head
        
        while pointer2:
            pointer1.val, pointer2.val = pointer2.val, pointer1.val
            if pointer2.next is None:
                break
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next.next
        return head
    
    def print_list(self, head):
        current = head
        while current:  # Traverse the list
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
LList = SLL()
LList.insert(1)
LList.insert(2)
LList.insert(3)
LList.insert(4)
LList.insert(5)
print(LList)
head = LList.get()

Solution().swapPairs(head)
Solution().print_list(head)

# very hacky way of coding this problem
# strategy 1: two pointer
# strategy 2: recursion