import sys
r=sys.stdin.readline
lst=[]
for _ in range(int(r())):
    lst.append(int(r()))
print(*sorted(lst,reverse=True))
