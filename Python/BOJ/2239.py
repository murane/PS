import sys
def dfs(idx):
    #0으로 표시된 좌표를 모두 채웠기때문에 종료
    if idx==len(tovisit):
        for i in range(len(board)):
            print(''.join(map(str,board[i])))
        exit(0)
    x,y=tovisit[idx]
    #print(f'now on {x} {y} depth {idx+1}')

    #가로 세로 해당블록에서 후보숫자를 0으로 표시하여 필터링
    candidates=[1]*10
    for i in range(9):
        candidates[board[x][i]]=0
        candidates[board[i][y]]=0
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            candidates[board[i][j]]=0
    #가능한 수가 없는경우
    if max(candidates)==0:return
    for i in range(1,10):
        if candidates[i]==0:continue
        #백트래킹
        board[x][y]=i
        dfs(idx+1)
        board[x][y]=0

if __name__ == "__main__":
    r=sys.stdin.readline
    #sys.setrecursionlimit(10**6)
    board=[list(map(int,r().strip())) for _ in range(9)]
    tovisit=[]
    #0으로 표시된 좌표를 탐색
    for x in range(9):
        for y in range(9):
            if board[x][y]==0:
                tovisit.append((x,y))
    dfs(0)
    print("1")
