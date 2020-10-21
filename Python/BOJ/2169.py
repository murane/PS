import sys
r=sys.stdin.readline
N,M=map(int,r().split())
area=[]
for _ in range(N):
    area.append(list(map(int,r().split())))
start=(0,0)
end=(N-1,M-1)
dp=[[-1]*M for _ in range(N)]
for i in range(N):#행
    for j in range(M):#열
        