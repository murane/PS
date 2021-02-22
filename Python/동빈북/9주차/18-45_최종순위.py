import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n=int(r())
    lastYear=list(map(int,r().split()))
    g=[[] for _ in range(n+1)]
    degree=[0]*(n+1)
    left=set(list(range(1,n+1)))
    for i in range(len(lastYear)):
        cur=lastYear[i]
        left.remove(cur)
        g[cur].extend(list(left))
        
    for _ in range(int(r())):
        a,b=map(int,r().split())
        if b in g[a]:
            g[a].remove(b)
            g[b].append(a)
        else:
            g[b].remove(a)
            g[a].append(b)
    
    ans=[]
    
    left=set(list(range(1,n+1)))
    for i in range(1,n+1):
        for j in g[i]:
            degree[j]+=1
    while len(ans)<n:
        q=[]
        for i in left:
            if degree[i]==0:
                q.append(i)
        #사이클이 있다는뜻
        if not q:
            print("IMPOSIIBLE")
            break
        if len(q)>1:
            print("?")
            break
        ans.append(q[0])
        left.remove(q[0])
        for x in g[q[0]]:
            degree[x]-=1
    if len(ans)==n:
        print(*ans)

