'''quick Union'''
ids=[]

def quickFind(n):
    for i in range (0, n, 1):
        ids.append(i)

def root(i):
    while(ids[i] != i):
        i = ids[i]
    return i

def find(p,q):
    return root(p) == root(q)

def union(p,q):
    ids[root(p)] = root(q)
    
quickFind(10)
union(2,8)
print(ids)
union(7,1)
print(ids)
union(9,2)
print(ids)
union(7,2)
print(ids)
print(find(7,2))
