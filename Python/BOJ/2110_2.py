import sys
r=sys.stdin.readline
N,C=map(int,r().split())
X=[]
for _ in range(N):
    X.append(int(r()))
X.sort()
S,E=X[0],X[-1]
lo,hi=0,N-1
