import sys
def wall(num):
    res=[0,0,0,0]
    for i,n in enumerate(reversed(format(num,'b'))):
        if n=='1':
            res[i]=1
    return res
def dfs(x,y,roomNum):
    if check[x][y]!=-1: return False
    check[x][y]=roomNum
    global roomCnt
    roomCnt+=1
    for i in range(4):
        Nx,Ny=x+dx[i],y+dy[i]
        if 0<=Nx<m and 0<=Ny<n:
            if castle[Nx][Ny][tb[i]]==castle[x][y][i]==0:
                dfs(Nx,Ny,roomNum)
    return True
def dfs2(x,y):
    stack=[(x,y)]
    Neighbor=set()
    roomNum=check[x][y]
    while stack:
        x,y=stack.pop()
        visited[x][y]=1
        for i in range(4):
            Nx,Ny=x+dx[i],y+dy[i]
            if 0<=Nx<m and 0<=Ny<n:
                if visited[Nx][Ny]!=-1: continue
                if check[x][y]==check[Nx][Ny]:
                    stack.append((Nx,Ny))
                else:
                    Neighbor.add(check[Nx][Ny])
    return roomNum,list(Neighbor)

if __name__ == '__main__':
    r=sys.stdin.readline
    n,m=map(int,r().split())
    castle=[]
    tb={0:2,2:0,1:3,3:1}
    dx=[0,-1,0,1]#
    dy=[-1,0,1,0]
    #서,북,동,남
    for _ in range(m):
        tmp=list(map(int,r().split()))
        castle.append(list(map(wall,tmp)))
    check=[[-1]*n for _ in range(m)]
    room=1
    maxRoomcnt=[]
    for i in range(m):
        for j in range(n):
            roomCnt=0
            if dfs(i,j,room):
                room+=1
                maxRoomcnt.append(roomCnt)
    visited=[[-1]*n for _ in range(m)]
    tmp3=[]
    for i in range(m):
        for j in range(n):
            if visited[i][j]==-1:
                roomnum,lst=dfs2(i,j)
                for item in lst:
                    tmp3.append(maxRoomcnt[roomnum-1]+maxRoomcnt[item-1])
    print(room-1)
    print(max(maxRoomcnt))
    print(max(tmp3))
    