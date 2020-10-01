import sys
from collections import deque
r=sys.stdin.readline
N,M,T=map(int,r().split())
onepan=[[]]
for _ in range(N):
    onepan.append(deque(map(int,r().split())))
def calc():#원판에 써있는값의 총합 평균을 위한 숫자갯수를 반환
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
    record=set()#한번에 업데이트하기위한 set
    if d==0:#시계방향
        for i in range(x,N+1,x):
            onepan[i].rotate(k)#deque의 rotate를 통해 원판을 돌림
    else:
        for i in range(x,N+1,x):
            onepan[i].rotate(-k)
    for i in range(1,len(onepan)):#숫자를 맞추기 위해 1부터 원판의 갯수만큼
        for j in range(M):
            if onepan[i][j]!='':#지워진 숫자는 제외하고
                if onepan[i][(j+1)%M]==onepan[i][j]:       #왼쪽 오른쪽을 기록
                    record.update([(i,j),(i,(j+1)%M)])
                if onepan[i][j-1]==onepan[i][j]:
                    record.update([(i,j),(i,j-1)])
                if i==1 and onepan[i][j]==onepan[i+1][j]:   #가장 안쪽 원판일때
                    record.update([(i,j),(i+1,j)])
                elif i==len(onepan) and onepan[i][j]==onepan[i-1][j]:#바깥쪽
                    record.update([(i,j),(i-1,j)])
                elif i!=1 and i!=N:                         #중간원판의 경우
                    if onepan[i][j]==onepan[i+1][j]:        #안쪽 바깥쪽 기록
                        record.update([(i,j),(i+1,j)])
                    if onepan[i][j]==onepan[i-1][j]:
                        record.update([(i,j),(i-1,j)])
    if len(record)==0:#기록이 없는경우
        cnt,acc=calc()#평균값을 계산해옴
        if cnt==0:      #업데이트할게 없는경우
            continue
        aver=acc/cnt#실수로 계산
        for i in range(1,len(onepan)):
            for j in range(M):
                if onepan[i][j]!='':
                    if onepan[i][j]>aver:
                        onepan[i][j]-=1
                    elif onepan[i][j]<aver:
                        onepan[i][j]+=1
    for x,y in record:#기록이 있을때
        onepan[x][y]=''#공백처리해줘서 지움
print(calc()[1])#T번의 수행후 sum을 출력
