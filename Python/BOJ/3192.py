import sys
r=sys.stdin.readline
square=[]
for _ in range(3):
    square.append(list(map(int,r().split())))
case=0
line=0
coord=[]
for y in range(3):
    row=0
    flg=True
    for x in range(3):
        if square[y][x]==0:
            case+=1
            flg=False
            coord.append((y,x))
        row+=square[y][x]
    if flg:
        line=row
for x in range(3):
    col=0
    flg=True
    for y in range(3):
        if square[y][x]==0:
            flg=False
        col+=square[y][x]
    if flg:
        line=col
if square[0][0]!=0 and square[1][1]!=0 and square[2][2]!=0:
    line=square[0][0]+square[1][1]+square[2][2]
if square[0][2]!=0 and square[1][1]!=0 and square[2][0]!=0:
    line=square[0][2]+square[1][1]+square[2][0]
tmp=0
if case==1:
    for x in range(3):
        tmp+=square[coord[0][0]][x]
    square[coord[0][0]][coord[0][1]]=line-tmp
if case==2:
    #같은 x축이면
    if coord[0][0]!=coord[1][0]:
        for x in range(3):
            tmp+=square[coord[0][0]][x]
        square[coord[0][0]][coord[0][1]]=line-tmp
        tmp=0
        for x in range(3):
            tmp+=square[coord[1][0]][x]
        square[coord[1][0]][coord[1][1]]=line-tmp
    #같은 x축이 아니므로 y좌표기준으로
    else:
        for y in range(3):
            tmp+=square[y][coord[0][1]]
        square[coord[0][0]][coord[0][1]]=line-tmp
        tmp=0
        for y in range(3):
            tmp+=square[y][coord[1][1]]
        square[coord[1][0]][coord[1][1]]=line-tmp
if case==3:
    #대각선으로 구성됐을때
    if line==0:
        line=sum(list(map(sum,square)))//2
        for x in range(3):
            tmp+=square[coord[0][0]][x]
        square[coord[0][0]][coord[0][1]]=line-tmp
        tmp=0
        for x in range(3):
            tmp+=square[coord[1][0]][x]
        square[coord[1][0]][coord[1][1]]=line-tmp
        tmp=0
        for x in range(3):
            tmp+=square[coord[2][0]][x]
        square[coord[2][0]][coord[2][1]]=line-tmp
    else:
        for y in range(3):
            if square[y].count(0)==1:
                co_x,co_y=0,0
                tmp=0
                for x in range(3):
                    tmp+=square[y][x]
                    if square[y][x]==0:
                        co_x,co_y=x,y
                square[co_y][co_x]=line-tmp
        for x in range(3):
            if list(zip(*square))[x].count(0)==1:
                co_x,co_y=0,0
                tmp=0
                for y in range(3):
                    tmp+=square[y][x]
                    if square[y][x]==0:
                        co_x,co_y=x,y
                square[co_y][co_x]=line-tmp
for y in range(3):
    for x in range(3):
        print(square[y][x],end=" ")
    print("")