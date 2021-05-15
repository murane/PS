import sys
from collections import deque
r=sys.stdin.readline
S=r().strip()
back=True
q=deque()
for ch in S:
    if ch=="R":
        back^=True
    else:
        if back:
            if q and q[-1]==ch:
                q.pop()
            else:
                q.append(ch)
        else:
            if q and q[0]==ch:
                q.popleft()
            else:
                q.appendleft(ch)

if back:
    print(''.join(q))
else:
    print(''.join(reversed(q)))
