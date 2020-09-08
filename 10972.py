import sys
r=sys.stdin.readline
N=int(r())
seq=list(map(int,r().split()))
if seq==sorted(seq,reverse=True):
    print("-1")
else:
    i=0
    for i in range(len(seq)-1,-1,-1):
        if seq[i]