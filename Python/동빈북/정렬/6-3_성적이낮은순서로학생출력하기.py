import sys
r=sys.stdin.readline
lst=[]
for _ in range(int(r())):
    lst.append(list(r().split()))
lst.sort(key=lambda x: x[1])
print(*[x[0] for x in lst])