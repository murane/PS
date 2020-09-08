import sys
from operator import itemgetter
r=sys.stdin.readline
N=int(r())
conf=[]
for _ in range(N):
    conf.append(list(map(int, r().split())))
conf=conf.sort(key=itemgetter(1,0))
cnt,cur,tmp=0,0,0
choose=[]
while True:
    if cur==0:
        tmp=conf[cur]
    