import sys
r = sys.stdin.readline
tups=[]
for _ in range(int(r())):
    x,y=list(map(int,r().split()))
    tups.append((x,y))
for x,y in tups:
    cnt=0
    for v,w in tups:
        if x<v and y<w:
            cnt+=1
    print(cnt+1,end=" ")