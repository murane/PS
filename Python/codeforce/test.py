import sys
from collections import defaultdict
r=sys.stdin.readline
n,m=map(int,r().split())
subjs=defaultdict(list)
in_cnt=[0]*(n+1)
out_cnt=[0]*(n+1)
for _ in range(m):
    u,v=map(int,r().split())
    in_cnt[v]+=1
    out_cnt[v]+=1
    subjs[u].append(v)
need_sub=int(r())
start_lst=[]
for i in range(1,len(in_cnt)):
    if in_cnt[i]==0:
        start_lst.append(i)

