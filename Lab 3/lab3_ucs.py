graph={"A":["B","C"],
       "B":["D","E"],
       "C":["F"],
       "D":[],
       "E":["G"],
       "F":[],
       "G":[]}
cost = {("A","B"):1,("A","C"):5,("B","D"):4,
        ("B","E"):1,("C","G"):7,("C","F"):2,("E","G"):1}
def bfs (start, goal):
    q = [(start, [start])]; seen = {start}
    while q:
        node, path = q.pop(0)
        if node == goal : return path
        for n in graph[node]:
            if n not in seen:
                seen.add(n); q.append((n,path+ [n]))
def ucs (start, goal):
    frontire = [(0, start,[start])]; explored = set(); order = []
    while frontire:
        best= frontire[0]
        for item in frontire:
            if item in frontire:
                if item[0] <best [0]: best = item
        frontire.remove(best)
        total, node , path = best
        if node in  order:continue
        order.append(node)
        if node ==goal:
            return "FOUND",path,total,order
        for n in graph[node]:
            if n not in order:
                frontire.append((total+ cost[(node,n)],n,path+ [n]))
    return "FAILUER", None,None , order
def path_cost(path):
    total = 0
    for i in range (len(path)-1):
        total = total+ cost[(path[i],path[i+ 1])]
    return total
print("UCS")
status, path, total,order = ucs("A","G")
print(status, path, "Cost", total,"hope", len(path)-1)
print(f"Processing order: {order}")
print("Cost check again: ", path_cost(path))
print("BFS")
b = bfs("A","G")
print(b, "cost", path_cost(b),"hope", len(b)-1)
print("Start equal goal: ", ucs("A","A"))
print("Unreachable goal: ", ucs("G","A"))
graph= {"A":["B"],
        "B":["A","C"],
        "C":[]}
cost = {("A","B"):1,
        ("B","A"):1,
        ("B","C"):2}
print("cycle, goal not in graph: ",ucs("A","Z"))
print("cycle, goal, C: ", ucs("A", "C"))
