import sys
r=sys.stdin.readline
MOD=10**9+7
def powRecur(x,y,mod):
    ans=1
    while y:
        if y&1:
            ans=(x*ans)%mod
        x=(x**2)%mod
        y=y//2
    return ans

N,K=map(int,r().split())

fac=[1 for _ in range(N+1)]
for i in range(2,N+1):
    fac[i]=(fac[i-1]*i)%MOD
A=fac[N]
B=(fac[N-K]*fac[K])%MOD
print((A%MOD)*powRecur(B,MOD-2,MOD)%MOD)
