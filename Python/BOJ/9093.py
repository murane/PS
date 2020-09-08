import sys
r=sys.stdin.readline
T=int(r())
for _ in range(T):
    case=r().strip()
    for word in case.split():
        print(word[::-1],end=" ")
    print("")