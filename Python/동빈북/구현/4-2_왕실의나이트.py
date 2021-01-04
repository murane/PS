import sys
r=sys.stdin.readline
knight_move=[(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
#나이트의 이동 변위를 미리 생성
cur=r().strip()
cur=(ord(cur[0])-ord('a'),int(cur[1]))
#현좌표를 ord함수로 변환하여 저장
ans=0
for dx,dy in knight_move:
    nx,ny=cur[0]+dx,cur[1]+dy
    if 1<=nx<=8 and 1<=ny<=8:
        ans+=1
print(ans)

#시공간에 큰 변수는 없어보인다
#변위를 어떻게나타낼지 생각해보면 매우 간단