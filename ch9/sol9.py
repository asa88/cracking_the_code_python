''' placing 8queens on 8 x8 board sol 9'''
def isValid(UsedCol,row,col):
    valid=True
    for prevRow in range(0,row):
        prevCol=UsedCol[prevRow]
        if abs(col-prevCol)==(row-prevRow) :
            valid=False
    if col in UsedCol:
        valid=False
    return valid

def configs(row,UsedCol,N):
    if row==N-1:
        for col in range(0,N):
            if isValid(UsedCol,row,col):  
                UsedCol[row]=col
                print UsedCol
        return
    
    else:
        for col in range(0,N):
            if isValid(UsedCol,row,col):
                newCol=deepcopy(UsedCol)
                newCol[row]=col
                configs(row+1,newCol,N)
                
results=[]
N=8
configs(0,[None]*N,N)                    
    
