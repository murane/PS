import sys
r=sys.stdin.readline
a,b=list(map(int,r().split()))
if b<a:
    a,b=b,a
gcd=0
for div in range(a,0,-1):
    if a%div==0 and b%div==0:
        gcd=div
        break
print(gcd)
print(int(a*b/gcd))

