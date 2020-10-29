import sys
r=sys.stdin.readline
W,H=map(int,r().split())
shopPos=[]
for _ in range(int(r())):
    shopPos.append(list(map(int,r().split())))
guardPos=list(map(int,r().split()))
def getdist(x,y):
    xC,xDist=x
    yC,yDist=y
    if xC>yC:
        xC,yC=yC,xC
        xDist,yDist=yDist,xDist
    if xC==yC:#같은방향
        return abs(xDist-yDist)
    elif abs(xC-yC)==1 and (xC*yC==2 or xC*yC==12):#반대
        if xC<=2:
            return H+xDist+yDist
        else:
            return W+xDist+yDist
    else:#직각
        tmp=[xC,yC]
        if tmp==[1,3]:
            return xDist+yDist
        elif tmp==[1,4]:
            return W-xDist+yDist
        elif tmp==[2,3]:
            return H-yDist+xDist
        elif tmp==[2,4]:
            return W-xDist+H-yDist
s=0
total=2*W+2*H
for coords in shopPos:
    d=getdist(guardPos,coords)
    s+=min(d,total-d)
print(s)