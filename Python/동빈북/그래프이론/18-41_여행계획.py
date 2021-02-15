import sys
r=sys.stdin.readline
N,M=map(int,r().split())
g=[]
for _ in range(N):
    line=list(map(int,r().split()))
    g.append(line)
plan=list(map(int,r().split()))
def find(lst,X):
    if lst[X]==X:
        return X
    lst[X]=find(lst,lst[X])
    return lst[X]
def union(lst,X,Y):
    X=find(lst,X)
    Y=find(lst,Y)
    if X==Y:
        return
    if X>Y:
        lst[X]=Y
    else:
        lst[Y]=X
parent=list(range(N))
for i in range(N):
    for j in range(N):
        if g[i][j]==1:
            union(parent,i,j)
ans=[]
for i in range(1,len(plan)):
    if find(parent,plan[0]-1)==find(parent,plan[i]-1):
        continue
    else:
        print("NO")
        exit(0)
print("YES")