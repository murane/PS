import sys
r=sys.stdin.readline
N,L=map(int,r().split())
leak=list(map(int,r().split()))
cnt=0
tape=[]
for cur in sorted(leak):
    if not tape:
        tape.append((cur-0.5,cur-0.5+L))
        cnt+=1
    else:
        if cur+0.5<=tape[0][1]:
            continue
        else:
            tape[0]=(cur-0.5,cur-0.5+L)
            cnt+=1
print(cnt)