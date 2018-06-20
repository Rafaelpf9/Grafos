from priodict import priorityDictionary
from collections import defaultdict
import networkx as nx

graph = defaultdict(lambda: defaultdict(int))
def addEdge(graph,u,v,x):
    graph[u][v]= x
def addvertice(graph,u):
    graph[u]=defaultdict(int)



def desenhabelldijkstra(graph,p):
    G1=nx.DiGraph()
    i=0
    for node in p:
            n=p[node]
            G1.add_edge(n,node,weight=graph[n][node])
    weight =nx.get_edge_attributes(G1,'weight')  
    pos=nx.circular_layout(G1)
    nx.draw(G1, pos,with_labels=True)
    nx.draw_networkx_edge_labels(G1,pos,edge_labels=weight)


def Dijkstra(G, start, end=None):

    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()  # estimated distances of non-final vertices
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        if v == end:
            break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


def shortestPath(G, start, end):
    """
    Find a single shortest path from the given start vertex to the given
    end vertex. The input has the same conventions as Dijkstra(). The
    output is a list of the vertices in order along the shortest path.
    """

    D, P = Dijkstra(G, start, end)
    Path = []
    while 1:
        Path.append(end)
        if end == start:
            break
        end = P[end]
    Path.reverse()
    return Path


addEdge(graph,'s','u',10)
addEdge(graph,'s','x',5)

addEdge(graph,'u','v',1)
addEdge(graph,'u','x',2)

addEdge(graph,'v','y',4)

addEdge(graph,'x','u',3)
addEdge(graph,'x','v',9)
addEdge(graph,'x','y',2)

addEdge(graph,'y','s',7)
addEdge(graph,'y','v',6)




A = {'s': {'u':10, 'x':5},
    'u': {'v':1, 'x':2},
    'v': {'y':4},
    'x':{'u':3,'v':9,'y':2},
    'y':{'s':7,'v':6}}

q='s'
d,p = Dijkstra(graph,q)
desenhabelldijkstra(graph,p)

for x in d:
    print("custo de",q," para ",x," e =",d[x])
