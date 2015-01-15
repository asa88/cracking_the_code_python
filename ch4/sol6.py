'''Find the inOrder successor in a Binary Search Tree, given a parent pointer '''

#Method 1: using parent pointer

def findSucessor(node, n):
    if n.right!=None:
        return minValue(n.right)
    #we would backtrack if n.right is None to find the next Node
    p =n.parent
    while(p!=None and p.right==n):
        n=p
        p=p.parent
    return p
    
    

def minValue(node):
    #In a BST leftmost node is the min value
    while node.left!=None:
        node=node.left
    return node.left

#Method 2: without using parent pointer

def get_successor(node,n):
    if n.right!=None:
        return minValue(n.right)
    succ=None
    while(node!=None):
        if (n.data< node.data ):
            succ=node.data
            node=node.left
        elif(n.data>node.data):
            node=node.right
        else:
            break
    return succ
        
