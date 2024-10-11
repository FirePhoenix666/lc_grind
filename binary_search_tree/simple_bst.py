class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert_node(self, node, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            if new_node.value <= node.value:
                if node.left is None:
                    node.left = new_node
                else:
                    self.insert_node(node.left, value)
            else:
                if node.right is None:
                    node.right = new_node
                else:
                    self.inser_node(node.right, data)



