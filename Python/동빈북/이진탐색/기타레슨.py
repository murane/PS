import sys
r=sys.stdin.readline
N,M=map(int,r().split())
arr=list(map(int,r().split()))
lo,hi=1,5*(10**9)
def canRecord(leng):
    cnt=0
    total=0
    for each in arr:
        if each>leng:
            return False
        if total==0:
            cnt+=1
            total+=each
        else:
            if total+each<=leng:
                total+=each
            else:
                cnt+=1
                total=each
        if cnt>M:
            return False
    return True
while lo<=hi:
    m=(lo+hi)//2
    if canRecord(m):
        hi=m-1
    else:
        lo=m+1
print(lo)
