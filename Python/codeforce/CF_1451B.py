import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n,q=map(int,r().split())
    s=r().strip()
    for _ in range(q):
        l,r=map(int,r().split())
        substr=s[l-1:r]
        global tmpstr
        
    