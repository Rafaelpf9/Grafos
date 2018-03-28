'''quick find '''
ids=[]

def quickFind(n):
    for i in range (0, n, 1):
        ids.append(i)
       
def find(p, q):
    return ids[p] == ids[q]

def union(p, q):
    idp = ids[p]
    for i in range (0, len(ids)-1, 1):
        if(ids[i] == idp):
            ids[i] = ids[q]
        
quickFind (10)
print (ids)
union (2, 5)
print (ids)
union (1, 6)
print (ids)
union (7, 1)
print (ids)
union (7, 2)
print (ids)
print (find(7,2))
