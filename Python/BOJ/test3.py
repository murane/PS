from collections import deque
def solution(board):
    d=[(1,0),(-1,0),(0,1),(0,-1)]
    l=len(board)
    h_visit=[[-1]*(l-1) for _ in range(l)]#가로
    v_visit=[[-1]*l for _ in range(l-1)]#세로
    h_visit[0][0]=0
    ans=0
    q=deque()
    q.append((0,0,True))#True는 가로 False는 세로
    while q:
        x,y,di=q.popleft()
        if x==l-1 and y==l-2 and di:
            ans=h_visit[x][y]
            break
        elif x==l-2 and y==l-1 and not di:
            ans=v_visit[x][y]
            break
        for i in range(4):
            Nx,Ny=x+d[i][0],y+d[i][1]
            if di:
                if not 0<=Nx<l or not 0<=Ny<l-1: continue
                if board[Nx][Ny+1]!=0: continue
                if h_visit[x][y]+1<=h_visit[Nx][Ny]:continue
                print(f'{x},{y}:{h_visit[x][y]} -> {Nx},{Ny}:{h_visit[Nx][Ny]}')
                h_visit[Nx][Ny]=h_visit[x][y]+1
                q.append((Nx,Ny,True))
            else:
                if not 0<=Nx<l-1 or not 0<=Ny<l: continue
                if board[Nx+1][Ny]!=0: continue
                if v_visit[x][y]+1<=v_visit[Nx][Ny]:continue
                v_visit[Nx][Ny]=v_visit[x][y]+1
                q.append((Nx,Ny,False))
        if di:#가로->세로
            if x!=0 and board[x-1][y]==board[x-1][y+1]==0:
                if h_visit[x][y]+1>v_visit[x-1][y]:
                    v_visit[x-1][y]=h_visit[x][y]+1
                    q.append((x-1,y,False))
                if h_visit[x][y]+1>v_visit[x-1][y+1]:
                    v_visit[x-1][y+1]=h_visit[x][y]+1
                    q.append((x-1,y+1,False))
            if x!=l-1 and board[x+1][y]==board[x+1][y+1]==0:
                if h_visit[x][y]+1>v_visit[x][y]:
                    v_visit[x][y]=h_visit[x][y]+1
                    q.append((x,y,False))
                if h_visit[x][y]+1>v_visit[x][y+1]:
                    v_visit[x][y+1]=h_visit[x][y]+1
                    q.append((x,y+1,False))
        else:#세로->가로
            if y!=0 and board[x][y-1]==board[x+1][y-1]==0:
                if v_visit[x][y]+1>h_visit[x][y-1]:
                    h_visit[x][y-1]=v_visit[x][y]+1
                    q.append((x,y-1,True))
                if v_visit[x][y]+1>h_visit[x+1][y-1]:
                    h_visit[x+1][y-1]=v_visit[x][y]+1
                    q.append((x+1,y-1,True))
            if y!=l-1 and board[x][y+1]==board[x+1][y+1]==0:
                if v_visit[x][y]+1>h_visit[x][y]:
                    h_visit[x][y]=v_visit[x][y]+1
                    q.append((x,y,True))
                if v_visit[x][y]+1>h_visit[x+1][y]:
                    h_visit[x+1][y]=v_visit[x][y]+1
                    q.append((x+1,y,True))  
    return ans

if __name__ == '__main__':
    board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
    solution(board)
    