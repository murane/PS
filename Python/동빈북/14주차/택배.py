import sys
from collections import defaultdict,deque
r=sys.stdin.readline
N,C=map(int,r().split())
M=int(r())
boxLst=[]
for _ in range(M):
    send,receive,boxCnt=map(int,r().split())
    boxLst.append((send,receive,boxCnt))
boxLst.sort(key=lambda x:(x[0],x[1]))
boxQ=deque(boxLst)
tot=0
truck=defaultdict(int)
cur=0
for i in range(1,N+1):
    #내려놓을건 내려놓고
    if i in truck:
        tmp=truck.pop(i)
        tot+=tmp
        cur-=tmp
    #실을수 있는건 최대한 싣고
    while boxQ and i==boxQ[0][0]:
        send,rec,boxCnt=boxQ.popleft()
        if cur==C:
            continue
        else:
            can=C-cur
            if can >= boxCnt+cur:
                cur+=boxCnt
                truck[rec]+=boxCnt
            else:
                cur+=can
                truck[rec]+=can
print(tot)
            