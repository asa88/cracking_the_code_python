''' solution to problem 9.1'''


''' Recursive Solution O(3^N)'''
def countWays(n,map_n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return countWays(n-1)+countWays(n-2)+ countWays(n-3)
    
'''Dynamic Programming O(N)'''

def countWays(n,map_n):
    if n<0:
        return 0
    elif n==0:
        return 1
    elif map_n[n]:
        return map_n[n]
    else:
        map_n[n]=countWays(n-1,map_n)+countWays(n-2,map_n)+ countWays(n-3,map_n)
        return map_n[n]


val=4
map_n=[None]*(val+1)
countWays(val,map_n)
