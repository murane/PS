import sys
r=sys.stdin.readline
n=int(r())
pair=[]
for _ in range(n):
    a,b=map(int,r().split())
    pair.append((a,b))
d=int(r())
pair.sort(key=lambda x:x(0,1))
L=pair[0][0]
R=pair[-1][1]
window=0
ans=0
for i in range()