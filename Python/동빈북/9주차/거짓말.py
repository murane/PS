import sys
r=sys.stdin.readline
N,M=map(int,r().split())
truth=list(map(int,r().split()))
truth=truth[1:]
ans=0
parent=list(range(N))
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
for i in range(len(truth)-1):
    union(parent,truth[i]-1,truth[i+1]-1)
partylst=[]
for _ in range(M):
    party=list(map(int,r().split()))
    party=party[1:]
    partylst.append(party)
    for i in range(1,len(party)):
        union(parent,party[0]-1,party[i]-1)
for party in partylst:
    flg=True
    for member in party:
        if truth and find(parent,member-1) == find(parent,truth[0]-1):
            flg=False
            break
    if flg:
        ans+=1
print(ans)