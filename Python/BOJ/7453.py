import sys,bisect
r=sys.stdin.readline
n=int(r())
A,B,C,D=[],[],[],[]
for _ in range(n):
    a,b,c,d=map(int,r().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
cnt=0
AB,CD=[],[]
for i in range(n):
    for j in range(n):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])
CD.sort()
for num in AB:
    l=bisect.bisect_left(CD,-num)
    r=bisect.bisect_right(CD,-num)
    if l!=r:
        cnt+=(r-l)
print(cnt)