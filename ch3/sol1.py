''' How could you use a single array to implement a stack'''

class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        return self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if len(self.items)==0:
            return None
        else:
            return self.items[-1]


arry=[]
for i in range(0,3):
    arry.append(Stack())
