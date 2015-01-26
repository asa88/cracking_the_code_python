'''
You have given a binary search tree. Using this tree make a sorted doubly linked list 
using the elements of binary tree.

(this should be done in place. That means once you are done with procedure your tree should destroy 
and it should be converted to the doubly linked list of course sorted )
'''


'''Sol: Use modified inOrder traversal to generate doubly linked list in-place'''

# Class for Node
class Node:
    def __init__(self,data):
        self.data=data # store data
        self.next=None # point to next node
        self.prev=None # point to previous node

# Class for a doubly linked list
class LinkedList():
    #constructor creates the sentinal code
    def __init__(self):
        self.sentinal=Node(None)
        self.sentinal.prev=self.sentinal
        self.sentinal.next=self.sentinal
        
    # Return a reference to the first node in the list, if there is one.
    # If the list is empty, return None.
    def first_node(self):
        if self.sentinal.next==self.sentinal:
            return None
        else:
            return self.sentinal.next
 
    # Insert a new node with data after node x.
    def insert_after(self, x, data):
        newNode=Node(data) # assign data to node
        
        temp=x.next #create a temp var
        x.next=newNode # assign new node between x and temp
        newNode.next=temp 
        newNode.prev=x
        temp.prev=newNode
        
        return
    
    # Insert a new node at the end of the list.    
    def append(self,data):        
        last_node=self.sentinal.prev # get the last node
        
        self.insert_after(last_node,data) #call insert_after to append
        return
    # list with a sentinel, just as if it were a Python list.
    def __str__(self):
        node=self.sentinal
        s="["
        while (node.next!=self.sentinal):
            s=s+str(node.data)
            node=node.next
            if (node.next!=self.sentinal):
                s=s+ ","
        s=s+"]"
        return s


class TreeNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
class BinarySearchTree:
   
    def __init__(self):
        self.rootNode=TreeNode(None)
        self.lList=LinkedList()
        
    def insert_inTree(self,node,data):
        if data < node.data :
            if node.left:
                self.insert_inTree(node.left,data)
            else:
                node.left=TreeNode(data)
        else:
            if node.right:
                self.insert_inTree(node.right,data)
            else:
                node.right=TreeNode(data)
    
    def insert(self,data):
        if self.rootNode.data!=None:
            self.insert_inTree(self.rootNode,data)
        else:
            self.rootNode.data=data
        return
    def inOrder_traversal(self,node):
        if node != None:
            self.inOrder_traversal(node.left)
            self.lList.append(node.data)
            self.inOrder_traversal(node.right)
        return
           
    def inOrder(self):
        node=self.rootNode
        self.inOrder_traversal(node)
        return
       return
    def printL(self):
        return self.lList.__str__()
   
bTree = BinarySearchTree()
bTree.insert(5)
bTree.insert(2)
bTree.insert(7)
bTree.insert(9)
bTree.insert(3)
bTree.insert(1)
bTree.insert(10)
bTree.insert(8)
bTree.insert(6)
bTree.insert(11)
bTree.inOrder()
bTree.printL()  #print doubly link list 
