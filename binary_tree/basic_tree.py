class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []  # Avoid mutable default argument

    def add_child(self, node):  # Use lowercase here
        self.children.append(node)

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Example tree setup
root = Node(data="root")
child1 = Node(data="child1")
child2 = Node(data="child2")

root.add_child(child1)
root.add_child(child2)

print(root)
