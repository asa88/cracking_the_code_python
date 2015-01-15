''' FInd the lowest common ancestor, given two nodes in a binary tree'''


#Method 1: No parent pointer given

'''Without a parent pointer'''
def find_lca(node,p,q):
    if node== None:
        return None
    if node.data==p or node.data==q:
        return node.data
    left_s=find_lca(node.left,p,q)
    right_s=find_lca(node.right,p,q)
    
    if left_s and right_s:
        return node.data
    if left_s:
        return left_s
    else:
        return right_s


#Method 2: Using parent pointer 


'''With a parent pointer'''
def find_lcaP(node,p,q):
    d1=getDepth(p)
    d2=getDepth(q)
    iter1=p
    iter2=q
    if d1>d2:
        while(d1!=d2):
            iter1=iter1.parent
            d1-=1
    else:
        while(d1!=d2):
            iter2=iter2.parent
            d2-=1
            
    while (iter1.data!=iter2.data):
        iter1=iter1.parent
        iter2=iter2.parent
    return iter1.data
        
