import sys
r=sys.stdin.readline
moon=r().strip()
S=0
for n in range(1,len(moon)+1):
    cnt=set()
    for substr in range(len(moon)+1-n):
        cnt.add(moon[substr:substr+n])
    S+=len(cnt)
print(S)