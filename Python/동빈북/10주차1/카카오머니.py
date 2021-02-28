import sys,math
r=sys.stdin.readline
logs=[]
flg=False
for i in range(int(r())):
    a,b=map(int,r().split())
    logs.append((a,b))

balance=0
canBeOne=[]
res=[]
for a,b in logs:
    
    before=balance
    after=b
    withdrawl=a

    if withdrawl>0 and before+withdrawl!=after:
        print(-1)
        exit(0)

    if withdrawl<0 and after==0:
        canBeOne.append(True)
        res.append(-withdrawl)

    if withdrawl<0 and after>0:
        if abs(a)>before:
            canBeOne.append(False)
            tmp = after - before - withdrawl
            res.append(tmp)
        else:
            if before+withdrawl!=after:
                print(-1)
                exit(0)

    balance=b


if all(canBeOne):
    print(1)
else:
    ans=res[0]
    for x in res:
        ans=math.gcd(ans,x)
    if ans==1:
        print(-1)
    else:
        if ans in res:
            print(ans)
        else:
            print(-1)