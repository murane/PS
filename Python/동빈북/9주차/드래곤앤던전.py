import sys,math
r=sys.stdin.readline
N,H=map(int,r().split())
roomLst=[]
for _ in range(N):
    t,a,h=map(int,r().split())
    roomLst.append((t,a,h))

def canWin(MaxHp):
    curHp=MaxHp
    curAtk=H
    for t,a,h in roomLst:
        if t==1:#몬스터
            attachCnt=math.ceil(h/curAtk)
            curHp-=a*(attachCnt-1)
        else:#물약
            curAtk+=a
            curHp+=h
            if curHp>MaxHp:
                curHp=MaxHp
        if curHp<=0:
            return False
    return True

lo=1
hi=10**12
ans=hi
while lo<=hi:
    mid=(lo+hi)//2
    if canWin(mid):
        hi=mid-1
        ans=mid
    else:
        lo=mid+1
print(ans)