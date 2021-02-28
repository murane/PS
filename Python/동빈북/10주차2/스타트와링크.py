import sys
from itertools import combinations
r=sys.stdin.readline
N=int(r())
g=[]
for _ in range(N):
    g.append(list(map(int,r().split())))
teams=set(list(range(N)))
group = list(combinations(range(N),N//2))



def get(a,b):
    return g[a][b]+g[b][a]