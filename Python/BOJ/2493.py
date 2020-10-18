import sys
r=sys.stdin.readline
N=int(r())
top=list(map(int,r().split()))
res=[]
stack=[]
for i,v in enumerate(top):
    if i==0:
        res.append(0)
        stack.append((i+1,v))
    else:
        if v>stack[-1][1]:
            while stack and stack[-1][1]<v:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][0])
            stack.append((i+1,v))
        else:
            stack.append((i+1,v))
            res.append(i)

print(' '.join(map(str,res)))