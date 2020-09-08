import sys
r=sys.stdin.readline
def gcd(a,b):
    if a>b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
for _ in range(int(r())):
    A,B=map(int, r().split())
    print(int(A*B/gcd(A,B)))
