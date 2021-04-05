import sys
from collections import deque
r=sys.stdin.readline
N,M,T=map(int,r().split())
onepan=[[]]
for _ in range(N):
    onepan.append(deque(map(int,r().split())))
def calc():
    acc=0
    cnt=0
    for i in range(1,len(onepan)):
        for j in range(M):
            if onepan[i][j]!='':
                acc+=onepan[i][j]
                cnt+=1
    return cnt,acc
for _ in range(T):
    x,d,k=map(int,r().split())
    record=set()
    if d==0:#시계방향
        for i in range(x,N+1,x):
            onepan[i].rotate(k)
    else:
        for i in range(x,N+1,x):
            onepan[i].rotate(-k)
    for i in range(1,len(onepan)):
        for j in range(M):
            if onepan[i][j]!='':
                if onepan[i][(j+1)%M]==onepan[i][j]:
                    record.update([(i,j),(i,(j+1)%M)])
                if onepan[i][j-1]==onepan[i][j]:
                    record.update([(i,j),(i,j-1)])
                if i==1 and onepan[i][j]==onepan[i+1][j]:
                    record.update([(i,j),(i+1,j)])
                elif i==len(onepan) and onepan[i][j]==onepan[i-1][j]:
                    record.update([(i,j),(i-1,j)])
                elif i!=1 and i!=N:
                    if onepan[i][j]==onepan[i+1][j]:
                        record.update([(i,j),(i+1,j)])
                    if onepan[i][j]==onepan[i-1][j]:
                        record.update([(i,j),(i-1,j)])
    if len(record)==0:
        cnt,acc=calc()
        if cnt==0:
            continue
        aver=acc/cnt
        for i in range(1,len(onepan)):
            for j in range(M):
                if onepan[i][j]!='':
                    if onepan[i][j]>aver:
                        onepan[i][j]-=1
                    elif onepan[i][j]<aver:
                        onepan[i][j]+=1
    for x,y in record:
        onepan[x][y]=''
print(calc()[1])
