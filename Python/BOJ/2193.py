import sys
r=sys.stdin.readline
N=int(r())
tb=[(-1,-1),(0,1),(1,0),(1,1)]+[(-1,-1)]*89
def pinary(x):
    if tb[x][0]!=-1 or tb[x][1]!=-1:
        return tb[x]
    else:
        tmp=pinary(x-1)
        tb[x]=(tmp[0]+tmp[1],tmp[0])
        return tb[x]
res=pinary(N)
print(res[0]+res[1])