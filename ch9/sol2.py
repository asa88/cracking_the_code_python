'''9.2 robot question '''





def Ways(x,y,p):
    if x==0 and y==0:
        return 1
    elif x<0 or y<0 #or !isFree(x,y): #assume isFree checks if that location is blocked or not
        return 
    elif p.has_key((x,y)):
        return p[(x,y)]
    else:
        p[(x,y)]= Ways(x-1,y,p)+Ways(x,y-1,p)
        return p(x,y)


path={}
Ways(5,5,path)
