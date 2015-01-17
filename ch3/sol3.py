import sys
class Stack:    
    thresh=5
    curr_idx=0
    def __init__(self):
        self.items=[[]]
    def push(self,data):
        if len(self.items[Stack.curr_idx])==Stack.thresh:
            Stack.curr_idx+=1  
            self.items.append([])
        return self.items[Stack.curr_idx].append(data)
    def pop(self):
        if len(self.items[Stack.curr_idx])==0:
            del self.items[Stack.curr_idx]
            Stack.curr_idx-=1
            
        return self.items[Stack.curr_idx].pop()
    def popAt(self,idx):
        return self.items[idx].pop()
    def set_thresh(self,val):
        Stack.thresh=val
        return 
    def peek(self):
        if len(self.items)==0:
            return None
        else:
            return self.items[-1] 
    def printS(self):
        print self.items

newS=Stack()
newS.push(5)
newS.push(3)
newS.push(7)
newS.push(2)
newS.push(9)
newS.push(1)  

newS.printS() 
