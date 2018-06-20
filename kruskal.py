import networkx as nx


vertices = []
arestas = set()
def addaresta(u,v,x):
    arestas.add((x,u,v))
def addvertice(u):
    vertices.append(u)






parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]: 
            rank[root2] += 1

def kruskal():
    for vertice in vertices:
        make_set(vertice)
        minimum_spanning_tree = set()
        edges = list(arestas)
        edges.sort()
	#print edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    
    return sorted(minimum_spanning_tree)




    
addvertice('a')
addvertice('b')
addvertice('c')
addvertice('d')
addvertice('e')
addvertice('f')
addvertice('g')
addvertice('h')
addvertice('i')


addaresta('a','b',4)
addaresta('b','c',8)
addaresta('d','c',7)
addaresta('d','e',9)
addaresta('e','f',10)
addaresta('f','g',2)
addaresta('g','h',1)
addaresta('a','h',8)

addaresta('h','i',7)

addaresta('g','i',6)
addaresta('f','c',4)
addaresta('f','d',14)
addaresta('i','c',2)
addaresta('b','h',11)


z=kruskal()

def desenhaKruskal():
    G1=nx.Graph()
    for s in z:
        G1.add_edge(s[2],s[1],weight=s[0])
  
    weight =nx.get_edge_attributes(G1,'weight')  
    pos=nx.circular_layout(G1)
    nx.draw(G1, pos,with_labels=True)
    nx.draw_networkx_edge_labels(G1,pos,edge_labels=weight)         

desenhaKruskal()
