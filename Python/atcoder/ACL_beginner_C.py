import sys
r=sys.stdin.readline
N,M=map(int,r().split())
city=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,r().split())
    city[a].append(b)
    city[b].append(a)
check=[True]+[False]*(N)
def dfs(v):
    stack=[v]
    while stack:
        cur=stack.pop()
        check[cur]=True
        for v in city[cur]:
            if not check[v]:
                stack.append(v)
cnt=0
for i in range(1,N+1):
    if not check[i]:
        dfs(i)
        cnt+=1
print(cnt-1)