'''Check if a Binary tree is Binary Search Tree'''

#There are number of solutions to this problem. Here Method 2 and 3 provide solutions efficient in both space and time

'''Method 1: This is enefficent as for each node we compute max and min value for left and right subtree '''
import sys
def check_BST(node):
    if node==None:
        return True
    if (node.left!=None and maxValue(node.left)>node.data):
        return False
    if (node.right!=None and minValue(node.right)<node.data):
        return False
    if check_BST(node.left) and check_BST(node.right):
        return True
    return False

def maxValue(node):
    if node==None:
        return -sys.maxint-1
    return max(node.data,maxValue(node.left),maxValue(node.right))

def minValue(node):
    if node==None:
        return sys.maxint
    return min(node.data,maxValue(node.left),maxValue(node.right))

print check_BST(Btree.root)
Btree.inOrder()

'''Method 2: Using InOrder traversal, if Binary Tree is a BST the array should be sorted
		the space optimization can be done by just tracking previous and current data value 
   O(n) time and O(1) space '''

def isBST2(tree, lastNode=[prev]): 
    if tree is None: 
        return True   
   
    if not isBST2(tree.left, lastNode):
        return False 
    if tree.data < lastNode[0]: 
        return False   
    
    lastNode[0]=tree.data   
   
    return isBST2(tree.right, lastNode)
prev=-sys.maxint-1
print isBST2(Btree.root)


''' Method 3: check all conditions O(n) time O(1) space'''

minVal=-sys.maxint-1
maxVal=sys.maxint
def isValid(node):
     return isValidBST(node, minVal,maxVal)

def isValidBST(node, minV, maxV):
     if(node == None):
         return True
     if(node.data > minV 
        and node.data < maxV
        and isValidBST(node.left, minV, min(node.data,maxV))
        and isValidBST(node.right, max(node.data,minV), maxV)):
         return True
     else :
         return False;

print isValid(Btree.root)
