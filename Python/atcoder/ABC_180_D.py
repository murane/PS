import sys,math
r=sys.stdin.readline
X,Y,A,B=map(int,r().split())
res=0
while True:
    if X+B>=Y and X*A>=Y:
        break
    if X+B>X*A:
        X*=A
        res+=1
    else:
        if (Y-X)%B==0:
            res+=((Y-X)//B-1)
        else:
            res+=(math.floor((Y-X)/B))
        break
print(int(res))