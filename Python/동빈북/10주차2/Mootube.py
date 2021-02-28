import sys
r=sys.stdin.readline
N,Q=map(int,r().split())
g=[]
for _ in range(N-1):
    p,q,r=map(int,r().split())
    p,q=min(p,q),max(p,q)
    g.append((p,q,r))


    
for _ in range(Q):
    k,v=map(int,r().split())
