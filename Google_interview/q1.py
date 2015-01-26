'''
You are given a 1D array of integers, such as: 
int[] array = [3,4,7,2,2,6,0,9]; 
Suppose you need to treat this array as a 2D table with a given number of rows. 
You want to sum the columns of the table. 
One value of numRows is 4..in that case the resultant array would look like
what if numRows==4? 
3 4 
7 2 
2 6 
0 9 
—- 
12 21

'''


''' O(n) solution '''
def split(A,numRows):
    row_sz=len(A)/numRows
    sum_val=[0 for i in range(0,row_sz)]
    
    col_num=0
    for i in range(0,len(A)):
        sum_val[col_num]+=A[i]
        col_num+=1
        if col_num==row_sz:
            col_num=0
            
    print sum_val
A=[3,4,7,2,2,6,0,9]
split(A,4)
