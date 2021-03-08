import sys
import bisect
r=sys.stdin.readline
pair=set()
start = []
end = []
for _ in range(int(r())):
    x,y=map(int,r().split())
    start.append(x)
    end.append(y)
    pair.add((x,y))

