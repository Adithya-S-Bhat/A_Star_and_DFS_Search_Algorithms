import heapq

#implementation of priority queue using list
"""
You can create any other helper funtions.
Do not modify the given functions
"""

"""class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def insert(self, vertex, cost,parent,s):
        if self.contains([vertex]):
            for i in range(len(self.queue)):
                if self.queue[i][0]==vertex:
                    index=i
                    break
            if cost<self.queue[index][1]:
                self.queue[index][1]=cost
                parent[vertex]=s
        else:
            self.queue.append([vertex,cost])
            parent[vertex]=s
  
    # for popping an element based on Priority
    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if (self.queue[i][1]) < (self.queue[min][1]):
                    min = i
                elif (self.queue[i][1]) == (self.queue[min][1]):
                    if self.queue[i][0] < self.queue[min][0]:
                        min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()
      
    def contains(self,goals):
        for i in range(len(self.queue)):
                if self.queue[i][0] in goals:
                        return 1
                        
        return 0"""

def pQcontains(pQ,vertex):
    for i in range(len(pQ)):
        if pQ[i][1]==vertex:
            return i
    return -1

def isEmpty(queue):
    return len(queue) == 0  

def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []
    # TODO
    explored=[]
    parent=[]
    for i in range(len(cost[0])):
        explored.append(0)
        parent.append(-1)
    pQ=[]
    heapq.heappush(pQ,[heuristic[start_point]+0,start_point])
    s=0

    while not isEmpty(pQ) and not s in goals:
        c,s=heapq.heappop(pQ)
        explored[s]=1
        currCost=c-heuristic[s]
        for i in range(1,len(cost[0])):
            if cost[s][i]!=0 and cost[s][i]!=-1:
                if not explored[i]:
                    totalCost=currCost+heuristic[i]+cost[s][i]
                    index=pQcontains(pQ,i)
                    if index>=0:
                        if (totalCost)<pQ[index][0]:
                            pQ[index][0]=totalCost
                            heapq.heapify(pQ)
                            parent[i]=s
                    else:
                        heapq.heappush(pQ,[totalCost,i])
                        parent[i]=s
    
    path=[]
    if s in goals:
        while s!=start_point:
            path.append(s)
            s=parent[s]
        path.append(start_point)
        path.reverse()
    return path


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    path = []
    # TODO
    explored=[]
    for i in range(len(cost[0])):
        explored.append(0)
    
    path=dfs(start_point,goals,cost,explored)
    return path

#recursive   
"""def dfs(start_point,goals,path,cost,explored):
        explored[start_point]=1
        path.append(start_point)
        if start_point in goals:
                return -1
        for i in range(1,len(cost[0])):
                if cost[start_point][i]!=0 and cost[start_point][i]!=-1 and not explored[i]:
                        j=dfs(i,goals,path,cost,explored)  
                        if j==-1:
                                return -1
        return 0"""

#iterative with parent
def dfs(start_point,goals,cost,explored):
    frontier = []#stack
    parent=[]
    for i in range(len(cost[0])):
        parent.append(-1)
 
    frontier.append(start_point)
    parent[start_point]=start_point

    while(len(frontier)):
        v=frontier[-1]
        frontier.pop()
        explored[v]=1

        if v in goals:
            break

        for i in range(len(cost[0])-1,0,-1):
            if cost[v][i]!=0 and cost[v][i]!=-1 and not explored[i]:
                frontier.append(i)
                parent[i]=v
    
    path=[]
    if v in goals:
        while v!=start_point:
            path.append(v)
            v=parent[v]
        path.append(start_point)
        path.reverse()
    return path

#iterative w/o parent
"""def dfs(start_point,goals,cost,explored):
    frontier = []#stack
    tempPath=[]
 
    frontier.append([start_point,0])
    explored[start_point]=1
    tempPath.append(start_point)

    while(len(frontier)):
        v=frontier[-1]
        if v[0] in goals: #if goal state is reached
            if v[0] in goals:
                return tempPath
        
        elif v[1]==len(cost[0]):#if all neighbours are explored,i.e,backtracking
            #explored[v[0]]=0
            tempPath.pop()
            frontier.pop()

        else:
            i=v[1]
            if cost[v[0]][i]!=0 and cost[v[0]][i]!=-1 and not explored[i]:
                frontier.append([i,0])
                explored[i]=1
                tempPath.append(i)
            v[1]=v[1]+1
    return tempPath"""