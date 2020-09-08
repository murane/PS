import sys
r=sys.stdin.readline
N=int(r())
res=0
tb=[0,1,2]+[-1]*(1000-1)
for i in range(3,N+1):
    tb[i]=tb[i-2]+tb[i-1]
print(tb[N]%10007)