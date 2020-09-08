import sys
from collections import deque
r=sys.stdin.readline
stack=[]
op = []
T = int(r())
f=True
left = deque([x for x in range(1,T+1)])
seq=[]
for _ in range(T):
    seq.append(int(r()))
for i in range(T):
    tmp = seq[i]
    while True:
        if len(left)==0:
            check = stack.pop()==tmp
            if check:
                op.append('-')
                break
            else:
                f=False
                break
        elif len(stack) != 0 and stack[-1]==tmp:
            stack.pop()
            op.append('-')
            break
        elif left[0]==tmp:
            stack.append(left.popleft())
            op.append('+')
            stack.pop()
            op.append('-')
            break
        elif left[0]<tmp:
            stack.append(left.popleft())
            op.append('+')
        else:
            f=False
            break
    if not f:
        break
if not f:
    print("NO")
else:
    for operand in op:
        print(operand)
