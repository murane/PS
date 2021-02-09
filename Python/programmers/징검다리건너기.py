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
    lo,hi=0,len(stones)
    ans=0
    while lo<=hi:
        mid=(lo+hi)//2
        if canGo(mid):
            lo=mid+1
        else:
            ans=mid
            hi=mid-1
    return ans
if __name__ == '__main__':
    stones=	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k=3
    solution(stones,k)
    