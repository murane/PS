#BFS를 진행하되 여러칸을 방문할때 더러운칸을 청소하고 순회해야하기때문에
#비트마스킹 BFS를 통해 최소값을 보장한다
import sys
from collections import deque
r=sys.stdin.readline
def bfs(x,y):
    q=deque()
    #dirty의 길이만큼 0을 부여하여 비트를 설정한다
    q.append((x,y,'0'*len(dirty),0))
    #visit배열도 최상위 차원으로 2**dirty만큼의 True False여부를 설정할 수 있게한다
    visit=[[[False]*w for _ in range(h)] for _ in range(2**len(dirty))]
    visit[int('0'*len(dirty),2)][x][y]=True
    while q:
        x,y,mask,dist=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            tmpDist=dist
            tmpMask=mask
            if not 0<=nx<h or not 0<=ny<w: continue
            if bang[nx][ny]=='X': continue
            tmpDist+=1
            if visit[int(tmpMask,2)][nx][ny]: continue
            if bang[nx][ny]=='.':
                q.append((nx,ny,tmpMask,tmpDist))
                visit[int(tmpMask,2)][nx][ny]=True
            #더러운칸을 만나면 dirty dict에서 idx를 가져오고 
            #마스크를 갱신하여 visit체크해준다
            elif bang[nx][ny]=='*':
                idx=dirty[(nx,ny)]
                tmpMask=tmpMask[:idx]+'1'+tmpMask[idx+1:]
                visit[int(tmpMask,2)][nx][ny]=True
                q.append((nx,ny,tmpMask,tmpDist))
                #종료조건
                if tmpMask=='1'*len(dirty):
                    return tmpDist
    return -1
while True:
    w,h=map(int,r().split())
    if w==h==0:break
    bang=[]
    for i in range(h):
        bang.append(list(r().strip()))
    dirty={}
    seq=-1
    start=[]
    #dirty를 미리 탐색해서 seq를 부여한다.
    for i in range(h):
        for j in range(w):
            if bang[i][j]=='o':
                start=[i,j]
                bang[i][j]='.'
            elif bang[i][j]=='*':
                seq+=1
                dirty[(i,j)]=seq
    print(bfs(start[0],start[1]))
#20X20크기의 격자에 더러운칸은 10개이므로 400*(2**10)크기의 visit배열 공간을 탐색한다

    