import sys
from itertools import combinations
r=sys.stdin.readline
N=int(r())
bok=[]
for _ in range(N):
    bok.append(list(r().split()))
teachers=[]
canInstalls=[]
studentCnt=N**2-len(teachers)-len(canInstalls)
for i in range(N):
    for j in range(N):
        if bok[i][j]=='T':
            teachers.append((i,j))
        if bok[i][j]=='X':
            canInstalls.append((i,j))

dxy=[(1,0),(-1,0),(0,1),(0,-1)]

def check(a,b,c):
    visit=set()

    for teacher in teachers:
        tx,ty=teacher
        for i in range(4):
            nx,ny=tx,ty
            while True:
                nx,ny=nx+dxy[i][0],ny+dxy[i][1]
                if not 0<=nx<N or not 0<=ny<N:
                    break
                if (nx,ny) in [a,b,c]:
                    break
                if bok[nx][ny]=='S':
                    visit.add((nx,ny))

    if len(visit)==0:
        return True
    else:
        return False

for a,b,c in combinations(canInstalls,3):
    if check(a,b,c):
        print("YES")
        exit(0)
print("NO")