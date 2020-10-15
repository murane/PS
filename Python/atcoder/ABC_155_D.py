import sys
from collections import defaultdict
r=sys.stdin.readline
N,K=map(int,r().split())
A=list(map(int,r().split()))
zero=[]
neg=[]
pos=[]
for a in range(A):
    if A<0:
        neg.append(a)
    elif A>0:
        pos.append(a)
    else:
        zero.append(a)
neg.sort()
pos.sort()
negCnt=len(neg)*len(pos)
zeroCnt=len(zero)*(len(neg)+len(pos))+len(zero)*(len(zero)-1)//2
posCnt=len(neg)*len(neg)+len(pos)*len(pos)
if K<=negCnt:#음수범위에 해당하는 경우

elif K<=negCnt+zeroCnt: #0인경우
    print(0)
else:#양수인경우