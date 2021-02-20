import sys
r=sys.stdin.readline

N,M=map(int,r().split())

grid=[]
for _ in range(N):
    grid.append(list(map(int,r().split())))

ans=0

for i in range(N):
    for j in range(M-3):
        ans=max(ans,sum(grid[i][j:j+4]))
for i in range(N-3):
    for j in range(M):
        tmp=sum([grid[i][j]+grid[i+1][j]+grid[i+2][j]+grid[i+3][j]])
        ans=max(ans,tmp)
for i in range(N-1):
    for j in range(M-1):
        tmp=sum([grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1]])
        ans=max(ans,tmp)
for i in range(N-1):#ㅗㅜ
    for j in range(M-2):
        tmp=sum([grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1],grid[i][j+2],grid[i+1][j+2]])
        tmp2=[
            grid[i][j]+grid[i+1][j+2],
            grid[i+1][j]+grid[i][j+2],
            grid[i][j]+grid[i][j+2],
            grid[i+1][j]+grid[i+1][j+2],
            grid[i][j]+grid[i][j+1],
            grid[i+1][j]+grid[i+1][j+1],
            grid[i][j+1]+grid[i][j+2],
            grid[i+1][j+1]+grid[i+1][j+2]
        ]
        ans=max(ans,tmp-min(tmp2))
for i in range(N-2):#ㅏㅓ
    for j in range(M-1):
        tmp=sum([grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1],grid[i+2][j],grid[i+2][j+1]])
        tmp2=[
            grid[i+2][j]+grid[i][j+1],
            grid[i][j]+grid[i+2][j+1],
            grid[i][j]+grid[i+2][j],
            grid[i][j+1]+grid[i+2][j+1],
            grid[i][j]+grid[i+1][j],
            grid[i+1][j]+grid[i+2][j],
            grid[i][j+1]+grid[i+1][j+1],
            grid[i+1][j+1]+grid[i+2][j+1]
        ]
        ans=max(ans,tmp-min(tmp2))
print(ans)