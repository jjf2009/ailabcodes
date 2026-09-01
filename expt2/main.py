from collections import deque

def bfs(a, s):
    visited = [False]*len(a)
    queue = deque([s])
    visited[s] = True
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for neighbour in a[u]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return order

def count_vertices(a,s,v):
    visited = [False]*len(a)
    order = []
    for neighbour in a[v]:
        if not visited[neighbour]:
            visited[neighbour] = True
            order.append(neighbour)
    return order

def ispath(a, s,d):
    visited = [False]*len(a)
    queue = deque([s])
    visited[s] = True
    order = []
    found = False
    while queue:
        u = queue.popleft()
        if u == d :
            found = True
            print(f"There Exits a path from {s} to {d}")
        order.append(u)
        
        for neighbour in a[u]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
   
    if(found==False):
        print(f"No Path exists from {s} to {d}")
        
def distance(a,s,b,c):
    visited = [False]*len(a)
    queue = deque([s])
    visited[s] = True
    while queue:
        u = queue.popleft()

        for neighbour in a[u]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return distance 


a = [[1,2],[2,0],[0,1,3,4],[2],[2]]
print("BFS traversal:", bfs(a, 0))
print("Count:",count_vertices(a,0,2))
ispath(a,0,2)
ispath(a,0,5)