def canGo(maze,x,y,d):
    if d[0]==-1 and x==0:
        return False
    elif d[0]==1 and x==len(maze)-1:
        return False
    elif d[1]==-1 and y==0:
        return False
    elif d[1]==1 and y==len(maze)-1:
        return False
    else:
        if maze[x+d[0]][y+d[1]]==1:
            return False
        return True
    
def solution(maze):
    #위 오른쪽 아래 왼쪽
    direction=[(-1,0),(0,1),(1,0),(0,-1)]
    cur=1
    x,y=0,0
    time=0
    N=len(maze)-1
    while x!=N and y!=N:
        if canGo(maze,x,y,direction[cur]):
            x=x+direction[cur][0]
            y=y+direction[cur][1]
        elif canGo(maze,x,y,direction[(cur+1)%4]):
            x=x+direction[(cur+1)%4][0]
            y=y+direction[(cur+1)%4][1]
            cur=(cur+1)%4
        elif canGo(maze,x,y,direction[(cur+1)%4]):
            x=x+direction[(cur+1)%4][0]
            y=y+direction[(cur+1)%4][1]
            cur=(cur+1)%4
        elif canGo(maze,x,y,direction[(cur+1)%4]):
            x=x+direction[(cur+1)%4][0]
            y=y+direction[(cur+1)%4][1]
            cur=(cur+1)%4
        time+=1
    return time
if __name__ == '__main__':
    maze=[[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
    print(solution(maze))
    #print(solution(info, query))
	