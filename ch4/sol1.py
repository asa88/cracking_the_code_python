''' Write a function to check a Binary Tree is balanced ''''
'''basic BTree implementation structure from Btree.py is used'''

'''polynomial time algorithm O(n^2): for every node the check_height method is called, so a skewed tree
might lead to worse case performance O(n^2)'''
def balanced(node):
    if node==None:
        return True
    height_diff=calc_height(node.left)-calc_height(node.right)
    if abs(height_diff)>1:
        return False
    else:
        return balanced(node.left) and balanced(node.right)
def calc_height(node):
    if node==None:
        return 0
    left_h=calc_height(node.left)
    right_h=calc_height(node.right)
    
    return 1+ max(left_h,right_h)

''' O(n) algorithm: integrate height calcualtion and balance check in one'''

def check_balanced(node):
    if node==None:
        return 0
    left_h=check_balanced(node.left)
    if left_h ==-1:
        return -1
    right_h=check_balanced(node.right)
    if right_h==-1:
        return -1 
    if abs(left_h-right_h)>1:
        return -1
    else:
       return 1+max(left_h,right_h)


#calc_height(Btree.root)
check_balanced(Btree.root)
balanced(Btree.root)
