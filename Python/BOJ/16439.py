import sys
from itertools import combinations
r=sys.stdin.readline
ans=0
N,M=map(int,r().split())

member=[]
for _ in range(N):
    member.append(list(map(int,r().split())))

for comb in combinations(range(M),3):
    x,y,z=comb
    tmp=0
    for i in range(N):
        tmp+=max([member[i][j] for j in [x,y,z]])
    ans=max(ans,tmp)

print(ans)

