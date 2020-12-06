import sys
r=sys.stdin.readline
N,C=map(int,r().split())
house=[]
for _ in range(N):
    house.append(int(r()))
house.sort()
lo,hi=1,(house[-1]-house[0])//(C-1)

def canInstall(x):
    cnt=1
    cur=house[0]#초기 설치 위치
    for pos in house:
        if pos-cur>=x:
            cnt+=1
            cur=pos
            if cnt==C:
                break
    if cnt==C:
        return True
    return False

while lo<=hi:
    mid=(lo+hi)//2
    if canInstall(mid):
        lo=mid+1
    else:
        hi=mid-1
print(hi)

    

