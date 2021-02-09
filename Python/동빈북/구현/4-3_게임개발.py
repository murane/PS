import sys
r=sys.stdin.readline
N,M=map(int,r().split())
#X,Y를 각각 좌표로 입력받고 di는 방향을 나타낸다
X,Y,di=map(int,r().split())
#현재의 좌표를 cur 리스트에 X,Y로 나타낸다
cur=[X,Y]
#tb 딕셔너리로 정수에 대응하는 x,y좌표값을 변화를 나타낸다
tb={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
Map=[]
#방문한 좌표를 visit배열로 기록한다.
visit=[[False]*M for _ in range(N)]
visit[cur[0]][cur[1]]=True
for _ in range(N):
    Map.append(list(map(int,r().split())))
ans=1
def move(cur,di):
    global ans
    for _ in range(4):
        #현재 방향으로부터 4번 tb을 순회한다.
        di= 3 if di==0 else di-1
        x,y=cur[0]+tb[di][0],cur[1]+tb[di][1]
        #이동한 좌표가 테이블의 범위 안이고
        # 바다가 아니며 방문하지 않았을때 처리해준다.
        if not 0<=x<N or not 0<=y<M:continue
        if Map[x][y]==0 and not visit[x][y]:
            cur=[x,y]
            visit[x][y]=True
            ans+=1
            return True,cur,di
    return False,cur,di

while True:
    flg,cur,di=move(cur,di)
    #이동이 실패하고 뒤로 물러날수도 없을때 종료한다.
    if not flg:
        nx,ny=cur[0]-tb[di][0], cur[1]-tb[di][1]
        if Map[nx][ny]==1 or visit[nx][ny]:
            break
print(ans)
#50X50 격자의 모든 좌표를 순회하며 네 방향을 다탐색해도
#연산량은 크지 않다.