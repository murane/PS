import sys,copy
r=sys.stdin.readline
fish=[[] for _ in range(17)]
g=[[-1]*4 for _ in range(4)]
d=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
ans=[]
for i in range(4):
    tmp=[]
    line=list(map(int,r().split()))
    for j in range(4):
        #a->물고기번호 1~16번 b->방향 인덱스
        a,b=line[2*j],line[2*j+1]
        g[i][j]=a
        fish[a]=[b-1,i,j]

def move(num,g,fish,cx,cy):
    def swap(num1,num2,nx,ny):
        if num2!=0:
            d1,i1,j1=fish[num1]
            d2,i2,j2=fish[num2]
            g[i2][j2]=num1
            g[i1][j1]=num2
            fish[num1]=[d1,i2,j2]
            fish[num2]=[d2,i1,j1]
        else:
            d1,i1,j1=fish[num1]
            g[i1][j1]=0
            g[nx][ny]=num1
            fish[num1][1]=nx
            fish[num1][2]=ny

    if fish[num]==0:
        return
    for _ in range(9):
        x,y=fish[num][1],fish[num][2]
        nx,ny=x+d[fish[num][0]][0],y+d[fish[num][0]][1]
        if not 0<=nx<4 or not 0<=ny<4 or (nx,ny)==(cx,cy):
            fish[num][0] = (fish[num][0]+1)%8
            continue
        targetNum=g[nx][ny]
        swap(num,targetNum,nx,ny)
        return

x,y,di=0,0,fish[g[0][0]][0]
number=g[0][0]
fish[number]=0
g[0][0]=0

def solve(g,fish,curFeed,x,y,dire):
    def getEatableFishs():
        tmp=[]
        tmpx,tmpy=x,y
        while True:
            nx,ny=tmpx+d[dire][0],tmpy+d[dire][1]
            if not 0<=nx<4 or not 0<=ny<4: break
            if g[nx][ny]!=0:
                tmp.append((nx,ny))
                tmpx,tmpy=nx,ny
            else:break
        return tmp
    lst=getEatableFishs()
    if not lst:
        ans.append(curFeed)
        return
    for i in range(1,17):
        move(i,g,fish,x,y)
    for tx,ty in lst:
        targetNum=g[tx][ty]
        g[tx][ty]=0
        td=fish[targetNum][0]
        fish[targetNum]=0
        gg=copy.deepcopy(g)
        ffish=copy.deepcopy(fish)
        solve(gg,ffish,curFeed+targetNum,tx,ty,td)
        g[tx][ty]=targetNum
        fish[targetNum]=[td,tx,ty]

solve(g,fish,number,x,y,di)
    
print(max(ans))