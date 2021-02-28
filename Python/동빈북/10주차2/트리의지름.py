import sys
r=sys.stdin.readline
V=int(r())
tree=[dict() for _ in range(V+1)]
for _ in range(V):
    line=list(map(int,r().split()))
    target=line[0]
    line=line[1:-1]
    for i in range(len(line)//2):
        tree[target][line[i*2]]=line[i*2+1]
        tree[line[i*2]][target]=line[i*2+1]

leng=0
pole=0
visit=[False]*(V+1)
def dfs(V,Cur):
    global leng
    global pole
    visit[V]=True
    if leng<Cur:
        leng=Cur
        pole=V
    for Node,W in tree[V].items():
        if not visit[Node]:
            visit[Node]=True
            dfs(Node,Cur+W)

dfs(1,0)

leng=0
visit=[False]*(V+1)

dfs(pole,0)

print(leng)

    