import sys
from collections import deque
r=sys.stdin.readline
N=int(r())
Q=deque()
for _ in range(N):
    op=list(r().split())
    if op[0]=="push":
        Q.append(int(op[1]))
    elif op[0]=="pop":
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    elif op[0]=="size":
        print(len(Q))
    elif op[0]=="empty":
        if not Q:
            print(1)
        else:
            print(0)
    elif op[0]=="front":
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif op[0]=="back":
        if not Q:
            print(-1)
        else:
            print(Q[-1])