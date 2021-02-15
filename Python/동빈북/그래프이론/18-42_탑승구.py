import sys
from collections import defaultdict
r=sys.stdin.readline
G=int(r())
P=int(r())
match=defaultdict(set)
for i in range(1,P+1):
    