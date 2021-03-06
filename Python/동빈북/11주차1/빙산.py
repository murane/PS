import sys
r=sys.stdin.readline
N,M=map(int,r().split())
sea=[]
for _ in range(N):
    sea.append(list(map(int,r().split())))

iceberg=set()
for i in range(N):
    for j in range(M):
        if sea[i][j]!=0:
            iceberg.add((i,j))

def melt(iceberg):
    meltDict=dict()
    for x,y in iceberg:
        cnt=0
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if not 0<=nx<N or not 0<=ny<M: continue
            if sea[nx][ny]==0:cnt+=1
        meltDict[(x,y)]=cnt
    for k,v in meltDict.items():
        x,y=k
        sea[x][y]-=v
        if sea[x][y]<=0:
            sea[x][y]=0
            iceberg.remove((x,y))

def isSplited():
    visit=set()
    def dfs(x,y):
        visit.add((x,y))
        q=[]
        q.append((x,y))
        while q:
            x,y = q.pop()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if not 0<=nx<N or not 0<=ny<M: continue
                if (nx,ny) in visit: continue
                if (nx,ny) in iceberg:
                    visit.add((nx,ny))
                    q.append((nx,ny))
    cnt=0
    for x,y in iceberg:
        if (x,y) not in visit:
            dfs(x,y)
            cnt+=1
    return cnt>1 or cnt==0

year=0
while not isSplited():
    year+=1
    melt(iceberg)

if not iceberg:
    print(0)
    exit(0)
print(year)