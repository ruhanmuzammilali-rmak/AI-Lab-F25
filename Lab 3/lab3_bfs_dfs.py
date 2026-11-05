from collections import deque
graph={"A":["B","C"],
       "B":["D","E"],
       "C":["F"],
       "D":[],
       "E":["G"],
       "F":[],
       "G":[]}
def bfs(start, goal):
    q=deque([(start,[start])]); seen={start}
    while q:
        node,path=q.popleft()
        if node==goal: return path
        for n in graph[node]:
            if n not in seen:
                seen.add(n); q.append((n,path+[n]))
def dfs(start, goal):
    stack=[(start,[start])]; seen=set()
    while stack:
        node,path=stack.pop()
        if node==goal: return path
        if node in seen: continue
        seen.add(node)
        for n in reversed(graph[node]): stack.append((n,path+[n]))
print(bfs("A","G")); print(dfs("A","G"))

def bfs_trace(start, goal):
    q= deque([(start, [start])]); seen = {start}; order = []
    while q:
        node, path = q.popleft()
        order.append(node)
        print("processed:", node, "path:",path)
        if node == goal:
            print(f"bfs visit order is: {order}")
            return path
        for n in graph[node]:
            if n not in seen:
                seen.add(n); q.append((n, path+[n]))
        print("queue: ",[x[0] for x in q])
def dfs_trace(start, goal):
    stack = [(start, [start])]; seen = {start}; order = []
    while stack:
        node, path = stack.pop()
        if node in seen : continue
        order.append(node)
        print("processed:", node, "path:",path)
        if node ==goal:
            print(f"Dfs visit order is: {order}")
            return path
        seen.add(node)
        for n in reversed(goal,[node]): stack.append((n,path+[n]))
        print("stack",[x[0] for x in stack])
print("BFS tarce")
print(bfs_trace("A","G"))
print("DFS trace")
print(dfs_trace("A","G"))
print("start equals goal: ",bfs("A","A"),dfs("A","A"))
print("unreachable goal: ",bfs("G","A"),dfs("G","A"))
