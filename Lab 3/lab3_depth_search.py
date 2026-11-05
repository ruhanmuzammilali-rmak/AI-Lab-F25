graph={"A":["B","C"],
       "B":["D","E"],
       "C":["F"],
       "D":[],
       "E":["G"],
       "F":[],
       "G":[]}
def dls (node, goal, limit, path):
    if node == goal: return "FOUND",path
    if limit == 0:
        if len(graph[node]) > 0 : return "CUTOFF",None
        else: return "FALIURE",None
    cutoff = False
    for n in graph[node]:
        if n in path:
            continue
        status, results = dls(n, goal , limit -1, path+ [n])
        if status == "FOUND": return status, results
        if status == "CUTOFF": cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None
def iddfs(start, goal, max_depth):
    for limit in range(0, max_depth +1):
        status, path = dls(start, goal, limit, [start])
        print(f"limit {limit} -> {status} {path}")
        if status == "FOUND":
            return status, path, limit
        return status, path, max_depth
print("DLS")
for limit in [1,2,3,4]:
    status, path = dls("A","G",limit,["A"])
    print(f"limit {limit} status {status} path {path}")
print()
print("IDDFS")
for max_depth in [1,2,3,4]:
    print(f"max depth {max_depth}")
    status, path , last = iddfs("A","G" ,max_depth)
    print(f"result {status}, path {path} last limit try {last}")
    