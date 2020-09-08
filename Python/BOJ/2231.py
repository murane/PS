import sys
r = sys.stdin.readline
N=int(r())
length = len(str(N))
for i in range(max(1,N - 9 * length), N + 9 * length + 1):
    sum=0
    for j in str(i):
        sum+=int(j)
    if i+sum==N:
        print(i)
        sys.exit(0)
print("0")