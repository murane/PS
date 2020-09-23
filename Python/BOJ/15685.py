import sys
r=sys.stdin.readline
N=int(r())
board=[[0]*101 for _ in range(101)]
di=[(0,1),(-1,0),(0,-1),(1,0)]
for _ in range(N):
    y,x,d,g=map(int,r().split())
    current_g=0
    stack=[]
    while current_g<=g:
        tmp=stack[:]
        if current_g==0:
            board[x][y]+=1
            x,y=x+di[d][0],y+di[d][1]
            board[x][y]+=1
            stack.append(d)
        else:
            while tmp:
                cur=(tmp.pop()+1)%4
                x,y=x+di[cur][0],y+di[cur][1]
                board[x][y]+=1
                stack.append(cur)
        current_g+=1
cnt=0
for i in range(100):
    for j in range(100):
        if board[i][j]>0 and board[i+1][j]>0 and board[i][j+1]>0 and board[i+1][j+1]>0:
            cnt+=1
print(cnt)