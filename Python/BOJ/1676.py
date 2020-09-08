import sys
r=sys.stdin.readline
N=int(r())
acc=0
for i in range(1,N+1):
    acc=(i//5)
print(acc)