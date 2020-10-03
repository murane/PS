import sys,math
r=sys.stdin.readline
def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b>0:
        a,b=b,a%b
    return a
def lcm(arr):
    while len(arr)!=1:
        a=arr.pop()
        b=arr.pop()
        c=gcd(a,b)
        arr.insert(0,int(a*b/c))
    return arr[0]
N,M=map(int,r().split())
seq=list(map(int,r().split()))
seq=list(set(seq))
seq.sort(reverse=True)
T=lcm(list(map(lambda x: x//2,seq)))
if T>M:
    print(0)
    exit(0)
print(math.floor(M//T/2+0.5))



