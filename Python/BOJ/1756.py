from collections import deque
import sys
r=sys.stdin.readline
D,N=list(map(int,r().split()))
tmp=list(map(int,r().split()))
doughs=list(map(int,r().split()))
oven=[]
for i in range(len(tmp)):
    if i==0:
        oven.append(tmp[i])
    else:
        if oven[i-1]>tmp[i]:
            oven.append(tmp[i])
        else:
            oven.append(oven[i-1])
pos=[]
for dough in doughs:
    if not oven:
        print("0")
        exit(0)
    else:
        while oven:
            if oven.pop()>=dough:
                pos.append(len(oven))
                break
print(pos[-1]+1)
                
