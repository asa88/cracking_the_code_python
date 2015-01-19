'''generate n possible valid pairs of parenthsis'''

def parenthsis(leftRem,RightRem,string):
    if RightRem==0:
        print string
        return
    if leftRem>0:
        parenthsis(leftRem-1,RightRem,string+"(")
        if leftRem < RightRem:
            parenthsis(leftRem,RightRem-1,string+")")
    else:
        parenthsis(leftRem,RightRem-1,string+")")

print parenthsis(3,3,"")
