from collections import defaultdict
import networkx as nx



graph = defaultdict(lambda: defaultdict(int))
def addEdge(graph,u,v,x):
    graph[u][v]= x
def addvertice(graph,u):
    graph[u]=defaultdict(int)


    
def desenhafloydwarshal(graph,p):
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
   

def floydwarshall(graph):

    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = 1000
            pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u

    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if (newdist < dist[u][v]):
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v] # route new path through t

    return dist, pred


g = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3: 9},
         3 : {},
         4 : {5:3},
         5 : {2: 7, 3:4}}



q='a'
d, p = floydwarshall(g)


print (d)
