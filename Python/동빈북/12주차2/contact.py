import sys,re
r=sys.stdin.readline
pat=re.compile("(100+1+|01)+")
for _ in range(int(r())):
    s=r().strip()
    if re.fullmatch(pat,s):
        print("YES")
    else:
        print("NO")