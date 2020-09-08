import sys
from collections import deque
r=sys.stdin.readline
q=deque([])
for _ in range(int(r())):
    op=list(r().split())
    if op[0]=="push":
        q.appendleft(op[1])
    elif op[0]=="pop":
        if not q:
            print("-1")
        else:
            print(q.pop())
    elif op[0]=="size":
        print(len(q))
    elif op[0]=="empty":
        if not q:
            print("1")
        else:
            print("0")
    elif op[0]=="front":
        if not q:
            print("-1")
        else:
            print(q[-1])
    elif op[0]=="back":
        if not q:
            print("-1")
        else:
            print(q[0])