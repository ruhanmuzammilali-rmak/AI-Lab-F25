# lab 4
import heapq
def astar(graph, h,start ,goal):
    pq=[(h[start],0,start,[start])]; best={start:0}
    while pq:
        f,g,node,path=heapq.heappop(pq)
        if node==goal: return g,path
        if g!=best[node]: continue
        for nxt,w in graph.get(node,[]):
            ng=g+w
            if ng < best.get(nxt,float("inf")):
                best[nxt]=ng
                heapq.heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))
g={"S":[("A",1),("B",4)],
   "A":[("C",2)],
   "B":[("G",5)],
   "C":[("G",3)],
   "G":[]}
h={"S":5,
   "A":4,
   "B":4,
   "C":2,
   "G":0}
print(astar(g,h,"S","G"))
h0={"S":0,
"A":0,
"B":0,
"C":0,
"G":0}
 
def run(graph,h ,start ,goal):
    pq=[(h[start],0,start,[start])]; best={start:0}

    trace=[]; step=[];expand=[]; stale=0
    while pq:
        f, g,node ,path= heapq.heappop(pq)
        if g!= best[node]:
            stale+= 1
            continue
        trace.append(node)
        step.append((node ,g ,h[node],f))
        if node ==goal: return path,g, trace, step, expand, stale
        expand.append(node)
        for nxt,w in graph.get(node,[]):
            ng =g+w
            if ng < best.get(nxt,float("inf")):
                best[nxt]=ng
                heapq.heappush(pq, (ng+h[nxt], ng, nxt, path+[nxt]))
    return [],float("inf"),trace, step ,expand ,stale
def pathCost(path):
    total=0
    for i in range(len(path)-1):
        for nxt,w in g[path[i]]:
            if nxt== path[i+1]: total=total+w
    return total
def showResult(title,hh):
    path,cost, trace, step, expand, stale=run(g,hh,"S","G")
    print("\n"+title)
    print("path:"," -> ".join(path))

    print("return cost:",cost)
    print("calculat path cost:",pathCost(path))
    print("process node:",trace)
    print("node detail:")
    for node, gg,hn ,f in step:
        print(f"{node}: g={gg}, h={hn}, f={f}")
    print("expand node:",expand)
    print("expansion count:",len(expand))
    print("stale entries skip:",stale)
    return path,cost,expand
trueCost={}
for node in g:
    trueCost[node]=run(g,h0,node,"G")[1]
def showFrontier(pq):
    if len(pq)==0: return "empty"
    item=[]
    for f,gg, node,path in sorted(pq):
        item.append(f"{node} (g={gg}, h={h[node]}, f={f})")
    return ", ".join(item)
def task1():
    print("\nTASK 1: first three expansion")
    pq=[(h["S"],0,"S",["S"])]; best={"S":0}
    for step in range(1,4):
        print(f"\nexpansion {step}")

        print("frontier before:",showFrontier(pq))
        f,gg,node,path=heapq.heappop(pq)
        print("selected node:",node)
        print("g = ",gg,"h = ",h[node],"f = ",f)
        print("frontier after removing:",showFrontier(pq))
        for nxt,w in g[node]:
            ng=gg+w
            nf=ng+h[nxt]
            print(f"{nxt}: g = {gg} + {w} = {ng}, f = {ng} + {h[nxt]} = {nf}")
            if ng < best.get(nxt,float("inf")):
                best[nxt]=ng
                heapq.heappush(pq,(nf,ng,nxt,path+[nxt]))
        print("frontier now:",showFrontier(pq))
        if len(pq)>0: print("next node:",sorted(pq)[0][2])
def audit():
    print("\nheuristic audit")
    print("true remaining costs:",trueCost)
    print("\nadmissibility check:")
    for node in h:
        print(f"{node}: {h[node]} <= {trueCost[node]} : {h[node]<=trueCost[node]}")
    print("\ncheck consistency:")
    for u in g:
        for v,w in g[u]:
            print(f"{u}->{v}: {h[u]} <= {w} + {h[v]} = {w+h[v]} : {h[u]<=w+h[v]}")
# a* vs ucs
def task2():
    print("\nTASK 2: A* VS UCS")
    showResult("A* Search",h)
    showResult("UCS Search",h0)
    print("\nthe goal is process but the goal is not count as expand.")
# task 3
def task3():
    print("\nTASK 3: overestimated heuristic")
    h2=h.copy()
    h2["C"]=10
    print("original h(C):",h["C"])
    print("modified h(C):",h2["C"])
    print("true remaining cost of C:",trueCost["C"])
    print("admissible after change:",h2["C"]<=trueCost["C"])
    p1,c1,e1=showResult("original heuristic",h)
    p2,c2,e2=showResult("modified heuristic",h2)
    print("\ncomparison")
    print("path changed:",p1!=p2)
    print("cost changed:",c1!=c2)
    print("expansion count changed:",len(e1)!=len(e2))
    print("original path and cost:",p1,c1)
    print("modified path and cost:",p2,c2)
    h3=h.copy()
    h3["C"]=4
    p3,c3,e3=showResult("Extra test: h(C) = 4",h3)
    print("\ndid the extra test change the path?",p3!=p1)
task1()
audit()
task2()
task3()
# extra test
print("\nextra test")
print("start and goal same:",astar(g,h,"S","S"))
print("goal can't be reached:",run(g,h,"G","S")[0])
