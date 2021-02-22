import sys
from collections import defaultdict
r=sys.stdin.readline
N,M,K=map(int,r().split())
grid=[]
for _ in range(N):
    grid.append(list(map(int,r().split())))
priority=[[]]
sharkDire=[0]+list(map(int,r().split()))
dire={1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
sharkDict={}

for i in range(N):
    for j in range(N):
        if grid[i][j]!=0:
            sharkDict[grid[i][j]]=(i,j)
for i in range(M):
    tmp=[[]]
    for j in range(1,5):
        tmp.append(list(map(int,r().split())))
    priority.append(tmp)

timeDict=[]
#smellDict=defaultdict(list)
smell=[[[0,0]]*N for _ in range(N)]
time=0

def getCoords(x,y):
    tmp=[]
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if not 0<=nx<N or not 0<=ny<N:continue
        tmp.append((nx,ny))
    return tmp
def smellCk(lst):
    tmp=set(lst)
    for x,y in lst:
        for k in smellDict.keys():
            if (x,y) in smellDict[k]:
                tmp.remove((x,y))
                break
    return list(tmp)
def move():
    for sharkNum,val in sharkDict.items():
        curX,curY=val
        
        lst=getCoords(curX,curY)
        noSmellLst=smellCk(lst)
        curDire=sharkDire[sharkNum]
        prioLst=priority[sharkNum][curDire]
        #냄새없는칸이 있을때
        if noSmellLst:
            for prioIdx in prioLst:
                nx,ny=curX+dire[prioIdx][0],curY+dire[prioIdx][1]
                if (nx,ny) in noSmellLst:
                    sharkDict[sharkNum]=(nx,ny)
                    sharkDire[sharkNum]=prioIdx
                    break
        #없을때
        else:
            for prioIdx in prioLst:
                nx,ny=curX+dire[prioIdx][0],curY+dire[prioIdx][1]

                if not 0<=nx<N or not 0<=ny<N:continue
                if (nx,ny) in lst and (nx,ny) in smellDict[sharkNum]:
                    sharkDict[sharkNum]=(nx,ny)
                    sharkDire[sharkNum]=prioIdx
                    break

#초기 세팅
tmp=[]
for k,v in sharkDict.items():
    smellDict[k].append(v)
    tmp.append((k,v))
timeDict.append(tmp)

while True:
    ckDict=defaultdict(list)
    #현재 시간에 따라 냄새 제거
    if time-K>=0:
        targetSmells=timeDict[time-K]
        for k,v in targetSmells:
            smellDict[k].remove(v)
    #모든상어 이동
    move()
    #냄새뿌리기
    tmp=[]
    time+=1

    for k,v in sharkDict.items():
        smellDict[k].append(v)
        tmp.append((k,v))
        ckDict[v].append(k)
        sharkDire[k]

    timeDict.append(tmp)
    #상어 제거
    for k,v in ckDict.items():
        if len(v)>1:
            v.sort()
            for i in range(1,len(v)):
                sharkDict.pop(v[i])
    
    #종료조건 확인
    if time>1000:
        print(-1)
        exit(0)
    if len(sharkDict)==1:break
print(time)