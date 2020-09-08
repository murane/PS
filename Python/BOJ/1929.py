import sys

def prime(n):
    tb=[False,False]+[True]*n
    if n==1:
        return None
    else:
        for i in range(2, int(n**0.5+1)):
            if tb[i]:
                for j in range(i*2,n,i):
                    tb[j]=False
    return [i for i in range(2,n+1) if tb[i]]


r = sys.stdin.readline
M, N = list(map(int,r().split()))
for item in prime(1000000):
    if item>=M and item<=N:
        print(item)