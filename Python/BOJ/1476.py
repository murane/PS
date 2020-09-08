import sys
r=sys.stdin.readline
E,S,M=map(int,r().split())
cnt,e,s,m=0,0,0,0
while E!=e or S!=s or M!=m:
    cnt+=1
    e+=1
    s+=1
    m+=1
    if e>15:
        e=1
    if s>28:
        s=1
    if m>19:
        m=1
print(cnt)