import sys
import bisect
r=sys.stdin.readline
M,N,L=map(int,r().split())
guns=list(map(int,r().split()))
guns.sort()
animals=list()
for _ in range(N):
    animals.append(tuple(map(int,r().split())))
ans=0
def ck(x,y,mid):
    if abs(guns[mid]-x)+y<=L:
        return True
    return False
for animal in animals:
    x,y=animal
    lo,hi=0,len(guns)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if ck(x,y,mid):
            ans+=1
            break
        else:
            if guns[mid]==x:
                break
            elif x<guns[mid]:
                hi=mid-1
            else:
                lo=mid+1
print(ans)