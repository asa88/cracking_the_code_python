''' design a stack to push pop and min in O(1) time'''

import sys
class Stack:    
    def __init__(self):
        self.items=[]
        self.minS=[sys.maxint]
    def push(self,data):
        if data< self.minS[-1]:
            self.minS.append(data)
        return self.items.append(data)
    def pop(self):
        if self.items[-1]== self.minS[-1]:
            self.minS.pop()
        return self.items.pop()
    def minValue(self):
        return self.minS[-1]
    def peek(self):
        if len(self.items)==0:
            return None
        else:
            return self.items[-1] 

