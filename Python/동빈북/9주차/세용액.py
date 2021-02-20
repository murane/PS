import sys,bisect
r=sys.stdin.readline
N=int(r())
liq=list(map(int,r().split()))
liq.sort()
candidate=[]
ans=3*(10**9)
for i in range(len(liq)-2):
    piv1=liq[i]
    l,r=i+1,len(liq)-1
    while l!=r:
        cur=sum([piv1,liq[l],liq[r]])
        if abs(cur)<abs(ans):
            candidate=[piv1,liq[l],liq[r]]
            ans=cur
        if cur<=ans:
            l+=1
        else:
            r-=1
print(*sorted(candidate))