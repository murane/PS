import sys
from collections import defaultdict
r=sys.stdin.readline
n=int(r())
friend=defaultdict(set)
for _ in range(int(r())):
    a,b=map(int,r().split())
    friend[a].add(b)
    friend[b].add(a)
invite=set()

for dongi in friend[1]:
    invite.add(dongi)
    for dongi2 in friend[dongi]:
        invite.add(dongi2)
print(len(invite)-1)