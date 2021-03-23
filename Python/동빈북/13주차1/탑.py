import sys
r=sys.stdin.readline
N=int(r())
top=list(map(int,r().split()))
ans=[]
info=[]
for idx,height in enumerate(top):
    if idx==0:
        info.append((idx,height))
        ans.append(0)
    else:
        while info and info[-1][1]<height:
            info.pop()
        if not info:
            info.append((idx,height))
            ans.append(0)
        else:
            ans.append(info[-1][0]+1)
            info.append((idx,height))
print(*ans)