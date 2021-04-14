import sys
r=sys.stdin.readline
N=int(r())
M=int(r())
conn=[[]]
for _ in range(N):
    conn.append([0]+list(map(int,r().split())))
plan=list(map(int,r().split()))

parents=list(range(N+1))
def find(N):
    if parents[N]==N:
        return N
    else:
        tmp=find(parents[N])
        parents[N]=tmp
        return parents[N]
def union(X,Y):
    X,Y=find(X),find(Y)
    if X==Y:
        return
    else:
        if X>Y:
            parents[Y]=X
        else:
            parents[X]=Y
for i in range(1,N+1):
    for j in range(i,N+1):
        if conn[i][j]==1:
            union(i,j)
ans=True
for i,x in enumerate(plan):
    if i==0:
        cur=x
    else:
        if find(cur)!=find(x):
            ans=False
            break
print("YES" if ans else "NO")