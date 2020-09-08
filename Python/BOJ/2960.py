import sys
r=sys.stdin.readline
N,K=list(map(int,r().split()))
tb=[0,0]+[1]*(N-1)
k=0
for i in range(2,N+1):
    if tb[i]==0:
        continue
    for j in range(i,N+1,i):
        if tb[j]==0:
            continue
        k+=1
        tb[j]=0
        if k==K:
            print(j)