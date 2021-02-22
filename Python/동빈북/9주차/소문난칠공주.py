import sys
r=sys.stdin.readline
ban=[]
for _ in range(5):
    ban.append(list(r().strip()))
visit=[[False]*5 for _ in range(5)]
ans=0

def solve(CurCnt,Scnt,x,y):
    global ans;
    if ban[x][y]=='S':
        Scnt+=1
    if 7-CurCnt+Scnt<4:
        return
    if CurCnt==7:
        if Scnt>=4:
            ans+=1
        return
    for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<5 and 0<=ny<5 and not visit[nx][ny]:
            visit[nx][ny]=True
            solve(CurCnt+1,Scnt,nx,ny)
            visit[nx][ny]=False


for i in range(5):
    for j in range(5):
        visit[i][j]=True
        solve(1,0,i,j)
        visit[i][j]=False
print(ans)

