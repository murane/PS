import sys
r=sys.stdin.readline
papers=[]
for _ in range(int(r())):
    a,b=map(int,r().split())
    papers.append((a,b))
ans=0
