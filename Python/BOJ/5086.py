import sys
r = sys.stdin.readline
while True:
    x, y=list(map(int,r().split()))
    if x==0 and y==0:
        break
    elif y%x==0:
        print("factor")
    elif x%y==0:
        print("multiple")
    else:
        print("neither")