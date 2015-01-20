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

def configs(row,UsedCol):
    if row==7:
        for col in range(0,8):
            if isValid(UsedCol,row,col):  
                UsedCol[row]=col
        if UsedCol[row]!=None:
            for i in range(0,8):
                print(i,UsedCol[i]),
            print
    
        return 
    else:
        for col in range(0,8):
            if isValid(UsedCol,row,col):
                UsedCol[row]=col
                configs(row+1,UsedCol)
                UsedCol[row]=None
                

configs(0,[None]*8)   
