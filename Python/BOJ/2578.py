import sys
r=sys.stdin.readline
tb=dict()
for i in range(5):
    line=list(map(int,r().split()))
    for j,num in enumerate(line):
        tb[num]=(i,j)
ck=[False]*
