from collections import defaultdict
import networkx as nx



graph = defaultdict(lambda: defaultdict(int))
def addEdge(graph,u,v,x):
    graph[u][v]= x
def addvertice(graph,u):
    graph[u]=defaultdict(int)


    
def desenhabellmanford(graph,p):
    G1=nx.DiGraph()
    i=0
    for node in p:
        if(i>0):
            n=p[node]
            G1.add_edge(n,node,weight=graph[n][node])
        i+=1
    weight =nx.get_edge_attributes(G1,'weight')  
    pos=nx.circular_layout(G1)
    nx.draw(G1, pos,with_labels=True)
    nx.draw_networkx_edge_labels(G1,pos,edge_labels=weight)     
   



def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p



addEdge(graph,'a','b',-1)
addEdge(graph,'a','c',4)

addEdge(graph,'b','c',3)
addEdge(graph,'b','d',2)
addEdge(graph,'b','e',2)

addvertice(graph,'c')

addEdge(graph,'d','b',1)
addEdge(graph,'d','c',5)

addEdge(graph,'e','d',1)



q='a'
d, p = bellman_ford(graph, q)
desenhabellmanford(graph,p)
y=0
for x in d:
    print("custo de",q," para ",x," e =",d[x
