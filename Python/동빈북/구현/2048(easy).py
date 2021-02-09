import sys
from copy import deepcopy
r=sys.stdin.readline
N=int(r())
board=[]
lst=[]
dxy=[(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(N):
    board.append(list(map(int,r().split())))
def move(curBoard,di):
    
    # if di[1]==0:#세로
    #     for i in range(N):      #i번째 열에 대해
    #         if di[0]<0:         #ㅗ
            
    #         else:               #ㅜ
    
    #el
    if di[0]==0:#가로
        for i in range(N):      #i번째 행에 대해
            if di[1]<0:         #ㅓ
                flg=True
                for j in range(1,N-1):
                    curBlock=curBoard[i][j]
                    for k in range(j-1,0,-1):
                        if curBoard[i][k]==0:
                            curBoard[i][k]=curBlock
                            curBoard[i][k+1]=0
                        if curBoard[i][k]==curBoard[i][k+1] and flg:
                            flg=False
                            curBoard[i][k]*=2
                            curBoard[i][k+1]=0
                            break
                        else:
                            flg=True
                            break                      
            # else:               #ㅏ
    return curBoard
def dfs(N,curBoard,di):
    if N==5:
        lst.append(max(map(max,curBoard)))
    curBoard=move(curBoard,di)
    tmp_board=deepcopy(curBoard)
    # for i in range(4):
    #     dfs(N+1,tmp_board,i)
    dfs(N+1,tmp_board,3)

dfs(N,board,3)    
print(max(lst))