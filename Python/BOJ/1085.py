import sys
r=sys.stdin.readline
x,y,w,h=list(map(int,r().split()))
print(min([x,y,w-x,h-y]))