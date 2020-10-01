import sys
r=sys.stdin.readline
N,M=map(int,r().split())
arr=list(map(int,r().split()))
plus=[x for x in arr if x>0]
minus=[-x for x in arr if x<0]
plus.sort(reverse=True)
minus.sort(reverse=True)
res=0
cnt=0
if not plus:
    while cnt<len(minus):
        if cnt==0:
            res+=minus[0]
        else:
            res+=minus[cnt]*2
        cnt+=M
elif not minus:
    while cnt<len(plus):
        if cnt==0:
            res+=plus[0]
        else:
            res+=plus[cnt]*2
        cnt+=M
else:
    if plus[0]>minus[0]:
        while cnt<len(minus):
            res+=minus[cnt]*2
            cnt+=M
        cnt=0
        while cnt<len(plus):
            if cnt==0:
                res+=plus[0]
            else:
                res+=plus[cnt]*2
            cnt+=M
    else:
        while cnt<len(plus):
            res+=plus[cnt]*2
            cnt+=M
        cnt+=M
        cnt=0
        while cnt<len(minus):
            if cnt==0:
                res+=minus[0]
            else:
                res+=minus[cnt]*2
            cnt+=M
print(res)

