import sys,math
from collections import defaultdict
r=sys.stdin.readline
R,C,T=map(int,r().split())
grid=[]
cl,rcl=(0,0),(0,0)
for i in range(R):
    line = list(map(int,r().split()))
    grid.append(line)
    if rcl==(0,0) and line[0]==-1:
        rcl=(i,0)
    elif rcl!=(0,0) and line[0]==-1:
        cl=(i,0)
dusts=defaultdict(int)
for i in range(R):
    for j in range(C):
        if grid[i][j]>0:
            dusts[(i,j)]=grid[i][j]
time=0
di=[(0,1),(1,0),(0,-1),(-1,0)]
def hwaksan():
    tmpDict=defaultdict(int)
    for coord,dust in dusts.items():
        x,y=coord
        cnt=0
        for dx,dy in di:
            nx,ny=x+dx,y+dy
            if dust//5==0:break
            if not 0<=nx<R or not 0<=ny<C:continue
            if grid[nx][ny]!=-1:
                tmpDict[(nx,ny)]+=dust//5
                cnt+=1 
        dusts[(x,y)]=dust-cnt*(dust//5)
        grid[x][y]=dust-cnt*(dust//5)
    for coord,dust in tmpDict.items():
        x,y=coord
        dusts[(x,y)]+=dust
        grid[x][y]=dusts[(x,y)]
def air(start,clock):
    coord=start
    cur=0
    curDi=0
    while True:
        x,y=coord
        if not 0<=x+clock[curDi][0]<R or not 0<=y+clock[curDi][1]<C:
            curDi+=1
        nx,ny=x+clock[curDi][0],y+clock[curDi][1]
        if (nx,ny)==start:
            break
        tmp=cur
        cur=grid[nx][ny]
        grid[nx][ny]=tmp
        dusts[(nx,ny)]=tmp
        coord=(nx,ny)

while time<T:
    hwaksan()
    air(cl,[(0,1),(1,0),(0,-1),(-1,0)])
    air(rcl,[(0,1),(-1,0),(0,-1),(1,0)])
    time+=1
print(sum([sum(x) for x in grid])+2)

