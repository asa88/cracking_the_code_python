''' Create a Binary Search Tree, give a sorted list'''

#using Btree implementation from Btree.py
def build_BTree(A):
    if len(A)==0:
        return None
    
    M=(len(A)-1)/2
    node=Node(A[M])
    node.left=build_BTree(A[:M])
    node.right=build_BTree(A[M+1:])
    
    return node

Btree= BinaryTree()
A=[2,3,4,5,6,7,8,9,10,11]
x=build_BTree(A)
Btree.inOrder_traversal(x)

