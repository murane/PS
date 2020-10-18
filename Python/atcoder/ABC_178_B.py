import sys
r=sys.stdin.readline
a,b,c,d=map(int,r().split())
print(max([a*c,a*d,b*c,b*d]))