'''Given a Graph, check if a path exist between two nodes'''

#sample graph implementation

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['E'],
         'D': [],
         'E': ['F'],
         'F': []}

#just checks if the path is possible or not
def bfs(start,goal):
    open_ls=[]
    closed=[]
    open_ls.append(start)
       
    while(True):
        try:
            curr_node=open_ls.pop(0)
            if curr_node==goal:
                return True
            succesors=graph[curr_node]
            for item in succesors:
                if item not in closed:
                    open_ls.append(item)
            closed.append(curr_node)
        
        except:
            return False      
        


#modification of the above, also returns the path if possible
def bfs(start,goal):
    open_ls=[]
    closed=[]
    open_ls.append([start])
    
    while(True):
        try:
            curr_node=open_ls.pop(0)
            if curr_node[-1]==goal:
                return curr_node
            succesors=graph[curr_node[-1]]
            for item in succesors:
                if item not in closed:
                    open_ls.append(curr_node+[item])
            closed.append(curr_node[-1])
        
        except:
            return False      
        
