class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
    
    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
    
    def preorder_traversal(self,)
        if not self.root:
            return
        print(root.data)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def inorder_traversal(self,)
        if not self.root:
            return
        self.inorder_traversal(root.left)
        print(root.data)
        self.inorder_traversal(root.right)

    def postorder_traversal(self,)
        if not self.root:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data)

    def levelorder_traversal(self,)
        if not self.root:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
