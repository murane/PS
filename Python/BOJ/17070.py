import sys
r=sys.stdin.readline
#가로0 세로1 대각2
route=0
N=int(r())
house=[list(map(int,r().split())) for _ in range(N)]
tb=[[[0,0,0] for _ in range(N)] for _ in range(N)]
def valid(x,y):
    if x>=0 and x<N and y>=0 and y<N and house[x][y]!=1:
        return True
tb[0][1][0]=1
for i in range(N):
    for j in range(2,N):
        if house[i][j]==0:
            #가로방향
            if valid(i,j-1):
                tb[i][j][0]+=(tb[i][j-1][0]+tb[i][j-1][2])
            #세로방향
            if valid(i-1,j):
                tb[i][j][1]+=(tb[i-1][j][1]+tb[i-1][j][2])
            #대각선
            if valid(i,j-1) and valid(i-1,j) and valid(i-1,j-1):
                tb[i][j][2]=sum(tb[i-1][j-1])

print(sum(tb[N-1][N-1]))