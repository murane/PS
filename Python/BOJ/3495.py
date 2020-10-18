import sys
r=sys.stdin.readline
h,w=map(int,r().split())
area=0
flg=False
for _ in range(h):
    line=r().strip()
    for ch in line:
        if flg:
            if ch==".":
                area+=1
            if ch in "\/":
                area+=0.5
                flg=False
        else:
            if ch==".":
                continue
            if ch in "\/":
                area+=0.5
                flg=True
    flg=False
print(int(area))