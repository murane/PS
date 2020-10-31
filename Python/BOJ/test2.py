from collections import deque
def dfs(x,y,v,visit):
    d=[(1,0),(-1,0),(0,1),(0,-1)]
    cur=v[x][y]
    stack=[]
    stack.append((x,y))
    visit[x][y]=True
    while stack:
        x,y=stack.pop()
        for i in range(4):
            Nx,Ny=x+d[i][0],y+d[i][1]
            if not 0<=Nx<len(v) or not 0<=Ny<len(v): continue
            if v[Nx][Ny]!=cur or visit[Nx][Ny]: continue
            stack.append((Nx,Ny))
            visit[Nx][Ny]=True
    return cur,visit
def solution(v):
    answer = [0,0,0]
    visit=[[False]*len(v) for _ in range(len(v))]
    for i in range(len(v)):
        for j in range(len(v)):
            if not visit[i][j]:
                ans,after=dfs(i,j,v,visit)
                answer[ans]+=1
                visit=after
    
    return answer

if __name__ == '__main__':
    v=[[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]
    print(solution(v))
    #print(solution(info, query))
	