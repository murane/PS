import sys
r=sys.stdin.readline
teams=[]
N=int(r())
for _ in range(N):
    A,B,C,D,E=map(int,r().split())
    teams.append((A,B,C,D,E))
Fir,Sec=-1,-1
twoMax=0
for i in range(N-1):
    for j in range(i+1,N):
        cur=min([max(teams[i][x],teams[j][x]) for x in range(5)])
        if twoMax==0 or twoMax<cur:
            twoMax=cur
            Fir,Sec=i,j
ans=0
for k in range(N):
    if k in [Fir,Sec]: continue
    cur = min([max(teams[Fir][x],teams[Sec][x],teams[k][x]) for x in range(5)])
    ans=max(cur,ans)
print(ans)
        