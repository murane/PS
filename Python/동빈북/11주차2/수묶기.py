import sys
from collections import deque
r=sys.stdin.readline
seq=[]
for _ in range(int(r())):
    seq.append(int(r()))
#10000개..

seq.sort()
pos = [x for x in seq if x>0]
zero = [x for x in seq if x==0]
neg = [x for x in seq if x<0]
ans=0
def calc(lst):
    tmp=0
    for i in range(len(lst)//2):
        if lst[i*2]*lst[i*2+1]>lst[i*2]+lst[i*2+1]:
            tmp+=(lst[i*2]*lst[i*2+1])
        else:
            tmp+=(lst[i*2]+lst[i*2+1])
    return tmp
if len(pos)%2==0:
    ans+=calc(pos)
else:
    ans+=(calc(pos[1:])+pos[0])
if len(neg)%2==0:
    ans+=calc(neg)
else:
    ans+=calc(neg[:-1])
    if len(zero)==0:
        ans+=neg[-1]

print(ans)