import sys
from itertools import permutations
r=sys.stdin.readline
N=int(r())
info=[]
for _ in range(N):
    info.append([-1]+list(map(int,r().split())))
p=[2,3,4,5,6,7,8,9]
ans=0
for order in permutations(p,8):
    idx=1
    point=0
    order=list(order)  
    order=order[:3]+[1]+order[3:]
    for inning in range(N):
        out=0
        b1,b2,b3=0,0,0
        while out<3:
            if info[inning][order[idx-1]]==1:
                point+=(b3)
                b1,b2,b3=1,b1,b2
            elif info[inning][order[idx-1]]==2:
                point+=(b3+b2)
                b1,b2,b3=0,1,b1
            elif info[inning][order[idx-1]]==3:
                point+=(b3+b2+b1)
                b1,b2,b3=0,0,1
            elif info[inning][order[idx-1]]==4:
                point+=(b3+b2+b1+1)
                b1,b2,b3=0,0,0
            else:
                out+=1
            idx=idx%9+1
        ans=max(ans,point)
print(ans)