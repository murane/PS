import sys
from collections import Counter
r=sys.stdin.buffer.readline
N=int(r())
horror=list(map(int,r().split()))
horror.sort(reverse=True)
ans=0
while horror:
    cur=horror.pop()
    cnt=1
    flg=False
    while horror and cnt<cur:
        horror.pop()
        cnt+=1
        flg=True
    if flg or cur==1:
        ans+=1
print(ans)

