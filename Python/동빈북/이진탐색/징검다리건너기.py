def solution(stones, k):
    def canGo(n):
        cur=1
        for stone in stones:
            if n-stone>=1:
                cur+=1
                if cur>k:
                    return False
            else:
                cur=1
        return True
    lo,hi=1,200000000
    ans=0
    while lo<=hi:
        mid=(lo+hi)//2
        if canGo(mid):
            lo=mid+1
            ans=mid
        else:
            hi=mid-1
    return ans