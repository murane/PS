import sys
r=sys.stdin.readline
N=int(r())
def getLeng(l):
    if l==0:
        return 0
    return 9*(10**(l-1))*l
res=0
L=len(str(N))
for i in range(1,L):
    res+=getLeng(i)
res+=((N-10**(L-1)+1)*L)
print(res)