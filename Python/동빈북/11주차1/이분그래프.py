import sys
r=sys.stdin.readline
for _ in range(int(r())):
    V,E=map(int,r().split())
    g=[[]for _ in range(V+1)]
    for _ in range(E):
        a,b=map(int,r().split())
        g[a].append(b)
        g[b].append(a)
    ck=[0]*(V+1)

    def dfs(V):
        if ck[V]!=0:
            return True
        q=[]
        q.append(V)
        ck[V]=1
        while q:
            cur=q.pop()
            curCk=ck[cur]
            for nextNode in g[cur]:
                nxtCk=ck[nextNode]
                if nxtCk==curCk:
                    return False
                if nxtCk!=0 and nxtCk!=curCk: continue
                if nxtCk==0:
                    q.append(nextNode)
                    ck[nextNode]=-curCk
        return True
    flg=True
    for i in range(1,V+1):
        if not dfs(i):
            print("NO")
            flg^=True
            break
    if flg:
        print("YES")
