import sys
r=sys.stdin.readline
MOD=10**9+7
def pow(a,b):
    ans=1
    while b:
        if b&1:
            ans=(ans*a)%MOD
        a=(a**2)%MOD
        b=b//2
    return ans
def powDAC(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%2==0:
        tmp=powDAC(a,b/2)
        return (tmp**2)%MOD
    else:
        return a*powDAC(a,b-1)%MOD
for _ in range(int(r())):
    N=int(r())
    if N==1:
        print(1)
        continue
    else:
        #print(pow(2,N-2))
        print(powDAC(2,N-2))
