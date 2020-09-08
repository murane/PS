import sys
r=sys.stdin.readline
def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b!=0:
        a,b=b,a%b
    return a
N=int(r())
arr=list(map(int,r().split()))
for num in arr[1:]:
    tmp=gcd(arr[0],num)
    print(f'{arr[0]//tmp}/{num//tmp}')