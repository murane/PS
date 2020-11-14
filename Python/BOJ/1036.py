import sys
from string import ascii_lowercase,digits
def convert(num,base):
    T=digits+ascii_lowercase
    q,r=divmod(num,base)
    if q==0:
        return T[r]
    else:
        return convert(q,base)+T[r]

r=sys.stdin.readline
N=int(r())
c=[0]*36
for _ in range(N):
    num=r().strip()
    l=len(num)
    for i,v in enumerate(reversed(num)):
        c[int(v,36)]+=
K=int(r())


