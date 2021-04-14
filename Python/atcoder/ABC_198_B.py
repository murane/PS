import sys
r=sys.stdin.readline
N=int(r())
s=str(N)
if s[::-1]==s:
    print("Yes")
else:
    while s.endswith('0'):
        s=s[:-1]
    if s==s[::-1]:
        print("Yes")
    else:
        print("No")
