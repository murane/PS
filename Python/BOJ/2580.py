import sys,copy
def possibleNum(board,x,y):
    #가로
    candidate=set(list(range(1,10)))
    tmp=set()
    for i in range(9):
        tmp.add(board[x][i])
    #세로
    for j in range(9):
        tmp.add(board[j][y])
    #3*3
    for j in range((x//3)*3,(x//3)*3+3):
        for i in range((y//3)*3,(y//3)*3+3):
            tmp.add(board[j][i])
    return list(candidate-tmp)
def dfs(cnt):
    if cnt==len(coords):
        return board
    else:
        x=coords[cnt][0]
        y=coords[cnt][1]
        nums=list(possibleNum(board,x,y))
        if not nums:
            return
        for num in nums:
            board[x][y]=num
            res = dfs(cnt+1)
            if res is not None:
                return res
            board[x][y]=0

r=sys.stdin.readline
board=[list(map(int,r().split())) for _ in range(9)]
coords=[]
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]==0:
            coords.append((i,j))
board = dfs(0)
for i in range(len(board)):
    print(' '.join(map(str,board[i])))
