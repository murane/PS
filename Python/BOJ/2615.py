import sys
r=sys.stdin.readline
board=[]
for _ in range(19):
    board.append(list(map(int,r().split())))
flg=0
coords=[]
di=[(0,1),(1,0),(-1,1),(1,1)]
#가로0 세로 1 좌상~우하2 좌하~우상3
def check(color,coords):
    x,y=coords
    for i in range(4):
        sameCnt=1
        X,Y=x,y
        _x,_y=x-di[i][0],y-di[i][1]
        if 0<=_x<19 and 0<=_y<19 and board[_x][_y]==color:
            continue
        while True:
            Nx,Ny=X+di[i][0],Y+di[i][1]
            if sameCnt==5:
                if Nx<0 or Nx>=19 or Ny<0 or Ny>=19:#끝인경우
                    pass
                elif board[Nx][Ny]!=color:#오목인경우
                    pass
                else:#육목인경우
                    sameCnt=1
                break
            if Nx<0 or Nx>=19 or Ny<0 or Ny>=19 or board[Nx][Ny]!=color:
                break
            X,Y=Nx,Ny
            sameCnt+=1
        if sameCnt==5:
            return color
    return 0
for i in range(19):
    for j in range(19):
        if board[i][j]==0:
            continue
        elif board[i][j]==1:
            flg=check(1,(i,j))
        else:
            flg=check(2,(i,j))
        if flg!=0:
            coords.extend([i+1,j+1])
            if flg==1:
                print(1)
                print(*coords)
            else:
                print(2)
                print(*coords)
            exit(0)
print(0)

