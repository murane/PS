import sys
r=sys.stdin.readline
N,K=list(map(int,r().split()))
tb=[[0]*100 for _ in range(100)]
def bino_coef(n,k):
    if tb[n][k]:
        return tb[n][k]
    else:
        if k==1:
            tb[n][k]=n
            return tb[n][k]
        elif k==0 or (n==k):
            tb[n][k]=1
            return tb[n][k]
        else:
            tb[n][k]=bino_coef(n-1,k-1)+bino_coef(n-1,k)
            return tb[n][k]
print(bino_coef(N,K))