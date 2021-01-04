import sys
from collections import deque
r=sys.stdin.readline
N=int(r())
apple=set()
di=[(0,1),(1,0),(0,-1),(-1,0)]
for _ in range(int(r())):
    row,col=map(int,r().split())
    apple.add((row-1,col-1))
snake_info=deque()
for _ in range(int(r())):
    tmp=r().split()
    X,C=int(tmp[0]),tmp[1]
    snake_info.append((X,C))
time=0
#뱀의 이동경로를 가지는 큐와 셋
snake_set=set()
snake_set.add((0,0))
snake_queue=deque([(0,0)])
cur_di=0
while True:
    time+=1
    x,y=snake_queue[-1][0],snake_queue[-1][1]
    #시간에 맞는 회전처리
    if snake_info and snake_info[0][0]+1==time:
        _,C=snake_info.popleft()
        if C=='D':
            cur_di=(cur_di+1)%4
        elif C=='L':
            cur_di=(cur_di-1)%4
    nx,ny=x+di[cur_di][0],y+di[cur_di][1]
    #이동후 벽을 넘거나 자신의 몸이면 종료
    if not 0<=nx<N or not 0<=ny<N:break
    if (nx,ny) in snake_set:break
    #사과면 사과 셋에서 제거후 늘어났으므로 추가만
    if (nx,ny) in apple:
        apple.remove((nx,ny))
        snake_set.add((nx,ny))
        snake_queue.append((nx,ny))
    #그렇지 않으면 다음좌표의 추가와 함께
    #꼬리를 제거
    else:
        snake_set.add((nx,ny))
        snake_queue.append((nx,ny))
        tail=snake_queue.popleft()
        snake_set.remove(tail)
print(time)
#전처리와 set을 통해 최적화 하였으므로
#최대 100^100번의 이동이 가능하다
#사용하는 공간또한 10000개의 좌표를 큐와 셋으로 저장하는것은 충분하다