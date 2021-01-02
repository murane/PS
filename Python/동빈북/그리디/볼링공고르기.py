import sys
r=sys.stdin.readline
N,M=map(int,r().split())
W=list(map(int,r().split()))
ans=0
for i in range(len(W)-1):
    for j in range(i+1,len(W)):
        if i!=j and W[i]!=W[j]:
            ans+=1
print(ans)