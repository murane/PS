import sys
r=sys.stdin.readline
N=int(r())
sys.setrecursionlimit(10**9)
Integers=list(map(int,r().split()))
pal=[[-1]*(N+1) for _ in range(N+1)]

def sol(s,e):
    #기저사례
    if s==e:
        pal[s][e]=1
        return pal[s][e]
    #이미계산됨
    if pal[s][e]!=-1:
        return pal[s][e]
    
    if Integers[s-1]!=Integers[e-1]:
        pal[s][e]=0
        return pal[s][e]
    else:
        if (e-s)==1:
            pal[s][e]=1
        else:
            pal[s][e]=sol(s+1,e-1)
    return pal[s][e]

# for i in range(N-1):
#     for j in range(i+1,N):
#         sol(i,j)
for _ in range(int(r())):
    S,E=map(int,r().split())
    print(sol(S,E))

