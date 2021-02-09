import sys
r=sys.stdin.readline
N=int(r())
move=list(r().split())
cur=(1,1)
tb={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
# 상하좌우 움직임별로 x,y축 좌표이동을 매핑
for ch in move:
    nx,ny=cur[0]+tb[ch][0],cur[1]+tb[ch][1]
    #각각의 움직임을 카운트하고 벗어나는 경우를 예외처리
    if not 1<=nx<=N or not 1<=ny<=N:
        continue
    cur=(nx,ny)
print(*cur)

#시간복잡도는 move의 길이에 비례한다.
#공간복잡도는 별도의 공간을 사용하지 않으므로 입력값 move에 비례한다
