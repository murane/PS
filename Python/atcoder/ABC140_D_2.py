import sys
from collections import defaultdict
r=sys.stdin.readline
N=int(r())
A=list(map(int,r().split()))
B=list(map(int,r().split()))
C=list(map(int,r().split()))

# i -> 1 ~ N
Adict=defaultdict(int)
Bdict=defaultdict(int)

for i in range(N):
    Adict[A[i]]+=1
    Bdict[B[C[i]-1]]+=1
ans=0
for k in Adict.keys():
    ans+=Adict[k]*Bdict[k]
print(ans)


