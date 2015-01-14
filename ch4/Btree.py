'''Binary Tree Implementation'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=Node(None)
    def inOrder_traversal(self,node):
        if node!=None:
            self.inOrder_traversal(node.left)
            print node.data
            self.inOrder_traversal(node.right)
        
    def inOrder(self):
        node=self.root
        self.inOrder_traversal(node)


Btree= BinaryTree()
Btree.root.data=1
Btree.root.left=Node(2)
Btree.root.right=Node(3)
Btree.root.left.left=Node(4)
Btree.root.left.right=Node(5)
Btree.root.right.left=Node(6)
Btree.root.right.right=Node(7)
Btree.root.right.right.right=Node(10)
Btree.root.right.right.right.right=Node(11)
