import sys
r=sys.stdin.readline
C,R=map(int,r().split())
grid=[[0]*C for _ in range(R)]
K=int(r())
curDi=0
curNum=1
di=[(1,0),(0,1),(-1,0),(0,-1)]
x,Nx,Ny,y=0,0,0,0
flg=False
while curNum<=C*R:
    if 0<=Nx<R and 0<=Ny<C and grid[Nx][Ny]==0:
        grid[Nx][Ny]=curNum
        if curNum==K:
            res=[Nx,Ny]
        flg=True
        x,y=Nx,Ny
    else:
        curDi=(curDi+1)%4
        flg=False
    if flg:
        curNum+=1
    Nx=x+di[curDi][0]
    Ny=y+di[curDi][1]
try:
    print(res[1]+1,res[0]+1)
except:
    print(0)
