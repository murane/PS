import sys
r=sys.stdin.readline
tb=dict()
for i in range(5):
    line=list(map(int,r().split()))
    for j,num in enumerate(line):
        tb[num]=(i,j)
ck=[[False]*5 for _ in range(5)]
call=[]
for _ in range(5):
    line=list(map(int,r().split()))
    call.extend(line)
bingo=0
def xA(i,j):
    for x in range(5):
        if ck[i][x]:continue
        else:
            return False
    return True
def yA(i,j):
    for y in range(5):
        if ck[y][j]:continue
        else:
            return False
    return True
def lbTrt():
    if ck[4][0]==ck[3][1]==ck[2][2]==ck[1][3]==ck[0][4]==True:
        return True
    return False
def ltTrb():
    if ck[0][0]==ck[1][1]==ck[2][2]==ck[3][3]==ck[4][4]==True:
        return True
    return False
for i in range(1,26):
    x,y=tb[call[i-1]]
    ck[x][y]=True
    if x+y==4:
        if lbTrt():
            bingo+=1
    elif x==y:
        if ltTrb():
            bingo+=1
    if xA(x,y):
        bingo+=1
    if yA(x,y):
        bingo+=1
    if bingo>=3:
        print(i)
        break


