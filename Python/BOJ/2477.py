import sys
r=sys.stdin.readline
k=int(r())
N=[]
S=[]
E=[]
W=[]
tb={1:E,2:W,3:S,4:N}
for _ in range(6):
    di,leng=map(int,r().split())
    tb[di].append(leng)
