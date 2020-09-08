import sys
r=sys.stdin.readline
S=int(r())
n = 1
while n * (n + 1) / 2 <= S:
    n += 1
print(n - 1)