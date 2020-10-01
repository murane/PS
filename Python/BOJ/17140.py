import sys
from operator import itemgetter
from itertools import chain
from collections import deque,Counter
R=sys.stdin.readline
r,c,k=map(int,R().split())
r-=1
c-=1
matrix=[[0]*100 for _ in range(100)]
for i in range(3):
    x,y,z=map(int,R().split())
    matrix[i][:3]=[x,y,z]
row=3#행
col=3#열
time=0
if matrix[r][c]==k:#시작부터 끝
    print(time)
    exit(0)
while time<=100:#백번까지
    if row>=col:#R연산
        length=0
        for j in range(row):#각행별로
            counter=Counter()
            for i in range(col):
                if matrix[j][i]==0:#0은생략
                    continue
                counter[matrix[j][i]]+=1        #숫자별 빈도를 계산하기위해 counter에 입력
                matrix[j][i]=0                  #입력된값은 지움
            tmp=list(counter.items())           #list에 넣고 빈도->숫자 순으로 정렬
            tmp.sort(key=itemgetter(1,0))
            tmp=list(chain.from_iterable(tmp))  #chain을 통해 flat 해주고
            tmp=tmp[:100]                       #100으로 끊음
            length=max(length,len(tmp))         #길이는 기록
            for x in range(len(tmp)):
                matrix[j][x]=tmp[x]             #행을 기록한 tmp에서 재배치해준다
            #matrix[j]=tmp+matrix[j][len(tmp)+1:]
        col=length                              #저장해놓은 max길이로 col을 갱신
    else:#C연산
        length=0
        for i in range(col):
            counter=Counter()
            for j in range(row):
                if matrix[j][i]==0:
                    continue
                counter[matrix[j][i]]+=1
                matrix[j][i]=0
            tmp=list(counter.items())
            tmp.sort(key=itemgetter(1,0))
            tmp=list(chain.from_iterable(tmp))
            for x in range(len(tmp)):
                matrix[x][i]=tmp[x]
            length=max(length,len(tmp))
        row=length
    time+=1
    if matrix[r][c]==k:#종료조건
        print(time)
        exit(0)
print(-1)#100초과시