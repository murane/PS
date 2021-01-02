import sys
r=sys.stdin.readline
N,M=map(int,r().split())
MOD=10**9+7
friend=list(range(N))
group_cnt=N
def find(x):
    if friend[x]==x:
        return x
    friend[x]=find(friend[x])
    return friend[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        friend[x]=y
for _ in range(M):
    x,y=map(int,r().split())
    if find(x)!=find(y):
        union(x,y)
        group_cnt-=1
    else:
        
