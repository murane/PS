import sys
from collections import Counter
r=sys.stdin.readline
name=r().strip()
counter=Counter(name)
cnt=0
res=""
if len(name)%2==0:#
    for k in sorted(counter.keys()):
        v=counter[k]
        res+=k*(v//2)
        if v%2!=0:
            cnt+=1
        if cnt>=1:
            print("I'm Sorry Hansoo")
            exit(0)
    print(res+res[::-1])
else:
    mid=""
    for k in sorted(counter.keys()):
        v=counter[k]
        res+=k*(v//2)
        if v%2!=0:
            mid=k
            cnt+=1
        if cnt>1:
            print("I'm Sorry Hansoo")
            exit(0)
    print(res+mid+res[::-1])
