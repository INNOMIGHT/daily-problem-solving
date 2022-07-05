from msilib.schema import Binary


class BinaryTree:

    def __init__(self, root):

        self.root = root
        self.left = self.right = None
    
    def add_left(self, val):
        if self.left is None:
            new_node = BinaryTree(val)
            self.left = new_node
        else:
            t = BinaryTree(val)
            t.left = self.left
            self.left = t.left
    
    def add_right(self, val):
        if self.right is None:
            new_node = BinaryTree(val)
            self.right = new_node
        else:
            t = BinaryTree(val)
            t.right = self.right
            self.right = t.right
    
    def preorder_traversal(self, node):
        if self.root is not None:
            print(self.preorder_traversal(self.left))
            print(node)
            print(self.preorder_traversal(self.right))


new_tree = BinaryTree(10)
new_tree.add_left(11)
new_tree.add_left(12)
new_tree.add_left(13)
new_tree.add_right(14)
new_tree.add_right(15)
new_tree.add_right(16)

new_tree.preorder_traversal(new_tree)