import sys
r=sys.stdin.readline
H,W=map(int,r().split())
block=list(map(int,r().split()))
ans=0

def solve(i):
    cur=block[i]
    l,r=max(block[:i]),max(block[i+1:])
    if l>cur and r>cur:
        return min(l,r)-cur
    return 0

for i in range(W):
    if i==0 or i==W-1:
        continue
    ans+=solve(i)
print(ans)