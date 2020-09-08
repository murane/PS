import sys
r=sys.stdin.readline
while True:
    N=r().strip()
    if N=='0':
        break
    elif N==N[::-1]:
        print("yes")
    else:
        print("no")