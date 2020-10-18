import sys
#from functools import lru_cache
#@lru_cache(None)
def make_album(n,a,b,c):
    if n==0:
        if a==b==c==0:
            return 1
        else:
            return 0
    if a<0 or b<0 or c<0: return 0
    if tb[n][a][b][c]!=-1:
        return tb[n][a][b][c]
    cnt=0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i+j+k==0:continue    #a모두 부르지 않는경우 제외
                #a, b, c, ab, ac, bc, abc 7가지의 곡을 앨범에 추가
                cnt+=make_album(n-1,a-i,b-j,c-k)
    cnt%=(10**9+7)
    tb[n][a][b][c]=cnt
    return cnt

if __name__ == "__main__":
    r=sys.stdin.readline
    S,D,K,H=map(int,r().split())
    tb=[[[[-1]*(H+1) for _ in range((K+1))] for _ in range((D+1))] for _ in range((S+1))]
    ans=make_album(S,D,K,H)
    print(ans)