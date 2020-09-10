import sys
r=sys.stdin.readline
#가로0 세로1 대각2
direction=0
move={0:[1,2],1:[0,2],2:[0,1,2]}
route=0
N=int(r())
house=[list(map(int,r().split())) for _ in range(N)]
tb=[[0]*N for _ in range(N)]
"""
for i in range(N-1):
    for j in range(1,N-1):
"""
def square(x,y):
    if house[x+1][y]!=1 and house[x][y+1]!=1 and house[x+1][y+1]!=1:
        return True
    else:
        return False
def canMove(x,y,dire):
    tmp=[]
    for di in move[dire]:
        if di==0 and y+1<N and house[x][y+1]!=1:
            tmp.append((x,y+1,dire))
        if di==1 and x+1<N and house[x+1][y]!=1:
            tmp.append((x+1,y,dire))
        if di==2 and y+1<N and x+1<N and square(x,y):
            tmp.append((x+1,y+1,2))
    return tmp
def dfs(x,y,dire):
    global route
    if x==N-1 and y==N-1:
        route+=1
        return
    else:
        lst = canMove(x,y,dire)
        if not lst:
            return
        for x,y,dire in lst:
            dfs(x,y,dire)

dfs(0,1,direction)
print(route)

