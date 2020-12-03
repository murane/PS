import sys,random
r=sys.stdin.readline
for _ in range(int(r())):
    n=int(r())
    res=[]
    tmp=list(range(1,n+1))
    idx=n
    #idx will n -> 0
    while idx>0:
        cur=random.randint(1,idx)
        if tmp[cur-1]==len(res)+1:
            continue
        else:
            res.append(tmp.pop(cur-1))
            idx-=1

    print(*res)