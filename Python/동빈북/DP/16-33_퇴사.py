import sys
r=sys.stdin.readline
N=int(r())
sangdam=[]
for _ in range(N):
    t,p=map(int,r().split())
    sangdam.append((t,p))
ans=0
def solve(day,total):
    global ans
    if day>N:
        return
    ans=max(ans,total)
    for i in range(day,N):
        solve(i+sangdam[i][0],total+sangdam[i][1])
solve(0,0)
print(ans)